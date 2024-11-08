#!/usr/bin/env python3
"""Define the class."""
from flask_babel import Babel, _ # type: ignore
from flask import render_template, Flask, request
import typing
from typing import List, Optional


app = Flask(__name__)


class Config:
    LANGUAGES: LIST[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"

app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    """Define the default path."""

    return render_template('4-index.html')


def get_locale() -> Optional[str]:
    """get the locale for a specific language."""

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run(debug=True)
