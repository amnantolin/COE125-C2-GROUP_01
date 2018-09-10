# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_close.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_admin_close(object):
    def setupUi(self, admin_close):
        admin_close.setObjectName("admin_close")
        admin_close.resize(650, 450)
        admin_close.setMinimumSize(QtCore.QSize(650, 450))
        admin_close.setMaximumSize(QtCore.QSize(650, 450))
        self.label = QtWidgets.QLabel(admin_close)
        self.label.setGeometry(QtCore.QRect(210, 30, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_close)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 150, 271, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sys_an = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sys_an.setFont(font)
        self.sys_an.setText("")
        self.sys_an.setMaxLength(12)
        self.sys_an.setObjectName("sys_an")
        self.verticalLayout.addWidget(self.sys_an)
        self.sys_pin = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sys_pin.setFont(font)
        self.sys_pin.setText("")
        self.sys_pin.setMaxLength(6)
        self.sys_pin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sys_pin.setObjectName("sys_pin")
        self.verticalLayout.addWidget(self.sys_pin)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(admin_close)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(110, 150, 165, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayoutWidget = QtWidgets.QWidget(admin_close)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 310, 351, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sys_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_delete.setFont(font)
        self.sys_delete.setObjectName("sys_delete")
        self.horizontalLayout.addWidget(self.sys_delete)
        self.sys_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_cancel.setFont(font)
        self.sys_cancel.setObjectName("sys_cancel")
        self.horizontalLayout.addWidget(self.sys_cancel)
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_4.raise_()
        self.horizontalLayoutWidget.raise_()

        self.retranslateUi(admin_close)
        QtCore.QMetaObject.connectSlotsByName(admin_close)

    def retranslateUi(self, admin_close):
        _translate = QtCore.QCoreApplication.translate
        admin_close.setWindowTitle(_translate("admin_close", "Close Account"))
        self.label.setText(_translate("admin_close", "CLOSE ACCOUNT"))
        self.label_4.setText(_translate("admin_close", "ACCOUNT NUMBER:"))
        self.label_3.setText(_translate("admin_close", "PIN NUMBER:"))
        self.sys_delete.setText(_translate("admin_close", "CONFIRM"))
        self.sys_cancel.setText(_translate("admin_close", "CANCEL"))





