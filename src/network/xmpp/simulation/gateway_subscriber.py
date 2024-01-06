import time
import csv
import os


# path
path = '/xmpp/log/csv/csv'

# Ensure the directory exists, create it if not
if not os.path.exists(path):
    os.makedirs(path)

current_time = time.strftime("%Y-%m-%d %H:%M:%S")
# Specify the file name
filename = 'subscriber.csv'

# Construct the full file path
filepath = os.path.join(path, filename)

fieldnames = ["Topic", "Event Type", "Message", "Time"]

data = {"Topic": 'subscriber', "Event Type": "connection-completed", "Message": 'Hello World!!', "Time": current_time}

try:
    with open(filepath, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is empty
        if file.tell() == 0:
            writer.writeheader()

        # Write new data
        writer.writerow(data)
    print(f'CSV file created successfully at: {filepath}')
except Exception as e:
    print(f'Error creating CSV file: {e}')