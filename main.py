from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import random

nummer = random.randint(0, 10000)

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
alle_nummers = 'Alle liedjes - Blad1.csv'

class getClasses(Resource):  # /get
    def get(self):
        # returnt containernummer en een leuke tekst
        return {'container': nummer,
                'nummers': gekozen_nummers_refr()
                }

def random_gen(max):  # fills a list with random numers of indexes of which the total is filled in above
    gekozen_index = set([])
    vol_lijst_grott = len(vol_lijst)
    while len(gekozen_index) < max:
        gekozen_index.add(random.randint(0, vol_lijst_grott))
    return gekozen_index

def gekozen_nummers_refr():
    gekozen_nummers = []
    for j in random_gen(aantal_nums):
        gekozen_nummers.append(vol_lijst[j])
    return gekozen_nummers

aantal_nums = 6
vol_lijst = []

with open(alle_nummers, 'r', encoding='utf8') as f:  # maakt een lijst van alle nummers
    for lijnen in f.readlines():
        temp = lijnen.strip('\n').split(',')
        vol_lijst.append(temp[0])
    vol_lijst.pop(0)

api.add_resource(getClasses, '/get')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='443')


