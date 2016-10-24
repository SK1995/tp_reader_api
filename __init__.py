from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import config


app = Flask(__name__, template_folder="templates")
app.config.from_object(config)
try:
    db = SQLAlchemy(app)
    print "connected to db successfully"
except:
    print "failed connecting to database"


import views
import router