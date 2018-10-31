import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 1234)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(2)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'Mensagem de "%s" ->  "%s"' % (client_address,data)
            if data:
                connection.sendall(data)
            
            if data == "bye":
                connection.close()
                break
            
    finally:
        connection.close()