import socket



format = "utf-8"
data = 16
port = 5050

disconnected_msg = "Off"
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_addr = (host_addr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_addr)

server.listen()
print("Server is listening now")

while True:
 conn, addr = server.accept()
 print("Connected to", addr)
 connected = True

 while connected:
  initial_msg = conn.recv(data).decode(format)
  print("Length of the message", initial_msg)
  if initial_msg:
   msg_length = int(initial_msg)
   msg = conn.recv(msg_length).decode(format)
   if msg == disconnected_msg:
    conn.send("Goodbye. It was nice to meet you.".encode(format))
    print("Terminating connection with", addr)
    connected = False
   else:
    print(msg)
    conn.send("Message Received".encode(format))
    
 conn.close()

