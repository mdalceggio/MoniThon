import smtplib
from email.message import EmailMessage


def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)

    gmail_user = 'martincamba@gmail.com'
    gmail_password = 'Technet.4370'
    msg['Subject'] = subject
    msg['From'] = "martincamba@gmail.com"
    msg['To'] = to

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    email_alert("Test", "https://discord.gg/cAWW5qq", "3095824273@vtext.com")