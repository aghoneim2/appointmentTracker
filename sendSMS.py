import email, smtplib, ssl
from providers import PROVIDERS
import dmvSelenium
import time


def send_sms_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
):

    subject: str = "ALERT"
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 465

    sender_email, sender_password = sender_credentials
    receiver_email = f"{number}@{PROVIDERS.get(provider).get('sms')}"
    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, sender_password)
        email.sendmail(sender_email, receiver_email, email_message)


def main():
    number = "2012756909"
    message = "There are dmv appointments available!!!"
    provider = "T-Mobile"

    sender_credentials = ("almalek154@gmail.com", "onpikrtafyqqzzmf")

    send_sms_email(number, message, provider, sender_credentials)


def constantRun():
    count = 1
    while True:
        print(f"Run #{count}")
        count+=1
        
        response = dmvSelenium.runScraper()

        if response != "No Appointments Available":
            main()
        
        time.sleep(30)


if __name__ == "__main__":
    constantRun()
