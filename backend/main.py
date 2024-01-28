import csv
import requests

HEADERS = ['Event Name', 'Event Image Src', 'Event Time', 'Event Location', 'Event Address']
API_KEY = 'AIzaSyA3eqFuwarzFiN4CIY4hkKBMpyxWTYgyRM'

def getcoords(address, key = API_KEY):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        'address': address,
        'key': key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        latitude, longitude = location['lat'], location['lng']
        return latitude, longitude
    else:
        print(f"Error: {data['status']}")
        return None

def removecommas(string):
    return string.replace(',', '')

def writecsv(data, filename, headers = HEADERS):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(headers)

def get_data(data):
    for i in data:
        eventname = i[0]
        imagesrc = i[1]
        eventime = i[2]
        eventlocation = i[3]
        eventaddress = i[4]

def main():
    with open('eventinfo.csv', mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        #get_data(data)

if __name__ == '__main__':
    main()
