import socket

def connection_with_server():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    data=client_socket.send("client2".encode())

    data=client_socket.recv(1024).decode()
    print(data)

    return client_socket
    
def recive_word_and_hint_from_server(client_socket):
    guess_word = client_socket.recv(1024).decode().strip()
    hint = client_socket.recv(1024).decode().strip()
    return guess_word, hint

def choose_letter():
    while True:
        letter=input("Introduceti litera: ")
        if len(letter)>1 or len(letter)==0:
            print("Introduceti o singura litera!")
        elif letter.lower() not in "abcdefghijklmnopgrstuvwxyz":
            print("Introduceti o litera valida!")
        else:
            break
    return letter.lower()

def game(client_socket,guess_word,hint):
    chance=5
    
    while chance>0:
        print("\nINDICIUL: ",hint)
        print(guess_word, "  ", chance)
        
        letter=choose_letter()
        client_socket.send(letter.encode())
        
        guess_word=client_socket.recv(1024).decode().strip()
        data=client_socket.recv(1024).decode().strip()
        
        if data=="False":
            print("Litera nu se afla in cuvant!")
            chance-=1
        if data=="True":
            print("\nAti ghicit cuvantul!")
            break
    else:
        print("\nAti pierdut!")

if __name__ == '__main__':
    client_socket=connection_with_server()
    guess_word, hint = recive_word_and_hint_from_server(client_socket)
    game(client_socket,guess_word,hint)