import datetime
import random
import re
import string

import requests
from faker import Faker

from flask import jsonify, Response, render_template

from flask import Flask
from marshmallow import validate
from webargs import fields
from webargs.flaskparser import use_kwargs

from db import execute_query
from http_status import HTTP_200_OK, HTTP_204_NO_CONTENT
from utils import format_records

app = Flask(__name__)



@app.route("/password")
@use_kwargs(
    {
        "length": fields.Int(
            missing=10,
            validate=[validate.Range(min=1, max=999)],
        ),
        "specials": fields.Bool(
            missing=False,
            validate=[validate.Range(min=0, max=1)],
        ),
        "digits": fields.Bool(
            missing=False,
            validate=[validate.Range(min=0, max=1)],
        ),
    },
    location="query",
)
def generate_password(length, specials, digits):
    length = request.args.get('length', '10')
    specials = request.args.get('specials', False)
    digits = request.args.get('digits', False)


    if not length.isdigit():
        return 'ERROR: not a number'

    length = int(length)

    if not 1 < length < 100:
        return 'ERROR: out of range [1..100]'

    param_len = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length))

    if specials:
        param += string.punctuation

    if digits:
        param += string.digits

    return param_len


@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.Str(
            missing='USD',
        ),
    },
    location="query",
)
def get_bitcoin_rate(currency):
    url = 'https://bitpay.com/api/rates'
    res = requests.get(url)
    result = res.json()
    stats = {}

    for entry in result:
        if entry['code'] == currency:
            stats[entry['rate']] = stats.get(entry['rate'], entry['code'])
    return stats



@app.route('/unique_names')
def get_unique_names():
    query = 'select FirstName from customers'

    records = execute_query(query)

    names = []
    for record in records:
        unique = True
        for name in names:
            if record == name:
                unique = False
        if unique:
            names.append(record)

    print(names)
    return ''.join('Количество уникальных имён: ' + str(len(names)))



@app.route('/tracks_count')
def get_tracks_count():
    query = 'select * from tracks'

    records = execute_query(query)
    return ''.join('Количество записей в таблице Tracks: ' + str(len(records)))



@app.route('/fill_companies')
@use_kwargs(
    {
        "company": fields.Str(
            required=False,
            missing=None,
        ),
    },
    location="query",
)
def get_customers(company):
    query = 'SELECT Company FROM customers'
    records = execute_query(query)

    companies = []

    for record in records:
        if str(record) == '(None,)':
            fake = Faker()
            companies.append((fake.company()))
        else:
            companies.append(record)

    return str(companies)


app.run()