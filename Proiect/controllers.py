from flask import jsonify, request
import hashlib
import secrets

def create_user():
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