from flask import jsonify, request
from sqlalchemy import or_
import hashlib
import secrets


def create_user():
    """
    This function creates a new user with the username and password provided in the request data.
    It validates the username and password, generates a salt and hashes the password, and then stores the user in the database.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains a message indicating whether the user was created successfully or the username already exists. The status code is 201 if the user was created successfully, or 400 if the username already exists.
    """

    from server.server import db, app, Users, Password

    data = request.get_json()

    # Validări
    if Users.query.filter_by(username=data['username']).first():
        return jsonify({'message': 'An account with this username already exists.'}), 400

    password = data['password']
    if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.islower() for char in password):
        return jsonify({'message': 'Password must be at least 8 characters long and contain at least one digit and one lowercase letter.'}), 400

    # Generare salt și criptare parolă
    salt = secrets.token_hex(16)  # Generare salt
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

    # Adaugare in tabela Passwords
    new_password = Password(username=data['username'], salt=salt)
    db.session.add(new_password)
    db.session.commit()

    # Adaugare in tabela Users
    new_user = Users(username=data['username'], password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Username already exists.'}), 400

def authenticate_user():
    """
    This function authenticates a user with the username and password provided in the request data.
    It retrieves the salt for the user, hashes the provided password with the salt, and checks if the hashed password matches the stored password.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains a message indicating whether the user was authenticated successfully or the credentials are invalid. The status code is 200 if the user was authenticated successfully, or 401 if the credentials are invalid.
    """

    from server.server import db, app, Users, Password

    data = request.get_json()

    username = data['username']
    password = data['password']

    # Obține salt-ul din tabela Passwords
    stored_password = Password.query.filter_by(username=username).first()

    if stored_password:
        salt = stored_password.salt
        hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

        # Verifică dacă parola este corectă
        user = Users.query.filter_by(username=username, password=hashed_password).first()

        if user:
            return jsonify({'message': 'User authenticated successfully', 'username': username}), 200 
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    else:
        return jsonify({'message': 'Invalid credentials'}), 404

def check_username():
    """
    This function checks if a username exists in the database.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains a message indicating whether the username exists or not. The status code is 200 if the username exists, or 404 if it does not.
    """

    from server.server import db, app, Users

    data = request.get_json()
    my_username = data['my_username']
    username = data['username']

    # Verifică dacă numele de utilizator există în baza de date
    user = Users.query.filter_by(username=username).first()

    if user != None and username != my_username:
        return jsonify({'message': 'Username exists', 'username': username}), 200 
    elif user != None and username == my_username:
         return jsonify({'message': 'You cannot create a conversation with yourself'}), 404
    else:
        return jsonify({'message': 'Username does not exist'}), 404

def store_key():
    """
    This function stores a conversation key for two users in the database.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains a message indicating whether the key was stored successfully or the usernames were not found. The status code is 201 if the key was stored successfully, or 404 if one or both usernames were not found.
    """

    from server.server import db, app, Users, Password, ConversationKey

    data = request.get_json()

    # Extrageți numele de utilizator și cheia din datele cererii
    username1 = data['username1']
    username2 = data['username2']
    key = data['key']

    # Căutați ID-urile numelor de utilizator în tabela Users
    user1 = Users.query.filter_by(username=username1).first()
    user2 = Users.query.filter_by(username=username2).first()

    if user1 is None or user2 is None:
        return jsonify({'message': 'One or both usernames not found.'}), 404

    # Inserează cheia în tabela ConversationKey
    new_key = ConversationKey(user1_id=user1.id, user2_id=user2.id, key=key)
    db.session.add(new_key)
    db.session.commit()

    return jsonify({'message': 'Key stored successfully!'}), 201

def get_key():
    """
    This function retrieves a conversation key for two users from the database.

    Returns:
    A tuple containing a JSON response and a status code. The JSON response contains the conversation key if it was found, or a message indicating that no key was found. The status code is 200 if the key was found, or 404 if it was not.
    """

    from server.server import db, app, Users, Password, ConversationKey

    data = request.get_json()

    # Extrageți numele de utilizator din datele cererii
    username1 = data['username1']
    username2 = data['username2']

    # Căutați ID-urile numelor de utilizator în tabela Users
    user1 = Users.query.filter_by(username=username1).first()
    user2 = Users.query.filter_by(username=username2).first()

    if user1 is None or user2 is None:
        return jsonify({'message': 'One or both usernames not found.'}), 404

    # Căutați cheia în tabela ConversationKey
    conversation_key = ConversationKey.query.filter(
        or_(
            (ConversationKey.user1_id == user1.id) & (ConversationKey.user2_id == user2.id),
            (ConversationKey.user1_id == user2.id) & (ConversationKey.user2_id == user1.id)
        )
    ).first()

    if conversation_key is None:
        return jsonify({'message': 'No key found for this conversation.'}), 404

    # Returnați cheia
    return jsonify({'key': conversation_key.key}), 200

