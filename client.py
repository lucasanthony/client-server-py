import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

endereco = "localhost"
porta = 1234

#endereco = raw_input("Endereco: ")
#porta = int(raw_input("porta: "))

server_address = (endereco, porta)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    while True:
        message = raw_input()
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)

        if message == "bye":
            sock.close()
            break

        amount_received = 0
        amount_expected = len(message)
    
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
