# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_hp.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import admin_log
import admin_open
import admin_close

class Ui_admin_hp(object):
    def setupUi(self, admin_hp):
        admin_hp.setObjectName("admin_hp")
        admin_hp.resize(650, 450)
        admin_hp.setMinimumSize(QtCore.QSize(650, 450))
        admin_hp.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(admin_hp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 100, 271, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sys_open = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_open.setFont(font)
        self.sys_open.setObjectName("sys_open")
        self.verticalLayout.addWidget(self.sys_open)
        self.sys_close = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_close.setFont(font)
        self.sys_close.setObjectName("sys_close")
        self.verticalLayout.addWidget(self.sys_close)
        self.sys_info = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_info.setFont(font)
        self.sys_info.setObjectName("sys_info")
        self.verticalLayout.addWidget(self.sys_info)
        self.sys_logout = QtWidgets.QPushButton(self.centralwidget)
        self.sys_logout.setGeometry(QtCore.QRect(230, 340, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_logout.setFont(font)
        self.sys_logout.setObjectName("sys_logout")
        admin_hp.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_hp)
        QtCore.QMetaObject.connectSlotsByName(admin_hp)

    def retranslateUi(self, admin_hp):
        _translate = QtCore.QCoreApplication.translate
        admin_hp.setWindowTitle(_translate("admin_hp", "Admin HomePage"))
        self.sys_open.setText(_translate("admin_hp", "Open Account"))
        self.sys_close.setText(_translate("admin_hp", "Close Account"))
        self.sys_info.setText(_translate("admin_hp", "View Account Info"))
        self.sys_logout.setText(_translate("admin_hp", "LOG-OUT"))



