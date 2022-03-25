# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\LIMITLESS.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Player_Menu(object):
    def setupUi(self, Main_Player_Menu):
        Main_Player_Menu.setObjectName("Main_Player_Menu")
        Main_Player_Menu.resize(644, 375)
        Main_Player_Menu.setMinimumSize(QtCore.QSize(644, 375))
        Main_Player_Menu.setMaximumSize(QtCore.QSize(644, 375))
        Main_Player_Menu.setStyleSheet("background-image: url(:/SPCTF Logo/SourceSpace2.jpg);")
        self.label = QtWidgets.QLabel(Main_Player_Menu)
        self.label.setGeometry(QtCore.QRect(71, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/SPCTF Logo/color.png);")
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setObjectName("label")
        self.BackButton = QtWidgets.QPushButton(Main_Player_Menu)
        self.BackButton.setGeometry(QtCore.QRect(5, 12, 61, 36))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.BackButton.setFont(font)
        self.BackButton.setStyleSheet("background-image: url(:/SPCTF Logo/color.png);\n"
"image: url(:/SPCTF Logo/LeftArrow.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 11px;\n"
"border-color: white;\n"
"padding: 3px;\n"
"color: rgb(255, 255, 255);")
        self.BackButton.setText("")
        self.BackButton.setObjectName("BackButton")
        self.ForwardButton = QtWidgets.QPushButton(Main_Player_Menu)
        self.ForwardButton.setGeometry(QtCore.QRect(577, 12, 61, 36))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.ForwardButton.setFont(font)
        self.ForwardButton.setStyleSheet("background-image: url(:/SPCTF Logo/color.png);\n"
"image: url(:/SPCTF Logo/RightArrow.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 11px;\n"
"border-color: white;\n"
"padding: 3px;\n"
"color: rgb(255, 255, 255);")
        self.ForwardButton.setText("")
        self.ForwardButton.setObjectName("ForwardButton")
        self.label_2 = QtWidgets.QLabel(Main_Player_Menu)
        self.label_2.setGeometry(QtCore.QRect(10, 57, 335, 311))
        self.label_2.setStyleSheet("color: rgb(85, 255, 127);\n"
"background-image: url(:/SPCTF Logo/color.png);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.Label = QtWidgets.QLabel(Main_Player_Menu)
        self.Label.setGeometry(QtCore.QRect(351, 84, 286, 31))
        self.Label.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/SPCTF/RAW IMG/color.png);")
        self.Label.setFrameShape(QtWidgets.QFrame.Panel)
        self.Label.setTextFormat(QtCore.Qt.RichText)
        self.Label.setObjectName("Label")
        self.Download = QtWidgets.QLabel(Main_Player_Menu)
        self.Download.setGeometry(QtCore.QRect(350, 175, 286, 31))
        self.Download.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(170, 0, 255);\n"
"background-image: url(:/SPCTF/RAW IMG/color.png);")
        self.Download.setFrameShape(QtWidgets.QFrame.Panel)
        self.Download.setTextFormat(QtCore.Qt.RichText)
        self.Download.setObjectName("Download")
        self.Submit = QtWidgets.QPushButton(Main_Player_Menu)
        self.Submit.setGeometry(QtCore.QRect(375, 301, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Submit.setFont(font)
        self.Submit.setAutoFillBackground(False)
        self.Submit.setStyleSheet("background-image: url(:/SPCTF Logo/RAW IMG/color.png);\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-radius: 11px;\n"
"border-color: white;\n"
"padding: 3px;\n"
"color: rgb(255, 255, 255);")
        self.Submit.setObjectName("Submit")
        self.Flag_Input = QtWidgets.QTextEdit(Main_Player_Menu)
        self.Flag_Input.setGeometry(QtCore.QRect(351, 210, 284, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Flag_Input.setFont(font)
        self.Flag_Input.setStyleSheet("background-color: rgb(25, 25, 25);\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/SPCTF/RAW IMG/color.png);")
        self.Flag_Input.setObjectName("Flag_Input")

        self.retranslateUi(Main_Player_Menu)
        QtCore.QMetaObject.connectSlotsByName(Main_Player_Menu)

    def retranslateUi(self, Main_Player_Menu):
        _translate = QtCore.QCoreApplication.translate
        Main_Player_Menu.setWindowTitle(_translate("Main_Player_Menu", "SPCTF"))
        self.label.setText(_translate("Main_Player_Menu", "<html><head/><body><p align=\"center\">Points: XXX</p></body></html>"))
        self.label_2.setText(_translate("Main_Player_Menu", "> "))
        self.Label.setText(_translate("Main_Player_Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Title</span></p></body></html>"))
        self.Download.setText(_translate("Main_Player_Menu", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">🡻 Files 🡻</span></p></body></html>"))
        self.Submit.setText(_translate("Main_Player_Menu", "Submit"))
        self.Flag_Input.setHtml(_translate("Main_Player_Menu", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">flag{}</p></body></html>"))
