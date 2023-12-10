import json
import os
import base64
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDesktopWidget, QSpacerItem, QSizePolicy, QTextEdit
from PyQt5.QtCore import pyqtSignal, Qt, QUrl, QByteArray, QEventLoop
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

    def __init__(self, conversation_window):
        super().__init__()
        self.conversation_window = conversation_window

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

            self.conversation_window.conversation()
            self.showConversationWindow.emit()
            self.hide()
        else:
            QMessageBox.critical(self, "Error", message)

class ConversationWindow(QWidget):
    key_received = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.key = None 

        self.layout = QVBoxLayout()

        # Adăugați un widget de afișare a mesajelor
        self.message_display = QTextEdit()
        self.message_display.setReadOnly(True)
        self.layout.addWidget(self.message_display)

        # Adăugați un widget de introducere a mesajelor
        self.message_entry = QLineEdit()
        self.layout.addWidget(self.message_entry)

        # Definește butonul de trimitere a mesajelor
        self.button_start_conversation = QPushButton("Send")

        # Conectați slotul de trimitere a mesajelor la butonul de trimitere
        self.button_start_conversation.clicked.connect(self.send_message)

        # Adăugați butonul la layout
        self.layout.addWidget(self.button_start_conversation)

        self.setLayout(self.layout)

    def conversation(self):
        # Sortează alfabetic numele de utilizator
        sorted_usernames = sorted([user.username, user.conversation_partner])

        # Generează numele fișierului
        log_filename = f'{sorted_usernames[0]}-{sorted_usernames[1]}.log'

        # Verifică dacă fișierul log există și nu este gol
        if os.path.exists(f'logs/{log_filename}') and os.path.getsize(f'logs/{log_filename}') > 0:
            print("fis exista")

            # Citirea conversației criptate din fișierul log
            with open(f'logs/{log_filename}', 'rb') as f:
                encrypted_conversation = f.read()

            print("encr conv:", encrypted_conversation)

            # obtine cheia de decriptare din db
            key = self.get_key()

            # Decriptarea conversației
            cipher_suite = Fernet(key)
            conversation_string = cipher_suite.decrypt(encrypted_conversation).decode('utf-8')
            print("conv citita din fisier:", conversation_string)

            # Încărcarea conversației dintr-un șir XML
            root = ET.fromstring(conversation_string)
            conversation = [message.attrib for message in root.findall('message')]

        elif not os.path.exists(f'logs/{log_filename}'):
            print("fis nu exista")

            # Generarea unei chei de criptare
            key = Fernet.generate_key()
            cipher_suite = Fernet(key)

            # Convertirea cheii într-un șir
            key_str = key.decode()

            # salvarea key-ul in database
            network_manager = QNetworkAccessManager(self)
            url = QUrl("http://localhost:5000/store_key")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            data = {"username1": user.username, "username2": user.conversation_partner, "key": key_str}
            reply = network_manager.post(request, QByteArray(json.dumps(data).encode('utf-8')))

        print("conversatia salvata in fisier:", conversation)

        # obtinem cheia de criptare din database
        key = self.get_key()

        # criptam conversatia cu cheia obtinuta din db
        cipher_suite = Fernet(key)

        # Crearea unui șir XML din conversație
        root = ET.Element('conversation')
        for message in conversation:
            message_element = ET.SubElement(root, 'message')
            message_element.text = message
        conversation_string = ET.tostring(root, encoding='utf-8')

        # Criptarea șirului XML cu obiectul Fernet
        encrypted_conversation = cipher_suite.encrypt(conversation_string)

        # Stocarea conversației criptate în fișierul log
        with open(f'logs/{log_filename}', 'wb') as f:
            f.write(encrypted_conversation)

    def get_key(self):
        network_manager = QNetworkAccessManager(self)
        url = QUrl("http://localhost:5000/get_key")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        data = {"username1": user.username, "username2": user.conversation_partner}
        reply = network_manager.post(request, QByteArray(json.dumps(data).encode('utf-8')))
        reply.finished.connect(self.handle_get_key)

        self.loop = QEventLoop()
        reply.finished.connect(self.handle_get_key)
        self.loop.exec_()  # start the event loop
        print("1. Key received:", self.key)
        return self.key

    def handle_get_key(self):
        reply = self.sender()
        response_str = reply.readAll().data().decode('utf-8')

        if response_str.strip():  # check if the response is not empty
            try:
                response_data = json.loads(response_str)
            except json.JSONDecodeError:
                print("Invalid JSON received:", response_str)
                return

            if 'key' in response_data:
                self.key = response_data.get('key', '')
                self.loop.quit()  # quit the event loop
            else:
                message = response_data['message']
                QMessageBox.critical(self, "Error", message)
        else:
            print("No response received.")


        # if 'key' in response_data:
        #     self.key = response_data.get('key', '') 
        #     self.key_received.emit()  # emit the signal

        # else:
        #     QMessageBox.critical(self, "Error", message)

    def load_messages_from_xml(self, filename):
        # Încărcați și analizați fișierul XML
        tree = ET.parse(filename)
        root = tree.getroot()

        # Parcurgeți fiecare mesaj din fișierul XML
        for message in root.findall('message'):
            sender = message.find('sender').text
            hour = message.find('hour').text
            content = message.find('content').text

            # Adăugați mesajul la afișaj
            self.add_message_to_display(sender, hour, content)

    def add_message_to_display(self, sender, hour, content):
        # Formatați mesajul
        message_str = f'{hour} {sender}: {content}\n'

        # Adăugați mesajul la afișaj
        self.message_display.append(message_str)

    def send_message(self):
        # Obțineți mesajul introdus de utilizator
        message = self.message_entry.text()

        # Adăugați mesajul la afișaj
        self.add_message_to_display(user.username, 'now', message)

        # Goliți câmpul de introducere a mesajelor
        self.message_entry.clear()

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=None):
        super().__init__(text)

    def mousePressEvent(self, event):
        self.clicked.emit()

def start_application():
    app = QApplication([])
    registration_window = RegistrationWindow()
    conversation_window = ConversationWindow()
    home_window = HomeWindow(conversation_window)
    login_window = LoginWindow(home_window)

    # Conectați semnalul din fereastra de autentificare la slotul pentru afișarea fereastra de înregistrare
    login_window.showRegistrationWindow.connect(registration_window.show)
    login_window.showHomeWindow.connect(home_window.show)
    registration_window.showLoginWindow.connect(login_window.show)
    home_window.showConversationWindow.connect(conversation_window.show)

    login_window.show()
    app.exec_()