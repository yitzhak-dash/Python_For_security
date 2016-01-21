import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = socket object
    s.connect(('127.0.0.1', 50001))  # connect
    received_message = s.recv(1024)  # get was server send
    s.close()  # close the socket
