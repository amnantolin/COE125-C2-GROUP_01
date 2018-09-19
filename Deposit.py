# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Deposit.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DepositAmount
import DepositError
import DepositReceipt

class Ui_Deposit(object):
    def setupUi(self, Deposit):
        Deposit.setObjectName("Deposit")
        Deposit.resize(400, 279)
        Deposit.setMinimumSize(QtCore.QSize(400, 279))
        Deposit.setMaximumSize(QtCore.QSize(400, 279))
        self.label = QtWidgets.QLabel(Deposit)
        self.label.setGeometry(QtCore.QRect(130, 60, 151, 21))
        self.label.setObjectName("label")
        self.savings = QtWidgets.QPushButton(Deposit)
        self.savings.setGeometry(QtCore.QRect(150, 150, 93, 28))
        self.savings.setObjectName("savings")
        self.checking = QtWidgets.QPushButton(Deposit)
        self.checking.setGeometry(QtCore.QRect(150, 200, 93, 28))
        self.checking.setObjectName("checking")

        self.retranslateUi(Deposit)
        QtCore.QMetaObject.connectSlotsByName(Deposit)
        self.savings.clicked.connect(self.valid)

    def valid(self):
        self.dialog = depositamnt()
        self.dialog.show()
        self.close()

  #  def invalid(self):
   #     self.dialog = depositerror()
    #    self.dialog.show()

    def retranslateUi(self, Deposit):
        _translate = QtCore.QCoreApplication.translate
        Deposit.setWindowTitle(_translate("Deposit", "Deposit"))
        self.label.setText(_translate("Deposit", "Choose Account type:"))
        self.savings.setText(_translate("Deposit", "Savings"))
        self.checking.setText(_translate("Deposit", "Checking"))

class depositamnt(QtWidgets.QMainWindow, DepositAmount.Ui_DepositAmount):
    def __init__(self):
        super(depositamnt, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Deposit = QtWidgets.QDialog()
    ui = Ui_Deposit()
    ui.setupUi(Deposit)
    Deposit.show()
    sys.exit(app.exec_())

