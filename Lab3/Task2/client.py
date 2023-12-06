import socket

format = "utf-8"
disconnected_msg = "Off"
data = 16
port = 5050
hostname = socket.gethostname()
host_addr = socket.gethostbyname(hostname)

server_socket_addr = (host_addr, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)

def msg_to_send(msg):
 message = msg.encode(format)
 msg_length = len(message)
 send_length = str(msg_length).encode(format)
 send_length += b" "*(data -len(send_length))


 client.send(send_length)
 client.send(message)

 print(client.recv(2048).decode(format))

while True:
 input_msg = input("Please enter something with vowels:")
 if input_msg == 'Done':
  msg_to_send(disconnected_msg)
  break
 else:
  msg_to_send(input_msg)