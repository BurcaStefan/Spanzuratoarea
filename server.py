import socket

def clients_connection(client1,client2):
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    
    while client1 is None or client2 is None:
        client_socket, client_address = server_socket.accept()
        identifier = client_socket.recv(1024).decode().strip()
        
        if identifier == "client1" and client1 is None:
            client1 = client_socket
            print("Client1 conectat.")
            client1.send("Conectat la server!\n".encode())
        elif identifier == "client2" and client2 is None:
            client2 = client_socket
            print("Client2 conectat.")
            client2.send("Conectat la server!\n".encode())
    
    return client1, client2
            
def recive_word_and_hint_from_client1(client1):
    word = client1.recv(1024).decode().strip()
    hint = client1.recv(1024).decode().strip()
    return word.lower(), hint

def send_word_and_hint_to_client2(client2, word, hint):
    guess_word=""
    word_list=list(word)
    for i in range(0,len(word)):
        if word_list[i] in "abcdefghijklmnopgrstuvwxyz":
            guess_word=guess_word+ "_"
        else:
            guess_word=guess_word + word_list[i]
    
    client2.send(guess_word.encode())
    client2.send(hint.encode())
    return guess_word
    
def game(client2,guess_word,word):
    chance=5
    while chance>0:
        letter=client2.recv(1024).decode().strip()
        if letter in word:
            for i in range(0,len(word)):
                if word[i]==letter:
                    guess_word_list=list(guess_word)
                    guess_word_list[i]=letter
                    guess_word="".join(guess_word_list)
            if word==guess_word:
                client2.send(guess_word.encode())
                client2.send("True".encode())
                break
            client2.send(guess_word.encode())
            client2.send("Continue".encode())
        else:
            client2.send(guess_word.encode())
            client2.send("False".encode())
            chance-=1
    
if __name__ == '__main__':
    client1=None
    client2=None
    client1, client2= clients_connection(client1,client2)
    word, hint = recive_word_and_hint_from_client1(client1)
    guess_word=send_word_and_hint_to_client2(client2, word, hint)
    game(client2,guess_word,word)
