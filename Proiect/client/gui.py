import json
import os
import base64
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import pyqtSignal, Qt, QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtGui import QFont, QColor
from cryptography.fernet import Fernet

class User:
    def __init__(self):
        self.username = None
        self.is_authenticated = False
        self.conversation_partner = None

    def login(self, username):
        self.username = username
        self.is_authenticated = True

    def logout(self):
        self.username = None
        self.is_authenticated = False
        self.conversation_partner = None
    
    def start_conversation(self, partner_username):
        self.conversation_partner = partner_username  # Stocarea numelui de utilizator al partenerului de conversație

    def end_conversation(self):
        self.conversation_partner = None  # Ștergerea numelui de utilizator al partenerului

user = User()

class LoginWindow(QWidget):
    showRegistrationWindow = pyqtSignal()
    showHomeWindow = pyqtSignal()

    def __init__(self, home_window):
        super().__init__()
        self.home_window = home_window

        # Setează dimensiunile dorite pentru fereastră
        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat - Login")
        self.layout = QVBoxLayout()
        self.layout.addSpacing(100)

        self.label_title = QLabel("Welcome to QuickChat!")  # Adaugă titlul
        self.label_title.setFont(QFont('Times', 18))  # Schimbă fontul și dimensiunea textului
        self.label_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_title)

        self.label_subtitle = QLabel("Log in into your account right now!")  # Adaugă subtitlul
        self.label_subtitle.setFont(QFont('Times', 12))  # Schimbă fontul și dimensiunea textului
        self.label_subtitle.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_subtitle)

        self.layout.addSpacing(100)

        self.label_username = QLabel("Username:")
        self.label_username.setFont(QFont('KBZipaDeeDooDah', 10))  # Schimbă fontul și dimensiunea textului
        self.entry_username = QLineEdit()
        self.entry_username.setFont(QFont('KBZipaDeeDooDah', 8))  # Schimbă fontul și dimensiunea textului

        self.label_password = QLabel("Password:")
        self.label_password.setFont(QFont('Times', 10))  # Schimbă fontul și dimensiunea textului
        self.entry_password = QLineEdit()
        self.entry_password.setFont(QFont('Times', 8))  # Schimbă fontul și dimensiunea textului
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton("Login")
        self.button_login.setFont(QFont('Times', 8))  # Schimbă fontul și dimensiunea textului
        self.button_login.setStyleSheet("background-color: #2fa190; color: white;")  # Adaugă culoare butonului
        self.button_login.clicked.connect(self.authenticate_user)

        self.button_no_account = QPushButton("Don't have an account? Create one right now!")
        self.button_no_account.setFont(QFont('Times', 8))  # Schimbă fontul și dimensiunea textului
        self.button_no_account.setStyleSheet("background-color: #2E7267; color: white;")  # Adaugă culoare butonului
        self.button_no_account.clicked.connect(self.show_registration_window)

        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.button_login)
        self.layout.addWidget(self.button_no_account)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Adaugă spațiere în partea de jos

        self.setLayout(self.layout)

    def authenticate_user(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if not username or not password:
            QMessageBox.critical(self, "Error", "Both fields must be filled in!")
        else:
            # Creează un manager de acces la rețea
            network_manager = QNetworkAccessManager(self)
            
            # Construiește URL-ul pentru autentificare
            url = QUrl("http://localhost:5000/authenticate_user")
            
            # Construiește cererea
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            
            # Construiește datele JSON pentru autentificare
            data = {"username": username, "password": password}
            
            # Creează și trimite cererea POST
            reply = network_manager.post(request, QByteArray(json.dumps(data).encode('utf-8')))
            
            # Conectează slot-ul de răspuns la cerere
            reply.finished.connect(self.handle_authentication_response)
    
    def handle_authentication_response(self):
        reply = self.sender()
        response_data = json.loads(reply.readAll().data().decode('utf-8'))
        message = response_data.get('message', '')

        if message == "User authenticated successfully":
            QMessageBox.information(self, "Succes", message)
            username = response_data.get('username', '')
            user.login(username)

            self.home_window.check_user()
            self.showHomeWindow.emit()
            self.hide()
        else:
            QMessageBox.critical(self, "Error", message)

    def show_registration_window(self):
        self.showRegistrationWindow.emit()
        self.hide()

class RegistrationWindow(QWidget):
    showLoginWindow = pyqtSignal()

    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat - Create New Account")
        self.layout = QVBoxLayout()
        self.layout.addSpacing(100)

        self.label_title = QLabel("Create a new account right now!")  # Adaugă titlul
        self.label_title.setFont(QFont('Times', 18))  # Schimbă fontul și dimensiunea textului
        self.label_title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_title)

        self.layout.addSpacing(140)

        self.label_username = QLabel("Username:")
        self.entry_username = QLineEdit()

        self.label_password = QLabel("Password:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.label_repassword = QLabel("Re-enter password:")
        self.entry_repassword = QLineEdit()
        self.entry_repassword.setEchoMode(QLineEdit.Password)

        self.button_create_acc = QPushButton("Create your account now!")
        self.button_create_acc.setStyleSheet("background-color: #2fa190; color: white;")  # Adaugă culoare butonului
        self.button_create_acc.clicked.connect(self.create_account)

        self.button_login = QPushButton("Go to Login Page!")
        self.button_login.setStyleSheet("background-color: #2E7267; color: white;")  # Adaugă culoare butonului
        self.button_login.clicked.connect(self.show_login_window)

        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.label_repassword)
        self.layout.addWidget(self.entry_repassword)
        self.layout.addWidget(self.button_create_acc)
        self.layout.addWidget(self.button_login)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(self.layout)
    
    def create_account(self):

        username = self.entry_username.text()
        password = self.entry_password.text()
        repassword = self.entry_repassword.text()

        if not username or not password or not repassword:
            QMessageBox.critical(self, "Error", "All fields must be filled in!")
        elif password != repassword:
            QMessageBox.critical(self, "Error", "Passwords must match!")
        elif username == password and username == repassword:
            QMessageBox.critical(self, "Error", "The password must not match with the username!")
        else:
            # Creează un manager de acces la rețea
            network_manager = QNetworkAccessManager(self)
            
            # Construiește URL-ul pentru autentificare
            url = QUrl("http://localhost:5000//create_user")
            
            # Construiește cererea
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            
            # Construiește datele JSON pentru autentificare
            data = {"username": username, "password": password}
            
            # Creează și trimite cererea POST
            reply = network_manager.post(request, QByteArray(json.dumps(data).encode('utf-8')))
            
            # Conectează slot-ul de răspuns la cerere
            reply.finished.connect(self.handle_create_account_response)

    def handle_create_account_response(self):
        reply = self.sender()
        response_data = json.loads(reply.readAll().data().decode('utf-8'))
        message = response_data.get('message', '')

        if message == "User created successfully!":
            QMessageBox.information(self, "Succes", message)

            self.showLoginWindow.emit()
            self.hide()
        else:
            QMessageBox.critical(self, "Error", message)

    def show_login_window(self):
        self.showLoginWindow.emit()
        self.hide()

