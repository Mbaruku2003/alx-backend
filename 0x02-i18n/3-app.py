#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel, _  # type: ignore
import typing
from typing import Optional, List

app = Flask(__name__)
# mypy: ignore-missing-imports


class Config:
    """Created  a new config file for the project."""

    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)

babel = Babel(app)


def get_locale() -> Optional[str]:
    """returns an expected language that fits the best."""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)
@app.route('/')
def index() -> str:
    """Render template for the index."""

    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
