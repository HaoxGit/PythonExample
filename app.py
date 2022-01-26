__author__="Jorge"
__copyright__="Curso de Python"
__credits__=["Pepe","Jose Luis","Roberto"]
__license__="GPL"
__version__="1.0"
__email__="japp@denebola.org"
__status__="Development"

def cubo(x):
	"""Calcula el cubo de un numero"""
	y=x**3
	return y

if __name__=="__main__":
	x=int(input("Dame un numero: "))
	y=cubo(x)
	print("El cubo de %.2f es %.2f" % (x,y
))
