# Felipe Rivera: Por más ejemplos consultar:
# https://docs.python.org/3/library/socket.html

import socket
import dns.resolver

# 0) Vamos a consultar el estado de un buzón de correo utilizando el protocolo POP3

usuario = "ort-grupo2"
password = "ort-grupo2"

dominio = 'lab.ort.edu.uy'  # Nombre de dominio al que quiero enviar correo


# 1) Determinar servidor SMTP del dominio lab.ort.edu.uy

restpuesta_consulta_MX = dns.resolver.resolve(dominio, 'MX')
print("Respuesta a consulta registro MX: ", "\r\n", restpuesta_consulta_MX)

mail_exchange = restpuesta_consulta_MX[0].exchange
print("Mail Exchange: ", "\r\n", mail_exchange)
print(type(mail_exchange))

mail_exchange_str = str(mail_exchange)
print("Mail Exchange STR: ", "\r\n", mail_exchange_str)
print(type(mail_exchange_str))

# 2) Necesito determinar el registro A del servidor de correo encontrado en (1)
# 2) Puedo obtenerlo mediante una consulta independiente
# 2) O puede encontrarse como Additional Record en la consulta anterior

mail_exchange_A = restpuesta_consulta_MX.nameserver
print("Registro A de Mail Exchange: ", "\r\n", mail_exchange_A)
print(type(mail_exchange_A))


# 3) Puedo consultar el estado de la casilla

PUERTO = 110  # Puerto definido por la IANA para POP3


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mi_socket:
    mi_socket.connect((mail_exchange_A, PUERTO))
    respuesta = mi_socket.recv(2048)

    # Establecemos conexión POP3 con el servidor de correo.
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    # Naturalmente debería contemplar la ocurrencia de errores y manejarlos de forma acorde
    # Por ejemplo utilizando try / catch
    # Pero ese detalle esta más allá del alcance del ejemplo

    MENSAJE_POP3 = "USER" + " " + usuario + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_POP3 = "PASS" + " " + password + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_POP3 = "LIST" + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_POP3 = "RETR 1" + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_POP3 = "DELE 1" + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_POP3 = "QUIT" + "\r\n"
    print(MENSAJE_POP3)
    mi_socket.sendall(MENSAJE_POP3.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    mi_socket.close()




