# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(1182, 651)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 1181, 651))
        self.widget.setStyleSheet(u"background-color: none;\n"
"color: white;")
        self.layoutWidget = QWidget(self.widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1188, 661))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.output = QLabel(self.layoutWidget)
        self.output.setObjectName(u"output")
        self.output.setMaximumSize(QSize(16777215, 100))
        self.output.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.output)

        self.button_e = QPushButton(self.layoutWidget)
        self.button_e.setObjectName(u"button_e")
        self.button_e.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"font-size: 25pt\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout.addWidget(self.button_e)

        self.button_t = QPushButton(self.layoutWidget)
        self.button_t.setObjectName(u"button_t")
        self.button_t.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"font-size: 30pt\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout.addWidget(self.button_t)

        self.third_row = QHBoxLayout()
        self.third_row.setObjectName(u"third_row")
        self.button_7 = QPushButton(self.layoutWidget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.third_row.addWidget(self.button_7)

        self.button_8 = QPushButton(self.layoutWidget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.third_row.addWidget(self.button_8)

        self.button_9 = QPushButton(self.layoutWidget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.third_row.addWidget(self.button_9)

        self.button_d = QPushButton(self.layoutWidget)
        self.button_d.setObjectName(u"button_d")
        self.button_d.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.third_row.addWidget(self.button_d)

        self.button_c = QPushButton(self.layoutWidget)
        self.button_c.setObjectName(u"button_c")
        self.button_c.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.third_row.addWidget(self.button_c)


        self.verticalLayout.addLayout(self.third_row)

        self.second_row = QHBoxLayout()
        self.second_row.setObjectName(u"second_row")
        self.button_4 = QPushButton(self.layoutWidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.second_row.addWidget(self.button_4)

        self.button_5 = QPushButton(self.layoutWidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.second_row.addWidget(self.button_5)

        self.button_6 = QPushButton(self.layoutWidget)
        self.button_6.setObjectName(u"button_6")
        self.button_6.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.second_row.addWidget(self.button_6)

        self.button_x = QPushButton(self.layoutWidget)
        self.button_x.setObjectName(u"button_x")
        self.button_x.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.second_row.addWidget(self.button_x)

        self.button_m = QPushButton(self.layoutWidget)
        self.button_m.setObjectName(u"button_m")
        self.button_m.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.second_row.addWidget(self.button_m)


        self.verticalLayout.addLayout(self.second_row)

        self.first_row = QHBoxLayout()
        self.first_row.setObjectName(u"first_row")
        self.button_0 = QPushButton(self.layoutWidget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.first_row.addWidget(self.button_0)

        self.button_1 = QPushButton(self.layoutWidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.first_row.addWidget(self.button_1)

        self.button_2 = QPushButton(self.layoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.first_row.addWidget(self.button_2)

        self.button_3 = QPushButton(self.layoutWidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.first_row.addWidget(self.button_3)

        self.button_p = QPushButton(self.layoutWidget)
        self.button_p.setObjectName(u"button_p")
        self.button_p.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; \n"
"width: 230px;\n"
"height: 50px; \n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.first_row.addWidget(self.button_p)


        self.verticalLayout.addLayout(self.first_row)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.output.setText("")
        self.button_e.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.button_t.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_d.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.button_m.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_p.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

