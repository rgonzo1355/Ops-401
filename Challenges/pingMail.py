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
    log_filename = "uptime_log.txt"
    sender_email = input("Enter the sender email address to monitor: ")
    password = getpass.getpass("Enter your email App password: ")
    recipient_email = sender_email # Assuming the sender is also the recipient

    previous_status = None

    try:
        with open(log_filename, "a") as log_file:
            while True:
                is_alive = ping_host(target_ip)
                current_status = "Active" if is_alive else "Inactive"
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                if current_status != previous_status and previous_status is not None:
                    subject = f"Status Change Detected for {target_ip}"
                    body = f"{timestamp}: Host {target_ip} changed status from {previous_status} to {current_status}"
                    send_email(sender_email, password, recipient_email, subject, body)

                print(f"{timestamp} Network {current_status} to {target_ip}")
                log_file.write(f"{timestamp} Network {current_status} to {target_ip}\n")
                log_file.flush()

                previous_status = current_status
                time.sleep(10) # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Monitoring stopped.")
