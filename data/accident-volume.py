import csv
import sys


def extract(row, fields):
    return {f: row[f] for f in fields}


def read_data(filename):
    with open(filename) as csvfile:
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
            print d
            data.append(d)

    return None


def main():
    read_data('accidents_2012_to_2014.csv')


if __name__ == '__main__':
    sys.exit(main())
