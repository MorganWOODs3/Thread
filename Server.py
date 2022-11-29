import platform
import socket
import psutil
import os

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


server_socket = socket.socket()
server_socket.bind(((HOST,PORT)))
server_socket.listen(1)
conn, address = server_socket.accept()
print("J'accepte la connection au client depuis %s:%s " % (address[0], address[1]))
udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Server"



while message != "kill":
    msg = conn.recv(1024)
    message = msg.decode()
    # conn.send("Server connecté ".encode())
    # print(message)



    if message == "name":
        host = socket.gethostname()
        print(f"Le message vien de : {host}")
        conn.send(f"le nom de l'host {host}".encode())


    if message == "reset":
        conn.close()
        print("Connexion terminé")
        server_socket = socket.socket()
        server_socket.bind(((HOST, PORT)))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("J'accept la connection au client depuis %s:%s " % (address[0], address[1]))


    if message == "os":
        print(f"l'os est{platform.node()}")
        conn.send(platform.node().encode())

    if message == "cpu":
        load1, load5, load15 = psutil.getloadavg()
        Cpu_usage = (load15 / os.cpu_count()) * 100
        print("l'usage du CPU est  ", Cpu_usage)
        conn.send(f"L'usage du CPU est de {str(Cpu_usage)}%".encode())

    if message == "ram":
        print(f"Ram :{psutil.virtual_memory()}")
        ram = str(psutil.virtual_memory())
        conn.send(f'Le test de la Ram aboutie à : {ram}'.encode())

    if message == 'discconect':
        conn.send(f'la connexion du client est fini'.encode())
        conn.close()
        print("Connexion arrêter : Client")

    if message == 'ping':
        ip = input('ip :')
        os.system(('ping -n 4 {}'.format(ip)))

conn.send(f'la connexion du server est fini'.encode())
server_socket.close()
print("Connexion arrêter : Server")






