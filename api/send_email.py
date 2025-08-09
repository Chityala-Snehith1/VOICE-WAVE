from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import smtplib
import speech_recognition as sr
import pyttsx3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = FastAPI()

# Dummy unique code check (replace with real logic)
USER_CODES = {
    "user@example.com": "UNIQUECODE123"
}

@app.post("/send-email/")
async def send_email(
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    code: str = Form(...)
):
    # Security check
    if USER_CODES.get(email) != code:
        return JSONResponse(status_code=403, content={"error": "Invalid code for this account."})

    try:
        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = os.environ.get('EMAIL_USER')
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))
        server.send_message(msg)
        server.quit()
        return {"status": "Email sent successfully!"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Note: Speech recognition and TTS are not available in Vercel serverless functions.
# For a web UI, use browser APIs for speech and send the result to this endpoint.
