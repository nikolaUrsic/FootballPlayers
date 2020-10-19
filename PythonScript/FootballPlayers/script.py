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

# kreiranje igraca
for i in range(1000):
    data = {'FirstName': 'Name' + str(i),
            'LastName': 'Surname' + str(i),
            'Age': 20 + i % 4,
            'FieldPosition': position(i % 4)}
    r = requests.post(url=URL, data=data)

# dohvat svih podataka i spremanje
r = requests.get(url=URL)
data = r.json()
csvFile = open('E:\export.csv', 'w', newline='', encoding='utf-8')  # TODO namjestit
columns = ['Id', 'FirstName', 'LastName', 'Age', 'FieldPosition']
writer = csv.DictWriter(csvFile, delimiter=',', fieldnames=columns)
writer.writeheader()

for d in data:
    writer.writerow({'Id': d['Id'], 'FirstName': d['FirstName'], 'LastName': d['LastName'], 'Age': d['Age'],
                     'FieldPosition': d['FieldPosition']})

# dohvat jednog podataka i spremanje
playerId = 1;  # postavljanje kojeg igraca zelimo dohvatit
r = requests.get(url=URL + '/' + str(playerId))
data = r.json()
csvFile = open('E:\exportOnePlayer.csv', 'w', newline='', encoding='utf-8')  # TODO namjestit
writer = csv.DictWriter(csvFile, delimiter=',', fieldnames=columns)
writer.writeheader()
writer.writerow({'Id': data['Id'], 'FirstName': data['FirstName'], 'LastName': data['LastName'], 'Age': data['Age'],
                 'FieldPosition': data['FieldPosition']})
# update igraca
data = {'Id': 1,
        'FirstName': 'NewName',
        'LastName': 'NewSurname',
        'Age': 20,
        'FieldPosition': 'Forward'}
r = requests.put(url=URL, data=data)

# brisanje igraca
playerId = 2;  # postavljanje kojeg igraca zelimo obrisati
r = requests.delete(url=URL + '/' + str(playerId))
