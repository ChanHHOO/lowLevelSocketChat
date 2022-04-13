import socket
from _thread import *
# https://stickode.tistory.com/225

client_sockets = [] # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '127.0.0.1'
PORT = 9999

# 서버 소켓 생성
print('>> Server Start')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

try:
    client_socket, addr = server_socket.accept()
    client_sockets.append(client_socket)
    while True:
        print('>> Wait')


        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            
            splitedData = data.decode().split("\r\n")
            # get http method
            method = splitedData[0].split()
            method = method[0]

            # file modify
            if method == "POST":
                ...
            elif method == "GET":
                ...
            elif method == "PUT":
                ...
            else:
                ...
            #print('>> Received from ' + addr[0], ':', addr[1], data)

            #         client.send(data)

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

except Exception as e :
    print ('에러는? : ',e)

finally:
    server_socket.close()

