import socket

def connection_with_server():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    data=client_socket.send("client1".encode())

    data=client_socket.recv(1024).decode()
    print(data)
    
    return client_socket
    
def send_word_and_hint_to_server(client_socket):
    word=input("Introduceti cuvantul: ")
    hint=input("Introduceti indiciul: ")
    client_socket.send(word.encode())
    client_socket.send(hint.encode())
    
if __name__ == '__main__':
    client_socket=connection_with_server()
    send_word_and_hint_to_server(client_socket)