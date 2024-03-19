#!/usr/bin/python3
import sys
import socket

def client_program(host, port):

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    host = socket.gethostname()
    port = 5000

    if len(sys.argv) > 1:
        host = sys.argv[1]

    if len(sys.argv) > 2:
        try:
            port = int(sys.argv[2])
        except:
            print("El puerto debe ser un numero.")
            print("Uso: client.py <ip> <puerto>")
            exit()

    client_program(host, port)

