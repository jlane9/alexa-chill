#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""chill app

.. codeauthor:: Time Stamper <timothy@thestampers.net>
.. codeauthor:: John Lane <john.lane93@me.com>

"""

import logging
import requests
from flask import Flask, render_template
from flask_ask import Ask, statement, session,  question, request


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


'''def get_movie_recommendation(**kwargs):
    response = requests.post("/api/movies/recommendation", json=kwargs)
    return response'''


@ask.launch
def start():

    return question(render_template('welcome.html'))


@ask.intent("AMAZON.HelpIntent")
def help_me():

    return statement(render_template('help.html'))


@ask.intent("AMAZON.FallbackIntent")
def fallback():

    return statement("I'm sorry, I don't understand. ")


@ask.intent("AMAZON.CancelIntent")
def cancel():

    return statement("ok, I'll stop working on that")


@ask.intent("MovieRecommendationIntent")
def get_movie_recommend():

    return question(render_template("movie_recommend.html"))


@ask.intent("MovieGenreIntent")
def get_movie_genre(movie_genre):

    return question(render_template("movie_genre.html", genre=movie_genre))


@ask.intent("ShowRecommendationIntent")
def get_show_recommend():

    return statement(render_template("show_recommend.html"))


@ask.intent("ShowGenreIntent")
def get_show_genre(show_genre):
    return question(render_template("show_genre.html", genre=show_genre))


@ask.intent("ConfirmationIntent")
def confirmation():

    return statement(render_template("confirmation.html"))


@ask.intent("DenyIntent")
def deny():

    return question(render_template("deny.html"))


if __name__ == "__main__":

    app.run()
