
# Voice Wave: Voice-Controlled Email Bot (Vercel Ready)

This project is a Vercel-deployable, Python-based bot with a modern web interface that enables users to send emails using only their voice. The web UI leverages browser speech recognition for voice input, while the backend uses FastAPI to securely send emails. This hands-free approach is especially useful for accessibility, multitasking, and situations where typing is inconvenient or impossible.

## How it Works
1. Open the web interface (`public/index.html`) deployed on Vercel.
2. Enter the recipient's email, subject, message, and your unique code, or use the microphone buttons to fill in the subject/message by voice.
3. The browser's speech recognition API transcribes your voice input.
4. On form submission, the FastAPI backend validates your unique code and sends the email securely.
5. You receive a real-time status update in the web UI.

### Features
- Modern, responsive web UI with voice input for subject and message
- Secure email sending with unique code per account
- Real-time feedback and error handling
- Ready for Vercel deployment (serverless API + static frontend)

This project can be extended to support additional features such as scheduling emails, reading incoming emails aloud, or integrating with other messaging platforms.

## Prerequisites
For local development, make sure you have the following Python packages installed:

- fastapi
- uvicorn
- smtplib
- email
- python-multipart

You can install them using pip:
```sh
pip install -r requirements.txt
```

## Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo.git
   ```
2. Change into the project directory:
   ```sh
   cd your-repo
   ```
3. (Optional) Set up a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. To run locally:
   ```sh
   uvicorn api.send_email:app --reload
   ```
5. Open `public/index.html` in your browser for the web UI.

## Usage
Deploy to Vercel for production, or use locally as described above. Use the web UI to send emails by voice or text.

## Security
This bot is highly secure. Each account is integrated with a unique code, ensuring that only authorized users can send emails from their accounts. All sensitive operations are handled server-side, and credentials should be managed using environment variables on Vercel.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


