# coding=utf-8
# cs2910-lab02-zawadzkip-chuna.py Lab 2 -- UDP/TCP send/receive
# Team members: Patrick Zawadzki (zawadzkip), Aaron Chun (chuna)

# import the "socket" module -- not using "from socket import *" in order to selectively use items with "socket." prefix
import socket

# Port number definitions
# (May have to be adjusted if they collide with ports in use by other programs/services.)
UDP_PORT = 12000
TCP_PORT = 12100

# Host address when acting as "receiver" ("server").
# The address '' means accept any connection for our "receive" port from any network interface
# on this system (including 'localhost' loopback connection).
LISTEN_FOR_HOST = ''

# Address of the "other" ("server") host that should be connected to for "send" operations.
# When connecting on one system, use 'localhost'
OTHER_HOST = '155.92.72.17'
# When "sending" to another system, use its IP address (or DNS name if there it has one)
# OTHER_HOST = '155.92.78.250'

def main():
    # Get chosen operation from the user.
    action = raw_input('Select "(1-TS) tcpsend", or "(2-TR) tcpreceive":')
    # Execute the chosen operation.
    if action in ['1', 'TS', 'ts', 'tcpsend']:
        message = 'X' * 10000;
        tcp_send(OTHER_HOST, TCP_PORT, message);
    elif action in ['2', 'TR', 'tr', 'tcpreceive']:
        tcp_receive(TCP_PORT);
    else:
        print "Unknown action: '{0}'".format(action)


# Send a TCP message to a designated host/port.
# Receive a one-character response from the "server".
# Print the received response.
# Close the socket
# Return
def tcp_send(server_host, server_port, message):
    print "tcp_send: dst_host='{0}', dst_port={1}, message='{2}'".format(server_host, server_port, message)
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.connect((server_host, server_port))
    # Replace this comment with your code.
    i = 0
    while (i != 10):
        socket_obj.send(message)
        i+=1
    socket_obj.send("Q")
    print "Return message {}".format(socket_obj.recv(256))
    socket_obj.close()


# Listen for a TCP connection on a designated "listening" port
# Accept the connection, creating a connection socket
# Print the address and port of the sender
# Receive the message string (one "socket.recv" call is sufficient for now)
# Print the message length and message string
# Send a single-character response (e.g., "Y") back to the sender
# Close the connection socket
# Close the listening socket
# Return
def tcp_receive(listen_port):
    print "tcp_receive (server): listen_port={0}".format(listen_port)
    # Replace this comment with your code.
    socket_listen_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_listen_obj.bind((LISTEN_FOR_HOST, listen_port))
    socket_listen_obj.listen(2)
    data_socket_tuple = socket_listen_obj.accept()
    message = data_socket_tuple[0].recv(256)
    print "tcp message received '{0}'...length {1}".format(message, len(message))
    data_socket_tuple[0].send("Y")
    data_socket_tuple[0].close()
    socket_listen_obj.close()

# Invoke the main method to run the program.
main()
