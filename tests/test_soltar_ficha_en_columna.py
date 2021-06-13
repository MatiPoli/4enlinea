from src.cuatroenlinea import soltarFichaEnColumna

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