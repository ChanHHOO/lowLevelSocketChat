import socket
from _thread import *
import json
import time

HOST = '192.168.55.35'
# HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# 서버로부터 메세지를 받는 메소드
# 스레드로 구동 시켜, 메세지를 보내는 코드와 별개로 작동하도록 처리
def recv_data(client_socket) :

    while True :
        
        data = client_socket.recv(1024)
        
        print(data.decode())

        print("\n===========================================================")

start_new_thread(recv_data, (client_socket,))
print ('>> Connect Server')


mehods = ["POST", "GET", "PUT", "HEAD"]
while True:
    message = "{} HTTP/1.1\r\nUser-Agent:python3(macOS)\r\nAccept:*/*\r\nAccept-Charset: utf-8\r\nnCache-Control: no=cache\r\nnHost: 192.168.55.82\r\nConnection: keep-alive\r\nContent-Length:{}"
    user = ""
    print("choose http method")
    methodNum = int(input("1.POST / 2.GET / 3.PUT / 4.HEAD : "))
    method = mehods[methodNum-1]

    if method == "GET" or method == "HEAD":
        message = message.format(method, 0)


    else:
        # input user info
 
            
        email = input("insert email : ")
        password = ","+input("insert password : ")

        user = "\r\n\r\nuser:" + email + password

        if method == "POST":
            postOption = input("input login or signup : ")
            user += ","+postOption
        if method == "PUT":
            putOption = input("input id :")
            user += ","+putOption

        message = message.format(method, len(user))
        message += user

    if user == 'quit':
        close_data = user
        break
    
    client_socket.send(message.encode())

    # 쓰레드 별 출력 시간이 달라 잠시 대기
    time.sleep(0.1)
    


client_socket.close()