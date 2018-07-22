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


# TODO: We'll work on this later
def get_movie_recommendation(**kwargs):
    response = requests.post("/api/movies/recommendation", json=kwargs)
    return response








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

    return statement("ok, enjoy your day")


@ask.intent("MovieRecommendationIntent")
def get_movie_recommend():

    recommended_title = "Fight Club"
    return question(render_template("movie_recommend.html", title=recommended_title))


@ask.intent("MovieGenreIntent")
def get_movie_genre(movie_genre):

    recommended_title = "Fight Club"
    return question(render_template("movie_genre.html", genre=movie_genre, title=recommended_title))


@ask.intent("NotWatchedMovieIntent")
def get_not_watched_movie(boolean):

    return statement(render_template("not_watched_movie.html", title="Deadpool"))


@ask.intent("WatchedMovieIntent")
def get_watched_movie(boolean):

    return statement(render_template("watched_movie.html", title="Harry Potter"))


@ask.intent("NotWatchedMovieActorIntent")
def get_not_watched_movie_actor(actor, boolean):

    return statement(render_template("not_watched_movie_actor.html", title="Gone With The Wind"))


@ask.intent("NotWatchedMovieReleaseIntent")
def get_not_watched_movie_release(boolean, decade):

    return statement(render_template("not_watched_movie_release.html", title="Kangaroo Jack"))


@ask.intent("NotWatchedMovieRatingIntent")
def get_not_watched_movie_rating(rating, boolean):

    return statement(render_template("not_watched_movie_rating.html", title="The Fast and The Furious: Tokyo Drift"))


@ask.intent("NotWatchedMovieTrendingIntent")
def get_not_watched_movie_trending(boolean):

    return statement(render_template("not_watched_movie_trending.html", title="Saving Private Ryan"))


@ask.intent("NotWatchedMoviePopularIntent")
def get_not_watched_movie_popular(boolean):

    return statement(render_template("not_watched_movie_popular.html", title="James Bond: License to Kill"))


@ask.intent("NotWatchedMovieRelatedIntent")
def get_not_watched_movie_related(related_title):

    return statement(render_template("not_watched_movie_related_title.html", title="Shrek"))


@ask.intent("ShowGenreIntent")
def get_show_genre(show_genre):
    return question(render_template("show_genre.html", genre=show_genre))


@ask.intent("NotWatchedShowIntent")
def get_not_watched_movie(boolean):

    recommended_title = "Shrek 2"
    return question(render_template("not_watched_show.html", title=recommended_title))


@ask.intent("WatchedShowIntent")
def get_watched_show(boolean):

    return statement(render_template("watched_show.html", title="The Office"))


@ask.intent("NotWatchedShowActorIntent")
def get_not_watched_show_actor(actor, boolean):

    return statement(render_template("not_watched_show_actor.html", title="Parks and Rec"))


@ask.intent("NotWatchedShowReleaseIntent")
def get_not_watched_show_release(boolean, decade):

    return statement(render_template("not_watched_show_release.html", title="Frazier"))


@ask.intent("NotWatchedShowRatingIntent")
def get_not_watched_show_rating(rating, boolean):

    return statement(render_template("not_watched_show_rating.html", title="Breaking Bad"))


@ask.intent("NotWatchedShowTrendingIntent")
def get_not_watched_show_trending(boolean):

    return statement(render_template("not_watched_show_trending.html", title="The Eric Andre Show"))


@ask.intent("NotWatchedShowPopularIntent")
def get_not_watched_show_popular(boolean):

    return statement(render_template("not_watched_show_popular.html", title="Mythbusters"))


@ask.intent("NotWatchedShowRelatedIntent")
def get_not_watched_show_related(boolean, related_title):

    return statement(render_template("not_watched_show_related_title.html", title="Sponge Bob"))


@ask.intent("ConfirmationIntent")
def confirmation():

    return statement(render_template("confirmation.html"))


@ask.intent("DenyIntent")
def deny():

    return question(render_template("deny.html"))


if __name__ == "__main__":

    app.run()
