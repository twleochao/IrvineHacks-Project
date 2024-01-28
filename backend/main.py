import csv
import requests
import os

HEADERS = ['Event Name', 'Event Image Src', 'Event Time', 'Event Location', 'Event Address']
API_KEY = 'AIzaSyA3eqFuwarzFiN4CIY4hkKBMpyxWTYgyRM'

coords = []

def getcoords(address, key = API_KEY):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': address,
        'key': key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if address == 'Private Location (sign in to display)' or address == 'Online Event':
        return None

    if response.status_code == 200 and data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        return latitude, longitude
    else:
        return None

def find_coords(data):
    for i in data:
        if i[0] == 'Event Name': continue

        loc = i[3]
        adr = i[4]

        if adr == "":
            adr = loc
        curcoords = getcoords(adr)
        coords.append(curcoords)

def specifypath():
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(cur_dir, 'eventinfo.csv')

    return filename

def removecommas(string):
    return string.replace(',', '')

def writecsv(data, filename, headers = HEADERS):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    with open('eventinfo.csv', mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        find_coords(data)

if __name__ == '__main__':
    main()
