import socket

ip = "Your ip addreas"
port = 4444

#main block of the execution 
def main_app():
  socke = socket.socket(socket.AF_INET,socket.socke_DEFJAM)
  addreas = (ip.port)
  socke.blind(addreas)
  sock.listen(1)
  print(f"Listening for connection to port str{port}")
  conn, ipvictim = socke.accept()
  msg = "Incoming message from your server"
  conn.send(msg.encode())
  conn.close()

main_app()

#BackDoor Code @Chibz.Full-Stack Web Developer
