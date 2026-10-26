# Medicine Recognition System 💊

An AI-powered web application built with **Python, Flask, and Google's Gemini API** to analyze medicine and healthcare-related images and generate descriptions of their visible contents.

Users can upload an image, validate its format, check whether it is healthcare-related using AI, and view a generated description.

> **Disclaimer:** This is an educational project, not a clinically validated medical tool. AI-generated information may be inaccurate and must not replace professional medical advice, diagnosis, or treatment.

## ✨ Features

- Upload medicine and healthcare-related images.
- Support JPG, JPEG, PNG, and WebP formats.
- Validate uploaded files before AI processing.
- Check healthcare relevance using Gemini.
- Generate AI-powered descriptions of visible image content.
- Display error messages for invalid uploads and API failures.
- Manage API credentials using environment variables.
- Restrict image uploads to a maximum of 5 MB.
- Provide a simple, responsive web interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Backend web framework |
| Google Gen AI SDK | Gemini API integration |
| Pillow | Image validation and processing |
| HTML5 | Web page structure |
| CSS3 | Interface styling |
| python-dotenv | Environment variable management |
| Git and GitHub | Version control |

## 📂 Project Structure

```text
Medicine-Recognition-System/
├── .venv/                 # Local Python environment
├── static/
│   └── style.css          # Website styling
├── templates/
│   └── index.html         # Main HTML page
├── .env                   # Private credentials (not committed)
├── .gitignore
├── app.py                 # Flask application
├── LICENSE
├── README.md
└── requirements.txt
```

**Security:** The `.env` and `.venv/` entries are shown for documentation purposes only. They should not be uploaded to GitHub.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or another compatible version
- Visual Studio Code
- Git
- A Google account
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 1. Clone the Repository

```bash
git clone https://github.com/Ashutoshkumarchoub/Medicine-Recognition-System.git
cd Medicine-Recognition-System
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API

Create an API key through [Google AI Studio](https://aistudio.google.com/app/apikey).

Create a `.env` file in the same directory as `app.py` and add:

```dotenv
GOOGLE_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_available_gemini_model
```

Replace the example values with your actual API key and a Gemini model available to your API project.

**Never commit your actual API key to GitHub.**

### 5. Run the Application

```bash
python app.py
```

Open your browser and visit:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🔄 Application Workflow

1. The user uploads a medicine or healthcare-related image.
2. Flask validates the file format and image content.
3. Gemini checks whether the image appears healthcare-related.
4. Relevant images are sent for description generation.
5. The generated description or an appropriate error message is displayed.

## 🧪 Testing

Test the application with:

- Valid healthcare-related images.
- Unrelated images.
- Unsupported file formats.
- Invalid or damaged image files.
- Images exceeding the upload size limit.
- Missing or invalid API credentials.
- Gemini API availability and quota errors.

AI classification can make mistakes. Passing the relevance check does not guarantee medical accuracy.

## 🔐 Security and Limitations

- API credentials are stored in environment variables.
- Uploaded images are validated before processing.
- AI-generated descriptions may be incomplete or incorrect.
- The application is not a diagnostic or treatment recommendation system.
- Do not upload identifiable patient records or sensitive medical information.
- Production deployment requires additional security, privacy, and monitoring controls.

## 🔮 Future Enhancements

- Add automated tests using pytest.
- Improve the interface with image previews and loading indicators.
- Add more robust API error handling and retry logic.
- Improve accessibility and multilingual support.
- Add stronger upload security and rate limiting.
- Evaluate description quality using verified sample images.
- Deploy using a production-ready hosting service.

## 📚 Learning Outcomes

This project provides practical experience with:

- Flask application development.
- Generative AI API integration.
- Image validation and processing.
- Environment variable and API credential management.
- Exception handling and debugging.
- Git and GitHub workflows.

## 🙏 Acknowledgment

This project builds upon the open-source [Medicine-Recognition-System](https://github.com/KalyanM45/Medicine-Recognition-System) repository by Kalyan Murapaka.

The original project's applicable license and copyright notices should be retained. Modifications and additional features should be documented accurately.

## 👨‍💻 Author

**Ashutosh Kumar Choubey**

- GitHub: [@Ashutoshkumarchoub](https://github.com/Ashutoshkumarchoub)

## 📄 License

See the `LICENSE` file included in this repository for the applicable license terms.

---

If you find this project useful, feel free to explore the code and suggest improvements.
