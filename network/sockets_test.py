import socket

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#       1.1. socket.AF_INET - IPv4
#       1.2. socket.AF_INET6 - IPv6
#       2.1. socket.SOCK_STREAM - TCP
#       2.2. socket.SOCK_DGRAM - UDP

# socket.bind((HOST, PORT)) - associates a socket object with a specific interface and port
#   HOST - the IP/Interface with which to associate
#   PORT - the logical address on an interface

# socket.listen(listenqueue) - sets the socket object in blocking mode waiting for a client to attempt connection
#   listenqueue - determines the number of a connections to permit while waiting for acceptance.

# conn, addr = socket.accept() - this is where a connection is fully negotiated, and data can begin travelling back and
#   conn - a new socket object, this one for specific client connection.
#   addr - address information about the client(IP, port, etc)

# socket.send(string) - sends a buffer to the specified target and returns the number of bytes sent. This return value is useful error check.

# socket.recv(bufsize[, flags]) - receives data from a connection.
#   bufsize - the amount of data to accept.

# socket.close() - the last function to use, this terminates connection and frees up the memory.
#  The interpreter will do this automatically,
#  but again; good habits are good habits.

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''
PORT = 50000
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()


