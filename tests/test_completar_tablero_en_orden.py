from src.cuatroenlinea import completarTableroEnOrden

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