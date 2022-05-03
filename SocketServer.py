import socket
from _thread import *
import json
import time
client_sockets = [] # 서버에 접속한 클라이언트 목록

# 서버 IP 및 열어줄 포트
HOST = '0.0.0.0'
PORT = 10000

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

        #\r\nDate:{}\r\nServer:Python3(windows10x64)\r\nAccept-Ranges:bytes\r\nContent-Length:{}\r\nKeep-Alive: timeout=10, max=100\r\nConnection: Keep-Alive
        
        message = "HTTP/1.1 {}\r\nContent-Type:text/html\r\nConnection: keep-alive\r\nContent-Length:{}\r\nDate: {} \r\n\r\n{}"
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

            if method == "GET":
                # login admin
                if isLogin:
                    if isAdmin:
                        # if admin
                        json_to_str = str(json_data)
                        date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                        message = message.format("200 OK", len(json_to_str), date, json_to_str)
                    else:
                        # if user
                        json_to_str = str(json_data["users"][userId-1])
                        message = message.format("200 OK", len(json_to_str), date, json_to_str)
                else:
                    # if not login
                    err = "Forbidden"
                    message = message.format("403 Forbidden", len(err), date, err)

                client_socket.send(message.encode())
                
            elif method == "HEAD":
                msg = ""
                message = message.format(
                    "200 OK", len(msg), date, msg)
                client_socket.send(message[:-5].encode())

            else:
                # get data that user sended
                body = request[-1][5:].split(",")

                if method == "POST":  # signin
                    if body[2] == "login":
                        # is admin?
                        isAdmin = True if (body[0] == json_data["users"][0]["email"] and body[1] == json_data["users"][0]["password"]) else False
                        
                        if isAdmin:
                            isLogin = True
                            msg = "Success Login. you are admin"
                            date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                            message = message.format("200 OK", len(msg),date, msg)
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
                                    date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                                    message = message.format("200 OK", len(msg), date, msg)
                                    client_socket.send(message.encode())
                                    break
                                    
                            else:
                                # if does not exist user info
                                msg = ""
                                date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                                message = message.format("401 Unauthorized", len(msg), date, "")
                                client_socket.send(message.encode())
                    else:
                        # post == true, signup == true
                        # signup

                        if len(body[0]) < 1 or len(body[0]) < 1 :
                            msg = ""
                            date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                            message = message.format("400 Bad Request", len(msg), date, msg)
                        else:
                            msg = "Success create user"

                            message = message.format("201 created", len(msg), date, msg)

                            newUser = {'id':len(json_data["users"])+1, 'email':body[0], 'password':body[1]}

                            json_data["users"].append(newUser)

                            with open('./users.json', 'w', encoding='utf-8') as f:
                                json.dump(json_data, f, indent="\t")

                        client_socket.send(message.encode())

                elif method == "PUT":
                    if len(json_data["users"]) <= int(body[2]):
                        msg = "can not found user"
                        date = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(time.time()))
                        message = message.format("404 not found", len(msg), date, msg)
                    else:

                        msg = "Success modify user"

                        message = message.format("200 OK", len(msg), date, msg)

                        json_data["users"][int(body[2])-1]["email"] = body[0] or ""
                        json_data["users"][int(body[2])-1]["password"] = body[1] or ""

                        with open('./users.json', 'w', encoding='utf-8') as f:
                            json.dump(json_data, f, indent="\t")
                    
                    client_socket.send(message.encode())
                continue

        except ConnectionResetError as e:
            print('>> Disconnected by ' + addr[0], ':', addr[1])
            break

finally:
    server_socket.close()

