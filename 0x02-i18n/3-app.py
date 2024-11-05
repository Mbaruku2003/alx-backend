#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import typing
from typing import Optional

app = Flask(__name__)


class Config:
    """Created  a new file."""

    LANGUAGES: list[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)


babel = Babel(app)


@babel.localeselector
def get_locale() -> Optional[str]:
    """returns an expected language that fits the best."""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Render template."""

    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
