import socket
from _thread import *
import json
import time
client_sockets = [] # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '0.0.0.0'
PORT = 9999

# cookie 로 사용할 데이터
isAdmin = False

isLogin = False

userId = None
# --------------------

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
        message = "HTTP/1.1 {}\r\nDate:{}\r\nServer:Python3(windows10x64)\r\nAccept-Ranges:bytes\r\nContent-Length:{}\r\nKeep-Alive: timeout=10, max=100\r\nConnection: Keep-Alive\r\nContent-Type:text/json\r\n\r\ndata:{}"
        status = 200
        contentLength = 0
        try:
            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)
            print(data.decode())
            if not data:
                print('>> Disconnected by ' + addr[0], ':', addr[1])
                break
            
            request = data.decode().split("\r\n")
            # get http method
            method = request[0].split()
            method = method[0]
            
            # get all user data
            with open('./users.json', 'r+', encoding='utf-8') as f:
                json_data = json.load(f)
                #print(json.dumps(json_data))

            if method == "GET":
                # login admin
                if isLogin:
                    if isAdmin:
                        # if admin
                        json_to_str = str(json_data)
                        message = message.format(200, time.ctime(time.time()), len(json_to_str), json_to_str)
                    else:
                        # if user
                        json_to_str = str(json_data["users"][userId-1])
                        message = message.format(200, time.ctime(time.time()), len(json_to_str), json_to_str)
                else:
                    # if not login
                    err = "Forbidden"
                    message = message.format(403, time.ctime(time.time()), len(err), err)

                client_socket.send(message.encode())
                
            elif method == "HEAD":
                msg = ""
                message = message.format(
                    200, time.ctime(time.time()), len(msg), msg)
                client_socket.send(message[:153].encode())

            else:
                # get data that user sended
                body = request[-1][5:].split(",")
                if method == "POST":  # signin
                    # is admin?
                    isAdmin = True if (body[0] == json_data["users"][0]["email"] and body[1] == json_data["users"][0]["password"]) else False
                    
                    if isAdmin:
                        isLogin = True
                        msg = "Success Login. you are admin"
                        message = message.format(200, time.ctime(time.time()), len(msg), msg)
                        client_socket.send(message.encode())
                    else:
                        # try login
                        for user in json_data["users"]:
                            if user['email'] == body[0] and user['password'] == body[1]:
                                # if exist user info
                                isLogin = True
                                isAdmin = False
                                userId = user["id"]

                                msg = "Success Login. you are user"
                                message = message.format(200, time.ctime(time.time()), len(msg), msg)
                                client_socket.send(message.encode())
                                break
                                
                        else:
                            # if does not exist user info
                            msg = "Unauthorized"
                            message = message.format(401, time.ctime(time.time()), len(msg), msg)
                            client_socket.send(message.encode())

                elif method == "PUT":  # signup

                    if len(body[0]) < 1 or len(body[0]) < 1 :
                        msg = "Bad reqeust"
                        message = message.format(400, time.ctime(time.time()), len(msg), msg)
                    else:
                        msg = "Success create user"

                        message = message.format(201, time.ctime(time.time()), len(msg), msg)

                        newUser = {'id':len(json_data["users"])+1, 'email':body[0], 'password':body[1]}

                        json_data["users"].append(newUser)

                        with open('./users.json', 'w', encoding='utf-8') as f:
                            json.dump(json_data, f, indent="\t")

                    client_socket.send(message.encode())



                continue

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

finally:
    server_socket.close()

