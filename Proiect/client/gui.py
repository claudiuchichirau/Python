from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, Qt

class LoginWindow(QWidget):
    showRegistrationWindow = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Setează dimensiunile dorite pentru fereastră
        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("QuickChat")
        self.layout = QVBoxLayout()

        self.label_username = QLabel("Utilizator:")
        self.entry_username = QLineEdit()

        self.label_password = QLabel("Parola:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.button_login = QPushButton("Autentificare")
        self.button_login.clicked.connect(self.authenticate_user)

        self.button_no_account = QPushButton("Nu ai cont? Creează unul aici")
        self.button_no_account.clicked.connect(self.show_registration_window)

        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.button_login)
        self.layout.addWidget(self.button_no_account)

        self.setLayout(self.layout)

    def authenticate_user(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if not username or not password:
            QMessageBox.critical(self, "Eroare", "Ambele câmpuri trebuie completate")
        elif not password:
            QMessageBox.critical(self, "Eroare", "Parola nu poate fi goală")
        else:
            QMessageBox.information(self, "Succes", "Autentificare reușită")

    def show_registration_window(self):
        self.showRegistrationWindow.emit()
        self.hide()

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        window_width = 600
        window_height = 700
        self.resize(window_width, window_height)

        self.setWindowTitle("Creare Cont Nou")

        self.layout = QVBoxLayout()

        self.label_username = QLabel("Utilizator:")
        self.entry_username = QLineEdit()

        self.label_password = QLabel("Parola:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.label_repassword = QLabel("Re-Parola:")
        self.entry_repassword = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.Password)

        self.button_create_acc = QPushButton("Creare Cont")
        self.button_create_acc.clicked.connect(self.login_user)

        self.layout.addWidget(self.label_username)
        self.layout.addWidget(self.entry_username)
        self.layout.addWidget(self.label_password)
        self.layout.addWidget(self.entry_password)
        self.layout.addWidget(self.label_repassword)
        self.layout.addWidget(self.entry_repassword)
        self.layout.addWidget(self.button_create_acc)

        self.setLayout(self.layout)
    
    def login_user(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if not username or not password:
            QMessageBox.critical(self, "Eroare", "Ambele câmpuri trebuie completate")
        elif not password:
            QMessageBox.critical(self, "Eroare", "Parola nu poate fi goală")
        else:
            QMessageBox.information(self, "Succes", "Autentificare reușită")

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def __init__(self, text=None):
        super().__init__(text)

    def mousePressEvent(self, event):
        self.clicked.emit()

def create_login_window():
    app = QApplication([])
    login_window = LoginWindow()
    registration_window = RegistrationWindow()

    # Conectați semnalul din fereastra de autentificare la slotul pentru afișarea fereastra de înregistrare
    login_window.showRegistrationWindow.connect(registration_window.show)

    login_window.show()
    app.exec_()