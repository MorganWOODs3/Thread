# echo-client.py
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys
import socket

host = "127.0.0.1"  # The server's hostname or IP address
port = 65432  # The port used by the server
#
# client_socket = socket.socket()
# client_socket.connect((HOST, PORT))
# message = "Client en attente"
# client_socket.send(message.encode())
# data = client_socket.recv(1024)
# print(data.decode())
# env = input("Envoie une commande: ")
# client_socket.send(env.encode())



message = 'Client'

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

while message != 'disconnect':
    message = input("Commande Server : ")
    client_socket.send(message.encode())
    print("Message envoyé")
    message = client_socket.recv(1024).decode()
    print(f"Message du serveur : {message}")

# Fermeture de la socket du client







# class TextEditDemo(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.i = 0
#         self.setWindowTitle("QTextEdit")
#         self.resize(300, 270)
#
#         self.textEdit = QTextEdit()
#         self.textEdit.setEnabled(False)
#         self.btnPress1 = QPushButton("Add message")
#         self.btnPress2 = QPushButton("Clear")
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.textEdit)
#         layout.addWidget(self.btnPress1)
#         layout.addWidget(self.btnPress2)
#         self.setLayout(layout)
#
#         self.btnPress1.clicked.connect(self.btnPress1_Clicked)
#         self.btnPress2.clicked.connect(self.btnPress2_Clicked)
#
#     def btnPress1_Clicked(self):
#         self.textEdit.append(f"Nouveau texte {self.i}")
#         self.i += 1
# #        self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")
#
#     def btnPress2_Clicked(self):
#         self.textEdit.setPlainText("")
# #        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = TextEditDemo()
#     win.show()
#     sys.exit(app.exec_())