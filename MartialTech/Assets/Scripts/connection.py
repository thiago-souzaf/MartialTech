import socket
import time

host, port = "127.0.0.1", 25001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((host, port))
    send = 0
    while True:
        message = input("Digite a mensagem (ou 'exit' para sair): ")
        message = "soco"
        if message.lower() == 'exit' or send == 5:
            break
        
        send += 1
        sock.sendall(message.encode("utf-8"))
        data = sock.recv(1024).decode("utf-8")
        print("Resposta do servidor:", data)
        time.sleep(1)
finally:
    sock.close()