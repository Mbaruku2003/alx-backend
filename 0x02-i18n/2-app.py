#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """created a config file."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """returns an expected language that fits the best."""

    return request.accept_languages.best_match(["en"])


@app.route('/')
def index():
    """Render template."""

    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
