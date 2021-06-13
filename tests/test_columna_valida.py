from src.cuatroenlinea import columnaValida

def test_columnas_ingresadas_estan_bien():
	columnas = [1,2,3,4,5]

	assert columnaValida([1,2,3,4,5]) == True