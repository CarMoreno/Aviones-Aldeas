 #!/usr/bin/python
 # -*- coding: utf-8 -*- 
from controlador.controlador import *
import ctypes
import sys
import os

if __name__ == '__main__':
	#myappid = 'ProyectoCompeljidad' # arbitrary string
	#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	print os.path.join(os.getcwd(), "icons\carpeta.png")
	app = QtGui.QApplication(sys.argv)
	#app.setWindowIcon(QtGui.QIcon('image/icon.png'))
	myapp = Controlador()
	myapp.show()
	sys.exit(app.exec_())