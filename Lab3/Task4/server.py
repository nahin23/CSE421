import socket
import threading



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

def handle_clients_of_server(conn, addr):
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
    worked = int(msg)
    normal_hours = 40
    regular_rate = 200
    extra = 300

    if worked <= normal_hours:
        total = worked * regular_rate
        conn.send(f"You will receive Tk{total} for {worked} hours.".encode(format))
    else:
        regular_pay = normal_hours * regular_rate
        extra_hours = worked - normal_hours
        overtime_pay = extra_hours * extra
        total = regular_pay + overtime_pay
        conn.send(f"You will receive Tk{total} for {worked} hours.".encode(format))
 
 conn.close()

while True:
  conn, addr = server.accept()
  thread = threading.Thread(target = handle_clients_of_server, args = (conn, addr))
  thread.start()

