from src.cuatroenlinea import tableroVacio

def test_tablero_vacio_tiene_6_filas():
	tablero = tableroVacio()

	assert len(tablero) == 6

def test_tablero_vacio_tiene_7_columnas():
	tablero = tableroVacio()

	assert len(tablero[0]) == 7

def test_tablero_vacio_es_vacio():
	tablero = tableroVacio()

	assert tablero == [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]