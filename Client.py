from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
import sys
import socket

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("untitled.ui", self)
        self.show()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()
# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setGeometry(100, 100, 200, 300)
#     window.setWindowTitle("My first app")
#
#
#
#     layout = QVBoxLayout()
#
#     label = QLabel("Press the Button Below")
#     textbox = QTextEdit()
#     button = QPushButton("Press Me!")
#
#     button.clicked.connect(lambda: clicked_on(textbox.toPlainText()))
#
#     layout.addWidget(label)
#     layout.addWidget(textbox)
#     layout.addWidget(button)
#
#     window.setLayout(layout)
#     # label = QLabel(window)
#     # label.setText("Bonjour Tout le monde")
#     # label.setFont(QFont("Arial", 16))
#     # label.move(50, 100)
#
#     window.show()
#     app.exec_()
#
# def clicked_on(msg):
#     message = QMessageBox()
#     message.setText(msg)
#     message.exec_()

if __name__ == '__main__':
    main()


host = "127.0.0.1"  # The server's hostname or IP address
port = 65432  # The port used by the server

message = 'Client'

print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")

while message != 'disconnect':
    message = input("\nCommande Server : ")
    client_socket.send(message.encode())
    print("\nMessage envoyé\n")
    message = client_socket.recv(1024).decode()
    print(f"Message du serveur : \n{message}\n")

# Fermeture de la socket du client
client_socket.close()
print("Connexion arrêter : Server")





#
#
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

