from flask import jsonify
from flask import render_template

import db_connector
from resp_dict import form_response_dictionary


# response codes:
# 0 - all OK
# 1 - user with provided data alredy exist
# 2 - no such user exist
# 3 - error parsing data
# 4 - error during working with database
# 5 - unknown error


def argument_checker(dict_of_given_arguments, list_of_required_arguments, list_of_unrequired_arguments=None):
    if list_of_unrequired_arguments is None:
        list_of_unrequired_arguments = []
    required_arguments_number_counter = 0
    if dict_of_given_arguments and len(dict_of_given_arguments) <= (
                len(list_of_required_arguments) + len(list_of_unrequired_arguments)):
        for arg in dict_of_given_arguments:
            if arg not in list_of_required_arguments and arg not in list_of_unrequired_arguments:
                return False
            if arg not in list_of_required_arguments and arg in list_of_unrequired_arguments:
                continue
            if arg in list_of_required_arguments and arg not in list_of_unrequired_arguments:
                required_arguments_number_counter += 1
        if (required_arguments_number_counter == len(list_of_required_arguments)):
            return True
    return False


def index_handler():
    return render_template("index.html")


def login_handler(args):
    pass


def registration_handler(args):
    if argument_checker(args, ['email', 'password'], ['name', 'surname', 'patronymic', 'sex']):
        email = args['email']
        password = args['password']
        name = 'Not indicated'
        surname = 'Not indicated'
        patronymic = 'Not indicated'
        sex = 'U'
        if 'name' in args.keys(): name = args['name']
        if 'surname' in args.keys(): surname = args['surname']
        if 'patronymic' in args.keys(): patronymic = args['patronymic']
        if 'sex' in args.keys(): sex = args['sex']
        try:
            db_conn, cursor = db_connector.connect()
            cursor.execute('SELECT uuid_generate_v4()')
            token = cursor.fetchone()[0]
            try:
                cursor.execute(
                    'INSERT INTO Users(email, password, name, surname, patronymic, sex, token) VALUES (%s,%s,%s,%s,%s,%s,%s);',
                    (email, password, name, surname, patronymic, sex, token))
                db_conn.commit()
                db_conn.close()
            except:
                return jsonify(form_response_dictionary(1))
            return jsonify(form_response_dictionary(0))
        except:
            return jsonify(form_response_dictionary(4))
    else:
        return jsonify(form_response_dictionary(3))
