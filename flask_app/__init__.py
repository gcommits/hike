from flask import Flask

app = Flask(__name__)

# This secret key was generated with Python. In the command link, import secrets,
#  and then use the command secrets.token_hex(16) to generate a 16 character key.
app.config['SECRET_KEY'] = 'c77e965b2ac1481447ef9fd5134e5dd9'