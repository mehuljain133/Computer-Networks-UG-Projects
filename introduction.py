# Introduction: Types of computer networks, Internet, Intranet, Network topologies, Network classifications

# Importing necessary libraries for simulation
import random

# Class to represent a Network
class Network:
    def __init__(self, network_type, topology, classification, devices=None):
        self.network_type = network_type          # Type of network (e.g., LAN, WAN, MAN)
        self.topology = topology                  # Network topology (e.g., Star, Ring, Bus)
        self.classification = classification      # Network classification (e.g., Private, Public)
        self.devices = devices if devices else [] # List of devices in the network
    
    def add_device(self, device):
        """Method to add a device to the network"""
        self.devices.append(device)
        print(f"Device {device} added to the {self.network_type} network.\n")
    
    def display_network_info(self):
        """Display information about the network"""
        print(f"Network Type: {self.network_type}")
        print(f"Network Topology: {self.topology}")
        print(f"Network Classification: {self.classification}")
        print(f"Devices in the Network: {', '.join(self.devices) if self.devices else 'No devices'}\n")

# Simulating Different Network Types

# LAN (Local Area Network) example
lan = Network("LAN (Local Area Network)", "Star Topology", "Private")

# MAN (Metropolitan Area Network) example
man = Network("MAN (Metropolitan Area Network)", "Ring Topology", "Private")

# WAN (Wide Area Network) example
wan = Network("WAN (Wide Area Network)", "Bus Topology", "Public")

# Simulate network topologies
def simulate_topology(network):
    """Simulate network communication based on topology"""
    if network.topology == "Star Topology":
        print(f"Simulating Star Topology for {network.network_type}...\n")
        print("Devices are connected to a central hub or switch.")
    elif network.topology == "Ring Topology":
        print(f"Simulating Ring Topology for {network.network_type}...\n")
        print("Devices are connected in a circular manner, and data flows in one direction.")
    elif network.topology == "Bus Topology":
        print(f"Simulating Bus Topology for {network.network_type}...\n")
        print("All devices share a single communication line.")
    else:
        print("Unknown Topology. Simulation cannot be done.\n")

# Network Classifications Simulation

def simulate_internet():
    """Simulate Internet network classification"""
    print("The Internet is a global public network connecting millions of devices.\n")
    print("It enables communication, access to information, and services like websites, emails, etc.\n")

def simulate_intranet():
    """Simulate Intranet network classification"""
    print("Intranet is a private network used by organizations to share information securely within.\n")
    print("Only authorized members within the organization have access to this network.\n")

# Function to simulate a real-world scenario where devices communicate in a network
def device_communication(network):
    """Simulate communication between devices in the network"""
    if not network.devices:
        print("No devices available in the network for communication.\n")
        return
    
    print(f"Simulating communication in {network.network_type}...\n")
    sender = random.choice(network.devices)
    receiver = random.choice(network.devices)
    
    # Avoid sender being the same as receiver
    while sender == receiver:
        receiver = random.choice(network.devices)
    
    print(f"Device {sender} sends a message to {receiver}.\n")
    print(f"Message successfully delivered from {sender} to {receiver} in {network.network_type}.\n")

# Main function to simulate all network features
def main():
    # Display Network Information
    print("Computer Network Simulation\n")
    print("-" * 50)
    
    # Add some devices to the networks
    lan.add_device("Laptop1")
    lan.add_device("Desktop1")
    man.add_device("Server1")
    man.add_device("Router1")
    wan.add_device("GlobalServer1")
    wan.add_device("GlobalRouter1")
    
    # Display the network details
    lan.display_network_info()
    man.display_network_info()
    wan.display_network_info()
    
    # Simulate network topologies
    simulate_topology(lan)
    simulate_topology(man)
    simulate_topology(wan)
    
    # Simulate classifications (Internet vs Intranet)
    print("-" * 50)
    print("Network Classifications Simulation:\n")
    simulate_internet()
    simulate_intranet()
    
    # Simulate device communication
    print("-" * 50)
    device_communication(lan)
    device_communication(man)
    device_communication(wan)
    
if __name__ == "__main__":
    main()
