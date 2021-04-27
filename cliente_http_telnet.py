# Felipe Rivera: Por más ejemplos consultar:
# https://docs.python.org/3/library/socket.html
# https://docs.python.org/3/library/telnetlib.html

import socket
from telnetlib import Telnet

# Datos del Laboratorio

SITIO_WEB = 'example.com' 
PUERTO = 80       # Puerto donde escucha el servidor HTTP


#################################################################
# PRIMERO: Consulto al DNS por el registro A de SITIO_WEB
#################################################################

IPv4_SERVIDOR = socket.gethostbyname(SITIO_WEB)

print('La direccion IPv4 de ' + SITIO_WEB + ' es: ')
print(IPv4_SERVIDOR)

######################################################################
# SEGUNDO: Damos formato a un string que represente una consulta HTTP
######################################################################

# Metodo GET
GET = "GET / HTTP/1.1" + "\r\n"

# Encabezado HOST
HOST = "Host: " + SITIO_WEB + "\r\n"

# Encabezado User-Agent
USER_AGENT = "User-agent: " + "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0" + "\r\n"

# Encabezado Accept
ACCEPT = "Accept: " + "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" + "\r\n"

# Encabezado Accept-Language
ACCEPT_LANGUAGE = "Accept-Language: " + "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3" + "\r\n"

# Encabezado Connection
CONNECTION = "Connection: " + "close" + "\r\n"

# Concatenamos:
MENSAJE_HTTP = GET + HOST + ACCEPT + ACCEPT_LANGUAGE + USER_AGENT + CONNECTION + "\r\n"

print('El mensaje HTTP es: ')
print(MENSAJE_HTTP)


#############################################################################################
# TERCERO: Utilizamos TELNET para establecer una conexion TCP con el puerto 80 del servidor
# En esta conexion escribimos el mensaje HTTP y leemos la respuesta
#############################################################################################

with Telnet(IPv4_SERVIDOR, PUERTO) as mi_telnet:
    mi_telnet.write(MENSAJE_HTTP.encode('ascii'))
    print(mi_telnet.read_all().decode('ascii'))
    mi_telnet.close()
