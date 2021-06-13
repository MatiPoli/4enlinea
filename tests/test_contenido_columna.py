from src.cuatroenlinea import contenidoColumna

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