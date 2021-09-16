import csv
import shutil
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tempfile import NamedTemporaryFile
from templates import get_template, render_context

file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
host = 'smtp.gmail.com'
port = 587
username = 'email@gmail.com' # Provide your gmail address
password = 'pass' # Provide your gmail password
from_email = username
to_list = ['xuanchuongdp@gmail.com']

class UserManager():

    def message_user(self, user_id = None, user_email = None):
        user_data = self.get_user_data(user_id=user_id, user_email=user_email)
        if user_data:
            plain_, html_ = self.render_message(user_data)
            user_email = user_data.get('email', 'xuanchuongdp@gmail.com')
            email_conn = smtplib.SMTP(host, port)
            email_conn.starttls()
            email_conn.login(username, password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = 'Hello there!'
            msg['From'] = from_email
            msg['To'] = user_email
            part1 = MIMEText(plain_, 'plain')
            msg.attach(part1)
            email_conn.sendmail(from_email, [user_email], msg.as_string())
            email_conn.quit()

    def render_message(self, user_data):
        file_txt = 'templates/email_message.txt'
        file_html = 'templates/email_message.html'

        template_string = get_template(file_txt)
        template_html = get_template(file_html)
        if isinstance(user_data, dict):
            context = user_data
            plain_ = render_context(template_string, context)
            html_ = render_context(template_html, context)
            return (plain_, html_)
        return (None, None)

    def get_user_data(self, user_id=None, user_email=None):
        file_name = file_path
        with open(file_name, 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row.get('id')):
                        return row
                    else:
                        print("User id {user_id} not found".format(user_id=user_id))
                elif user_email is not None:
                    if user_email == row.get('email'):
                        return row
                    else:
                        print("User email {user_email} not found".format(user_email=user_email))
        return None

    def append_data(self, file_path, name, email):
        field_names = ['id', 'name', 'email']
        next_id = self.get_length(file_path)
        with open(file_path, 'a') as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=field_names)
            # writer.writeheader()
            writer.writerow({
                'id': next_id,
                'name': name,
                'email': email
            })

    def get_length(file_path):
        with open(file_path) as csvFile:
            reader = csv.reader(csvFile)
            data_list = list(reader)
            return len(data_list)

    def edit_data(self, edit_id, email=None, amount=None, sent=None):
        file_name = 'data.csv'
        temp_file = NamedTemporaryFile(mode='w', delete=False)
        with open(file_name, 'r') as csvFile, temp_file:
            reader = csv.DictReader(csvFile)
            field_names = ['id', 'name', 'email', 'amount', 'sent']
            writer = csv.DictWriter(temp_file, fieldnames=field_names)
            writer.writeheader()
            for row in reader:
                if edit_id is not None:
                    if (int(row['id']) == edit_id):
                        row['sent'] = sent
                        row['amount'] = amount
                elif email is not None:
                    if (str(row['email']) == email):
                        row['sent'] = sent
                        row['amount'] = amount
                writer.writerow(row)
            shutil.move(temp_file.name, file_name)
