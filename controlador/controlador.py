 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from vista.ventana import *
from modelo.modelo import *
from PyQt4.QtCore import pyqtSlot
import os

class Controlador(QtGui.QMainWindow):
	"""Se encarga de gestionar los eventos y pasar los mensajes al modelo"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.vista = Ui_Ventana() #vista es un objeto de la clase Ui_Ventana (mi interface)
		self.modelo = Modelo() #objeto del modelo
		self.vista.setupUi(self)
		self.button_cargar = self.vista.button_cargar
		self.button_simplex = self.vista.button_simplex
		self.button_branch = self.vista.button_branch
		self.text_resultados = self.vista.text_resultados
		self.label_archivo = self.vista.label_archivo
		self.conectar()

	@pyqtSlot()	
	def cargar_archivo(self):
		"""Abre la ventana para seleccionar el archivo y lee el mismo"""
		fname = QtGui.QFileDialog.getOpenFileName(self, 'Abrir Archivo', os.getcwd())
		f = open(fname, 'r')
		self.label_archivo.setText(str(fname))
		with f:        
		    data = f.read() #Leemos el archivo  
		self.modelo.get_values_string(data)
		self.text_resultados.setText(data)#mostramos en el text edit     

	@pyqtSlot()
	def run_simplex(self):
		"""Slot para el el boton simplex"""
		respuesta = self.modelo.get_simplex()
		mensaje = """----------Respuesta Metodo Simplex---------
Con los datos ingresados se tiene la siguiente respuesta:

Z = {funcion}
Variables = {variables}
No. de iteraciones = {iter}""".format(funcion=respuesta.get('fun')*-1, variables=respuesta.get('x'), iter=respuesta.get('nit'))
		#print respuesta
		self.text_resultados.setText(mensaje)
	
	@pyqtSlot()
	def run_branch(self):
		"""Slot para el boton branch"""
		#self.modelo.get_branch()
		self.text_resultados.setText("Hola branch")

	def conectar(self):
		"""Asocia cada boton con su correspondiente slot: boton-->senal-->slot"""
		self.button_cargar.pressed.connect(self.cargar_archivo)
		self.button_simplex.pressed.connect(self.run_simplex)
		self.button_branch.pressed.connect(self.run_branch)		