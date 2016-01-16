import json

from flask import (Flask, redirect, render_template,
                   request, url_for, make_response, flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = '39rujPCVOTR7NICGJB,;RT65DI4rfv09/RT65DI4rfvwqpriej'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True, port=8000, host='0.0.0.0')
