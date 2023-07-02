from notification import User_notification
import sys
import sqlite3
from PyQt5 import QtWidgets
import time


class User_login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.buildingLink()

    def buildingLink(self):
        self.link = sqlite3.connect("Managements.db")
        self.cursor = self.link.cursor()
        self.cursor.execute("Create Table If not exists Teachers(Username TEXT, Password TEXT)")

        self.link.commit()

    def init_ui(self):
        self.usernameLabel = QtWidgets.QLabel("Username")
        self.username = QtWidgets.QLineEdit()
        self.passwordLabel = QtWidgets.QLabel("Password")
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.writingArea = QtWidgets.QLabel()

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.usernameLabel)
        v_box.addWidget(self.username)
        v_box.addWidget(self.passwordLabel)
        v_box.addWidget(self.password)
        v_box.addWidget(self.login)
        v_box.addStretch()
        v_box.addWidget(self.writingArea)
        v_box.addStretch()

        self.setLayout(v_box)

        self.login.clicked.connect(self.Login)

        self.setGeometry(900, 200, 320, 250)

        self.setWindowTitle("School Registration System")

        self.show()

    def Login(self):
        if self.username.text() != "" and self.password.text() != "":
            self.cursor.execute("Select * From Teachers Where Username = ? and Password = ?",
                                (self.username.text(), self.password.text()))
            user = str(self.cursor.fetchall())

            if user != "[]":
                self.close()
                time.sleep(2)
                self.user_notification = User_notification()

            else:
                self.writingArea.setText("The username or password you entered is incorrect.")

        else:
            self.writingArea.setText("Please fill in the username and password section.")

app = QtWidgets.QApplication(sys.argv)
user_login = User_login()
sys.exit(app.exec_())

