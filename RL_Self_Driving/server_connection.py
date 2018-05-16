import socket
import random
import json
import time

HOST = 'localhost'  # The remote host
PORT = 4449  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Starting connection message')

counting = False
last_traveled_distance=0

while True:
    json_data = s.recv(1024)
    # print('Received', repr(json_data))
    data = json.loads(json_data)
    distance = data["Distance"]
    status = data["Status"]
    traveled_distance = data["TraveledDistance"]
    print(distance, status, traveled_distance)
    # =============================================
    # calculate reward with time
    # =============================================
    if status == 0 and counting == False:
        start = time.time()
        counting = True
    elif status==0 and counting == True:
        last_traveled_distance=traveled_distance
    elif status == -1:
        done = time.time()
        elapsed = done - start
        print("Reward: ", elapsed, "Traveled distance: ",last_traveled_distance)
        counting = False

    # =============================================
    rand = random.randint(1, 3)
    if rand == 1:
        s.sendall(b'FORWARD')
    elif rand == 2:
        s.sendall(b'RIGHT')
    elif rand == 3:
        s.sendall(b'LEFT')

s.close()
