import requests
import csv


def position(i):
    switcher = {
        0: 'Goalkeeper',
        1: 'Defender',
        2: 'Midfielder',
        3: 'Forward'
    }
    return switcher.get(i, "Benchwarmer")


URL = "http://localhost:8080/api/footballPlayers"

# punjenje baze podatcima
for i in range(1000):
    data = {'FirstName': 'Name' + str(i),
            'LastName': 'Surname' + str(i),
            'Age': 20 + i % 4,
            'FieldPosition': position(i % 4)}
    r = requests.post(url=URL, data=data)

# dohvat podataka i spremanje
r = requests.get(url=URL)
data = r.json()
csvFile = open('E:\export.csv', 'w', newline='', encoding='utf-8')  # TODO namjestit
columns = ['Id', 'FirstName', 'LastName', 'Age', 'FieldPosition']
writer = csv.DictWriter(csvFile, delimiter=',', fieldnames=columns)
writer.writeheader()

for d in data:
    writer.writerow({'Id': d['Id'], 'FirstName': d['FirstName'], 'LastName': d['LastName'], 'Age': d['Age'],
                     'FieldPosition': d['FieldPosition']})
