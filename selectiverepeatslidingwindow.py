# . Simulate and implement selective repeat sliding window protocol

import random
import time

class SelectiveRepeatProtocol:
    def __init__(self, frames, window_size, error_probability=0.1):
        self.frames = frames  # List of data frames to send (binary frames)
        self.window_size = window_size  # Sender's window size (N)
        self.error_probability = error_probability  # Probability of error (0-1)
        self.timeout = 2  # Timeout for waiting for ACK (in seconds)
    
    # Simulate noise in the channel (bit flips)
    def simulate_noise(self, frame):
        noisy_frame = frame[:]
        for i in range(len(frame)):
            if random.random() < self.error_probability:
                noisy_frame[i] ^= 1  # Flip bit to simulate error
        return noisy_frame
    
    # Sender: Send a window of frames
    def sender(self, window_start):
        window_end = min(window_start + self.window_size, len(self.frames))
        print(f"\nSender: Sending frames {window_start + 1} to {window_end}...")
        
        sent_frames = []
        for i in range(window_start, window_end):
            frame = self.frames[i]
            noisy_frame = self.simulate_noise(frame)
            sent_frames.append(noisy_frame)
            print(f"Sender: Sent frame {i + 1}: {noisy_frame}")
        
        return sent_frames, window_end
    
    # Receiver: Receive a frame and check for errors
    def receiver(self, sent_frame, expected_frame):
        print(f"Receiver: Received frame {expected_frame + 1}: {sent_frame}")
        
        # Check if the received frame is correct
        if self.check_error(sent_frame):
            print(f"Receiver: Frame {expected_frame + 1} is correct. Sending ACK.")
            return True
        else:
            print(f"Receiver: Error in frame {expected_frame + 1}. Sending NAK.")
            return False
    
    # Simulate error detection (random errors based on probability)
    def check_error(self, received_frame):
        return random.random() > self.error_probability  # Simulate error if random number is less than error probability
    
    # Acknowledgment (ACK) or Negative Acknowledgment (NAK)
    def ack_or_nak(self, sent_frames, window_start):
        ack = []
        for i in range(len(sent_frames)):
            # Assume the receiver is expecting the next frame in sequence
            expected_frame = window_start + i
            if self.receiver(sent_frames[i], expected_frame):
                ack.append(True)
            else:
                ack.append(False)
        return ack
    
    # Main protocol loop (sender and receiver communication)
    def simulate(self):
        window_start = 0
        while window_start < len(self.frames):
            # Sender sends a window of frames
            sent_frames, window_end = self.sender(window_start)
            
            # Receiver acknowledges the frames (simulating noise)
            ack = self.ack_or_nak(sent_frames, window_start)
            
            # For Selective Repeat, only retransmit frames that were not acknowledged
            for i in range(len(ack)):
                if not ack[i]:
                    print(f"Sender: Retransmitting frame {window_start + i + 1}...\n")
            
            # Slide the window based on ACKs
            for i in range(len(ack)):
                if ack[i]:
                    window_start += 1  # Slide the window forward for each acknowledged frame
            
            # If no frames in the window were acknowledged, we don't slide the window
            if all(not a for a in ack):
                time.sleep(1)  # Simulate delay in the network
    
    # To simulate transmission of multiple frames
    def simulate_multiple_frames(self):
        print("Starting Selective Repeat Protocol simulation...\n")
        self.simulate()

# Example usage of the Selective Repeat Protocol with noisy channel simulation
if __name__ == "__main__":
    # Example binary data frames to send (each frame is a list of bits)
    frames = [
        [1, 0, 1, 0, 1],  # Frame 1: 10101
        [0, 1, 1, 0, 0],  # Frame 2: 01100
        [1, 1, 0, 1, 0],  # Frame 3: 11010
        [0, 0, 1, 1, 1],  # Frame 4: 00111
        [1, 0, 1, 1, 0],  # Frame 5: 10110
        [1, 1, 1, 0, 1],  # Frame 6: 11101
    ]
    
    # Create an instance of the Selective Repeat Protocol with window size 3 and 10% error
    protocol = SelectiveRepeatProtocol(frames, window_size=3, error_probability=0.1)
    
    # Simulate the protocol
    protocol.simulate_multiple_frames()
