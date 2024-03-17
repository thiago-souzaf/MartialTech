import socket
import pickle
import struct

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

    def send_message(self, golpe):
        if golpe.lower() != "exit":
            message_bytes = golpe.encode("utf-8")
            message_size = struct.pack("!L", len(message_bytes))
            
            self.client_socket.sendall(message_bytes)
        else:
            print("Fechando conexão")
            self.client_socket.close()
            self.server_socket.close()
        
    def send_image(self, image_encoded):
        data = pickle.dumps(image_encoded, protocol=3)
        size = struct.pack("!L", len(data))
        # print(len(data))

        self.client_socket.sendall(image_encoded)
