from flask import render_template, redirect, flash
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user
from sqlalchemy import exc
import models
from flask import jsonify
from __init__ import app
from resp_dict import form_response_dictionary


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(useremail):
    return models.User.query.get(useremail)


def argument_checker(dict_of_given_arguments, list_of_required_arguments, list_of_unrequired_arguments=[]):
    if dict_of_given_arguments and len(dict_of_given_arguments) == (
                len(list_of_required_arguments) + len(list_of_unrequired_arguments)):
        for arg in dict_of_given_arguments:
            if arg not in list_of_required_arguments:
                return False
        return True
    else:
        return False


def index_handler():
    return render_template("index.html")


def login_handler(args):
    if current_user.is_authenticated:
        return jsonify(form_response_dictionary(1))
    if argument_checker(args, ['email', 'password']):
        user = models.User.query.get(args['email'])
        if user is not None:
            if user.password == args['password']:
                if login_user(user):
                    return jsonify(form_response_dictionary(0))
        else:
            return jsonify(form_response_dictionary(2))
    return jsonify(form_response_dictionary(3))


def registration_handler(args):
    if current_user.is_authenticated:
        return jsonify(form_response_dictionary(1))
    if argument_checker(args, ['email', 'name', 'surname', 'password']):
        try:
            u = models.User(email=args['email'], name=args['name'], surname=args['surname'], password=args['password'])
            models.db.session.add(u)
            models.db.session.commit()
            return form_response_dictionary(0)
        except exc.IntegrityError as e:
            models.db.session().rollback()
            return jsonify(form_response_dictionary(4))
    else:
        return jsonify(form_response_dictionary(3))