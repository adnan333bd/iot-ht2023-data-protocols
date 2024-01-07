import csv
import datetime

def read_csv(filename):
    """Reads a CSV file and returns a list of rows."""
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
    delta = timestamp2_datetime - timestamp1_datetime
    return delta.total_seconds()

csv_file1 = "pub_1.csv"
csv_file2 = "sub_1.csv"
rows1 = read_csv(csv_file1)
rows2 = read_csv(csv_file2)

timestamp_differences = []
for row1, row2 in zip(rows1, rows2):
    timestamp1 = row1[4]  
    timestamp2 = row2[4]
    timestamp_difference = calculate_timestamp_difference(timestamp1, timestamp2)
    timestamp_differences.append(timestamp_difference)


for timestamp_difference in timestamp_differences:
    print(timestamp_difference)


