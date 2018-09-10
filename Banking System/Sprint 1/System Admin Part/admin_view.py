# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_view.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin_view(object):
    def setupUi(self, admin_view):
        admin_view.setObjectName("admin_view")
        admin_view.resize(650, 450)
        admin_view.setMinimumSize(QtCore.QSize(650, 450))
        admin_view.setMaximumSize(QtCore.QSize(650, 450))
        self.label = QtWidgets.QLabel(admin_view)
        self.label.setGeometry(QtCore.QRect(220, 30, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(admin_view)
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(admin_view)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(admin_view)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 310, 351, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sys_confirm = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_confirm.setFont(font)
        self.sys_confirm.setObjectName("sys_confirm")
        self.horizontalLayout.addWidget(self.sys_confirm)
        self.sys_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sys_cancel.setFont(font)
        self.sys_cancel.setObjectName("sys_cancel")
        self.horizontalLayout.addWidget(self.sys_cancel)

        self.retranslateUi(admin_view)
        QtCore.QMetaObject.connectSlotsByName(admin_view)

    def retranslateUi(self, admin_view):
        _translate = QtCore.QCoreApplication.translate
        admin_view.setWindowTitle(_translate("admin_view", "View Account"))
        self.label.setText(_translate("admin_view", "VIEW ACCOUNT"))
        self.label_4.setText(_translate("admin_view", "ACCOUNT NUMBER:"))
        self.label_3.setText(_translate("admin_view", "PIN NUMBER:"))
        self.sys_confirm.setText(_translate("admin_view", "CONFIRM"))
        self.sys_cancel.setText(_translate("admin_view", "CANCEL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_view = QtWidgets.QWidget()
    ui = Ui_admin_view()
    ui.setupUi(admin_view)
    admin_view.show()
    sys.exit(app.exec_())

