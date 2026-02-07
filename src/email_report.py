import os
# Import smtplib Python library to facilitate email usage
import smtplib
# Import MIMEText and MIMEMultipart from the email Python library to build the email message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Import the generated summary with summary
def send_email_report(summary):

    # Sender email, recipient email, email server, email user, and email password are all specified in .env
    sender = os.getenv("EMAIL_SENDER")
    recipient = os.getenv("EMAIL_RECIPIENT")
    email_server = os.getenv("SMTP_SERVER")
    email_user = os.getenv("SMTP_USER")
    email_password = os.getenv("SMTP_PASSWORD")

    # The email port is specified in the .env file under SMTP_PORT 
    # Defaults to 587 if not specified
    email_port = int(os.getenv("SMTP_PORT", 587))

    # Skip email sending if required configuration is missing
    if not all([sender, recipient, email_server, email_user, email_password]):
        print("Missing proper email configuration. Skipping email step.")
        return

    # msg is initialized as a MIMEMultipart alternative message
    msg = MIMEMultipart("alternative")

    # Subject, From, and To set
    msg["Subject"] = "Daily Marketing Summary"
    msg["From"] = sender
    msg["To"] = recipient

    # Create the summary part using MIMEText and attach it to the message
    summary_part = MIMEText(summary, "plain")
    msg.attach(summary_part)

    # Try to send email and print Exception message if it fails
    try:
        with smtplib.SMTP(email_server, email_port) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(sender, recipient, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
