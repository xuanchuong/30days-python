import csv
import shutil
from tempfile import NamedTemporaryFile

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

def edit_data(id, amount, sent):
    file_name = 'data.csv'
    temp_file = NamedTemporaryFile(mode='w', delete=False)
    with open(file_name, 'r') as csvFile, temp_file:
        reader = csv.DictReader(csvFile)
        field_names = ['id', 'name', 'email', 'amount', 'sent']
        writer = csv.DictWriter(temp_file, fieldnames=field_names)
        writer.writeheader()
        for row in reader:
            if (int(row['id']) == id):
                row['sent'] = sent
                row['amount'] = amount
            writer.writerow(row)
        shutil.move(temp_file.name, file_name)

edit_data(2, 8884.3, True)