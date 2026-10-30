import socket

def UDP_WLAN_Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 50000))
    print("Listening for WLAN messages...")
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Message from {addr}: {data.decode('utf-8')}")

def upd_wlan_client():
    sock = socket.socket(socket.AF_INET,socket.SOCK_GRAM)
    sock.setsockopt(
        socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    message = "Hello from Python over WLAN!"
    sock.sendto(message.encode("utf-8"), ("192.168.1.255",50000))
    sock.close()

def wlan_tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 50001))  # Bind to local machine IP on port 50001
    server.listen(1)
    print("Waiting for connection...")

    conn, addr = server.accept()
    print(f"Connected by {addr}")

    while True:
      data = conn.recv(1024)
      if not data:
        break
      print(f"Received: {data.decode('utf-8')}")
      conn.sendall(b"ACK: Message received")

    conn.close()

def wlan_tcp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Replace with the WLAN IP address of the machine running the TCP server
    client.connect(('192.168.X.XXX', 50001))

    client.sendall(b"Hello server over WLAN!")
    response = client.recv(1024)
    print(f"Server response: {response.decode('utf-8')}")
    client.close()
    
