import socket
import threading
import pickle


HEADER = 64
PORT = 5050
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def new_elo(msg):
    user = msg[0]
    outcome = int(msg[1])
    user_rating = int(msg[2])
    opp_rating = int(msg[3])
    diff = opp_rating - user_rating
    user_win_prob = 1/(1+10**(diff/400))
    if user_rating >= 2400:
        k_factor = 16
    elif user_rating >= 2100 and user_rating <= 2399:
        k_factor = 24
    else:
        k_factor = 32
    new_rating = user_rating + (k_factor * (outcome - user_win_prob))
    result = [user, int(new_rating)]
    return result

#target of connection for each client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = pickle.loads(conn.recv(HEADER))
        msg_length = int(msg_length)
        msg = pickle.loads(conn.recv(msg_length))
        print(f"Received: {msg}")
        if msg == DISCONNECT_MESSAGE:
            msg = pickle.dumps('Disconnected')
            conn.send(msg)
            print(f"Sending: {msg}")
            connected = False
        else:
            message = pickle.dumps(new_elo(msg))
            conn.send(message)
            print(f"Sending: {message}")
    conn.close()

#distributes connection to correct place
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()