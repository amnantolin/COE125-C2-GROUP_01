# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_log.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import admin_hp
import admin_error
import csv

class Ui_admin_log(object):

    def setupUi(self, admin_log):
        admin_log.setObjectName("admin_log")
        admin_log.resize(650, 450)
        admin_log.setMinimumSize(QtCore.QSize(650, 450))
        admin_log.setMaximumSize(QtCore.QSize(650, 450))
        self.centralwidget = QtWidgets.QWidget(admin_log)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(250, 140, 321, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sys_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sys_username.setFont(font)
        self.sys_username.setMaxLength(50)
        self.sys_username.setObjectName("sys_username")
        self.verticalLayout.addWidget(self.sys_username)
        self.sys_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sys_pass.setFont(font)
        self.sys_pass.setMaxLength(50)
        self.sys_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sys_pass.setObjectName("sys_pass")
        self.verticalLayout.addWidget(self.sys_pass)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 160, 131, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.sys_log = QtWidgets.QPushButton(self.centralwidget)
        self.sys_log.setGeometry(QtCore.QRect(240, 350, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_log.setFont(font)
        self.sys_log.setObjectName("sys_log")

        admin_log.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_log)
        QtCore.QMetaObject.connectSlotsByName(admin_log)

    def retranslateUi(self, admin_log):
        _translate = QtCore.QCoreApplication.translate
        admin_log.setWindowTitle(_translate("admin_log", "Admin Login"))
        self.label.setText(_translate("admin_log", "USERNAME:"))
        self.label_2.setText(_translate("admin_log", "PASSWORD:"))
        self.sys_log.setText(_translate("admin_log", "LOG-IN"))



