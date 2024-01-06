import csv
import os
from datetime import datetime

FIELD_FROM_DEVICE_ID = "From_Device_ID"
FIELD_TO_DEVICE_ID = "To_Device_ID"
FIELD_EVENT_TYPE = "Event_Type"
FIELD_TIME_STAMP = "Time_Stamp"
FIELD_MSG = "Message"
FIELD_NAMES = [
    FIELD_FROM_DEVICE_ID,
    FIELD_TO_DEVICE_ID,
    FIELD_EVENT_TYPE,
    FIELD_MSG,
    FIELD_TIME_STAMP,
]

EVENT_CONN_REQUEST = "EVENT_CONN_REQUEST"
EVENT_CONNECTED = "EVENT_CONNECTED"
EVENT_MSG_SENT = "EVENT_MSG_SENT"
EVENT_MSG_RECVD = "EVENT_MSG_RECD"


class Logger:
    global_file_logs = {}

    @staticmethod
    def get_file_log(file_name):
        return Logger.global_file_logs[file_name]

    @staticmethod
    def clear_file_logs(file_name):
        if file_name in Logger.global_file_logs:
            Logger.global_file_logs[file_name] = []

    @staticmethod
    def dump_logs():
        for file_name in Logger.global_file_logs.keys():
            Logger.dump_log(file_name)

    @staticmethod
    def dump_log(file_name):
        path = "/mosquitto/log/custom/csv"

        # Ensure the directory exists, create it if not
        if not os.path.exists(path):
            os.makedirs(path)

        # Construct the full file path
        filepath = os.path.join(path, file_name)

        try:
            with open(filepath, "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)

                # Write header if the file is empty
                if file.tell() == 0:
                    writer.writeheader()

                file_logs = Logger.get_file_log(file_name)
                for data in file_logs:
                    # Write new data
                    writer.writerow(data)
                Logger.clear_file_logs(file_name)
        except Exception as e:
            print(f"Error creating CSV file: {e}")

    def __init__(self, device_id):
        self.device_id = device_id
        self.file_name = device_id + ".csv"

    def log_message(self, event_type, from_device, to_device, message):
        now = datetime.now()

        # Format the time with millisecond precision
        # (first three digits of microseconds)
        current_time = now.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        data = {
            FIELD_FROM_DEVICE_ID: from_device,
            FIELD_TO_DEVICE_ID: to_device,
            FIELD_EVENT_TYPE: event_type,
            FIELD_MSG: message,
            FIELD_TIME_STAMP: current_time,
        }

        if self.file_name not in Logger.global_file_logs:
            Logger.global_file_logs[self.file_name] = []
        Logger.global_file_logs[self.file_name].append(data)

        return
