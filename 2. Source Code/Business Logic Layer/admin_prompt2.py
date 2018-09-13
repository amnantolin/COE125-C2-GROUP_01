# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_prompt2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin_prompt2(object):
    def setupUi(self, admin_prompt2):
        admin_prompt2.setObjectName("admin_prompt2")
        admin_prompt2.resize(358, 225)
        admin_prompt2.setMinimumSize(QtCore.QSize(358, 225))
        admin_prompt2.setMaximumSize(QtCore.QSize(358, 225))
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_prompt2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 40, 300, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(admin_prompt2)
        QtCore.QMetaObject.connectSlotsByName(admin_prompt2)

    def retranslateUi(self, admin_prompt2):
        _translate = QtCore.QCoreApplication.translate
        admin_prompt2.setWindowTitle(_translate("admin_prompt2", "Message"))
        self.label.setText(_translate("admin_prompt2", "Account has been deleted!"))



