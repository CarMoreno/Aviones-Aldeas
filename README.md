#Aviones y Aldeas

Proyecto para la asignatura de Complejidad y Optimización que resolverá el siguiente problema usando el método Simplex:

Se requiere transportar sacos con alimentos mediante `n` tipos de aviones `A1`, `A2`, ..., `An`, desde un aeropuerto y arrojarse en m aldeas  `V1`, `V2`, ..., `Vm`, afectadas por inundaciones. Cada avión `Ai` puede transportar una cantidad de alimentos `cij` a cada aldea `Vj`. Así mismo, cada avión `Ai` puede realizar un número máximo `ti` de viajes, mientras que cada aldea `Vj` puede recibir un número máximo `kj` de aviones. Se desea determinar el número de viajes que deberá hacer cada avión a cada aldea de forma que se maximice la cantidad de alimento distribuido por día. La aplicación debe ser capaz de cargar un archivo de texto con los coeficientes del sistema de inigualdades.

Está codificado en Python 2.7 usando Scientific Python (SciPy), Numeric Python (Numpy) y PyQt4 para la interfaz gráfica.