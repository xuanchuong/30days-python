import csv

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

append_data('data.csv', 'huy', 'huy.nguyen@nakivo.com')