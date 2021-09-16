import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.gmail.com'
port = 587
username = 'email' # Provide your gmail address
password = 'pass' # Provide your gmail password
from_email = username
to_list = ['xuanchuongdp@gmail.com']


class MessageUser:
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}
    Thank you for the purchase on {date}.
    We hope you are excited about using it. Just as a reminder the purchase total was ${total}.
    Have a great one!
    
    Team CFE  
    """

    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        new_amount = '%.2f' % amount
        today = datetime.date.today()
        date_text = '{today.day}/{today.month}/{today.year}'.format(today=today)
        detail = {
            'name': name,
            'amount': new_amount,
            'date': date_text
        }
        if email is not None:
            detail['email'] = email

        self.user_details.append(detail)

    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.user_details:
                name = detail['name']
                date = detail['date']
                amount = detail['amount']
                message = self.base_message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get('email')
                if user_email:
                    user_data = {
                        'email': user_email,
                        'message': message
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(message)
            return self.messages
        else:
            return []

    def get_users(self):
        return self.user_details

    def send_email(self):
        self.make_messages()
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                message = detail['message']
                try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.starttls()
                    email_conn.login(username, password)

                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = 'Hello there!'
                    msg['From'] = from_email
                    msg['To'] = user_email
                    part1 = MIMEText(message, 'plain')
                    msg.attach(part1)
                    email_conn.sendmail(from_email, [user_email], msg.as_string())
                    email_conn.quit()
                    print('Send email successfully')
                except smtplib.SMTPAuthenticationError:
                    print('Could not login')
                except:
                    print('exception occured')
            return True
        return False

messageUser = MessageUser()
messageUser.add_user("Chuong", 122.12, email='xuanchuongdp@gmail.com')
messageUser.send_email()