import socket

"""
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
"""

SAVE = "SAVE"
LOAD = "LOAD"


def load_data(connection, fname):
    print 'LOAD FILE'
    fobj = file(fname, "r+")
    data = fobj.read()
    print "%s\t%s" % (fname, data)
    connection.send(data)
    connection.close()
    fobj.close()
    pass


def main():
    file_list = []
    HOST = ''
    PORT = 50002
    sentinel = False
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    while not sentinel:
        s.listen(1)
        connection, address = s.accept()
        mode = connection.recv(4)
        if mode == SAVE:
            file_list.append(save_data(connection))
        elif mode == LOAD:
            fname = connection.recv(5)
            if fname not in file_list:
                connection.send("File Not Found")
                connection.close()
            else:
                load_data(connection, fname)
        else:
            print mode
            sentinel = True

    s.close()


def save_data(connection):
    print 'SAVE FILE'
    fname = connection.recv(5)
    fobj = file(fname, "w+")
    data = connection.recv(1024)
    print "%s:\t%s" % (fname, data)
    fobj.write(data)
    fobj.close()
    connection.close()
    return fname


main()
