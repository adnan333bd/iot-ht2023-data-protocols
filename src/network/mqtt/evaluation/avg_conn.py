import os
import pandas as pd
from datetime import datetime

directory_path = '../log/csv'

connection_times = []

for filename in os.listdir(directory_path):
    if filename.startswith('pub') and filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)

        conn_request_row = df[df['Event_Type'] == 'EVENT_CONN_REQUEST']
        connected_row = df[df['Event_Type'] == 'EVENT_CONNECTED']

        if not conn_request_row.empty and not connected_row.empty:
            conn_request_time = datetime.strptime(conn_request_row['Time_Stamp'].iloc[0], '%Y-%m-%d %H:%M:%S.%f')
            connected_time = datetime.strptime(connected_row['Time_Stamp'].iloc[0], '%Y-%m-%d %H:%M:%S.%f')

            connection_time = (connected_time - conn_request_time).total_seconds()

            connection_times.append(connection_time)


if connection_times:
    average_connection_time = sum(connection_times) / len(connection_times)
    print(f'The average connection time is: {average_connection_time} seconds')
else:
    print('No valid files found.')
