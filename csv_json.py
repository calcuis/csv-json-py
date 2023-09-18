import csv, json

data = []

with open('data.csv', encoding='utf-8-sig') as csvf:
    csvReader = csv.DictReader(csvf)

    for row in csvReader: 
        data.append(row)

with open('data.json', 'w', encoding='utf-8-sig') as jsonf:
    jsonf.write(json.dumps(data, indent=4))
