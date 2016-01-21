import socket


def main():
    HOST = ''
    PORT = 50001
    message_list = ['alpha', 'bravo', 'charlie', 'delta']
    print 'server started'
    for i in message_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        print 'socket listen'
        conn, addr = s.accept()
        print 'socket accept'
        conn.send(i)
        print 'server is sending \'%s\'. ' % i
        conn.close()
        print 'connection closed'

main()
