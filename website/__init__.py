"""Website package initializer."""
import flask
from flask_mail import Message, Mail

mail = Mail()
# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (website/config.py)
app.config.from_object('website.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/config/
app.config.from_envvar('WEBSITE_SETTINGS', silent=True)

mail.init_app(app)

import website.views  # noqa: E402  pylint: disable=wrong-import-position
