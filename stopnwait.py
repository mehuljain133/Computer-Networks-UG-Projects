#  Simulate and implement stop and wait protocol for noisy channel.

import random
import time

# Stop-and-Wait Protocol Simulation
class StopAndWaitProtocol:
    def __init__(self, frame_data, error_probability=0.1):
        self.frame_data = frame_data  # Data to send (a list of binary data frames)
        self.error_probability = error_probability  # Probability of error (0-1)
        self.timeout = 2  # Timeout for waiting for an ACK (seconds)
    
    # Simulate noise in the channel by flipping bits with a given probability
    def simulate_noise(self, frame):
        noisy_frame = frame[:]
        for i in range(len(frame)):
            if random.random() < self.error_probability:
                noisy_frame[i] ^= 1  # Flip bit to simulate noise
        return noisy_frame
    
    # Sender side: Send a frame and wait for ACK
    def sender(self, frame):
        print(f"Sender: Sending frame: {frame}")
        
        # Simulate noise in the channel by flipping some bits
        noisy_frame = self.simulate_noise(frame)
        
        # Simulate the transmission delay (just for demonstration purposes)
        time.sleep(1)
        
        print(f"Sender: Sent noisy frame: {noisy_frame}")
        
        return noisy_frame
    
    # Receiver side: Receive a frame, check for errors, and send ACK or NAK
    def receiver(self, frame):
        print(f"Receiver: Received frame: {frame}")
        
        # Check if the frame is received correctly (error detection via checksum)
        if self.check_error(frame):
            print("Receiver: No error detected. Sending ACK.")
            return "ACK"
        else:
            print("Receiver: Error detected. Sending NAK.")
            return "NAK"
    
    # Simulate error detection by checking if the received frame matches the original
    def check_error(self, received_frame):
        # For simplicity, we assume no error if the frame is exactly as expected (noisy or not)
        # In practice, this should be more sophisticated (CRC, checksum, etc.)
        # Here we simulate an error if any bit is flipped from the expected frame
        return random.random() > self.error_probability  # Simulate error based on error probability
    
    # Main protocol loop
    def simulate(self):
        for frame in self.frame_data:
            while True:
                # Sender sends the frame
                noisy_frame = self.sender(frame)
                
                # Receiver receives the frame and checks for errors
                ack_or_nak = self.receiver(noisy_frame)
                
                # If ACK received, the frame is successfully transmitted
                if ack_or_nak == "ACK":
                    print("Sender: ACK received. Frame transmitted successfully.")
                    break  # Move to next frame
                
                # If NAK received, retransmit the frame
                else:
                    print("Sender: NAK received. Retrying...")
                    time.sleep(1)  # Retry delay
    
    # To simulate transmission of multiple frames
    def simulate_multiple_frames(self):
        print("Starting Stop-and-Wait protocol simulation...\n")
        self.simulate()

# Example usage of the Stop-and-Wait protocol with noisy channel simulation
if __name__ == "__main__":
    # Example binary data frames to send (each frame is a list of bits)
    frames = [
        [1, 0, 1, 0, 1],  # Frame 1: 10101
        [0, 1, 1, 0, 0],  # Frame 2: 01100
        [1, 1, 0, 1, 0],  # Frame 3: 11010
        [0, 0, 1, 1, 1]   # Frame 4: 00111
    ]
    
    # Create an instance of the Stop-and-Wait Protocol with 10% noise
    protocol = StopAndWaitProtocol(frames, error_probability=0.1)
    
    # Simulate the protocol
    protocol.simulate_multiple_frames()
