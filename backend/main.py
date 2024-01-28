import csv
import requests
import os
import json

HEADERS = ['Event Name', 'Event Image Src', 'Event Time', 'Event Location', 'Event Address']
API_KEY = 'AIzaSyA3eqFuwarzFiN4CIY4hkKBMpyxWTYgyRM'

coords = []
fnldata = []

def getcoords(address, key = API_KEY):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': address,
        'key': key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    if "Private Location" in address or address == 'Online Event':
        return None

    if response.status_code == 200 and data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        return latitude, longitude
    else:
        return None


def find_coords(data):
    for i,obj in enumerate(data):
        if obj[0] == 'Event Name': continue

        loc = obj[3]
        adr = obj[4]

        if adr == "":
            adr = loc
        curcoords = getcoords(adr)
        coords.append(curcoords)

        dct = {"name": obj[0], "img src": obj[1], "time": obj[2], "loc": obj[3], "add": obj[4], "cords": coords[i-1]}
        fnldata.append(dct)


def writesorteddata():
    with open('fnl.json', 'w') as f:
        json.dump(fnldata, f, indent=2)


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
    readpath = specifypath()
    with open(readpath, mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        find_coords(data)
    writesorteddata()

if __name__ == '__main__':
    main()
