# Network layer: Networks and Inter networks, virtual circuits and datagrams, addressing, subnetting, Routing- (Distance vector and link state routing), Network Layer Protocols- (ARP,IPV4, ICMP, IPV6).

import random
import time

# Network Layer Simulation Class
class NetworkLayer:
    def __init__(self):
        # Simulated parameters
        self.ipv4_addresses = ["192.168.1.1", "192.168.1.2", "192.168.2.1", "192.168.2.2"]
        self.ipv6_addresses = ["2001:0db8:85a3:0000:0000:8a2e:0370:7334", "2001:0db8:85a3:0000:0000:8a2e:0370:7335"]
        self.subnet_mask = "255.255.255.0"
        self.routing_table = {
            "192.168.1.1": ["192.168.1.2", "192.168.2.1"],
            "192.168.2.1": ["192.168.2.2", "192.168.1.1"]
        }

    # Networks and Internetworks: Simulate a basic routing between two networks
    def internetwork(self):
        print("\nInternetworking: Routing between different networks")
        source_ip = "192.168.1.1"
        destination_ip = "192.168.2.2"
        print(f"Sending packet from {source_ip} to {destination_ip}...")
        route = self.routing_table[source_ip]
        print(f"Routing Table for {source_ip}: {route}")
        if destination_ip in route:
            print(f"Packet routed successfully to {destination_ip}.")
        else:
            print("Routing failed. Destination unreachable.")
    
    # Virtual Circuits vs. Datagrams: Simulate sending data using virtual circuit and datagram
    def virtual_circuit_vs_datagram(self):
        print("\nVirtual Circuit vs Datagram")
        print("Virtual Circuit Simulation: Establishes a path between source and destination.")
        print("Datagram Simulation: Each packet is routed independently with no predefined path.")
        time.sleep(1)
    
    # Addressing: Basic Address Resolution Protocol (ARP) Simulation
    def arp_protocol(self):
        print("\nARP (Address Resolution Protocol) Simulation:")
        ip_address = "192.168.1.1"
        mac_address = "00:1A:2B:3C:4D:5E"
        print(f"IP Address {ip_address} corresponds to MAC Address {mac_address}.")
        time.sleep(1)
    
    # Subnetting: Split a network into subnets
    def subnetting(self):
        print("\nSubnetting:")
        network = "192.168.1.0/24"
        subnet_mask = "255.255.255.0"
        print(f"Original Network: {network} with Subnet Mask: {subnet_mask}")
        # Simulate subnetting by dividing the network
        subnets = ["192.168.1.0/25", "192.168.1.128/25"]
        print(f"Subnets after splitting: {subnets}")
        time.sleep(1)
    
    # Routing Algorithms: Distance Vector Routing
    def distance_vector_routing(self):
        print("\nDistance Vector Routing:")
        distance_vector_table = {
            "192.168.1.1": {"192.168.1.2": 1, "192.168.2.1": 2},
            "192.168.2.1": {"192.168.2.2": 1, "192.168.1.1": 2}
        }
        print("Distance Vector Routing Table: ", distance_vector_table)
        source_ip = "192.168.1.1"
        destination_ip = "192.168.2.1"
        print(f"Finding the best route from {source_ip} to {destination_ip}...")
        distance = distance_vector_table[source_ip][destination_ip]
        print(f"Best route cost from {source_ip} to {destination_ip}: {distance}")
    
    # Routing Algorithms: Link State Routing
    def link_state_routing(self):
        print("\nLink State Routing:")
        link_state_table = {
            "192.168.1.1": {"192.168.1.2": 1, "192.168.2.1": 3},
            "192.168.2.1": {"192.168.2.2": 1, "192.168.1.1": 3}
        }
        print("Link State Routing Table: ", link_state_table)
        source_ip = "192.168.1.1"
        destination_ip = "192.168.2.2"
        print(f"Finding the best route from {source_ip} to {destination_ip}...")
        cost = link_state_table[source_ip][destination_ip]
        print(f"Best route cost from {source_ip} to {destination_ip}: {cost}")
    
    # Network Layer Protocols:
    def ipv4_protocol(self):
        print("\nIPv4 Protocol:")
        ip = "192.168.1.1"
        print(f"IPv4 Address: {ip}")
        print(f"IPv4 Header (Simplified): Version=4, Header Length=20, TTL=64")
        time.sleep(1)
    
    def ipv6_protocol(self):
        print("\nIPv6 Protocol:")
        ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        print(f"IPv6 Address: {ip}")
        print(f"IPv6 Header (Simplified): Version=6, Traffic Class=0, Flow Label=0")
        time.sleep(1)
    
    def icmp_protocol(self):
        print("\nICMP Protocol:")
        print("ICMP is used for error reporting and diagnostics in networking (e.g., Ping).")
        print("Sending Echo Request to 192.168.1.1...")
        time.sleep(1)
        print("Reply received from 192.168.1.1: bytes=32 time=1ms TTL=64")
    
# Main simulation class for the Network Layer
class NetworkLayerSimulation:
    def __init__(self):
        self.network_layer = NetworkLayer()

    def simulate(self):
        # Simulate Network Layer components
        self.network_layer.internetwork()
        self.network_layer.virtual_circuit_vs_datagram()
        self.network_layer.arp_protocol()
        self.network_layer.subnetting()
        self.network_layer.distance_vector_routing()
        self.network_layer.link_state_routing()
        self.network_layer.ipv4_protocol()
        self.network_layer.ipv6_protocol()
        self.network_layer.icmp_protocol()

# Main function to run the Network Layer simulation
def main():
    print("Network Layer Simulation: Routing, Addressing, and Protocols\n")
    
    # Run the simulation
    simulation = NetworkLayerSimulation()
    simulation.simulate()

# Execute the simulation
if __name__ == "__main__":
    main()
