import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, Qt, QUrl, QByteArray
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

import pygame
from pygame.locals import *

class LoginWindow:
    def __init__(self):
        pygame.init()

        # Setează dimensiunile dorite pentru fereastră
        window_width = 600
        window_height = 700
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("QuickChat - Login")

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font('./ui/fonts/BlanksscriptpersonaluseBdit-jEM6O', 36)

        self.username_label = self.create_text("Username:", (window_width/2, window_height/2 - 70))
        self.username_input = pygame.Rect(window_width/2 - 70, window_height/2 - 50, 140, 32)
        self.password_label = self.create_text("Password:", (window_width/2, window_height/2))
        self.password_input = pygame.Rect(window_width/2 - 70, window_height/2 + 20, 140, 32)
        self.login_button_text = self.create_text("Login", (window_width/2, window_height/2 + 70))
        self.login_button = pygame.Rect(window_width/2 - 70, window_height/2 + 50, 140, 32)  # Crează un Rect pentru butonul de login

        self.entry_username = ""
        self.entry_password = ""

    def create_text(self, text, position):
        text_surface = self.font.render(text, True, (255, 255, 255))
        return text_surface, text_surface.get_rect(center=position)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if self.username_input.collidepoint(event.pos):
                        self.get_input("username")
                    elif self.password_input.collidepoint(event.pos):
                        self.get_input("password")
                    elif self.login_button.collidepoint(event.pos):  # Verifică dacă butonul de login a fost apăsat
                        self.authenticate_user()

            self.screen.fill((100, 100, 100))  # Modifică culoarea de fundal

            self.screen.blit(*self.username_label)
            pygame.draw.rect(self.screen, (255, 255, 255), self.username_input, 2)
            self.screen.blit(*self.password_label)
            pygame.draw.rect(self.screen, (255, 255, 255), self.password_input, 2)
            pygame.draw.rect(self.screen, (0, 255, 0), self.login_button)  # Diferențiază butonul de celelalte elemente
            self.screen.blit(*self.login_button_text)

            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def get_input(self, field):
        input_box = ""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        if field == "username":
                            self.entry_username = input_box
                        elif field == "password":
                            self.entry_password = input_box
                        return
                    elif event.key == K_BACKSPACE:
                        input_box = input_box[:-1]
                    else:
                        input_box += event.unicode

            self.screen.fill((100, 100, 100))  # Modifică culoarea de fundal
            pygame.draw.rect(self.screen, (255, 255, 255), self.username_input, 2)
            pygame.draw.rect(self.screen, (255, 255, 255), self.password_input, 2)
            text_surface = self.font.render(input_box, True, (255, 255, 255))
            width = max(200, text_surface.get_width()+10)
            input_box_rect = pygame.Rect(window_width/2 - 70, window_height/2 - 50 if field == "username" else window_height/2 + 20, width, 32)
            pygame.draw.rect(self.screen, (255, 255, 255), input_box_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.password_input, 2)
            pygame.display.flip()
            self.clock.tick(30)

    def authenticate_user(self):
        if not self.entry_username or not self.entry_password:
            print("Both fields must be filled in!")
        else:
            # Emite semnalul pentru autentificare reușită
            self.showHomeWindow()



class RegistrationWindow(QWidget):
    showLoginWindow = pyqtSignal()

    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat - Create New Account")

        self.layout = QVBoxLayout()

        self.label_username = QLabel("Username:")
        self.entry_username = QLineEdit()

        self.label_password = QLabel("Password:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.label_repassword = QLabel("Re-enter password:")
        self.entry_repassword = QLineEdit()
        self.entry_repassword.setEchoMode(QLineEdit.Password)

        self.button_create_acc = QPushButton("Create your account now!")
        self.button_create_acc.clicked.connect(self.create_account)

        self.button_login = QPushButton("Go to Login Page!")
        self.button_login.clicked.connect(self.show_login_window)

        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.label_repassword)
        self.layout.addWidget(self.entry_repassword)
        self.layout.addWidget(self.button_create_acc)
        self.layout.addWidget(self.button_login)

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
    def __init__(self):
        super().__init__()

        # Setează dimensiunile dorite pentru fereastră
        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat - Home")
        self.layout = QVBoxLayout()

        # Adaugă textul și câmpul pentru introducerea numelui de utilizator
        label_welcome = QLabel("Open / Start a new conversation right now!")
        label_enter_username = QLabel("Enter the username of the person you want to chat with")
        self.entry_username = QLineEdit()

        # Adaugă butonul pentru deschiderea conversației
        button_open_conversation = QPushButton("Open Conversation")
        button_open_conversation.clicked.connect(self.open_conversation)

        # Adaugă elementele în layout
        self.layout.addWidget(label_welcome)
        self.layout.addWidget(label_enter_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(button_open_conversation)

        self.setLayout(self.layout)
    
    def open_conversation(self):
        # Aici poți adăuga logica pentru deschiderea unei noi conversații
        # Poți accesa username-ul introdus de utilizator folosind self.entry_username.text()
        QMessageBox.information(self, "Info", "Conversation opened with {}".format(self.entry_username.text()))

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=None):
        super().__init__(text)

    def mousePressEvent(self, event):
        self.clicked.emit()

def start_application():
    app = QApplication([])
    login_window = LoginWindow()
    registration_window = RegistrationWindow()
    home_window = HomeWindow()

    # Conectați semnalul din fereastra de autentificare la slotul pentru afișarea fereastra de înregistrare
    # login_window.showRegistrationWindow.connect(registration_window.show)
    # login_window.showHomeWindow.connect(home_window.show)
    # registration_window.showLoginWindow.connect(login_window.show)

    # login_window.show()
    login_window.run()
    app.exec_()