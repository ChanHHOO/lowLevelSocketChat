from socket import socket,error
headers = """GET http://www.google.com HTTP/1.1
                Host: www.google.com\r\n\r\n"""
try:
  s = socket()
  s.connect((host,int(port)))
  s.settimeout(4)
  s.send(headers.encode())
  s.recv(800)
  s.close()
except error:
  s.close()