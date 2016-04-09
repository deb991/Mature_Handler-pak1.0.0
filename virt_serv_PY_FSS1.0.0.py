/*This is the file for make any system as a virtual server independently with respect to the package management. This script is based on */
/*PYTHON 2.X. Being light weight its bit different & perfect for Fail-SAFE session issues on any kind of SYstems.*/
/*This is the prototype script where as, different commands are not mention here properly. But It can be designed as per user requirement*/
/*This program is provided here but user may need to set the path firt & then can be use it frequently. */
/* If there is any issue, Pleae mail me back @: net.aphos@yandex.com*/

import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s '% PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()
