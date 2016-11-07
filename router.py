from __init__ import app
from flask import request
import views


@app.route('/')
def index_handler():
    return views.index_handler()


@app.route('/api/login', methods=['POST'])
def login():
    return views.login_handler(request.args)


@app.route('/api/registration', methods=['POST'])
def register():
    return views.registration_handler(request.args)