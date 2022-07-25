import socket
import pickle


HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    print(f"Sending: {msg}")
    message = pickle.dumps(msg)
    msg_length = len(message)
    send_length = pickle.dumps(str(msg_length))
    
    send_length += b' ' * (HEADER - len(send_length ))
    client.send(send_length)
    client.send(message)
    result = pickle.loads(client.recv(1024))
    
    print(f"Received: {result}")
    return result

x = ['Frank', .5, 1000, 1200] #user, outcome, user rating, opponent rating

send(x)
send(DISCONNECT_MESSAGE)