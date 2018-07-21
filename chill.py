#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""chill app

.. codeauthor:: Time Stamper <timothy@thestampers.net>
.. codeauthor:: John Lane <john.lane93@me.com>

"""

import os
import logging
import requests
from flask import Flask, render_template
from flask_ask import Ask, statement, question, request


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start():

    return question(render_template('welcome.html'))


@ask.intent("AMAZON.HelpIntent")
def help_me():

    return statement(render_template('help.html'))


@ask.intent("AMAZON.FallbackIntent")
def fallback():

    expert = random.choice(['Kevin', 'Jesse', 'Jason Cameron', 'Nick Kline'])
    return statement(render_template('fallback.html', expert=expert))


@ask.intent("AMAZON.CancelIntent")
def cancel():

    return statement(render_template('cancel.html'))


if __name__ == "__main__":

    app.run()
