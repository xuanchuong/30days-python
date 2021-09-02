import smtplib

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
    email_conn.sendmail(from_email, to_list, "hello, message from python.")
    email_conn.quit()
    print('Send email successfully')
except smtplib.SMTPAuthenticationError:
    print('Could not login')
except:
    print('exception occured')