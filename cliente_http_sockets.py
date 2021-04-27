# Felipe Rivera: Por más ejemplos consultar:
# https://docs.python.org/3/library/socket.html

import socket


# Datos del Laboratorio

SITIO_WEB = 'example.com'  
PUERTO = 80       # Puerto donde escucha el servidor HTTP

#################################################################
# PRIMERO: Consulto al DNS por el registro A de example.com
#################################################################

IPv4_SERVIDOR = socket.gethostbyname(SITIO_WEB)

print('La direccion IPv4 de' + SITIO_WEB + 'es: ')
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
CONNECTION = "Connection: " + "keep-alive" + "\r\n"

# Concatenamos:
MENSAJE_HTTP = GET + HOST + ACCEPT + ACCEPT_LANGUAGE + USER_AGENT + CONNECTION + "\r\n"

print('El mensaje HTTP es: ')
print(MENSAJE_HTTP)

#############################################################################################
# TERCERO: Creamos un socket TCP tipo STREAM donde escribimos el mensaje y leemos la respueta
#############################################################################################

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mi_socket:
    mi_socket.connect((IPv4_SERVIDOR, PUERTO))
    mi_socket.sendall(MENSAJE_HTTP.encode('utf-8'))
    respuesta = mi_socket.recv(2048)
    mi_socket.close()

print('La respuesta recibida es: ')
print(respuesta.decode('ascii'))
