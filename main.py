# Proyecto: [Nombre del Proyecto]
# Estudiante: [Nombre del Estudiante]
# Fecha de Inicio: [dd/mm/aaaa]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.

from analisis_datos.carga_datos import generar_lista_compras
from analisis_datos.estadisticas import media

lista_compras = generar_lista_compras()
print(lista_compras)

precios = [precio for _, precio in lista_compras]
print("La media de compra:", media(precios))

def mediana(datos):
    #mediana
    #paso 1 : ordenar los valores ascedente
    datos = sorted(datos)
    print(datos)
    #Cantidad
    n = len(datos)


    mitad = n // 2
    # 0      1      2    3      
    #[1000, 2000, 3000, 4000, ]
    if n % 2 == 0:
        mediana = (datos[mitad -1 ] + datos[mitad])/2
    else:
        mediana = datos[mitad]
    return mediana