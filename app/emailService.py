import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email, subject, message_body, smtp_server='smtp.gmail.com', smtp_port=587):
    try:
        from_email = 'jesusboyonline@gmail.com'
        from_email_app_password = 'ktqxbygvlzxsrzus'
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(from_email, from_email_app_password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
        return 0
    except Exception as e:
        print(f"Failed to send email: {e}")
        return 1

 
