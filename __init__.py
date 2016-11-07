from flask import Flask
import config

app = Flask(__name__, template_folder="templates")

try:
    app.config.from_object(config)
    print "Configuration succeeded"
except:
    print "Configuration failed"

import views
import router