
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import smtplib
from email.message import EmailMessage
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:8000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





@app.post("/send-email/")
async def send_email(
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    try:
        # Set up the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASS'))

        email_msg = EmailMessage()
        email_msg['From'] = os.environ.get('EMAIL_USER')
        email_msg['To'] = email
        email_msg['Subject'] = subject
        email_msg.set_content(message)

        server.send_message(email_msg)
        server.quit()
        return {"status": "Email sent successfully!"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Note: Speech recognition and TTS are not available in Vercel serverless functions.
# For a web UI, use browser APIs for speech and send the result to this endpoint.
