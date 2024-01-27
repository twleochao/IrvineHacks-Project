import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

HEADERS = ['Event Name', 'Event Image Src', 'Event Time', 'Event Location', 'Event Address']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.model):
    name = db.Column(db.String(30), primary_key=True)

    def __repr__(self):
        return f"User('{self.id}')"


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
    with open('info.csv', mode = 'r') as csvfile:
        data = csv.reader(csvfile)
        get_data(data)

if __name__ == '__main__':
    main()
    db.create_all()
    app.run(debug=True)
