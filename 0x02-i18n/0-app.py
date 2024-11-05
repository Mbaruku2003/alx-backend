#!/usr/bin/env python3
""" basic flask app."""
from flask import Flask, render_template
import typing


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Render template."""

    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
