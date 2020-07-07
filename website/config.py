"""Portfolio development configuration."""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xbeZ\x850\x15|^|I \xd5\xdf\xfc\x9d\xbb\x8aA$\x8fx+\x97V\xe0'

# File Upload to var/uploads/
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'media',
)
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'ryandunnportfolio77@gmail.com'
MAIL_PASSWORD = 'waqMGgw9f4MUsDvR'
