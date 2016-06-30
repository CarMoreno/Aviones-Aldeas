 #!/usr/bin/python
 # -*- coding: utf-8 -*- 
import branch 
from itertools import izip
from scipy.optimize import linprog
import numpy as np

class Modelo(object):
	"""Se encarga de recibir los mensajes que envie el controlador y
	hacer los llamados correspondientes a Simplex o Branch segun el caso"""
	def __init__(self):
		self.data = ""
	
	def get_values_string(self, data):
		"""Retorna los datos del txt como un string"""
		self.data = data
		return data

	def get_values(self, data):
		"""Transforma la entrada en un arreglo, donde cada elento es un subarreglo de renglones,
		es decir, el primer renglon del txt queda en un subarreglo, el segundo tambien y así...
		[ ['3', '5'], ['10', '8', '6', '9', '12'], ['5' '3' '8' '4' '10'], ... ]"""
		data_full = []
		for line in data.splitlines():
			data_full.append(line.split())
		return data_full				
		
	def get_filas(self, data):
		"""Retorna un array donde cada elemento es un subarray
		con los alimentos llevados por un avion a cada aldea, es decir,
		retorna las filas."""
		filas = []
		array = self.get_values(data)
		array.pop(0) #Sacamos el primer elemento
		array.pop(len(array) - 2)#sacamos el penultimo elemento
		array.pop()#sacamos el ultimo elemento
		for fila in array:
			fila = [float(i) for i in fila]
			filas.append(fila)
		print filas	
		return filas

	def get_columnas(self, data):
		"""Retorna un array donde cada elemento es un subarray
		con los alimentos llevados por cada avion a una aldea, es decir,
		retorna las columans."""
		columnas = []
		fila = self.get_filas(data)

		for mapa in zip(*fila):
			mapa = [float(i) for i in mapa]
			columnas.append(list(mapa))
		print columnas		
		return columnas

	def get_aviones(self, data):
		"""Retorna la cantidad de aviones"""
		array = self.get_values(data)
		return int(array.pop(0).pop(0))

	def get_aldeas(self, data):
		"""Retorna la cantidad de aldeas"""		
		array = self.get_values(data)
		return int(array.pop(0).pop(1))

	def get_funcion_obj(self, data):
		"""Retorna la funcion objetivo del problema en un arreglo de coeficientes"""
		columnas = self.get_columnas(data)
		funcion_obj = columnas.pop(0)
		for columna in columnas:
			funcion_obj += columna
		
		funcion_obj = [i * -1 for i in funcion_obj]
		return funcion_obj

	def get_restriccion_columna(self, data):
		"""Retorna un array de arrays con los coeficientes para las restricciones de columna"""
		num_aviones = self.get_aviones(data)
		num_aldeas = self.get_aldeas(data) #num aldeas
		restricciones = np.repeat(np.identity(num_aldeas), num_aviones, axis=1)
		#print restricciones
		return restricciones

	def get_restriccion_fila(self, data):
		"""Retorna un array de arrays con los coeficientes para las restricciones de fila"""
		n = self.get_aviones(data) #filas
		m = self.get_aviones(data) * self.get_aldeas(data) #columnas
		restricciones = np.zeros((n, m), int)# Matriz de 3x15 (aviones x aviones*aldeas)
		i,j = np.indices(restricciones.shape)
		offsets = self.get_offset(data)
		for offset in offsets:
			restricciones[i==j-offset] = 1
		#print restricciones
		return restricciones

	def get_offset(self, data):
		"""Funcion auxiliar para obtener las restricciones de las filas"""
		num_aviones = self.get_aviones(data)
		num_aldeas = self.get_aldeas(data)
		offsets = []
		for i in xrange((num_aldeas*num_aviones) + 1):
			if i % num_aviones is 0:
			 	offsets.append(i)
		print offsets	 	
		return offsets

	def get_restricciones(self, data):
		"""Retorna una matriz de restricciones, concatenando las restricciones de fila y columna"""
		return np.concatenate((self.get_restriccion_columna(data), self.get_restriccion_fila(data)))
				
	def get_limites(self, data):
		"""Retorna un array con los limites de las restricciones"""
		array = self.get_values(data)
		limite_aldeas = self.get_values(data).pop()
		limite_aviones = self.get_values(data).pop(len(array) - 2)
		limites = limite_aldeas + limite_aviones
		limites = [int(i) for i in limites]
		#print limites
		return limites

	def get_paquete(self, data):
		"""Funcion que se encarga de agrupar los datos en un diccionario
		dada una inistancia del problema"""
		return {
			'funcion_objetivo' : self.get_funcion_obj(data),
			'restricciones' : self.get_restricciones(data),
			'limites' : self.get_limites(data),
		}

	def get_simplex(self):
		"""Realiza el metodo simplex con el problema modelado"""
		data = self.data
		respuesta = linprog(self.get_paquete(data).get('funcion_objetivo'),
							A_ub = self.get_paquete(data).get('restricciones'), 
							b_ub = self.get_paquete(data).get('limites'),
							method='simplex')										
		return respuesta
	
	
	def get_branch(self):
		"""Realiza el método branch and bound con el problema modelado"""
		data = self.data