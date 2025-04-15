import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv


load_dotenv()

def send_email_alert(subject, body):
    try:
        # Email sender details from environment variables
        from_email = os.getenv("EMAIL_USERNAME")
        password = os.getenv("EMAIL_PASSWORD")
        to_email = os.getenv("TO_EMAIL")

        if not from_email or not password:
            raise ValueError("Email credentials are missing from environment variables")

        # Create message
        message = MIMEMultipart()
        message["From"] = from_email
        message["To"] = to_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, message.as_string())
        
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

