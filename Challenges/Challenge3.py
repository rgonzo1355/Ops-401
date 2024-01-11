# Rodolfo Gonzalez
# 01-10-2024
# Uptime Sensor Tool Part 2 of 2

'''Finish writing an uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.
The script must:

-Ask the user for an email address and password to use for sending notifications.
-Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
-Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

Resources: 
https://g.co/bard/share/dc8ba53a59fc 
https://chat.openai.com/share/329b0313-0214-4226-8bdd-5ef15559dd9c
https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
'''

import os
import time
import smtplib
import getpass
from email.mime.text import MIMEText

def ping_host(target_ip):
    try:
        response = os.system(f"ping -c 1 {target_ip} > /dev/null 2>&1")
        return response == 0
    except Exception as e:
        print(f"Ping error: {str(e)}")
        return False

def send_email(sender_email, password, recipient_email, subject, body):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email was sent successfully.")
    except Exception as e:
        print("Email NOT sent:", str(e))

if __name__ == "__main__":
    target_ip = input("Enter the target IP address to monitor: ")
    sender_email = input("Enter your sender email address: ")
    password = getpass.getpass("Enter your email App password: ")
    recipient_email = sender_email

    previous_status = None

    try:
        while True:
            is_alive = ping_host(target_ip)
            current_status = "Active" if is_alive else "Inactive"
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

            if current_status != previous_status and previous_status is not None:
                subject = f"Status Change Detected for {target_ip}"
                body = f"{timestamp}: Host {target_ip} changed status from {previous_status} to {current_status}"
                send_email(sender_email, password, recipient_email, subject, body)

            print(f"{timestamp} Network {current_status} to {target_ip}")

            previous_status = current_status
            time.sleep(10)

    except KeyboardInterrupt:
        print("Monitoring stopped.")

