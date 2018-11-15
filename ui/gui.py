# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main.ui'
#
# Created: Thu Nov 15 01:33:17 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(499, 330)
        Dialog.setMinimumSize(QtCore.QSize(499, 330))
        Dialog.setMaximumSize(QtCore.QSize(499, 330))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/fa+.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 501, 101))
        self.frame.setStyleSheet("QFrame\n"
"{\n"
"    background-image: url(\':/logo/logo.png\');\n"
"}")
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 106, 481, 201))
        self.groupBox.setObjectName("groupBox")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 461, 81))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 61, 16))
        self.label_4.setObjectName("label_4")
        self.cbAlg = QtGui.QComboBox(self.groupBox)
        self.cbAlg.setGeometry(QtCore.QRect(320, 110, 121, 22))
        self.cbAlg.setObjectName("cbAlg")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(260, 112, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 140, 47, 13))
        self.label_6.setObjectName("label_6")
        self.btnExit = QtGui.QPushButton(self.groupBox)
        self.btnExit.setGeometry(QtCore.QRect(400, 170, 75, 23))
        self.btnExit.setAutoDefault(False)
        self.btnExit.setObjectName("btnExit")
        self.btnSimulate = QtGui.QPushButton(self.groupBox)
        self.btnSimulate.setGeometry(QtCore.QRect(320, 170, 75, 23))
        self.btnSimulate.setDefault(True)
        self.btnSimulate.setObjectName("btnSimulate")
        self.lbResult = QtGui.QLabel(self.groupBox)
        self.lbResult.setGeometry(QtCore.QRect(324, 140, 61, 16))
        self.lbResult.setTextFormat(QtCore.Qt.RichText)
        self.lbResult.setObjectName("lbResult")
        self.spnSalary = QtGui.QDoubleSpinBox(self.groupBox)
        self.spnSalary.setGeometry(QtCore.QRect(80, 109, 141, 21))
        self.spnSalary.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSalary.setDecimals(2)
        self.spnSalary.setMinimum(100.0)
        self.spnSalary.setMaximum(99999999.0)
        self.spnSalary.setProperty("value", 100.0)
        self.spnSalary.setObjectName("spnSalary")
        self.spnAge = QtGui.QDoubleSpinBox(self.groupBox)
        self.spnAge.setGeometry(QtCore.QRect(80, 139, 141, 21))
        self.spnAge.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnAge.setPrefix("")
        self.spnAge.setDecimals(0)
        self.spnAge.setMinimum(16.0)
        self.spnAge.setMaximum(10000000.0)
        self.spnAge.setObjectName("spnAge")
        self.spnLoan = QtGui.QDoubleSpinBox(self.groupBox)
        self.spnLoan.setGeometry(QtCore.QRect(80, 169, 141, 21))
        self.spnLoan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnLoan.setDecimals(2)
        self.spnLoan.setMinimum(100.0)
        self.spnLoan.setMaximum(99999999.0)
        self.spnLoan.setObjectName("spnLoan")
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 307, 500, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "FinalciAnalyzer+", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Análise", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Bem vindo ao FinanciAnalyzer plus.\n"
"\n"
"Selecione abaixo as informações relativas às condiçõesfinanceiras do cliente e depois clique em\n"
"\'simular\' para poder obter o resultado.\n"
"\n"
"Todas as categorias de informação são obrigatórias.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Salário:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Idade:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Empréstimo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Algoritmo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Risco:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnExit.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSimulate.setText(QtGui.QApplication.translate("Dialog", "Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.lbResult.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">--</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.spnSalary.setPrefix(QtGui.QApplication.translate("Dialog", "R$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.spnLoan.setPrefix(QtGui.QApplication.translate("Dialog", "R$ ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"center\">© 2018 - Master64k</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import ui.gui_rc
