import socket

# af_inet means using IPv4 address, sock_stream means use tcp packets for connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ip address of target machine
host = "192.168.207.1"
# enter the port to check
port = 80

# define a function. It takes host and port as input
def port_scanner(port):
    if sock.connect_ex((host,port)):
        print('Port is closed')
    else:
        print('Port %d is open')

# Function call
port_scanner(port)
