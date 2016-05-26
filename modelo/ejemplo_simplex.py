from scipy.optimize import linprog

"""
Max f(x) = 3x1 + x2 + 2x3
Suj:
	x1 + x2 + 3x3 <= 30
	2x1 + 2x2 + 5x3 <= 24
	4x1 + x2 + 2x3 <= 36
	x1, x2, x3 >= 0
"""
# funcion_objetivo = [-3, -1, -2]
# restricciones = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
# limites = [30, 24, 36]
# mensaje = {"dist" : True}

funcion_objetivo = [-10, -5, -7, -8, -3, -9, -6, -8, -6, -9, -4, -10, -12, -10, -4]
restricciones = [
	[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
	[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
	[0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
	[0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
]
limites = [100, 80, 70, 40, 20, 50, 90, 60]

mensaje = {"dist" : True}


respuesta = linprog(funcion_objetivo, A_ub=restricciones, b_ub=limites, method='simplex')
print respuesta