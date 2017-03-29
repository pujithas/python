import csv
from collections import OrderedDict

# If using Python 2.x - use `open('output.csv', 'wb') instead
with open('input.csv') as fin, open('output.csv', 'w') as fout:
    csvin = csv.DictReader(fin)
    csvout = csv.DictWriter(fout, fieldnames=csvin.fieldnames, quoting=csv.QUOTE_ALL)
    csvout.writeheader()
    for row in csvin:
        for k, v in row.items():
            row[k] = '|'.join(OrderedDict.fromkeys(v.split('|')))
        csvout.writerow(row)
