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

    return statement("Fallback")


@ask.intent("AMAZON.CancelIntent")
def cancel():

    return statement("ok, I'll stop working on that")


@ask.intent("AMAZON.MovieRecommendationIntent")
def movie_recommend():

    return statement(render_template(movie_recommend.html))


@ask.intent("AMAZON.ShowRecommendationIntent")
def show_recommend():

    return statement(render_template(show_recommend.html))


if __name__ == "__main__":

    app.run()
