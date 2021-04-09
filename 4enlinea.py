def tableroVacio():
	return [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0]
			]

def soltarFichaEnColumna(ficha,columna,tablero):
	for fila in range(6,0,-1):
		if tablero[fila-1][columna-1] == 0:
			tablero[fila-1][columna-1] = ficha
			return
def completarTableroEnOrden(secuencia,tablero):
	
	i = 0
	while i < len(secuencia):
		if i%2 == 0:
			soltarFichaEnColumna(1,secuencia[i],tablero)
		else:
			soltarFichaEnColumna(2,secuencia[i],tablero)
		i += 1
	return tablero
def dibujarTablero(tablero):
	if tablero == None:
		return
	for fila in tablero:
		for celda in fila:
			if celda == 0:
				print('   ', end='')
			else:
				print(' %s ' % celda, end='')
		print('')

secuencia = [1,2,3,0]
dibujarTablero(completarTableroEnOrden(secuencia, tableroVacio()))

