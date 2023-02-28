import psutil

for conn in psutil.net_connections():
    if conn.status == 'ESTABLISHED':
        print(f"Port: {conn.laddr.port}, Process: {conn.pid}")