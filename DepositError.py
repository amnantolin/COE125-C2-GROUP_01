# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepositError.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DepositError_2(object):
    def setupUi(self, DepositError_2):
        DepositError_2.setObjectName("DepositError_2")
        DepositError_2.resize(400, 300)
        self.DepositError = QtWidgets.QLabel(DepositError_2)
        self.DepositError.setGeometry(QtCore.QRect(70, 100, 261, 61))
        self.DepositError.setObjectName("DepositError")
        self.label = QtWidgets.QLabel(DepositError_2)
        self.label.setGeometry(QtCore.QRect(130, 80, 141, 41))
        self.label.setObjectName("label")

        self.retranslateUi(DepositError_2)
        QtCore.QMetaObject.connectSlotsByName(DepositError_2)

    def retranslateUi(self, DepositError_2):
        _translate = QtCore.QCoreApplication.translate
        DepositError_2.setWindowTitle(_translate("DepositError_2", "Error!"))
        self.DepositError.setText(_translate("DepositError_2", "You don\'t have the desired account type"))
        self.label.setText(_translate("DepositError_2", "Invalid account type! "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DepositError_2 = QtWidgets.QWidget()
    ui = Ui_DepositError_2()
    ui.setupUi(DepositError_2)
    DepositError_2.show()
    sys.exit(app.exec_())

