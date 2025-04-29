# Transport and Application Layer: Process to process Delivery- (client server paradigm,connectionless versus connection oriented service, reliable versus unreliable); User DatagramProtocols, TCP/IP protocol, Flow Control

import socket
import random
import time
import threading

# Transport Layer Class: Simulating Transport Layer protocols (TCP, UDP)
class TransportLayer:
    def __init__(self):
        self.buffer_size = 1024  # Simulating buffer size for data transmission
        self.server_address = ('localhost', 12345)
    
    # Simulate connection-oriented (TCP)
    def tcp_connection_oriented(self):
        print("\nConnection-Oriented Service (TCP) Simulation")
        print("Establishing TCP Connection...")
        print("Connection Established using 3-Way Handshake.")
        print("Data transmission using a reliable and ordered stream.")
        # Simulating TCP Transmission (Reliable)
        message = "TCP Message: This is a reliable connection-oriented service."
        print(f"Sending: {message}")
        print("Receiving message at receiver end...")
        time.sleep(2)  # Simulate latency
        print(f"Received: {message}")
        print("Connection closed after data transmission.")
        time.sleep(1)
    
    # Simulate connectionless (UDP)
    def udp_connectionless(self):
        print("\nConnectionless Service (UDP) Simulation")
        print("UDP does not establish a connection. It sends data packets independently.")
        message = "UDP Message: This is an unreliable connectionless service."
        print(f"Sending: {message}")
        print("Packet is sent without guarantee of delivery.")
        time.sleep(1)
    
    # Flow Control Mechanism
    def flow_control(self):
        print("\nFlow Control Simulation")
        sender_window_size = 5
        receiver_window_size = 3
        print(f"Sender's Window Size: {sender_window_size}")
        print(f"Receiver's Window Size: {receiver_window_size}")
        print("Flow control ensures that data is sent in manageable chunks.")
        for i in range(1, 11):
            if i <= sender_window_size:
                print(f"Sending packet {i} to receiver...")
            else:
                print(f"Sender waiting for ACK for packet {i - sender_window_size}...")
            time.sleep(1)
        print("All packets have been sent and flow control applied.\n")

# Application Layer Class: Simulating basic client-server communication
class ApplicationLayer:
    def __init__(self):
        self.client_socket = None
        self.server_socket = None
        self.client_address = ('localhost', 12345)
    
    # Simulating a Client-Server Communication using TCP
    def client_server_communication(self):
        print("\nClient-Server Communication (TCP) Simulation")
        
        # Server Simulation
        def server():
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind(self.client_address)
            self.server_socket.listen(1)
            print("Server is waiting for connection...")
            connection, client_address = self.server_socket.accept()
            print(f"Connection established with {client_address}.")
            message = connection.recv(1024)
            print(f"Server received: {message.decode()}")
            connection.sendall(b"Message received successfully.")
            connection.close()
        
        # Client Simulation
        def client():
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(self.client_address)
            message = "Hello Server, this is the client."
            print(f"Client sent: {message}")
            self.client_socket.sendall(message.encode())
            response = self.client_socket.recv(1024)
            print(f"Client received: {response.decode()}")
            self.client_socket.close()

        # Running server and client as threads
        server_thread = threading.Thread(target=server)
        client_thread = threading.Thread(target=client)
        
        server_thread.start()
        time.sleep(1)  # Delay to ensure server is waiting before client sends
        client_thread.start()
        
        server_thread.join()
        client_thread.join()
        time.sleep(1)

# Main Simulation Class for Transport and Application Layer
class TransportApplicationLayerSimulation:
    def __init__(self):
        self.transport_layer = TransportLayer()
        self.application_layer = ApplicationLayer()

    def simulate(self):
        # Simulate Transport Layer concepts
        self.transport_layer.tcp_connection_oriented()
        self.transport_layer.udp_connectionless()
        self.transport_layer.flow_control()
        
        # Simulate Application Layer client-server communication
        self.application_layer.client_server_communication()

# Main function to run the simulation
def main():
    print("Transport and Application Layer Simulation\n")
    
    # Run the simulation
    simulation = TransportApplicationLayerSimulation()
    simulation.simulate()

# Execute the simulation
if __name__ == "__main__":
    main()
