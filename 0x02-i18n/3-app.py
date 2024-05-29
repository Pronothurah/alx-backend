#!/usr/bin/env python3
"""task 2"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """has a LANGUAGES class attribute """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Uses request.accept_languages to determine the best
    match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """defines root index"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
