from src.cuatroenlinea import contenidoFila

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