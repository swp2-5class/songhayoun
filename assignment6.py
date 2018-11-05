import pickle
import sys
from PyQt5.QtWidgets import *


class Score(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.Text = ""
        self.key = "Name"

        self.nameedit = QLineEdit()
        self.ageedit = QLineEdit()
        self.scoreedit = QLineEdit()
        self.amountedit = QLineEdit()

        self.keycombo = QComboBox()
        self.keycombo.addItems(["Name", "Age", "Score"])

        addbtn = QPushButton("Add")
        Delbtn = QPushButton("Del")
        findbtn = QPushButton("Find")
        incbtn = QPushButton("Inc")
        showbtn = QPushButton("Show")

        namelb = QLabel("Name:")
        agelb = QLabel("Age:")
        scorelb = QLabel("Score:")
        amountlb = QLabel("Amount:")
        keylb = QLabel("Key:")
        resultlb = QLabel("Result:")
        nonelb = QLabel("")

        self.resultedit = QTextEdit()

        # 1번쨰 줄
        grid.addWidget(namelb, 0, 0)
        grid.addWidget(self.nameedit, 0, 1)
        grid.addWidget(agelb, 0, 2)
        grid.addWidget(self.ageedit, 0, 3)
        grid.addWidget(scorelb, 0, 4)
        grid.addWidget(self.scoreedit, 0, 5)

        # 2번째 줄
        grid.addWidget(nonelb, 1, 0)
        grid.addWidget(nonelb, 1, 1)
        grid.addWidget(amountlb, 1, 2)
        grid.addWidget(self.amountedit, 1, 3)
        grid.addWidget(keylb, 1, 4)
        grid.addWidget(self.keycombo, 1, 5)

        # 3번째 줄
        grid.addWidget(nonelb, 2, 0)
        grid.addWidget(addbtn, 2, 1)
        grid.addWidget(Delbtn, 2, 2)
        grid.addWidget(findbtn, 2, 3)
        grid.addWidget(incbtn, 2, 4)
        grid.addWidget(showbtn, 2, 5)

        # 4번째 줄
        grid.addWidget(resultlb, 3, 0)

        # 5번째 줄
        grid.addWidget(self.resultedit, 4, 0, 3, 6)

        # 버튼 실행
        addbtn.clicked.connect(self.addScoreDB)
        showbtn.clicked.connect(self.showScoreDB)
        incbtn.clicked.connect(self.incScoreDB)
        Delbtn.clicked.connect(self.delScoreDB)
        findbtn.clicked.connect(self.findScoreDB)

        self.setLayout(grid)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def findScoreDB(self):
        Text = ""
        scdb = self.scoredb
        name = self.nameedit.text()
        a = 0
        if name == "":
            self.resultedit.setText("이름은 공란일 수 없습니다.")
        else:
            for p in sorted(scdb, key=lambda person: person["Name"]):
                if p["Name"] == name:
                    a += 1
                    for attr in sorted(p):
                        Text += attr + "=" + str(p[attr]) + "\t"
                    Text += "\n"
            if a == 0:
                Text =  name + " 이/가 없습니다."
                Text+="\n"
                Text+="--- 학생 전체 목록 ---"
                Text+="\n"
            for p in sorted(scdb, key=lambda person: person["Name"]):
                if p["Name"] != name:
                    for attr in sorted(p):
                        Text += attr + "=" + str(p[attr]) + "\t"
                    Text += "\n"
            self.resultedit.setText(Text)

    def delScoreDB(self):
        scdb = self.scoredb
        name = self.nameedit.text()
        a = True
        if name == "":
            self.resultedit.setText("이름을 입력해 주세요.")
        else:
            while (a):
                if scdb == []:
                    a = False
                    break
                for i in scdb:
                    if i["Name"] == name:
                        scdb.remove(i)
                        continue
                    else:
                        a = False
            self.showScoreDB()

    def incScoreDB(self):
        name = self.nameedit.text()
        amount = self.amountedit.text()
        scdb = self.scoredb
        if name == "":
            self.resultedit.setText("이름을 입력해 주세요.")
        elif amount == "":
            self.resultedit.setText("Amount를 입력해 주세요")
        else:
            for i in scdb:
                if i["Name"] == name:
                    i["Score"] += int(amount)
            self.showScoreDB()

    def addScoreDB(self):
        scdb = self.scoredb
        name = self.nameedit.text()
        age = self.ageedit.text()
        score = self.scoreedit.text()
        if name == "":
            self.resultedit.setText("이름을 입력해 주세요.")
        elif age == "":
            self.resultedit.setText("나이를 입력해 주세요.")
        elif score == "":
            self.resultedit.setText("점수를 입력해 주세요.")
        else:
            record = {"Name": name, "Age": age, "Score": score}
            scdb += [record]
            self.showScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        self.Text = ""
        self.resultedit.setText(self.Text)
        key = self.keycombo.currentText()