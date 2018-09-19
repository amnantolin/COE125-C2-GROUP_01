# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepositAmount.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DepositAmount(object):
    def setupUi(self, DepositAmount):
        DepositAmount.setObjectName("DepositAmount")
        DepositAmount.resize(400, 295)
        self.label = QtWidgets.QLabel(DepositAmount)
        self.label.setGeometry(QtCore.QRect(140, 70, 181, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(DepositAmount)
        self.lineEdit.setGeometry(QtCore.QRect(110, 130, 181, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.buttonBox = QtWidgets.QDialogButtonBox(DepositAmount)
        self.buttonBox.setGeometry(QtCore.QRect(100, 220, 193, 28))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(DepositAmount)
        QtCore.QMetaObject.connectSlotsByName(DepositAmount)

    def retranslateUi(self, DepositAmount):
        _translate = QtCore.QCoreApplication.translate
        DepositAmount.setWindowTitle(_translate("DepositAmount", "Deposit Amount"))
        self.label.setText(_translate("DepositAmount", "Enter Peso Amount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepositAmount = QtWidgets.QDialog()
    ui = Ui_DepositAmount()
    ui.setupUi(DepositAmount)
    DepositAmount.show()
    sys.exit(app.exec_())

