# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WithdrawError.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_withdrawError(object):
    def setupUi(self, withdrawError):
        withdrawError.setObjectName("withdrawError")
        withdrawError.resize(400, 300)
        self.label = QtWidgets.QLabel(withdrawError)
        self.label.setGeometry(QtCore.QRect(20, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(withdrawError)
        self.line.setGeometry(QtCore.QRect(20, 90, 351, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(withdrawError)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(withdrawError)
        QtCore.QMetaObject.connectSlotsByName(withdrawError)

    def retranslateUi(self, withdrawError):
        _translate = QtCore.QCoreApplication.translate
        withdrawError.setWindowTitle(_translate("withdrawError", "Form"))
        self.label.setText(_translate("withdrawError", "ERROR"))
        self.label_2.setText(_translate("withdrawError", "(ERROR MESSAGE TO BE DISPLAYED HERE)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    withdrawError = QtWidgets.QWidget()
    ui = Ui_withdrawError()
    ui.setupUi(withdrawError)
    withdrawError.show()
    sys.exit(app.exec_())

