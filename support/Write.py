import csv
from datetime import datetime

def append_to_csv(file_path, message):
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Data to be appended to the CSV file
    data = [timestamp, message]

    # Open the CSV file in append mode
    with open(file_path, 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="|")
        # Write the data to the CSV file
        csv_writer.writerow(data)