import socket

class UnityServer:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor ouvindo em {self.host}:{self.port}")
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Conexão estabelecida com {self.client_address}")

    def send_message(self, golpe):
        if golpe.lower() != "exit":
            self.client_socket.sendall(golpe.encode("utf-8"))
        else:
            print("Fechando conexão")
            self.client_socket.close()
            self.server_socket.close()
