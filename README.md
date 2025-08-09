## Prerequisites
Make sure you have the following Python packages installed:

- speechrecognition
- pyttsx3
- smtplib
- email
- pyaudio (for microphone input)

You can install them using pip:
```sh
pip install SpeechRecognition pyttsx3 pyaudio
```

# Voice-Controlled Email Bot


This project is a Python-based bot that enables users to send emails using only their voice. The bot leverages speech recognition to capture spoken commands, converts them into text, and then uses email protocols to send messages directly to the intended recipients. This hands-free approach is especially useful for accessibility, multitasking, and situations where typing is inconvenient or impossible.

### How it Works
1. The bot prompts the user to speak the recipient's email address, subject, and message body.
2. It uses speech recognition to transcribe the spoken input into text.
3. The bot confirms the details with the user (optional step for accuracy).
4. Once confirmed, the bot sends the email using secure authentication and a unique code for each account.
5. The user receives a notification (via voice or console) that the email has been sent successfully.

This project can be extended to support additional features such as scheduling emails, reading incoming emails aloud, or integrating with other messaging platforms.

## Security
This bot is highly secure. Each account is integrated with a unique code, ensuring that only authorized users can send emails from their accounts. This adds an extra layer of protection and privacy for all users.

## Features
- Send emails using voice commands
- Speech-to-text conversion
- Automatic email delivery
- User-friendly and hands-free operation

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

## Usage
Run the bot and follow the voice prompts to send an email:
```sh
python sp.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
