import string
import requests
import faker
import flask
import datetime
from flask import Flask
from flask import request
from faker import Faker
import random

from marshmallow import validate
from webargs import fields
from webargs.flaskparser import use_kwargs

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

    param = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=length))

    if specials:
        param += string.punctuation

    if digits:
        param += string.digits

    return param




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



app.run()