# Simulate Cyclic Redundancy Check (CRC) error detection algorithm for noisy channel

import random

# CRC class: Simulate Cyclic Redundancy Check (CRC) error detection
class CRC:
    def __init__(self, polynomial):
        self.polynomial = polynomial  # The generator polynomial (in binary)
        self.polynomial_degree = len(polynomial) - 1  # Degree of the polynomial

    # Perform binary division (XOR operation for CRC)
    def divide(self, data, polynomial):
        # Append 0s to the data (remainder size)
        data = data + [0] * (len(polynomial) - 1)
        
        # Perform division using XOR (simulate the CRC algorithm)
        for i in range(len(data) - self.polynomial_degree):
            if data[i] == 1:  # Only perform XOR if the bit is 1
                for j in range(len(polynomial)):
                    data[i + j] ^= polynomial[j]
        
        return data[-(self.polynomial_degree):]  # Return the remainder

    # Encode data by calculating the CRC and appending it to the original data
    def encode(self, data):
        remainder = self.divide(data, self.polynomial)
        encoded_data = data + remainder  # Append CRC to data
        return encoded_data

    # Decode and check the data to detect errors
    def decode(self, encoded_data):
        remainder = self.divide(encoded_data, self.polynomial)
        if any(remainder):  # If remainder is non-zero, error detected
            return False  # Error detected
        return True  # No error detected

    # Simulate noise by randomly flipping bits
    def simulate_noise(self, data, error_probability=0.1):
        noisy_data = data[:]
        for i in range(len(data)):
            if random.random() < error_probability:
                noisy_data[i] ^= 1  # Flip the bit (simulate error)
        return noisy_data

# Main function to simulate CRC
def main():
    print("CRC (Cyclic Redundancy Check) Simulation\n")

    # Define the generator polynomial (example: x^3 + x + 1)
    # Represented as [1, 0, 1, 1] for x^3 + x + 1
    generator_polynomial = [1, 0, 1, 1]
    
    # Create CRC object
    crc = CRC(generator_polynomial)
    
    # Simulated data to send (binary data)
    data = [1, 0, 1, 1, 0]  # Example data: 10110

    print("Original Data: ", data)

    # Step 1: Encode the data by appending CRC
    encoded_data = crc.encode(data)
    print("Encoded Data (with CRC): ", encoded_data)
    
    # Step 2: Simulate noisy channel (random errors)
    noisy_data = crc.simulate_noise(encoded_data, error_probability=0.2)
    print("Noisy Data (with potential errors): ", noisy_data)

    # Step 3: Decode the noisy data and check for errors
    is_valid = crc.decode(noisy_data)
    
    if is_valid:
        print("Receiver: No error detected!")
    else:
        print("Receiver: Error detected in the data!")

# Run the CRC simulation
if __name__ == "__main__":
    main()
