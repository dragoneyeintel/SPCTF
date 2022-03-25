# -*- coding: utf-8 -*-
# "C:\Users\Nick3214\Desktop\SPCTF - Simple Python CTF\venv\Scripts\pyrcc5.exe" -x "C:\Users\Nick3214\Desktop\SPCTF - Simple Python CTF\GUI Implementation\Res.qrc" -o Res_rc.py
# "C:\Users\Nick3214\Desktop\SPCTF - Simple Python CTF\venv\Scripts\pyuic5.exe" -x "C:\Users\Nick3214\Desktop\SPCTF - Simple Python CTF\GUI Implementation\SPCTF.ui" -o SPCTF.py

import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import QObject, pyqtSignal, QEvent
from PyQt5.QtWidgets import QMessageBox, QPlainTextEdit
from requests import get
import socket
import Main_Player_Menu.MPM as MPM
import Challenges_UI.Twisted_Threads.TwistedThreads as Twisted_Threads
import Challenges_UI.Julius.Julius as Julius
import Challenges_UI.FixME.FixME as FixME
import Challenges_UI.ForceME.ForceME as ForceME
import Challenges_UI.RSA.RSA as RSA
import Challenges_UI.DarkMode.DarkMode as DarkMode
import Challenges_UI.Wrongdacted.Wrongdacted as Wrongdacted
import Challenges_UI.Suspicious_Program.SusProg as SusProg
import Challenges_UI.Tight_Pixels.TightPixels as TightPixels
import Challenges_UI.TM.TM as TM
import Challenges_UI.Eighty.Eighty as Eighty
import Challenges_UI.RDP.RDP as RDP
import Challenges_UI.LiedaPro.LiedaPro as LiedaPro
import Challenges_UI.Maze.Maze as Maze
import Challenges_UI.Dictionary.Dictionary as Dictionary
import Challenges_UI.Memory.Memory as Memory
import ChalCpy.TwistedThreads as TwistedThreadsExec
import ChalCpy.Julius as JuliusExec
import ChalCpy.FixME as FixMEExec
import ChalCpy.ForceME as ForceMEExec
import ChalCpy.Wrongdacted as WrongdactedExec
import ChalCpy.Sus as SusExec
import ChalCpy.TP as TPExec
import ChalCpy.TM as TMExec
import ChalCpy.Eighty as EightyExec
import ChalCpy.RDP as RDPExec
import ChalCpy.LP as LPExec
import ChalCpy.Maze as MazeExec
import ChalCpy.Dictionary as DictionaryExec
import ChalCpy.Memory as MemoryExec
import ChalCpy.RSA as RSAExec
import ChalCpy.DRK as DRKExec

import Start_Menu.Res_rc


