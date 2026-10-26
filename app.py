
import os
from io import BytesIO

from dotenv import load_dotenv
from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError
from google import genai
from google.genai import types

# Load settings from the .env file
load_dotenv()

app = Flask(__name__)

# Maximum uploaded image size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Use a currently documented Gemini model
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

MIME_TYPES = {
    "JPEG": "image/jpeg",
    "PNG": "image/png",
    "WEBP": "image/webp",
}


def get_gemini_client():
    """Create a Gemini client using the private API key."""
    api_key = (
        os.getenv("GOOGLE_API_KEY")
        or os.getenv("GEMINI_API_KEY")
    )

    if not api_key or api_key == "PASTE_YOUR_API_KEY_HERE":
        raise RuntimeError(
            "API key missing. Check your .env file."
        )

    return genai.Client(api_key=api_key)


def validate_medical_image(client, image_part):
    """Check whether the actual uploaded image is healthcare-related."""
    prompt = """
    Examine the supplied image.

    Is the image clearly related to medicine or healthcare?
    Examples include medicine packaging or labels, medical
    equipment, anatomical images, clinical images, or medical
    documents.

    Reply with only YES or NO.
    If the image is unclear or unrelated, reply NO.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image_part],
    )

    answer = (response.text or "").strip().upper()
    return answer.startswith("YES")


def describe_medical_image(client, image_part):
    """Generate a careful description of visible image content."""
    prompt = """
    Describe the visible content of this healthcare-related image.

    Follow these rules:
    1. Describe what is visibly present. Do not invent details.
    2. For medicine packaging, report a medicine name, ingredient,
       strength, or expiry date only when clearly readable.
    3. Never identify a loose pill from its colour or shape alone.
    4. For clinical or anatomical images, describe visible features
       without diagnosing a disease.
    5. Do not prescribe medicines, doses, or treatments.
    6. Clearly mention text or details that cannot be read.
    7. Use simple language and headings where useful.

    State that this is an AI-generated description, not a medical
    diagnosis. Recommend consulting a qualified healthcare
    professional for medical decisions.
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, image_part],
    )

    return (response.text or "").strip()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    uploaded_file = request.files.get("file")

    if not uploaded_file or not uploaded_file.filename:
        return render_template(
            "index.html",
            error="Please select an image first."
        ), 400

    if "." not in uploaded_file.filename:
        return render_template(
            "index.html",
            error="The selected file must be an image."
        ), 400

    extension = uploaded_file.filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return render_template(
            "index.html",
            error="Use a JPG, JPEG, PNG or WebP image."
        ), 400

    image_bytes = uploaded_file.read()

    try:
        # Validate the image using Pillow before sending it to Gemini.
        with Image.open(BytesIO(image_bytes)) as image:
            image_format = image.format
            image.verify()

        if image_format not in MIME_TYPES:
            return render_template(
                "index.html",
                error="This image format is not supported."
            ), 400

    except (UnidentifiedImageError, OSError, ValueError):
        return render_template(
            "index.html",
            error="The file is not a valid image or is damaged."
        ), 400

    # Create an image part from the uploaded bytes.
    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type=MIME_TYPES[image_format],
    )

    try:
        client = get_gemini_client()

        # Step 1: Check whether the image is healthcare-related.
        is_medical = validate_medical_image(
            client,
            image_part,
        )

        if not is_medical:
            return render_template(
                "index.html",
                error=(
                    "This image could not be verified as "
                    "healthcare-related. Please try another image."
                ),
            )

        # Step 2: Generate a description for relevant images.
        result = describe_medical_image(
            client,
            image_part,
        )

        if not result:
            result = "No description was returned. Please try again."

        return render_template(
            "index.html",
            result=result,
        )

    except Exception:
        app.logger.exception("Image processing failed")

        return render_template(
            "index.html",
            error=(
                "The AI request failed. Check your API key, "
                "internet connection and model access, then try again."
            ),
        ), 500


@app.errorhandler(413)
def file_too_large(_error):
    return render_template(
        "index.html",
        error="Image size must be 5 MB or less.",
    ), 413


if __name__ == "__main__":
    # Local development only. Do not use debug mode in production.
    app.run(debug=True)
