import sqlite3
from PyQt5 import QtWidgets


class User_notification(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.buildingLink()

    def buildingLink(self):
        self.link = sqlite3.connect("Managements.db")

        self.cursor = self.link.cursor()

        self.cursor.execute("Create Table If not exists Students(Name TEXT, Lastname TEXT, School_number TEXT, TR_identification_number TEXT)")

        self.link.commit()

        print("ali")

    def init_ui(self):
        self.name = QtWidgets.QLineEdit()
        self.nameLabel = QtWidgets.QLabel("Name")
        self.lastname = QtWidgets.QLineEdit()
        self.lastnameLabel = QtWidgets.QLabel("Lastname")
        self.studentNo = QtWidgets.QLineEdit()
        self.studentNoLabel = QtWidgets.QLabel("School Number")
        self.trIdentification = QtWidgets.QLineEdit()
        self.trIdentificationLabel = QtWidgets.QLabel("TR Identification Number")
        self.add = QtWidgets.QPushButton("Add")
        self.search = QtWidgets.QPushButton("Search")
        self.delete = QtWidgets.QPushButton("Delete")
        self.writingArea = QtWidgets.QLabel("You can do search and delete operations by entering student's school number or T.R. ID number.")

        v_box2 = QtWidgets.QVBoxLayout()
        v_box2.addWidget(self.nameLabel)
        v_box2.addWidget(self.name)
        v_box2.addWidget(self.lastnameLabel)
        v_box2.addWidget(self.lastname)
        v_box2.addWidget(self.studentNoLabel)
        v_box2.addWidget(self.studentNo)
        v_box2.addWidget(self.trIdentificationLabel)
        v_box2.addWidget(self.trIdentification)
        v_box2.addStretch()
        v_box2.addWidget(self.writingArea)
        v_box2.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.add)
        h_box.addStretch()
        h_box.addWidget(self.search)
        h_box.addStretch()
        h_box.addWidget(self.delete)
        h_box.addStretch()

        v_box2.addLayout(h_box)

        self.setLayout(v_box2)

        self.add.clicked.connect(self.studentAdd)
        self.search.clicked.connect(self.studentSearch)
        self.delete.clicked.connect(self.studentDelete)

        self.setGeometry(500, 200, 200, 600)
        self.setWindowTitle("School Registration System")
        self.show()

    def studentAdd(self):
        allRight = 1

        trIdentification = self.trIdentification.text()
        if (len(trIdentification) == 0):
            self.writingArea.setText("Please enter your T.R. ID number.")
            allRight = 0
        elif (len(trIdentification) != 11):
            self.writingArea.setText("T.R. the ID number consists of 11 digits.")
            allRight = 0

        studentNo = self.studentNo.text()
        if (len(studentNo) == 0):
            self.writingArea.setText("Please enter your school number.")
            allRight = 0
        elif (len(studentNo) != 11):
            self.writingArea.setText("School number consists of 11 digits.")
            allRight = 0

        lastname = self.lastname.text()
        if (lastname == ""):
            self.writingArea.setText("Please enter your lastname.")
            allRight = 0

        name = self.name.text()
        if (name == ""):
            self.writingArea.setText("Please enter your name.")
            allRight = 0

        if allRight == 1:
            self.cursor.execute("Insert into Students Values(?, ?, ?, ?)", (name, lastname, studentNo, trIdentification))
            self.name.clear()
            self.lastname.clear()
            self.studentNo.clear()
            self.trIdentification.clear()

        self.link.commit()

    def studentSearch(self):
        if len(self.trIdentification.text()) == 0 and len(self.studentNo.text()) == 0 :
            self.writingArea.setText(
                "For the search process, the student's school number or T.R. enter the ID number.")

        elif len(self.trIdentification.text()) == 11 and len(self.studentNo.text()) == 11:
            self.writingArea.setText(
                "For search and deletion processes, only the student's school number or T.R. enter the ID number.")

        elif len(self.studentNo.text()) != 0 and len(self.studentNo.text()) != 11:
            self.writingArea.setText("In order to search, you must enter the school number by 11 digits.")

        elif len(self.trIdentification.text()) != 0 and len(self.trIdentification.text()) != 11:
            self.writingArea.setText("In order to search, you must enter the T.R. identification number by 11 digits.")

        elif len(self.trIdentification.text()) == 11:
            self.cursor.execute("Select * From Students Where TR_identification_number = ?", (self.trIdentification.text(),))
            student = self.cursor.fetchall()

            if len(student) != 0:
                studentInformations = "Name:\n" + str(student[0][0]) + "\n\n" + "Lastname:\n" + str(
                    student[0][1]) + "\n\n" + "School Number:\n" + str(
                    student[0][2]) + "\n\n" + "T.R. Identification Number:\n" + str(
                    student[0][3]) + "\n\n\n\n"
                self.writingArea.setText(studentInformations)

            else:
                self.writingArea.setText("No student found with the T.R. ID number you entered.")

            self.link.commit()

        elif len(self.studentNo.text()) == 11:
            self.cursor.execute("Select * From Students Where School_number = ?", (self.studentNo.text(),))
            student = self.cursor.fetchall()

            if len(student) != 0:
                studentInformations = "Name:\n" + str(student[0][0]) + "\n\n" + "Lastname:\n" + str(student[0][1]) + \
                    "\n\n" + "School Number:\n" + str(student[0][2]) + "\n\n" + "T.R. Identification Number:\n" + str(
                    student[0][3]) + "\n\n\n\n"
                self.writingArea.setText(studentInformations)

            else:
                self.writingArea.setText("No student found with the school number you entered.")

            self.link.commit()

    def studentDelete(self):
        if len(self.trIdentification.text()) == 0 and len(self.studentNo.text()) == 0 :
            self.writingArea.setText(
                "For the deletion process, the student's school number or T.R. enter the ID number.")

        elif len(self.trIdentification.text()) == 11 and len(self.studentNo.text()) == 11:
            self.writingArea.setText(
                "For search and deletion processes, only the student's school number or T.R. enter the ID number.")

        elif len(self.studentNo.text()) != 0 and len(self.studentNo.text()) != 11:
            self.writingArea.setText("In order to search, you must enter the school number by 11 digits.")

        elif len(self.trIdentification.text()) != 0 and len(self.trIdentification.text()) != 11:
            self.writingArea.setText("In order to search, you must enter the T.R. identification number by 11 digits.")

        elif len(self.trIdentification.text()) == 11:
            self.cursor.execute("Select * From Students Where TC_kimlik_no = ?", (self.trIdentification.text(),))
            student = self.cursor.fetchall()

            if len(student) != 0:
                self.cursor.execute("Delete From Students Where TC_kimlik_no = ?", (self.trIdentification.text(),))
                studentInformations = "Name:\n" + str(student[0][0]) + "\n\n" + "Lastname:\n" + str(student[0][1]) + \
                "\n\n" + "School Number:\n" + str(student[0][2]) + "\n\n" + "T.R. Identification Number:\n" + str(
                student[0][3]) + "\n\n\ndeleted the student that has informations." + "\n\n\n\n"\

                self.writingArea.setText(studentInformations)

            else:
                self.writingArea.setText("No student found with the T.R. ID number you entered.")

        elif len(self.studentNo.text()) == 11:
            self.cursor.execute("Select * From Students Where School_number = ?", (self.studentNo.text(),))
            student = self.cursor.fetchall()

            if len(student) != 0:
                self.cursor.execute("Delete From Students Where School_number = ?", (self.studentNo.text(),))
                studentInformations = "Name:\n" + str(student[0][0]) + "\n\n" + "Lastname:\n" + str(student[0][1]) + \
                    "\n\n" + "School Number:\n" + str(student[0][2]) + "\n\n" + "T.R. Identification No:\n" + str(
                    student[0][3]) + "\n\n\ndeleted the student that has informations." + "\n\n\n\n"

                self.writingArea.setText(studentInformations)

            else:
                self.writingArea.setText("No student found with the school number you entered.")

            self.link.commit()
