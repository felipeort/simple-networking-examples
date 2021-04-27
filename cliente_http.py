# Felipe Rivera: Por más ejemplos consultar:
# https://docs.python.org/3/library/http.client.html#module-http.client

import http.client

# Datos del Laboratorio

SITIO_WEB = 'example.com'  

##########################################################################
# PRIMERO y UNICO PASO: Hablo el protocolo HTTP con el servidor
##########################################################################

conexion = http.client.HTTPConnection(SITIO_WEB)
conexion.request("GET", "/")
respuesta = conexion.getresponse()
print('Codigo de respuesta: ')
print(respuesta.status, respuesta.reason)
datos = respuesta.read()
print('Datos en la respuesta: ')
print(datos.decode('ascii'))
conexion.close()
