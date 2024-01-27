import csv

def organizetime(time):

def get_data(data):
    for i in data:
        eventname = i[0]
        imagesrc = i[1]
        eventime = i[2]
        eventlocation = i[3]
        eventaddress = i[4]

def main():
    with open('info.csv', mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        get_data(data)

main()
