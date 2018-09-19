# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepositReceipt.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DepositReceipt(object):
    def setupUi(self, DepositReceipt):
        DepositReceipt.setObjectName("DepositReceipt")
        DepositReceipt.resize(400, 300)
        self.label = QtWidgets.QLabel(DepositReceipt)
        self.label.setGeometry(QtCore.QRect(30, 90, 191, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DepositReceipt)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 191, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(DepositReceipt)
        self.lineEdit.setGeometry(QtCore.QRect(160, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(DepositReceipt)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 160, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.receipt = QtWidgets.QPushButton(DepositReceipt)
        self.receipt.setGeometry(QtCore.QRect(150, 240, 93, 28))
        self.receipt.setObjectName("receipt")

        self.retranslateUi(DepositReceipt)
        QtCore.QMetaObject.connectSlotsByName(DepositReceipt)

    def retranslateUi(self, DepositReceipt):
        _translate = QtCore.QCoreApplication.translate
        DepositReceipt.setWindowTitle(_translate("DepositReceipt", "Receipt"))
        self.label.setText(_translate("DepositReceipt", "Amount Deposit:"))
        self.label_2.setText(_translate("DepositReceipt", "Current Balance:"))
        self.receipt.setText(_translate("DepositReceipt", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepositReceipt = QtWidgets.QWidget()
    ui = Ui_DepositReceipt()
    ui.setupUi(DepositReceipt)
    DepositReceipt.show()
    sys.exit(app.exec_())

