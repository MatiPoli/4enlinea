from src.cuatroenlinea import todasColumnas

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