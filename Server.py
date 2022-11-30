import platform
import socket
import psutil
import os
import sys

Host = "127.0.0.1"  # Standard loopback interface address (localhost)
Port = 65432  # Port to listen on (non-privileged ports are > 1023)


server_socket = socket.socket()
server_socket.bind(((Host,Port)))
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

    if message == 'ip':
        ip = (str(server_socket.getsockname()[0]))
        print(f"L'IP du server est : {ip}")
        conn.send(f"L'IP du server est : {ip}".encode())

    if message == "reset":
        conn.close()
        print("Connexion terminé")
        server_socket = socket.socket()
        server_socket.bind(((Host, Port)))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("J'accept la connection au client depuis %s:%s " % (address[0], address[1]))


    if message == "os":
        print(f"\nL'os est : {platform.system()}")
        conn.send(f"\nL'os est : {platform.system()}".encode())

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

    if message == 'mkdir':
        nom = "toro"
        os.mkdir(nom)
        conn.send(f'\n Le fichier /{nom}/ est crée'.encode())
        print(f'\n Le fichier {nom} à été crée !')

    if message == "dir":
        com = os.popen('dir').read()
        print(f'\nVoici la commande dir \n{com}')
        conn.send(f'\nVoici la commande dir \n {com}'.encode())

    if message == "shell":
        process = os.popen('wmic process get description, processid').read()
        conn.send(process.encode())

    if message == 'version':
        vers = sys.version
        print("\n Version actuelle :\n", sys.version)
        conn.send(str(f'\nVoici la version de python : \n {vers}').encode())

    if message == 'ping':
        ip = "8.8.8.8"
        ping = os.popen(f"ping {ip}").read()
        print(f'\nVoici le ping : \n{ping}')
        conn.send(f'\nVoici le ping : \n {ping}'.encode())

conn.send(f'la connexion du server est fini'.encode())
server_socket.close()
print("Connexion arrêter : Server")






