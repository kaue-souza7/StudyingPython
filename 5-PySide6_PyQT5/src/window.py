# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 639)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 781, 531))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelResult = QLabel(self.gridLayoutWidget)
        self.labelResult.setObjectName(u"labelResult")
        font = QFont()
        font.setPointSize(40)
        self.labelResult.setFont(font)

        self.gridLayout.addWidget(self.labelResult, 0, 0, 1, 1, Qt.AlignHCenter) # type: ignore

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelName = QLabel(self.gridLayoutWidget)
        self.labelName.setObjectName(u"labelName")
        font1 = QFont()
        font1.setPointSize(20)
        self.labelName.setFont(font1)

        self.gridLayout_2.addWidget(self.labelName, 0, 0, 1, 1)

        self.lineName = QLineEdit(self.gridLayoutWidget)
        self.lineName.setObjectName(u"lineName")
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(False)
        self.lineName.setFont(font2)

        self.gridLayout_2.addWidget(self.lineName, 0, 1, 1, 1)

        self.buttonSend = QPushButton(self.gridLayoutWidget)
        self.buttonSend.setObjectName(u"buttonSend")
        font3 = QFont()
        font3.setPointSize(30)
        self.buttonSend.setFont(font3)

        self.gridLayout_2.addWidget(self.buttonSend, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"NOTHING HERE", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"SEU NOME: ", None))
        self.lineName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu Nome", None))
        self.buttonSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

