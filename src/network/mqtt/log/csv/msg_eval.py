import csv
import datetime

def read_csv(filename):
    rows = []
    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            rows.append(row)
    return rows

def calculate_timestamp_difference(timestamp1, timestamp2):
    """Calculates the difference between two timestamps in seconds."""
    timestamp1_datetime = datetime.datetime.strptime(timestamp1, "%Y-%m-%d %H:%M:%S.%f")
    timestamp2_datetime = datetime.datetime.strptime(timestamp2, "%Y-%m-%d %H:%M:%S.%f")
    print(timestamp1_datetime, timestamp2_datetime)
    delta = timestamp2_datetime - timestamp1_datetime
    return delta.total_seconds()

csv_file1 = "pub_1.csv"
csv_file2 = "sub_1.csv"
rows1 = read_csv(csv_file1)
rows2 = read_csv(csv_file2)

result_dict = {}
for row1, row2 in zip(rows1[2:], rows2[2:]):  
    message = row1[3]  
    timestamp1 = row1[4] 
    timestamp2 = row2[4]
    timestamp_difference = calculate_timestamp_difference(timestamp1, timestamp2)
    result_dict[message] = timestamp_difference

for key, value in result_dict.items():
    print(f"{key}, {value}")
