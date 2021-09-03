import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.gmail.com'
port = 587
username = 'your-email' # Provide your gmail address
password = 'your-password' # Provide your gmail password

from_email = username
to_list = ['xuanchuongdp@gmail.com']

try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.starttls()
    email_conn.login(username, password)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Hello there!'
    msg['From'] = from_email
    # msg['To'] = to_list
    plain_txt = "Testing the message"
    html_txt = '''
    <html>
        <head></head>
        <body>
            <p>Hey!</hey>
            Testing this email <b>message</b>. Make by <a href='https://joincfe.com'>Team CFE</a>
        </body>
    </html>
    '''
    part1 = MIMEText(plain_txt, 'plain')
    part2 = MIMEText(html_txt, 'html')
    msg.attach(part1)
    msg.attach(part2)


    email_conn.sendmail(from_email, to_list, msg.as_string())
    email_conn.quit()
    print('Send email successfully')
except smtplib.SMTPAuthenticationError:
    print('Could not login')
except:
    print('exception occured')