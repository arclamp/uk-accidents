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


def compute_accident_volume(data):
    print >>sys.stderr, 'sorting data'
    data.sort(lambda x, y: -1 if x < y else 1)

    compact = []
    cur = None
    for d in data:
        if cur is None:
            cur = {'Date': d['Date'],
                   'count': 1}

        if d['Date'] != cur['Date']:
            compact.append(cur)

            cur = {'Date': d['Date'],
                   'count': 1}
        else:
            cur['count'] += 1

    return compact


def main():
    print >>sys.stderr, 'reading data'
    data = read_data(sys.stdin)
    print >>sys.stderr, 'computing volume'
    volume = compute_accident_volume(data)

    print json.dumps(volume, indent=2)

if __name__ == '__main__':
    sys.exit(main())
