#!/usr/bin/python
import requests
from flask import Flask, request
app = Flask(__name__)

TOKEN = 'VGgoWiNMjlLy9J3JtOZxsn1r'

@app.route('/swansonme', methods=['POST'])
def swansonme():
    if request.form['token'] == TOKEN:
        r = requests.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes', headers=headers)
        print "r.text:",r.text
        reply = r.text
    else:
        reply = "Slash command token mismatch.  Something's wrong."

    return reply

if __name__ == '__main__':
    app.run()
