from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from server.server import db

def create_user():
    """
    This function creates a new user with the username and password provided in the request data.
    If the username already exists in the database, it returns an error message.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains a message indicating whether the user was created successfully or the username already exists. The status code is 201 if the user was created successfully, or 400 if the username already exists.
    """

    data = request.get_json()

    new_user = User(username=data['username'], password=data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists'}), 400