def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class Start(object):
    def setupUi(self, SPCTF):
        SPCTF.setObjectName("SPCTF")
        SPCTF.setEnabled(True)
        SPCTF.resize(644, 376)
        SPCTF.setMinimumSize(QtCore.QSize(644, 376))
        SPCTF.setMaximumSize(QtCore.QSize(644, 376))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SPCTF Logo/RAW IMG/Dragon_Eye_Intelligence1(S).png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        SPCTF.setWindowIcon(icon)
        SPCTF.setAutoFillBackground(False)
        SPCTF.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/bg.png);")
        self.Join_Server_Button = QtWidgets.QPushButton(SPCTF)
        self.Join_Server_Button.setGeometry(QtCore.QRect(80, 290, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(20)
        self.Join_Server_Button.setFont(font)
        self.Join_Server_Button.setAutoFillBackground(False)
        self.Join_Server_Button.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color2.png);\n"
                                              "color: rgb(38, 38, 38);")
        self.Join_Server_Button.setObjectName("Join_Server_Button")
        self.Create_Server_Button = QtWidgets.QPushButton(SPCTF)
        self.Create_Server_Button.setGeometry(QtCore.QRect(350, 290, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(20)
        self.Create_Server_Button.setFont(font)
        self.Create_Server_Button.setAutoFillBackground(False)
        self.Create_Server_Button.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color2.png);\n"
                                                "color: rgb(38, 38, 38);")
        self.Create_Server_Button.setDefault(False)
        self.Create_Server_Button.setObjectName("Create_Server_Button")
        self.Join_Server_IP = QtWidgets.QPlainTextEdit(SPCTF)
        self.Join_Server_IP.setGeometry(QtCore.QRect(80, 160, 201, 21))
        self.Join_Server_IP.setAutoFillBackground(False)
        self.Join_Server_IP.setStyleSheet("color: rgb(170, 255, 127);\n"
                                          "background-image: url(:/SPCTF Logo/RAW IMG/color.png);")
        self.Join_Server_IP.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Join_Server_IP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Join_Server_IP.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Join_Server_IP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_IP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_IP.setTabChangesFocus(True)
        self.Join_Server_IP.setDocumentTitle("")
        self.Join_Server_IP.setBackgroundVisible(False)
        self.Join_Server_IP.setObjectName("Join_Server_IP")
        self.Join_Server_Port = QtWidgets.QPlainTextEdit(SPCTF)
        self.Join_Server_Port.setGeometry(QtCore.QRect(80, 190, 201, 21))
        self.Join_Server_Port.setAutoFillBackground(True)
        self.Join_Server_Port.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color.png);\n"
                                            "color: rgb(170, 255, 127);")
        self.Join_Server_Port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Join_Server_Port.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Port.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Port.setTabChangesFocus(True)
        self.Join_Server_Port.setBackgroundVisible(True)
        self.Join_Server_Port.setObjectName("Join_Server_Port")
        self.Join_Server_Username = QtWidgets.QPlainTextEdit(SPCTF)
        self.Join_Server_Username.setGeometry(QtCore.QRect(80, 220, 201, 21))
        self.Join_Server_Username.setAutoFillBackground(True)
        self.Join_Server_Username.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color.png);\n"
                                                "color: rgb(170, 255, 127);")
        self.Join_Server_Username.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Join_Server_Username.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Username.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Username.setTabChangesFocus(True)
        self.Join_Server_Username.setBackgroundVisible(True)
        self.Join_Server_Username.setObjectName("Join_Server_Username")
        self.Join_Server_Password = QtWidgets.QPlainTextEdit(SPCTF)
        self.Join_Server_Password.setGeometry(QtCore.QRect(80, 250, 201, 21))
        self.Join_Server_Password.setAutoFillBackground(True)
        self.Join_Server_Password.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color.png);\n"
                                                "color: rgb(170, 255, 127);")
        self.Join_Server_Password.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Join_Server_Password.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Password.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Join_Server_Password.setTabChangesFocus(True)
        self.Join_Server_Password.setBackgroundVisible(True)
        self.Join_Server_Password.setObjectName("Join_Server_Password")
        self.Create_Server_Port = QtWidgets.QPlainTextEdit(SPCTF)
        self.Create_Server_Port.setGeometry(QtCore.QRect(350, 265, 201, 21))
        self.Create_Server_Port.setAutoFillBackground(False)
        self.Create_Server_Port.setStyleSheet("color: rgb(170, 255, 127);\n"
                                              "background-image: url(:/SPCTF Logo/color.png);")
        self.Create_Server_Port.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Create_Server_Port.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Create_Server_Port.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Create_Server_Port.setTabChangesFocus(True)
        self.Create_Server_Port.setBackgroundVisible(True)
        self.Create_Server_Port.setObjectName("Create_Server_Port")
        self.Your_IP = QtWidgets.QTextBrowser(SPCTF)
        self.Your_IP.setGeometry(QtCore.QRect(320, 170, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Your_IP.setFont(font)
        self.Your_IP.setAutoFillBackground(True)
        self.Your_IP.setStyleSheet("color: rgb(170, 255, 127);\n"
                                   "background-image: url(:/SPCTF Logo/color.png);")
        self.Your_IP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Your_IP.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Your_IP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Your_IP.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Your_IP.setObjectName("Your_IP")
        self.LocalIPLabel = QtWidgets.QLabel(SPCTF)
        self.LocalIPLabel.setGeometry(QtCore.QRect(495, 150, 81, 21))
        self.LocalIPLabel.setStyleSheet("color: rgb(170, 255, 127);\n"
                                        "background-image: url(:/SPCTF Logo/color.png);\n"
                                        "border-bottom-color: rgb(25, 25, 25);")
        self.LocalIPLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LocalIPLabel.setObjectName("LocalIPLabel")
        self.Your_IP_2 = QtWidgets.QTextBrowser(SPCTF)
        self.Your_IP_2.setGeometry(QtCore.QRect(320, 230, 256, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Your_IP_2.setFont(font)
        self.Your_IP_2.setAutoFillBackground(True)
        self.Your_IP_2.setStyleSheet("color: rgb(170, 255, 127);\n"
                                     "background-image: url(:/SPCTF Logo/color.png);")
        self.Your_IP_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Your_IP_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Your_IP_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Your_IP_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Your_IP_2.setObjectName("Your_IP_2")
        self.RemoteIPLabel = QtWidgets.QLabel(SPCTF)
        self.RemoteIPLabel.setGeometry(QtCore.QRect(495, 210, 81, 21))
        self.RemoteIPLabel.setStyleSheet("color: rgb(170, 255, 127);\n"
                                         "background-image: url(:/SPCTF Logo/color.png);\n"
                                         "border-bottom-color: rgb(25, 25, 25);")
        self.RemoteIPLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.RemoteIPLabel.setObjectName("RemoteIPLabel")
        self.Join_Server_Button.raise_()
        self.Join_Server_Button.clicked.connect(self.joinConnect)
        self.Create_Server_Button.raise_()
        self.Join_Server_Port.raise_()
        self.Join_Server_Username.raise_()
        self.Join_Server_Password.raise_()
        self.Create_Server_Port.raise_()
        self.Your_IP.raise_()
        self.Join_Server_IP.raise_()
        self.LocalIPLabel.raise_()
        self.Your_IP_2.raise_()
        self.RemoteIPLabel.raise_()

        self.Create_Server_Button.clicked.connect(self.NYI)


        self.retranslateUi(SPCTF)
        QtCore.QMetaObject.connectSlotsByName(SPCTF)

    def NYI(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This Feature Has Not Been Implemented Yet")
        msg.setWindowTitle("Not Yet Implemented")
        msg.setDetailedText("\\0/  NOOT NOOT  \\0/\nNotes: Add View Solution Button - When Click 0 Points Rewarded Will Download MP4 From 32-char Random Link; Once Link Navigated To Disable Points")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def CHK(self):
        input = self.ui.Flag_Input.toPlainText()
        hashed = hashlib.sha512(input.encode())
        hashed = hashed.hexdigest()
        print("Checking... " + str(input) + ":" + str(hashed))
        tmptxt = self.ui.label_2.text()
        self.ui.label_2.setText(tmptxt + "\nChecking... " + str(input) + ":" + str(hashed))

        if((hashed == "c4c94034ddb5dd75289a1c317188a3af2e735da2d380f5d52e4f43754d3e19864d6d732d7add3afef62cabeab088a265b9964a8fefb57900b90a20c77593c95c") |
        (hashed == "d764849c81edc4c4bf99ab32ae3c8164292c92ee0f22cd8a8ba185754e6b06156249911373416b4d4eceefcc0c5955e5d4c93596e88c23698678f64233d654a0") |
        (hashed == "5b4c2d30cfc6fb862a48fae38b6e3f4302bc7246f45656fe42650992a1af8ecfd4353df0d903e832cb00005a314d2d184dc4b2885464f1790e895c742888a004") |
        (hashed == "ded049320695b15b79520fda33d1e48ddf254f48d266cbc95f28899e7865fb03d6c79de82b68324c57dcb01348bc0f59542db5e453aab1f62fedd360af769c6a") |
        (hashed == "e927fc90de8e0e344111ffa11833b6d4891f21f5ba107acc7f6209e9a070ae18627439f54e57ea1199bbbefce99e0fbfc939ea0d39999695cb61f6dcabd2e858") |
        (hashed == "e7d65023e430c4f00387443de3d85225dedbd96b7483a622a0c217ee60ee2888090d6d0590898e4235ea4d998f9a4676c65349a3b9fd70d2debf9f85b32771f3") |
        (hashed == "52e5cf96b7bfd07d5fcd590e5dedbab55132031aca373601fc665b85b52c8ba81c7b7f467b6a1e2da0e8dfb128fbd328d7a7cb204551a0267d6e6f14cdf853df") |
        (hashed == "7a963d02e3531798d6ce1463b9aba747d4162a418b94ec6fd30b71fa84b66d23110365720fa36615d363e2f3b58b1c3940b908997f881faf9413816c4971a0f4") |
        (hashed == "04ed07ddd8116b4ea5a629195ea28fef4f98c4be49787a97c730f72acfa39aae800b7ff5955af106d2aef5a25560f1887ac21a9fbff35850830b8d6752d8882b") |
        (hashed == "a491fc3b695221672f27065b29f4494bbbb8b892d3a6ab824b22acdbb89b45f8bf1704c035feca11cebcc360dff383a26aab324a34134e0ade46d7f6c0999f2f") |
        (hashed == "9ca91bb52097882a6719be8e14304ff189a7e3122d6c0063c17b587c4dfc8b9b47ad7d3ff1ee5dcc38f48306d8b8486ac81a5e3742ada104b1f66e010d146566") |
        (hashed == "da14dccafa242941f5a6235bebc2dc39346dcb9fff3b93b0d405cb678cad79666c7ba650dbe29dc08de677538182e133542246768e56742a41a4ae1325c25f17") |
        (hashed == "b7d40a59853b34d2850bb8d9bde5da8bc4c10ee858987eb5e5a9c0e414150a6050f1b57b1d9e80bf3dec4b99785104834d027b5cd7d08f58d81fae842d5e6e5a") |
        (hashed == "87d2f90512c159563dbfcbcea3963021d95a05a547bdff42473a57ce63d49269616cab3203fcdd98c1c7e461ac200fe62d10863ce048798d96682a513750332c") |
        (hashed == "eea0c26c633b1c4cf921afb3bf1c21d078bad08521d931e1fe06a9210104db8d6df97373add1e755c227f582e1b94e0c2ff043e74eb9e7eb27b32f4289e10e74") |
        (hashed == "aa99388f7290089021a5b80d1c9c6873a1e02be0a1e62534d0143564a2336275c5891b03f9a7b7f288263714e605bbcc2a608e9a5dccfd7115c0c100ece1e6d3")):
            print("Success!")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            text_edit = QPlainTextEdit()
            tmp = open('flag.txt', 'a+')
            tmp.close()
            tmp = open('flag.txt').readlines()
            print(tmp)

            found = 0
            for line in tmp:
                if line == hashed:
                    print("\nAlready Submitted")
                    found = 1
                    break
            if found == 0:
                file = open("flag.txt", "a+")
                file.writelines("\n"+str(hashed))
                file.close()

            msg.setText("GOOD JOB!")
            tmptxt = self.ui.label_2.text()
            self.ui.label_2.setText(tmptxt + "\nGOOD JOB!\n")
            msg.setWindowTitle("SUCCESS!")
            msg.setDetailedText("\\0/  NOOT NOOT  \\0/")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            print("Invalid")
            tmptxt = self.ui.label_2.text()
            self.ui.label_2.setText(tmptxt + "\nInvalid\n")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Try Again")
            msg.setWindowTitle("Invalid")
            msg.setDetailedText("\\0/  NOOT NOOT  \\0/")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def msgBox(self, input):
        for i in input:
            tmptxt = self.ui.label_2.text()
            self.ui.label_2.setText(tmptxt + str(i))
            QtTest.QTest.qWait(50)

    def updatePts(self, i):
        print("Point Check")
        tmp = open('flag.txt', 'a+')
        tmp.close()
        tmp = open('flag.txt').readlines()
        print(tmp)
        num = 0
        for line in tmp:
            if line == "c4c94034ddb5dd75289a1c317188a3af2e735da2d380f5d52e4f43754d3e19864d6d732d7add3afef62cabeab088a265b9964a8fefb57900b90a20c77593c95c":
                num += 5
            if line == "d764849c81edc4c4bf99ab32ae3c8164292c92ee0f22cd8a8ba185754e6b06156249911373416b4d4eceefcc0c5955e5d4c93596e88c23698678f64233d654a0":
                num += 10
            if line == "5b4c2d30cfc6fb862a48fae38b6e3f4302bc7246f45656fe42650992a1af8ecfd4353df0d903e832cb00005a314d2d184dc4b2885464f1790e895c742888a004":
                num += 15
            if line == "ded049320695b15b79520fda33d1e48ddf254f48d266cbc95f28899e7865fb03d6c79de82b68324c57dcb01348bc0f59542db5e453aab1f62fedd360af769c6a":
                num += 20
            if line == "e927fc90de8e0e344111ffa11833b6d4891f21f5ba107acc7f6209e9a070ae18627439f54e57ea1199bbbefce99e0fbfc939ea0d39999695cb61f6dcabd2e858":
                num += 25
            if line == "e7d65023e430c4f00387443de3d85225dedbd96b7483a622a0c217ee60ee2888090d6d0590898e4235ea4d998f9a4676c65349a3b9fd70d2debf9f85b32771f3":
                num += 30
            if line == "52e5cf96b7bfd07d5fcd590e5dedbab55132031aca373601fc665b85b52c8ba81c7b7f467b6a1e2da0e8dfb128fbd328d7a7cb204551a0267d6e6f14cdf853df":
                num += 35
            if line == "7a963d02e3531798d6ce1463b9aba747d4162a418b94ec6fd30b71fa84b66d23110365720fa36615d363e2f3b58b1c3940b908997f881faf9413816c4971a0f4":
                num += 40
            if line == "04ed07ddd8116b4ea5a629195ea28fef4f98c4be49787a97c730f72acfa39aae800b7ff5955af106d2aef5a25560f1887ac21a9fbff35850830b8d6752d8882b":
                num += 45
            if line == "a491fc3b695221672f27065b29f4494bbbb8b892d3a6ab824b22acdbb89b45f8bf1704c035feca11cebcc360dff383a26aab324a34134e0ade46d7f6c0999f2f":
                num += 50
            if line == "9ca91bb52097882a6719be8e14304ff189a7e3122d6c0063c17b587c4dfc8b9b47ad7d3ff1ee5dcc38f48306d8b8486ac81a5e3742ada104b1f66e010d146566":
                num += 55
            if line == "da14dccafa242941f5a6235bebc2dc39346dcb9fff3b93b0d405cb678cad79666c7ba650dbe29dc08de677538182e133542246768e56742a41a4ae1325c25f17":
                num += 60
            if line == "b7d40a59853b34d2850bb8d9bde5da8bc4c10ee858987eb5e5a9c0e414150a6050f1b57b1d9e80bf3dec4b99785104834d027b5cd7d08f58d81fae842d5e6e5a":
                num += 65
            if line == "87d2f90512c159563dbfcbcea3963021d95a05a547bdff42473a57ce63d49269616cab3203fcdd98c1c7e461ac200fe62d10863ce048798d96682a513750332c":
                num += 70
            if line == "eea0c26c633b1c4cf921afb3bf1c21d078bad08521d931e1fe06a9210104db8d6df97373add1e755c227f582e1b94e0c2ff043e74eb9e7eb27b32f4289e10e74":
                num += 75
            if line == "aa99388f7290089021a5b80d1c9c6873a1e02be0a1e62534d0143564a2336275c5891b03f9a7b7f288263714e605bbcc2a608e9a5dccfd7115c0c100ece1e6d3":
                num += 80
        if i == 1:
            self.ui.label.setText("<html><head/><body><p align=\"center\">Points: "+str(num)+"</p></body></html>")
        return num

    def dir1(self):
        TwistedThreadsExec.TwistedThreads(self)
    def dir2(self):
        JuliusExec.Julius(self)
    def dir3(self):
        FixMEExec.FixME(self)
    def dir4(self):
        ForceMEExec.ForceME(self)
    def dir5(self):
        WrongdactedExec.Wrongdacted(self)
    def dir6(self):
        SusExec.Sus(self)
    def dir7(self):
        TPExec.TP(self)
    def dir8(self):
        TMExec.TM(self)
    def dir9(self):
        EightyExec.Eighty(self)
    def dir10(self):
        RDPExec.RDP(self)
    def dir11(self):
        LPExec.LP(self)
    def dir12(self):
        MazeExec.Maze(self)
    def dir13(self):
        DictionaryExec.Dictionary(self)
    def dir14(self):
        MemoryExec.Memory(self)
    def dir15(self):
        RSAExec.RSA(self)
    def dir16(self):
        DRKExec.DRK(self)


    def TwistedThreadsUI(self):
        print("Twisted Threads")
        self.window = QtWidgets.QMainWindow()
        self.ui = Twisted_Threads.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Twisted Threads</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir1)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox(" Twisted Threads\nCategory: Reverse Engineering\nDifficulty: Absolute Beginner\nHint: Google strings command :p\n")

    def JuliusUI(self):
        print("Julius")
        self.window = QtWidgets.QMainWindow()
        self.ui = Julius.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Julius</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir2)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox(" Julius\nCiphertext: rxms{VgXUg5OqmE4d}\nCategory: Cryptography\nDifficulty: Absolute Beginner\nHint: Twelve.\n")

    def FixMEUI(self):
        print("FixME")
        self.window = QtWidgets.QMainWindow()
        self.ui = FixME.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">FixME</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir3)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox(" FixME\nCategory: Programing\nDifficulty: Beginner\nHint: The update we pushed out will not run correctly, can you fix it?\n")

    def ForceMEUI(self):
        print("Force Me!")
        self.window = QtWidgets.QMainWindow()
        self.ui = ForceME.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Force Me</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir4)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox( "Force Me!\nCategory: Brute Forcing & Password Manipulation\nDifficulty: Beginner\nHint: Why be smart when you can brute force?\n")

    def WrongdactedUI(self):
        print("Wrongdacted")
        self.window = QtWidgets.QMainWindow()
        self.ui = Wrongdacted.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Wrongdacted</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir5)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Wrongdacted\nCategory: Stenography\nDifficulty: Beginner\nHint: We stole a message from the company server but it's redacted.\n")

    def SusProgUI(self):
        print("Suspicious Program")
        self.window = QtWidgets.QMainWindow()
        self.ui = SusProg.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Suspicious Program</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir6)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Suspicious Program\nCategory: Threat Hunting\nDifficulty: Beginner Intermediate\nHint: There seems to be a suspicious program running on your \nmachine. Find the program and input the flag in flag{ip:port} format.\n(E.G. flag{x.x.x.x:yyyy})\n")

    def TightPixelsUI(self):
        print("Tight Pixels")
        self.window = QtWidgets.QMainWindow()
        self.ui = TightPixels.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Tight Pixels</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir7)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Tight Pixels\nCategory: Stenography\nDifficulty: Beginner-Intermediate\nHint: Some of these pixels look closer than others.\n")

    def TMUI(self):
        print("TM")
        self.window = QtWidgets.QMainWindow()
        self.ui = TM.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">TM</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir8)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("TM\nCategory: Cryptography\nDifficulty: Beginner-Intermediate\nHint: It's not a trademark but a ****** Machine. (V1A)\n")

    def EightyUI(self):
        print("8086")
        self.window = QtWidgets.QMainWindow()
        self.ui = Eighty.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">8086</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir9)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("8086\nCategory: Programing\nDifficulty: Beginner-Intermediate\nHint: One of our functions seems to halt after only one execution.\n")

    def RDPUI(self):
        print("RDP")
        self.window = QtWidgets.QMainWindow()
        self.ui = RDP.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">RDP</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir10)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("RDP\nCategory: Threat Hunting\nDifficulty: Beginner\nHint: Provide the exploit used in flag{********} format.\n")

    def LiedaProUI(self):
        print("LiedaPro")
        self.window = QtWidgets.QMainWindow()
        self.ui = LiedaPro.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">LiedaPro</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir11)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Lieda Pro\nCategory: Reverse Engineering\nDifficulty: Intermediate\nHint: A boolean jump is a true or false statement which acts\naccordingly.\n")

    def MazeUI(self):
        print("Maze")
        self.window = QtWidgets.QMainWindow()
        self.ui = Maze.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Maze</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir12)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Maze\nCategory: Programing\nDifficulty: Intermediate\nHint: Maze Image (Check Files)\n")

    def DictionaryUI(self):
        print("Dictionary")
        self.window = QtWidgets.QMainWindow()
        self.ui = Dictionary.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Dictionary</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir13)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Dictionary\nCategory: Brute Forcing & Password Manipulation\nDifficulty: Intermediate\nHint: We have identified a user password as two dictionary words \nseparated by an underscore.The SHA256 hash obtained was: \nAF4DFE88F24D551E445C4688413C9F7BBB2D016B9E2F70C987B5CE\nE21FD6DAF4\n")

    def MemoryUI(self):
        print("Memory")
        self.window = QtWidgets.QMainWindow()
        self.ui = Memory.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Memory</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir14)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Memory\nCategory: Threat Hunting\nDifficulty: Intermediate Advanced\nHint: A memory dump of an active session on a suspects computer \nhas been obtained. Find the users user / password combo and \ninput the flag in flag{password} format.\n")

    def RSAUI(self):
        print("RSA")
        self.window = QtWidgets.QMainWindow()
        self.ui = RSA.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">RSA</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir15)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("RSA\nCategory: Cryptography\nDifficulty: Advanced\nHint: I kept getting the error \"key size too small\" so I constructed my\nown version of OpenSSL.\n")

    def DarkModeUI(self):
        print("Dark Mode")
        self.window = QtWidgets.QMainWindow()
        self.ui = DarkMode.Ui_Main_Player_Menu()
        self.ui.setupUi(self.window)
        self.ui.Label.setText(("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Dark Mode</span></p></body></html>"))
        self.window.show()
        self.updatePts(1)
        clickable(self.ui.Download).connect(self.dir16)
        self.ui.BackButton.clicked.connect(self.window.close)
        self.ui.ForwardButton.clicked.connect(self.NYI)
        self.ui.Submit.clicked.connect(self.CHK)
        self.msgBox("Dark Mode\nCategory: Reverse Engineering\nDifficulty: Intermediate Advanced\nHint: Its looking a little bright in here.\n")


    def joinConnect(self):
        self.Join_Server_Button.setParent(None)
        self.Create_Server_Button.setParent(None)
        self.Join_Server_Port.setParent(None)
        self.Join_Server_Username.setParent(None)
        self.Join_Server_Password.setParent(None)
        self.Create_Server_Port.setParent(None)
        self.Your_IP.setParent(None)
        self.Join_Server_IP.setParent(None)
        self.LocalIPLabel.setParent(None)
        self.Your_IP_2.setParent(None)
        self.RemoteIPLabel.setParent(None)

        print("Main Player Menu")
        SPCTF.close()
        ui = MPM.Ui_Main_Player_Menu()
        ui.setupUi(SPCTF)
        print(ui.label.text())
        ui.label.setText("<html><head/><body><p align=\"center\">Points: "+str(self.updatePts(0))+"</p></body></html>")
        SPCTF.show()



        ui.TwistedThreads_Button.clicked.connect(self.TwistedThreadsUI)
        ui.Julius_Button.clicked.connect(self.JuliusUI)
        ui.FixME_Button.clicked.connect(self.FixMEUI)
        ui.Force_Me_Button.clicked.connect(self.ForceMEUI)
        ui.RSA_Button.clicked.connect(self.RSAUI)
        ui.Dark_Mode_Button.clicked.connect(self.DarkModeUI)
        ui.Wrongdacted_Button.clicked.connect(self.WrongdactedUI)
        ui.Suspicious_Program_Button.clicked.connect(self.SusProgUI)
        ui.Tight_Pixels_Button.clicked.connect(self.TightPixelsUI)
        ui.TM_Button.clicked.connect(self.TMUI)
        ui.Eighty_Button.clicked.connect(self.EightyUI)
        ui.RDP_Button.clicked.connect(self.RDPUI)
        ui.Lieda_Pro_Button.clicked.connect(self.LiedaProUI)
        ui.Maze_Button.clicked.connect(self.MazeUI)
        ui.Dictionary_Button.clicked.connect(self.DictionaryUI)
        ui.Memory_Button.clicked.connect(self.MemoryUI)
        ui.ForwardButton.clicked.connect(self.NYI)
        ui.BackButton.clicked.connect(SPCTF.close)





    def retranslateUi(self, SPCTF):
        _translate = QtCore.QCoreApplication.translate
        SPCTF.setWindowTitle(_translate("SPCTF", "SPCTF"))
        self.Join_Server_Button.setText(_translate("SPCTF", "Join Server"))
        self.Create_Server_Button.setText(_translate("SPCTF", "Create Server"))
        self.Join_Server_IP.setPlaceholderText(_translate("SPCTF", "Server IP:"))
        self.Join_Server_Port.setPlaceholderText(_translate("SPCTF", "Server Port:"))
        self.Join_Server_Username.setPlaceholderText(_translate("SPCTF", "Username:"))
        self.Join_Server_Password.setPlaceholderText(_translate("SPCTF", "Password:"))
        self.Create_Server_Port.setPlaceholderText(_translate("SPCTF", "Server Port:"))
        self.Your_IP.setHtml(_translate("SPCTF",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">" + socket.gethostbyname(
                                            socket.gethostname()) + "</span></p></body></html>"))
        self.LocalIPLabel.setText(_translate("SPCTF", "Local IP"))
        self.Your_IP_2.setHtml(_translate("SPCTF",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">" + get(
                                              'https://api.ipify.org').text + "</span></p></body></html>"))
        self.RemoteIPLabel.setText(_translate("SPCTF", "Remote IP"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    SPCTF = QtWidgets.QDialog()
    ui = Start()
    ui.setupUi(SPCTF)
    SPCTF.show()
    sys.exit(app.exec_())
