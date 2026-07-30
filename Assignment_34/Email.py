import smtplib
from email.message import EmailMessage

def Marvellous_send_mail(sender,app_password,receiver,subject,body):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject


    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)

    smtp.quit()


def main():
    sender_email = "pratikraut.codex@gmail.com"

    app_password = "itwognxwlsadmfte"

    receiver_email = "pratikshapare12@gmail.com"


    subject = "I Love You Pratiksha, Testing Python Script"

    body = """
            Mand Pori,
            Abhayass kar...
            
            
            this mail is sent for testing 

            regards,
            Pratik Raut
            """
    Marvellous_send_mail(sender_email,app_password,receiver_email,subject,body)

    print("Mail send successfully")

if __name__ == "__main__":
    main()

