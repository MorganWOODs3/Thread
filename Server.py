import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


server_socket = socket.socket()
server_socket.bind(((HOST,PORT)))
server_socket.listen(1)
conn, address = server_socket.accept()
print("J'accept la connection au client depuis %s:%s "% (address[0], address[1]))

message = "Server"



while message != "kill":
    msg = conn.recv(1024)
    message = msg.decode()
    print(message)
    conn.send("Server connecté ".encode())


    if message == "nom":
        host = socket.gethostname()
        print(f"Le message vien de : {host}")

    udpSvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # if message == "msg":
    #     rep = input("Envoie un message: ")
    #     conn.send(rep.encode())
    #     print(rep)
    if message == "reset":
        conn.close()
        print("Connexion terminé")
        server_socket = socket.socket()
        server_socket.bind(((HOST, PORT)))
        server_socket.listen(1)
        conn, address = server_socket.accept()
        print("J'accept la connection au client depuis %s:%s " % (address[0], address[1]))



conn.close()
print("Connexion terminé du client")
server_socket.close()
print("Connexion terminé du Server")





