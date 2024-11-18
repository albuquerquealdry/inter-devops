# import socket

# def check_port(host: str, port: int, timeout: float = 3.0) -> bool:

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.settimeout(timeout)
#         try:
#             sock.connect((host, port))
#             return True
#         except (socket.timeout, socket.error):
#             return False

# if __name__ == "__main__":
#     host = input("Digite o endereço do servidor (exemplo: 127.0.0.1): ")
#     port = int(input("Digite a porta para verificar (exemplo: 22): "))

#     if check_port(host, port):
#         print(f"A porta {port} no servidor {host} está aberta.")
#     else:
#         print(f"A porta {port} no servidor {host} não responde.")
















