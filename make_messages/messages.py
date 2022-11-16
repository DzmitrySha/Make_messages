import os
import csv
from xlsx2csv import Xlsx2csv
from make_messages.in_out import create_dir

CSV_FILENAME = 'messages.csv'
TXT_FILENAME = 'messages.txt'


def make_messages_(source_path, output):

    create_dir(output)

    filepath = os.path.join(output, CSV_FILENAME)
    Xlsx2csv(source_path, outputencoding="utf-8").convert(filepath)

    with open(filepath, newline='') as csvfile:
        messagereader = csv.reader(csvfile, delimiter=',')
        messages = []
        for row in messagereader:
            comment = row[0]
            parent = row[1]
            child = row[2]
            message = row[3]
            message = message.replace('@parent', parent)
            message = message.replace('@child', child)
            messages.append(comment + "\n" + message)

    output_filepath = os.path.join(os.getcwd(), output, TXT_FILENAME)

    with open(output_filepath, 'w') as txtfile:
        for message in messages:
            message += '\n\n'
            txtfile.write(message)

    return output_filepath
