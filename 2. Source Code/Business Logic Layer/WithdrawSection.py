# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WithdrawSection.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_withdrawAmount(object):
    def setupUi(self, withdrawAmount):
        withdrawAmount.setObjectName("withdrawAmount")
        withdrawAmount.resize(400, 300)
        self.textEdit = QtWidgets.QTextEdit(withdrawAmount)
        self.textEdit.setGeometry(QtCore.QRect(90, 140, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(withdrawAmount)
        self.label.setGeometry(QtCore.QRect(70, 140, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(withdrawAmount)
        self.label_2.setGeometry(QtCore.QRect(30, 210, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(withdrawAmount)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(withdrawAmount)
        QtCore.QMetaObject.connectSlotsByName(withdrawAmount)

    def retranslateUi(self, withdrawAmount):
        _translate = QtCore.QCoreApplication.translate
        withdrawAmount.setWindowTitle(_translate("withdrawAmount", "Form"))
        self.textEdit.setHtml(_translate("withdrawAmount", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0.00</p></body></html>"))
        self.label.setText(_translate("withdrawAmount", "P"))
        self.label_3.setText(_translate("withdrawAmount", "Please Enter the Amount"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    withdrawAmount = QtWidgets.QWidget()
    ui = Ui_withdrawAmount()
    ui.setupUi(withdrawAmount)
    withdrawAmount.show()
    sys.exit(app.exec_())

