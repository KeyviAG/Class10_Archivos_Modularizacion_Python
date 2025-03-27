"""
Contenido de __init__.py
El archivo __init__.py puede contener varios tipos de código, dependiendo de las necesidades del paquete :

1. Inicialización del paquete: Puede incluir código que necesitas que se ejecute cuando el paquete es importado. 
Por ejemplo, puede realizar la configuración inicial que requieran los módulos dentro del paquete.

2. Importaciones: A menudo se utiliza para facilitar la accesibilidad a las clases y funciones de los módulos del paquete.
Por ejemplo, puedes importar ciertas funciones y clases en el archivo __init__.py para que estén disponibles directamente al importar el paquete, 
sin necesidad de acceder a los módulos individuales.    
"""
# __init__.py dentro del paquete analisis_datos

# Importamos las funciones 'media' y 'mediana' desde el módulo 'estadisticas' ubicado en el mismo paquete.



# Importamos las funciones 'generar_lista_compras' y 'guardar_lista_compras' desde el módulo 'carga_datos' ubicado en el mismo paquete.



# Definimos la lista '__all__' para especificar qué nombres serán exportados cuando se use 'from analisis_datos import *'.

