from src.cuatroenlinea import columnaValida
from src.cuatroenlinea import contenidoColumna
from src.cuatroenlinea import tableroVacio
from src.cuatroenlinea import todasColumnas
from src.cuatroenlinea import todasFilas
from src.cuatroenlinea import completarTableroEnOrden
from src.cuatroenlinea import soltarFichaEnColumna
from src.cuatroenlinea import contenidoFila
from src.cuatroenlinea import dibujarTablero

def test_columnas_validas():
	columnas = [1,2,3,4,5]

	assert columnaValida([1,2,3,4,5]) == True

def test_columnas_no_validas():
	columnas = [1,2,3,4,5]

	assert columnaValida([1,9,3,0,5]) == False

def test_todas_filas():
	tablero = [
			[0,1,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[1,1,2,2,1,2,2]
			]
	assert todasFilas(tablero) == [[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,2,0,0,0,0,0],[0,1,0,0,0,0,0],[0,2,0,0,0,0,0],[1,1,2,2,1,2,2]]

def test_todas_filas_invalido():
	tablero = None
	assert todasFilas(tablero) == ""

def test_contenido_columna():
	tablero = [
			[0,1,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[0,1,2,0,0,0,0]
			]
	assert contenidoColumna(2,tablero) == [1,1,2,1,2,1]

def test_contenido_columna_invalido():
	tablero = None
	assert contenidoColumna(2,tablero) == ""

def test_contenido_fila():
	tablero = [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[1,1,2,2,1,1,2]
			]
	assert contenidoFila(6,tablero) == [1,1,2,2,1,1,2]

def test_contenido_fila_invalido():
	tablero = None
	assert contenidoFila(6,tablero) == ""

def test_soltar_ficha_en_columna():
	tablero = [
			[0,1,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[1,1,2,2,1,2,2]
			]
	soltarFichaEnColumna(1,1,tablero)
	assert tablero == [[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,2,0,0,0,0,0],[0,1,0,0,0,0,0],[1,2,0,0,0,0,0],[1,1,2,2,1,2,2]]


def test_tablero_vacio_tiene_6_filas():
	tablero = tableroVacio()

	assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
	tablero = tableroVacio()

	assert len(tablero[0]) == 7

def test_tablero_vacio_es_vacio():
	tablero = tableroVacio()

	assert tablero == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def test_completar_tablero_en_orden():
	tablero = [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0]
			]
	secuencia = [1,2,3,4,5,6,1]
	tablero = completarTableroEnOrden(secuencia,tablero)
	assert tablero == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[1,2,1,2,1,2,0]]

def test_completar_tablero_en_orden_invalido():
	tablero = [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0]
			]
	secuencia = [1,2,3,9,5,6,1]
	tablero = completarTableroEnOrden(secuencia,tablero)
	assert tablero == None

def test_todas_columnas():
	tablero = [
			[0,1,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[0,1,0,0,0,0,0],
			[0,2,0,0,0,0,0],
			[1,1,2,2,1,2,2]
			]
	assert todasColumnas(tablero) == [[0,0,0,0,0,1],[1,1,2,1,2,1],[0,0,0,0,0,2],[0,0,0,0,0,2],[0,0,0,0,0,1],[0,0,0,0,0,2],[0,0,0,0,0,2]]

def test_todas_columnas_invalido():
	tablero = None
	assert todasColumnas(tablero) == ""

