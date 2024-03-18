import socket

class UnityServer:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.client_address = None
        self.is_connected = False

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor ouvindo em {self.host}:{self.port}")
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Conexão estabelecida com {self.client_address}")
        self.is_connected = True

    def restart(self):
        self.server_socket.listen()
        print(f"Servidor ouvindo em {self.host}:{self.port}")
        self.client_socket, self.client_address = self.server_socket.accept()
        print(f"Conexão estabelecida com {self.client_address}")
        self.is_connected = True

    def send_message(self, golpe):
        if not self.is_connected:
            print("Não foi possível enviar a mensagem: servidor não conectado")
        else:
            message_bytes = golpe.encode("utf-8")
            self.client_socket.sendall(message_bytes)


    def send_image(self, image_encoded):
        if self.is_connected:
            self.client_socket.sendall(image_encoded)


    def disconnect(self):
        print("Desconectando do cliente...")
        self.client_socket.close()
        self.is_connected = False
        self.restart()
