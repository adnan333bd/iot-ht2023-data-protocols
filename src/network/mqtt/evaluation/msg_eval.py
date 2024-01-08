import os
import csv
from datetime import datetime

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row.get('Event_Type') in ['EVENT_MSG_RECD', 'EVENT_MSG_SENT']:
                data.append(row)
    return data

def process_files(directory):
    publisher_files = []
    subscriber_files = []

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if file_name.startswith("pub") and file_name.endswith(".csv"):
            publisher_files.append(file_path)
        elif file_name.startswith("sub") and file_name.endswith(".csv"):
            subscriber_files.append(file_path)

    messages = {}

    for publisher_file in publisher_files:
        publisher_data = read_csv(publisher_file)
        for row in publisher_data:
            message_name = row['Message']
            timestamp_start = row['Time_Stamp']
            messages[message_name] = {'start': timestamp_start}

    for subscriber_file in subscriber_files:
        subscriber_data = read_csv(subscriber_file)
        for row in subscriber_data:
            message_name = row['Message']
            timestamp_end = row['Time_Stamp']
            if message_name in messages:
                messages[message_name]['end'] = timestamp_end
                
    return messages

if __name__ == "__main__":
    directory_path = "../log/csv"  
    result = process_files(directory_path)

    print("{")
    for key, value in result.items():
        print(f"    '{key}': {value},")
    print("}")
