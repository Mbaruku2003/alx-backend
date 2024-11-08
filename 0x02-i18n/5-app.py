#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel, _  # type: ignore
import typing
from typing import Optional, List, Dict

app = Flask(__name__)
# mypy: ignore-missing-imports


class Config:
    """Created  a new config file for the project."""

    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)

babel = Babel(app)


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user() -> Optional[Dict]:
    """Retreive a user by ID passed in the login_as query."""

    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set the logged in user to the global g content."""

    g.user = get_user()


def get_locale() -> Optional[str]:
    """returns an expected language that fits the best."""

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """Render template for the index."""

    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
