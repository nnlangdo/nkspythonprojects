import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))

def receive():
    while True:
        try:
            # Receive message from server
            # If 'NICK' send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)

        except:
            # Close connection when error
            print("An error ocurred!")
            client.close()
            break

# sending messages to server
def write():
    while True:
        message = '{}: {}'.format(nickname,input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
