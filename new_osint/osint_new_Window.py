# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(474, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 40, 341, 31))
        self.lineEdit.setStyleSheet(u"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(62, 110, 341, 31))
        self.lineEdit_2.setStyleSheet(u"border-radius: 6px;\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 10, 291, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 90, 301, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 150, 131, 16))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(180, 170, 98, 41))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(180, 200, 98, 24))
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(180, 220, 98, 24))
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(180, 240, 98, 24))
        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(180, 260, 98, 24))
        self.radioButton_6 = QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(180, 280, 141, 24))
        self.radioButton_7 = QRadioButton(self.centralwidget)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(180, 300, 151, 24))
        self.radioButton_8 = QRadioButton(self.centralwidget)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(180, 320, 98, 24))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(230, 350, 191, 16))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(240, 370, 151, 24))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(240, 400, 141, 24))
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(240, 430, 121, 24))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 480, 221, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color: rgb(16, 255, 72);\n"
"border-radius: 10px;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Google Dorks GUI", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0430\u0439\u0442 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u0444\u0430\u0439\u043b\u0430:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"WORD DOC", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"WORD DOCX", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"EXCEL XLS", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"EXCEL XLSX", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"POWER POINT PPT", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"POWER POINT PPTX", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"TEXT TXT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043f\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043e\u043f\u0435\u0440\u0430\u0442\u043e\u0440\u044b: ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"intitle (\u0432 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0435)", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"inurl (\u0432 \u0430\u0434\u0440\u0435\u0441\u0435)", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"intext (\u0432 \u0442\u0435\u043a\u0441\u0442\u0435)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\U0001f50d \U0000041f\U0000043e\U00000438\U00000441\U0000043a \U00000432 Google", None))
    # retranslateUi

