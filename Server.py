from __future__ import with_statement #for python 2.5
import platform
import socket
import psutil
import os
import sys

lines = []
with open("C:/Thread/numbers.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

Host = line
Port = 65432
#
#
server_socket = socket.socket()
server_socket.bind(((Host,Port)))
server_socket.listen(1)
conn, address = server_socket.accept()
print("J'accepte la connection au client depuis %s:%s " % (address[0], address[1]))
udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"L'OS : {platform.system()}")
print(f"L'Hostname : {socket.gethostname()}")
print(f"L'IP : {server_socket.getsockname()[0]}")



message = "Server"

# def serveur():
#     msg = "yhnynnh"
#     msg_split = msg.split()[0]
#
#     conn = None
#     server_socket = None
#     while msg != "kill":
#
#         server_socket = socket.socket()
#         server_socket.bind(("localhost", 65432))
#
#         print(f"L'OS : {platform.system()}")
#         print(f"L'Hostname : {socket.gethostname()}")
#         print(f"L'IP : {server_socket.getsockname()[0]}")
#
#         server_socket.listen(1)
#         print('Serveur en attente de connexion')
#         while msg != "kill" and msg != "reset":
#             msg = ""
#             try :
#                 conn, addr = server_socket.accept()
#                 print(addr)
#             except ConnectionError:
#                 print("erreur de connection")
#                 break
#             else :
#                 while msg != "kill" and msg != "reset" and msg != "disconnect":
#                     msg = conn.recv(1024).decode()
#                     print("Received from client: ", msg)
#                     # msg = input('Enter a message to send: ')
#                     conn.send(msg.encode())
#                 conn.close()
#         print("Connection fini")
#         server_socket.close()
#         print("Server fermer")
#
#     msg = conn.recv(1024).decode()
#     if msg_split == ('powershell'):
#         ps_data = os.popen(msg).read()
#         conn.send(ps_data.encode())
#
#     if message == "os":
#         print(f"\nL'os est : {platform.system()}")
#         conn.send(f"\nL'os est : {platform.system()}".encode())
#
# if __name__ == '__main__':
#     serveur()




while message != "kill":
    message = conn.recv(1024).decode()

    msg_split = message.split()[0]
    conn.send("Server connecté ".encode())
    print(message)

    if message == "name":
        host = socket.gethostname()
        print(f"Le message vien de : {host}")
        conn.send(f"le nom de l'host {host}".encode())



    if msg_split == ('powershell'):
        ps_data = os.popen(f'{msg}').read()
        conn.send(f'{ps_data}'.encode())



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






