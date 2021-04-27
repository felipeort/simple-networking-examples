# Felipe Rivera: Por más ejemplos consultar:
# https://docs.python.org/3/library/socket.html

import socket
import dns.resolver

# 0) Vamos a enviar un correo desde ort-grupo1@lab.ort.edu.uy a ort-grupo2@lab.ort.edu.uy

casilla_origen = "ort-grupo1"
casilla_destino = "ort-grupo2"

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


# 3) Puedo comenzar a elaborar el "sobre" del correo utilizando el protocolo SMTP

PUERTO = 25  # Puerto definido por la IANA para SMTP


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mi_socket:
    mi_socket.connect((mail_exchange_A, PUERTO))
    respuesta = mi_socket.recv(2048)

    # Establecemos conexión SMTP con el servidor de correo.
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    # Naturalmente debería contemplar la ocurrencia de errores y manejarlos de forma acorde
    # Por ejemplo utilizando try / catch
    # Pero ese detalle esta más allá del alcance del ejemplo

    MENSAJE_SMTP = "HELO" + " " + dominio + "\r\n"
    print(MENSAJE_SMTP)
    mi_socket.sendall(MENSAJE_SMTP.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_SMTP = "MAIL FROM:" + " " + "<" + casilla_origen + ">" + "\r\n"
    print(MENSAJE_SMTP)
    mi_socket.sendall(MENSAJE_SMTP.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_SMTP = "RCPT TO:" + " " + "<" + casilla_destino + ">" + "\r\n"
    print(MENSAJE_SMTP)
    mi_socket.sendall(MENSAJE_SMTP.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    MENSAJE_SMTP = "DATA" + "\r\n"
    print(MENSAJE_SMTP)
    mi_socket.sendall(MENSAJE_SMTP.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    # 4) Dentro del "sobre" SMTP va la "carta"

    DATA = "From: elon_musk@tesla.com" + "\r\n" + "To: felipe.rivera@fi365.ort.edu.uy " + "\r\n" + \
           "Subject: Felicidades" + "\r\n" + "@Feliz año 2021 !" + "\r\n" + "." + "\r\n"

    print(DATA)

    mi_socket.sendall(DATA.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    # 4) La "carta" ya fue enviada, puedo cerrar la sesión SMTP

    MENSAJE_SMTP = "QUIT" + "\r\n"
    print(MENSAJE_SMTP)
    mi_socket.sendall(MENSAJE_SMTP.encode())

    respuesta = mi_socket.recv(2048)
    print('La respuesta recibida es: ')
    print(respuesta.decode())

    mi_socket.close()




