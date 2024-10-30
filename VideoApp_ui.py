# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoApp.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(507, 466)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")

        self.gridLayout_2.addWidget(self.image_label, 1, 0, 1, 1)

        self.cams_selector = QComboBox(self.centralwidget)
        self.cams_selector.setObjectName(u"cams_selector")

        self.gridLayout_2.addWidget(self.cams_selector, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 507, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0441\u0442\u0438\u043a\u0430 \u043f\u043b\u0430\u0437\u043c\u0435\u043d\u043d\u044b\u0445 \u043f\u043e\u0442\u043e\u043a\u043e\u0432", None))
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

