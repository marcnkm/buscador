import sys, pygame
from pygame.locals import *
import aestrella, mapa, actor, buscador

from mock import patch
from mock import Mock

from aestrella import AEstrella

#Assegura que les posicions d'inicial al mapa.txt sigui la indicada
def test_buscarPos2():
 	m = mapa.Mapa()
 	assert aestrella.buscarPos(1,m.mapa) == [0,0]
 	assert aestrella.buscarPos(2,m.mapa) == [12,8]

#Assegura que les posicions en el seguents mapes siguin les esperades
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
"""
testesja la funcio de distancia per assegurar el seu correcte funcionament
per aquests diferents valors d'exemple
"""
def test_distancia():
	assert aestrella.distancia([12,8],[11,8]) == 1
	assert aestrella.distancia([11,8],[11,8]) == 0
	assert aestrella.distancia([12,10],[13,16]) == 7
	assert aestrella.distancia([11,8],[13,16]) == 10
	assert aestrella.distancia([10,8],[13,16]) == 11

#testeja que la funcio treu correctament l'ultim terme
def test_quitarUltimo():
	assert mapa.quitarUltimo(['# # # # # # # # # # # # # # # # #\n',
	 '# . . . . . . . . . . # . # . . #\n',
	  '# # # # # . # # # . . . . # . # #\n',
	   '# . . . . . . . . . # . . . . . #\n',
	    '# . # # # . # . # . # . # . # . #\n',
	     '# . # . # . # . # . # . # . # . #\n',
	      '# . # . # . # . # . . # # . # . #\n',
	       '# . # . . . # . # # . # . # . . #\n',
	        '# . . . # # # . . # . . . . . # #\n',
	         '# . . . . . . . # # . # # . . . #\n',
	          '# # # # . # . . . # . # . . # . #\n',
	           '# . . . . # . # . . . # # . # . #\n',
	            '# . # # . # . # T # . . . . . . #\n',
	             '# # # # # # # # # # # # # # # # #\n']
) == ['# # # # # # # # # # # # # # # # #',
 '# . . . . . . . . . . # . # . . #',
  '# # # # # . # # # . . . . # . # #',
   '# . . . . . . . . . # . . . . . #',
    '# . # # # . # . # . # . # . # . #',
     '# . # . # . # . # . # . # . # . #',
      '# . # . # . # . # . . # # . # . #',
       '# . # . . . # . # # . # . # . . #',
        '# . . . # # # . . # . . . . . # #',
         '# . . . . . . . # # . # # . . . #',
          '# # # # . # . . . # . # . . # . #',
           '# . . . . # . # . . . # # . # . #',
            '# . # # . # . # T # . . . . . . #',
             '# # # # # # # # # # # # # # # # #']

#testeja que els simbols de les cadenes es tradueixen de forma correcta
def test_listarCadena():
	assert mapa.listarCadena("# . # # . # . # T # . . . . . . #") == [1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 1]
	assert mapa.listarCadena("# . # # # . # . # . # . # . # . #") == [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]

#testeja que les distancies no siguin negatives
def test_distancia_no_negatius():
	for n in range(10):
		for m in range(10):
			for c in range(10):
				for k in range(10):
					yield mes_gran_0,n,m,c,k

def mes_gran_0(n,m,c,k):
	assert aestrella.distancia([n,m],[c,k]) >= 0


