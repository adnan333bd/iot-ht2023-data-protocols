from msg_eval import read_csv, process_files
from datetime import datetime

def calculate_time_difference(messages):
    time_differences = {}
    max_diff = 0
    for message, timestamps in messages.items():
        if 'start' not in timestamps or 'end' not in timestamps: 
            continue
        start_time = datetime.strptime(timestamps['start'], '%Y-%m-%d %H:%M:%S.%f')
        end_time = datetime.strptime(timestamps['end'], '%Y-%m-%d %H:%M:%S.%f')
        time_difference = end_time - start_time
        time_differences[message] = time_difference.total_seconds() * 1000
        if time_differences[message] > max_diff:
            max_diff = time_differences[message]

    if time_differences:
        average_difference = sum(time_differences.values()) / len(time_differences.keys())
        return time_differences, average_difference, max_diff, len(time_differences.keys())
    else:
        return {}, 0, 0, 0

if __name__ == "__main__":
    directory_path = "../log/csv"
    result = process_files(directory_path)

    time_diff_result, average_time_diff, max_diff, message_count = calculate_time_difference(result)

    print("{")
    for message, difference in time_diff_result.items():
        print(f"    '{message}': {difference},")
    print("}")

    print(f"\nAverage Time : {average_time_diff} mili second")
    print(f"\nMax Time : {max_diff} mili second")
    print(f"\nReceived Message Count : {message_count}")
    print(f"\nSent Message Count : {len(result.keys())}")
