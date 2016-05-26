# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ventana(object):
    def setupUi(self, Ventana):
        Ventana.setObjectName(_fromUtf8("Ventana"))
        Ventana.resize(601, 415)
        Ventana.setStyleSheet(_fromUtf8("#Ventana{\n"
"    background-color:#424242;\n"
"}\n"
"\n"
"#miframe{\n"
"    background-color: #757575;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QLabel, QPushButton, QTextEdit{\n"
"    font-family: Roboto;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#label_titulo{\n"
"    font-size: 24px;\n"
"    color: #81c784;\n"
"}\n"
"\n"
"#label_archivo{\n"
"    font-size: 12px;\n"
"}\n"
"#label_resultados{\n"
"    font-size: 15px;\n"
"    border: 2px solid #9e9e9e;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #81c784;\n"
"    border-radius: 4px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #66bb6a;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    border-radius: 4px;\n"
"    background-color: #9e9e9e;\n"
"    font-size: 13px;\n"
"    color: #424242; \n"
"    text-align: center; \n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"    background-color: #bdbdbd;\n"
"}"))
        self.centralwidget = QtGui.QWidget(Ventana)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.miframe = QtGui.QFrame(self.centralwidget)
        self.miframe.setGeometry(QtCore.QRect(30, 30, 541, 351))
        self.miframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.miframe.setFrameShadow(QtGui.QFrame.Raised)
        self.miframe.setObjectName(_fromUtf8("miframe"))
        self.label_titulo = QtGui.QLabel(self.miframe)
        self.label_titulo.setGeometry(QtCore.QRect(190, 10, 211, 31))
        self.label_titulo.setObjectName(_fromUtf8("label_titulo"))
        self.button_cargar = QtGui.QPushButton(self.miframe)
        self.button_cargar.setGeometry(QtCore.QRect(30, 100, 131, 51))
        self.button_cargar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icons/carpeta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(os.path.join(os.getcwd(), "icons\carpeta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)     
        self.button_cargar.setIcon(icon)
        self.button_cargar.setObjectName(_fromUtf8("button_cargar"))
        self.text_resultados = QtGui.QTextEdit(self.miframe)
        self.text_resultados.setEnabled(False)
        self.text_resultados.setGeometry(QtCore.QRect(230, 100, 281, 141))
        self.text_resultados.setObjectName(_fromUtf8("text_resultados"))
        self.label_archivo = QtGui.QLabel(self.miframe)
        self.label_archivo.setGeometry(QtCore.QRect(30, 200, 171, 31))
        self.label_archivo.setText(_fromUtf8(""))
        self.label_archivo.setObjectName(_fromUtf8("label_archivo"))
        self.label_resultados = QtGui.QLabel(self.miframe)
        self.label_resultados.setGeometry(QtCore.QRect(330, 70, 81, 31))
        self.label_resultados.setObjectName(_fromUtf8("label_resultados"))
        self.button_simplex = QtGui.QPushButton(self.miframe)
        self.button_simplex.setGeometry(QtCore.QRect(230, 270, 81, 31))
        self.button_simplex.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_simplex.setObjectName(_fromUtf8("button_simplex"))
        self.button_branch = QtGui.QPushButton(self.miframe)
        self.button_branch.setGeometry(QtCore.QRect(430, 270, 81, 31))
        self.button_branch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_branch.setObjectName(_fromUtf8("button_branch"))
        self.button_borrar = QtGui.QPushButton(self.miframe)
        self.button_borrar.setGeometry(QtCore.QRect(330, 270, 81, 31))
        self.button_borrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_borrar.setObjectName(_fromUtf8("button_borrar"))
        Ventana.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Ventana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Ventana.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Ventana)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Ventana.setStatusBar(self.statusbar)

        self.retranslateUi(Ventana)
        QtCore.QObject.connect(self.button_borrar, QtCore.SIGNAL(_fromUtf8("clicked()")), self.text_resultados.clear)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(_translate("Ventana", "Proyecto Complejidad", None))
        self.label_titulo.setText(_translate("Ventana", "Aviones y Aldeas ...", None))
        self.button_cargar.setText(_translate("Ventana", "Cargar Archivo", None))
        self.label_resultados.setText(_translate("Ventana", "Resultados", None))
        self.button_simplex.setText(_translate("Ventana", "Simplex", None))
        self.button_branch.setText(_translate("Ventana", "Branch", None))
        self.button_borrar.setText(_translate("Ventana", "Borrar", None))

