 #!/usr/bin/python
 # -*- coding: utf-8 -*- 
from itertools import izip
from scipy.optimize import linprog

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
		es decir, el primer renglon del txt queda en un subarreglo, el segundo y así...
		[ ['3', '5'], ['10', '8', '6', '9', '12'], ['5' '3' '8' '4' '10'], ... ]"""
		data_full = []
		for line in data.splitlines():
			data_full.append(line.split())
		#print data_full
		return data_full				
	
	def get_filas(self, data):
		"""Retorna un array donde cada elemento es un subarray
		con los alimentos llevados por un avion a cada aldea, es decir,
		retorna las filas."""
		filas = self.get_values(data)
		filas.pop(0) #Sacamos el primer elemento
		filas.pop(len(filas) - 2)#sacamos el penultimo elemento
		filas.pop()#sacamos el ultimo elemento
		print "FILAS",filas
		return filas

	def get_columnas(self, data):
		"""Retorna un array donde cada elemento es un subarray
		con los alimentos llevados cada avion a una aldea, es decir,
		retorna las columans."""
		columnas = []
		fila = self.get_filas(data)

		for mapa in zip(*fila):
			mapa = [int(i) for i in mapa]
			columnas.append(list(mapa))
		print "COLUMNAS",columnas		
		return columnas
			
	def get_funcion_obj(self, data):
		"""Retorna la funcion objetivo del problema en un arreglo de coeficientes"""
		funcion_obj = []
		for subarray in self.get_filas(data):
			suma = 0
			for i in subarray:
				suma = float(i) + suma
			funcion_obj.append(suma)
		funcion_obj = [int(i)*-1 for i in funcion_obj]			
		return funcion_obj


	def get_viajes_avion(self, data):
		"""Retorna un array con los viajes que puede hacer cada avion (primeras restrcciones)"""
		viajes_avion = self.get_values(data)
		viajes_avion = [(None, int(i)) for i in viajes_avion.pop(len(viajes_avion) - 2)]
		return viajes_avion

	def get_recibe_aldea(self, data):
		"""Retorna un array con los aviones que puede recibir cada aldea (limites de las restricciones)"""
		recibe_aldea = self.get_values(data).pop()
		recibe_aldea = [int(i) for i in recibe_aldea]
		return recibe_aldea


		

	def get_paquete(self, data):
		"""Funcion que se encarga de agrupar los datos en un diccionario
		dada una inistancia del problema"""
		return {
			'funcion_objetivo' : self.get_funcion_obj(data),
			'restricciones' : self.get_columnas(data),
			'limites' : self.get_recibe_aldea(data),
			'bounds' : self.get_viajes_avion(data),
		}

# 	def get_simplex(self, text_respuesta):
# 		"""Realiza el metodo simplex con el problema modelado"""
# 		data = self.data
# 		respuesta = linprog(self.get_paquete(data).get('funcion_objetivo'),
# 							A_ub = self.get_paquete(data).get('restricciones'), 
# 							b_ub = self.get_paquete(data).get('limites'),
# 							bounds = self.get_paquete(data).get('bounds'),
# 							method='simplex')	
# 		muestra = """----------Respuesta Metodo Simplex---------
# Con los datos ingresados se tiene la siguiente respuesta:

# Z = {funcion}
# Variables (en orden: x0, x1, x2) = {variables}""".format(funcion=respuesta.get('fun'), variables=respuesta.get('x'))

# 		text_respuesta.setText(muestra)

if __name__ == '__main__':
	filetxt = """3 5
10 8 6 9 12
5 3 8 4 10
7 9 6 10 4
50 90 60
100 80 70 40 20"""
	m = Modelo()
	#m.get_paquete(filetxt)
	#m.get_simplex(filetxt)	
	#m.get_values(filetxt)
	m.get_filas(filetxt)
	#m.get_viajes_avion(filetxt)	
	# m.get_recibe_aldea(filetxt)
	# m.get_funcion_obj(filetxt)
	m.get_columnas(filetxt)