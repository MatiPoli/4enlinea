def tableroVacio():
	return [
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0]
			]
def columnaValida(secuencia):
	for i in secuencia:
		if secuencia[i] < 1 or secuencia[i] >7:
			return False
	return True
def contenidoColumna(nrocolumna,tablero):
	if tablero == None:
		return ""
	columna = []
	for fila in tablero:
		celda = fila[nrocolumna - 1]
		columna.append(celda)
	return columna
def contenidoFila(nrofila,tablero):
	if tablero == None:
		return ""
	fila = []
	for columna in tablero[nrofila-1]:
		fila.append(columna)
	return fila
def todasColumnas(tablero):
	if tablero == None:
		return ""
	columnas = []
	for columna in range(1,7):
		columnas.append(contenidoColumna(columna,tablero))
	return columnas
def todasFilas(tablero):
	if tablero == None:
		return ""
	filas = []
	for fila in tablero:
		filas.append(fila)
	return filas
def soltarFichaEnColumna(ficha,columna,tablero):
	for fila in range(6,0,-1):
		if tablero[fila-1][columna-1] == 0:
			tablero[fila-1][columna-1] = ficha
			return
def completarTableroEnOrden(secuencia,tablero):
	if not (columnaValida(secuencia)):
		print("Una de las columnas de la secuencia es invalida!")
		return None
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

secuencia = [1,2,3,1,3,4]
tablero = tableroVacio()
tablero = completarTableroEnOrden(secuencia, tablero)
dibujarTablero(tablero)

print(contenidoColumna(1, tablero))
print(contenidoFila(5, tablero))
print(todasColumnas(tablero))
print(todasFilas(tablero))