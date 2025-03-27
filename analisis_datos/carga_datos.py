import random


def generar_lista_compras():
    canasta_basica = {
        'Arroz' : 1800,
        'Azúcar' : 2200,
        'Harina' : 1200,
        'Tomate' : 2500,
        'Frijoles' : 1400,
        'Papas' : 3000,
        'Lecha': 1000,
        'Cerveza' : 1000,
        'Cafe' : 5000,
        'Fideos': 800,
        'Jabón' : 1500,
        'Huevos' : 3500,
        'Naranjas' : 2500,
        'Sal': 800
    }
    #Aqui voy a seleccionar aleatoriamente 5 productos de la canasta Básica
    seleccion = random.sample(list(canasta_basica.items()),k=5)
    return seleccion