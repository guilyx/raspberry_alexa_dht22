# -*- coding: utf-8 -*-

import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import ht_sensors as sense

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def sense_home():
    card_title = "Raspberry Pi"
    init_msg = render_template('init')
    return statement(init_msg).simple_card(card_title, init_msg)


@ask.intent("TemperatureIntent")
def ask_temperature():
    temp = sense.get_temperature()
    temp_msg = render_template('temperature', temperature=temp)
    return statement(temp_msg)

@ask.intent("HumidityIntent")
def ask_humidity():
    hum = sense.get_humidity()
    hum_msg = render_template('humidity', humidity=hum)
    return statement(hum_msg)

if __name__ == "__main__":
    app.run(debug=False)
    
