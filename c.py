import socket
import threading
import sys
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

menu_string = 'Enter your passphrase:\n'
print(menu_string)
passphrase = input('> ')

def encrypt(passphrase, message):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=passphrase.encode("ascii"),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode("ascii")))
    f = Fernet(key)
    token = f.encrypt(message.encode("ascii"))
    return token

def decrypt(passphrase, token):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=passphrase.encode("ascii"),
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode("ascii")))
    f = Fernet(key)
    message = f.decrypt(token)
    return message

def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(data)
            #print(str(decrypt(passphrase, data.decode("utf-8"))))
        except:
            print("Disconnected")
            signal = False
            break
host = 'localhost'
port = 4488
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
except:
    print("Could not make a connection")
    input("Press enter to quit")
    sys.exit(0)
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

while True:
    message = input()
    sock.sendall(encrypt(passphrase, message))