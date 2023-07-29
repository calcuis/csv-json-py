import csv, json

def csv_to_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            data.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8-sig') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

csvFilePath = r'data.csv'
jsonFilePath = r'data.json'

csv_to_json(csvFilePath, jsonFilePath)
