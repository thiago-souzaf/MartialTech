import socket

host, port = "127.0.0.1", 25002

# Cria um socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liga o socket ao endereço e porta especificados
server_socket.bind((host, port))

# Habilita o servidor para aceitar conexões
server_socket.listen()

print(f"Servidor ouvindo em {host}:{port}")

# Aceita a conexão do cliente
client_socket, client_address = server_socket.accept()

try:
    print(f"Conexão estabelecida com {client_address}")

    while True:
        # Aguarda entrada do usuário
        message = input("Digite o golpe realizado para enviar ao unity (ou 'exit' para encerrar): ")

        if message.lower() == 'exit':
            break

        # Envia a mensagem para o unity
        client_socket.sendall(message.encode("utf-8"))

finally:
    print("Fechando conexão")
    client_socket.close()
    server_socket.close()
