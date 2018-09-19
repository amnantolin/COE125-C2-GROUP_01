# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WithdrawAccountType.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_withdrawAccType(object):
    def setupUi(self, withdrawAccType):
        withdrawAccType.setObjectName("withdrawAccType")
        withdrawAccType.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(withdrawAccType)
        self.pushButton.setGeometry(QtCore.QRect(110, 110, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(withdrawAccType)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 180, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(withdrawAccType)
        self.label.setGeometry(QtCore.QRect(90, 70, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(withdrawAccType)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(withdrawAccType)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(withdrawAccType)
        QtCore.QMetaObject.connectSlotsByName(withdrawAccType)

    def retranslateUi(self, withdrawAccType):
        _translate = QtCore.QCoreApplication.translate
        withdrawAccType.setWindowTitle(_translate("withdrawAccType", "Form"))
        self.pushButton.setText(_translate("withdrawAccType", "CHECKING ACCOUNT"))
        self.pushButton_2.setText(_translate("withdrawAccType", "SAVINGS ACCOUNT"))
        self.label.setText(_translate("withdrawAccType", "Please Select an Account Type"))
        self.label_2.setText(_translate("withdrawAccType", "HI!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    withdrawAccType = QtWidgets.QWidget()
    ui = Ui_withdrawAccType()
    ui.setupUi(withdrawAccType)
    withdrawAccType.show()
    sys.exit(app.exec_())

