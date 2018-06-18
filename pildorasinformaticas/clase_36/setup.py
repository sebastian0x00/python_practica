from setuptools import setup

setup(

	name="paquetecalculos",
	version="1.0",
	description="Paquete de redondeo y potencia",
	author="Juan",
	author_email="cursos@pildorasinformaticas.es",
	url="www.pildorasinformaticas.es",
	packages=["calculos","calculos.redondeo_potencia"]
	
	)

#desde una ventana de DOS, donde está el archivo python.py 
#python setup.py sdist
#pip3 install paquetescalculos-1.0.tar.gz
