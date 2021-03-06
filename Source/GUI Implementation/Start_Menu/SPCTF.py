# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\SPCTF.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SPCTF(object):
    def setupUi(self, SPCTF):
        SPCTF.setObjectName("SPCTF")
        SPCTF.setEnabled(True)
        SPCTF.resize(644, 376)
        SPCTF.setMinimumSize(QtCore.QSize(644, 376))
        SPCTF.setMaximumSize(QtCore.QSize(644, 376))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/SPCTF Logo/Dragon_Eye_Intelligence1(S).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.Join_Server_IP.setPlainText("")
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
        self.Join_Server_Port.setPlainText("")
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
        self.Join_Server_Username.setPlainText("")
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
        self.Join_Server_Password.setPlainText("")
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
        self.Create_Server_Port.setPlainText("")
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

        self.retranslateUi(SPCTF)
        QtCore.QMetaObject.connectSlotsByName(SPCTF)
        SPCTF.setTabOrder(self.Join_Server_IP, self.Join_Server_Port)
        SPCTF.setTabOrder(self.Join_Server_Port, self.Join_Server_Username)
        SPCTF.setTabOrder(self.Join_Server_Username, self.Join_Server_Password)
        SPCTF.setTabOrder(self.Join_Server_Password, self.Join_Server_Button)
        SPCTF.setTabOrder(self.Join_Server_Button, self.Your_IP)
        SPCTF.setTabOrder(self.Your_IP, self.Your_IP_2)
        SPCTF.setTabOrder(self.Your_IP_2, self.Create_Server_Port)
        SPCTF.setTabOrder(self.Create_Server_Port, self.Create_Server_Button)

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
        self.Your_IP.setHtml(_translate("SPCTF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">???.??.??.??</span></p></body></html>"))
        self.LocalIPLabel.setText(_translate("SPCTF", "Local IP"))
        self.Your_IP_2.setHtml(_translate("SPCTF", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:17pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">???.??.??.??</span></p></body></html>"))
        self.RemoteIPLabel.setText(_translate("SPCTF", "Remote IP"))
import Res_rc
