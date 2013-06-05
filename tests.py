import sys, pygame
from pygame.locals import *
import aestrella, mapa, actor, buscador

from mock import patch
from mock import Mock
from mapa import Mapa
from aestrella import AEstrella

# class Nodo:
# 	def __init__(self, pos=[0, 0], padre=None):
# 		self.pos = pos
# 		self.padre = padre
# 		self.h = 10
# 		if self.padre == None:
# 			self.g = 0
# 		else:
# 			self.g = self.padre.g + 1
# 		self.f = self.g + self.h


# if __name__ == '__main__':
# 	# mapp = mapa.leerMapa("mapa.txt")
# 	# print mapp
# 	mapp = mapa.Mapa()
# 	print mapp.col

# class test_AEstrella:
		
		#[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 3, 0, 1, 1, 0, 1, 0, 1], [1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


# @patch('aestrella.AEstrella')
@patch('mapa.Mapa')
def test_vecinos(mock_mapa ):
	nodo = Mock()
	nodo.pos = [0,0]
	nodo.padre = 'None'
	nodo.h = 10
	nodo.g = 0
	nodo.f = 10

	# mapaa = mapa.leerMapa("mapa.txt")
	#mapp = mapa.Mapa()

	# mock_aestrella.return_value.inicio = [0,0]
	# print mock_inicio.return_value.inicio
	mock_mapa.return_value = Mapa()
	#print mock_mapa.return_value
	#print mock_mapa.return_value.mapa

	# print mock_mapa.col
	# print mock_mapa.return_value.mapa
	# mapp = mapa.Mapa()
	# print mapp.fil
	# patcher = patch(test_vecinos, pos=[0,0], padre='None',h=10,g=0,f=10)
	# mock_thing = patcher.start()

	
	# @patch('mapa.Mapa')
	# mapa.return_value = mapaa
	#print nodo.padre

	# a = aestrella.AEstrella(mock_mapa.return_value.mapa)
	# a = aestrella.AEstrella(mock_mapa.return_value.mapa)

	# a.vecinos(nodo)
	# mock_aestrella.return_value.vecinos(nodo)
	AEstrella.vecinos(nodo)
	#assert AEstrella.vecinos(nodo) == 2
	

	assert 1==2


def test_buscarPos():
	assert aestrella.buscarPos(2,[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], 
		[1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
		[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], 
		[1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1], 
		[1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], 
		[1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1], 
		[1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1], 
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [12,8]
	assert aestrella.buscarPos(3,[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
		[1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1], 
		[1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
		[1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1], 
		[1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], 
		[1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1], 
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1], 
		[1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1], 
		[1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1], 
		[1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1], 
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [1,1]


def test_distancia():
	assert aestrella.distancia([12,8],[11,8]) == 1
	assert aestrella.distancia([11,8],[11,8]) == 0
	assert aestrella.distancia([12,10],[13,16]) == 7
	assert aestrella.distancia([11,8],[13,16]) == 10
	assert aestrella.distancia([10,8],[13,16]) == 11

def test_distancia_no_negatius():
	for n in range(10):
		for m in range(10):
			for c in range(10):
				for k in range(10):
					yield mes_gran_0,n,m,c,k

def mes_gran_0(n,m,c,k):
	assert aestrella.distancia([n,m],[c,k]) >= 0






# def setup():
# 	buscador.main()




#class Test_Aestrella:
# def test_vecinos():
# 	print "aadf"
# 	buscador.main()
	# M = buscador.leerMapa("mapa.txt")
	# A = aestrella.AEstrella(M)
	# N = Nodo([12,8])
	
	# #A = AEstrella(M)
	# #print M
	# #globals()["pos_f"] = buscarPos(3, M)
	# #print pos_f
	# A = AEstrella(M)
	# N = Nodo([12,8])
	

	
# print N.pos
	#V = AEstrella.vecinos(N)
	#assert V.pos == [11,8] 