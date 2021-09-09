import csv
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, user_email=None):
    file_name = 'data.csv'
    with open(file_name, 'r') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if user_id is not None:
                if int(user_id) == int(row.get('id')):
                    return row
                else:
                    return "User id {user_id} not found".format(user_id=user_id)
            elif user_email is not None:
                if user_email == row.get('email'):
                    return row
                else:
                    return "User email {user_email} not found".format(user_email=user_email)
    return None

def append_data(file_path, name, email):
    field_names = ['id', 'name', 'email']
    next_id = get_length(file_path)
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

def edit_data(edit_id, email=None, amount=None, sent=None):
    file_name = 'data.csv'
    temp_file = NamedTemporaryFile(mode='w', delete=False)
    with open(file_name, 'r') as csvFile, temp_file:
        reader = csv.DictReader(csvFile)
        field_names = ['id', 'name', 'email', 'amount', 'sent']
        writer = csv.DictWriter(temp_file, fieldnames=field_names)
        writer.writeheader()
        for row in reader:
            if edit_data is not None:
                if (int(row['id']) == edit_id):
                    row['sent'] = sent
                    row['amount'] = amount
            elif email is not None:
                if (str(row['email']) == email):
                    row['sent'] = sent
                    row['amount'] = amount
            writer.writerow(row)
        shutil.move(temp_file.name, file_name)

print(read_data())