class HomeWindow(QWidget):
    showConversationWindow = pyqtSignal()

    def __init__(self):
        super().__init__()

    def check_user(self):
       
        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat - Home")
        self.layout = QVBoxLayout()
        
        self.layout.addSpacing(120)

        self.label_welcome = QLabel(f"Welcome, {user.username}!")  # Adaugă mesajul de bun venit
        self.label_welcome.setFont(QFont('Times', 18))  # Schimbă fontul și dimensiunea textului
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_welcome)

        self.layout.addSpacing(20)

        self.label_prompt = QLabel("Enter the name of the user you want to start a new conversation with!")  # Adaugă prompt-ul
        self.label_prompt.setFont(QFont('Times', 12))  # Schimbă fontul și dimensiunea textului
        self.label_prompt.setAlignment(Qt.AlignCenter)
        self.label_prompt.setWordWrap(True)  # Permite înfășurarea cuvintelor
        self.layout.addWidget(self.label_prompt)

        self.layout.addSpacing(120)

        self.entry_username = QLineEdit()  # Adaugă câmpul pentru introducerea numelui de utilizator

        self.button_start_conversation = QPushButton("Start a conversation!")  # Adaugă butonul pentru începerea unei conversații
        self.button_start_conversation.setStyleSheet("background-color: #2fa190; color: white;")  # Adaugă culoare butonului
        self.button_start_conversation.clicked.connect(self.start_conversation)

        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.button_start_conversation)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # Adaugă spațiere în partea de jos

        self.setLayout(self.layout)


    def start_conversation(self):
        username = self.entry_username.text()

        if not username:
            QMessageBox.critical(self, "Error", "Username field must be filled in!")
        else:
            # Creează un manager de acces la rețea
            network_manager = QNetworkAccessManager(self)
            
            # Construiește URL-ul pentru autentificare
            url = QUrl("http://localhost:5000/check_username")
            
            # Construiește cererea
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            
            # Construiește datele JSON pentru autentificare
            data = {"my_username": user.username, "username": username}
            
            # Creează și trimite cererea POST
            reply = network_manager.post(request, QByteArray(json.dumps(data).encode('utf-8')))
            
            # Conectează slot-ul de răspuns la cerere
            reply.finished.connect(self.handle_conversation_response)

    def handle_conversation_response(self):
        reply = self.sender()
        response_data = json.loads(reply.readAll().data().decode('utf-8'))
        message = response_data.get('message', '')

        if message == "Username exists":
            QMessageBox.information(self, "Succes", message)
            username = response_data.get('username', '')
            user.start_conversation(username)

            self.showConversationWindow.emit()
            self.hide()
        else:
            QMessageBox.critical(self, "Error", message)

class ConversationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Generarea unei chei de criptare
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)

        log_filename = f'{user.username}-{user.conversation_partner}.log'

        # Criptarea numelui fișierului
        encrypted_filename = cipher_suite.encrypt(log_filename.encode('utf-8'))

        # Codificarea numelui fișierului criptat în Base64
        encoded_filename = base64.urlsafe_b64encode(encrypted_filename).decode('utf-8')

        # Verifică dacă fișierul log există și nu este gol
        if os.path.exists(encoded_filename) and os.path.getsize(encoded_filename) > 0:
            # Citirea conversației criptate din fișierul log
            with open(f'logs/{encoded_filename}', 'rb') as f:
                encrypted_conversation = f.read()

            # Decriptarea conversației
            conversation_string = cipher_suite.decrypt(encrypted_conversation).decode('utf-8')
            conversation = json.loads(conversation_string)

            # Afișarea conversației
            print(conversation)
        else:
            # Dacă fișierul log nu există sau este gol, inițializează o conversație goală
            conversation = {'messages': []}

        username = f'{user.username}'

        # Criptarea numelui fișierului
        encrypted_username = cipher_suite.encrypt(username.encode('utf-8'))

        # Codificarea numelui fișierului criptat în Base64
        encoded_username = base64.urlsafe_b64encode(encrypted_username).decode('utf-8')

        new_message = {'username': encoded_username, 'content': None}
        conversation['messages'].append(new_message)

        # Criptarea conversației actualizate
        conversation_string = json.dumps(conversation)
        encrypted_conversation = cipher_suite.encrypt(conversation_string.encode('utf-8'))

        # Stocarea conversației criptate în fișierul log
        with open(f'logs/{encoded_filename}', 'wb') as f:
            f.write(encrypted_conversation)

        # window_width = 600
        # window_height = 700
        # self.resize(window_width, window_height)

        # self.setWindowTitle("QuickChat - Home")
        # self.layout = QVBoxLayout()
        
        # self.layout.addSpacing(120)

        # self.label_welcome = QLabel("conv window}!")  # Adaugă mesajul de bun venit
        # self.label_welcome.setFont(QFont('Times', 18))  # Schimbă fontul și dimensiunea textului
        # self.label_welcome.setAlignment(Qt.AlignCenter)
        # self.layout.addWidget(self.label_welcome)

        # self.setLayout(self.layout)


class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=None):
        super().__init__(text)

    def mousePressEvent(self, event):
        self.clicked.emit()

def start_application():
    app = QApplication([])
    registration_window = RegistrationWindow()
    home_window = HomeWindow()
    login_window = LoginWindow(home_window)
    conversation_window = ConversationWindow()

    # Conectați semnalul din fereastra de autentificare la slotul pentru afișarea fereastra de înregistrare
    login_window.showRegistrationWindow.connect(registration_window.show)
    login_window.showHomeWindow.connect(home_window.show)
    registration_window.showLoginWindow.connect(login_window.show)
    home_window.showConversationWindow.connect(conversation_window.show)

    login_window.show()
    app.exec_()