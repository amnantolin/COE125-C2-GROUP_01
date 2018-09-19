# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WithdrawSuccess.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_withdrawSuccess(object):
    def setupUi(self, withdrawSuccess):
        withdrawSuccess.setObjectName("withdrawSuccess")
        withdrawSuccess.resize(400, 300)
        self.label = QtWidgets.QLabel(withdrawSuccess)
        self.label.setGeometry(QtCore.QRect(20, 50, 351, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(withdrawSuccess)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(withdrawSuccess)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(withdrawSuccess)
        self.label_4.setGeometry(QtCore.QRect(150, 150, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(withdrawSuccess)
        self.label_5.setGeometry(QtCore.QRect(70, 240, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(withdrawSuccess)
        self.line.setGeometry(QtCore.QRect(10, 180, 381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(withdrawSuccess)
        self.line_2.setGeometry(QtCore.QRect(10, 90, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(withdrawSuccess)
        QtCore.QMetaObject.connectSlotsByName(withdrawSuccess)

    def retranslateUi(self, withdrawSuccess):
        _translate = QtCore.QCoreApplication.translate
        withdrawSuccess.setWindowTitle(_translate("withdrawSuccess", "Form"))
        self.label.setText(_translate("withdrawSuccess", " The the transaction was successful!"))
        self.label_2.setText(_translate("withdrawSuccess", "CURRENT BALANCE"))
        self.label_3.setText(_translate("withdrawSuccess", "P"))
        self.label_4.setText(_translate("withdrawSuccess", "0.00"))
        self.label_5.setText(_translate("withdrawSuccess", "Thank You! Have a Good Day!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    withdrawSuccess = QtWidgets.QWidget()
    ui = Ui_withdrawSuccess()
    ui.setupUi(withdrawSuccess)
    withdrawSuccess.show()
    sys.exit(app.exec_())

