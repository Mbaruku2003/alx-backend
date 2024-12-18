#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template
from flask_babel import Babel
import typing


app = Flask(__name__)


class Config:
    """ creating a config file."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@app.route('/')
def index() -> str:
    """Render template."""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug="True")
