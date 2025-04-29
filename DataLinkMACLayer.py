# Data Link MAC Layer: Data link layer services, error-detection and correction techniques,error recovery protocols (stop and wait, go back n, selective repeat), multiple access protocols,(TDMA/FDP, CDMA/FDD/CSMA/CD, CSMA/CA), Datalink and MAC addressing, Ethernet,data link layer switching, point-to-point protocol.

import random
import time

# Data Link Layer Simulation Class
class DataLinkLayer:
    def __init__(self):
        self.frame_size = 8  # Example frame size (in bits)
        self.error_probability = 0.1  # Probability of error occurring in transmission
    
    # Error Detection and Correction (simple parity bit approach)
    def error_detection(self, data):
        print("\nError Detection and Correction:")
        parity_bit = sum([int(bit) for bit in data]) % 2
        print(f"Original Data: {data}")
        print(f"Calculated Parity Bit: {parity_bit}")
        received_data = data + str(parity_bit)
        if random.random() < self.error_probability:
            received_data = self.introduce_error(received_data)
            print(f"Received Data with Error: {received_data}")
        else:
            print(f"Received Data: {received_data}")
        return received_data
    
    def introduce_error(self, received_data):
        error_position = random.randint(0, len(received_data) - 1)
        received_data = list(received_data)
        received_data[error_position] = '1' if received_data[error_position] == '0' else '0'
        return ''.join(received_data)
    
    # Error Recovery Protocols
    def stop_and_wait(self, data):
        print("\nStop and Wait Protocol:")
        print(f"Sending Data: {data}")
        print("Receiver acknowledges the frame. Sending the next frame after receiving acknowledgment.")
        time.sleep(1)
        print("Data Sent Successfully.")

    def go_back_n(self, data, n):
        print("\nGo Back N Protocol:")
        for i in range(0, len(data), n):
            print(f"Sending Frame {i//n + 1}: {data[i:i+n]}")
            print(f"Receiver acknowledges frame {i//n + 1}")
            time.sleep(1)
        print("Data Sent Successfully.")

    def selective_repeat(self, data, n):
        print("\nSelective Repeat Protocol:")
        frames_sent = [data[i:i + n] for i in range(0, len(data), n)]
        for i, frame in enumerate(frames_sent):
            print(f"Sending Frame {i+1}: {frame}")
            if random.random() < 0.1:  # Simulating possible packet loss or error
                print(f"Frame {i+1} lost or errored, will retransmit.")
            else:
                print(f"Receiver acknowledges Frame {i+1}")
            time.sleep(1)
        print("Data Sent Successfully.")
    
    # Multiple Access Protocols
    def tdma(self):
        print("\nTDMA (Time Division Multiple Access):")
        print("Each user is allocated a specific time slot to send data.")
        time.sleep(1)
    
    def fdma(self):
        print("\nFDMA (Frequency Division Multiple Access):")
        print("Each user is allocated a specific frequency band for data transmission.")
        time.sleep(1)

    def cdma(self):
        print("\nCDMA (Code Division Multiple Access):")
        print("Each user is assigned a unique code to allow multiple users to transmit simultaneously.")
        time.sleep(1)
    
    def csma_cd(self):
        print("\nCSMA/CD (Carrier Sense Multiple Access with Collision Detection):")
        print("A node listens to the channel before sending data. If the channel is busy, it waits.")
        print("If a collision occurs, the node retransmits the data after a random backoff time.")
        time.sleep(1)

    def csma_ca(self):
        print("\nCSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):")
        print("Before sending data, nodes perform a random backoff to avoid collision.")
        time.sleep(1)

    # MAC Addressing Simulation (Ethernet addressing)
    def mac_addressing(self):
        print("\nMAC Addressing (Ethernet):")
        sender_mac = "00:1A:2B:3C:4D:5E"
        receiver_mac = "00:1A:2B:3C:4D:6F"
        print(f"Sender MAC Address: {sender_mac}")
        print(f"Receiver MAC Address: {receiver_mac}")
        time.sleep(1)

    # Point-to-Point Protocol (PPP)
    def point_to_point_protocol(self):
        print("\nPoint-to-Point Protocol (PPP):")
        print("PPP allows two devices to establish a direct connection and exchange data.")
        print("It provides authentication, encryption, and compression services.")
        time.sleep(1)

# Main simulation class for the Data Link Layer
class DataLinkLayerSimulation:
    def __init__(self):
        self.dl_layer = DataLinkLayer()

    def simulate(self):
        data = ''.join([random.choice(['0', '1']) for _ in range(self.dl_layer.frame_size)])

        # Simulate error detection
        received_data = self.dl_layer.error_detection(data)
        
        # Simulate error recovery protocols
        self.dl_layer.stop_and_wait(data)
        self.dl_layer.go_back_n(data, 4)
        self.dl_layer.selective_repeat(data, 4)
        
        # Simulate multiple access protocols
        self.dl_layer.tdma()
        self.dl_layer.fdma()
        self.dl_layer.cdma()
        self.dl_layer.csma_cd()
        self.dl_layer.csma_ca()

        # Simulate MAC Addressing and Point-to-Point Protocol
        self.dl_layer.mac_addressing()
        self.dl_layer.point_to_point_protocol()

# Main function to run the Data Link Layer simulation
def main():
    print("Data Link Layer (MAC Layer) Simulation\n")
    
    # Run the simulation
    simulation = DataLinkLayerSimulation()
    simulation.simulate()

# Execute the simulation
if __name__ == "__main__":
    main()
