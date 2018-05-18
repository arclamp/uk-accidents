import csv
import datetime
import json
import sys


def extract(row, fields):
    return {f: row[f] for f in fields}


def read_data(csvfile):
    reader = csv.reader(csvfile)

    headers = reader.next()

    data = []
    for row in reader:
        d = extract(dict(zip(headers, row)), [
            'Date',
            'Time',
            'Accident_Severity',
            'Number_of_Casualties',
            'Speed_limit'
        ])

        d['Date'] = datetime.datetime.strptime(d['Date'], '%d/%m/%Y').date().isoformat()

        data.append(d)

    return data


def main():
    data = read_data(sys.stdin)
    print json.dumps(data, indent=2)


if __name__ == '__main__':
    sys.exit(main())
