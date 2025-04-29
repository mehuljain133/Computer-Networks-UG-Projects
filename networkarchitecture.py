# Network Architecture Models: Layered architecture approach, OSI Reference Model, TCP/IPReference Model.

import time

# OSI Model Layers
class OSIModel:
    def __init__(self):
        self.layers = [
            "Physical Layer: Transmits raw bits over the physical medium.",
            "Data Link Layer: Handles node-to-node data transfer.",
            "Network Layer: Determines the path for data transfer (routing).",
            "Transport Layer: Ensures reliable data transfer between systems.",
            "Session Layer: Manages sessions between applications.",
            "Presentation Layer: Transforms data formats (encryption, compression).",
            "Application Layer: Provides network services to applications."
        ]

    def simulate_data_flow(self, data):
        print("\nSimulating Data Flow through OSI Model...")
        for layer in self.layers:
            print(f"Data is being processed at the {layer.split(':')[0]}...")
            time.sleep(1)  # Simulate time taken for data processing at each layer
        print("\nData transmission complete through OSI Model.\n")


# TCP/IP Model Layers
class TCPIPModel:
    def __init__(self):
        self.layers = [
            "Link Layer: Responsible for communication within the local network.",
            "Internet Layer: Handles logical addressing (IP), routing.",
            "Transport Layer: Manages end-to-end communication (TCP, UDP).",
            "Application Layer: Provides application-level services (HTTP, FTP, etc.)."
        ]

    def simulate_data_flow(self, data):
        print("\nSimulating Data Flow through TCP/IP Model...")
        for layer in self.layers:
            print(f"Data is being processed at the {layer.split(':')[0]}...")
            time.sleep(1)  # Simulate time taken for data processing at each layer
        print("\nData transmission complete through TCP/IP Model.\n")


# Network Communication Simulation
class NetworkCommunicationSimulation:
    def __init__(self):
        self.osi_model = OSIModel()
        self.tcpip_model = TCPIPModel()

    def simulate_communication(self, message):
        print("\nStarting communication...\n")
        
        # Simulate OSI model data flow
        self.osi_model.simulate_data_flow(message)

        # Simulate TCP/IP model data flow
        self.tcpip_model.simulate_data_flow(message)

        print(f"Final message delivered: {message}")


# Main function to simulate data transmission
def main():
    print("Network Communication Simulation (OSI vs TCP/IP)\n")
    
    # Initialize communication simulator
    simulation = NetworkCommunicationSimulation()
    
    # Simulate sending a message
    message = "Hello, this is a test message for real data transmission."
    simulation.simulate_communication(message)


# Run the simulation
if __name__ == "__main__":
    main()
