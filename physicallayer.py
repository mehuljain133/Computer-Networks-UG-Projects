# Physical Layer: Analog signal, digital signal, digital modulation techniques (ASK, PSK, QAM),encoding techniques, maximum data rate of a channel, transmission media (guided transmissionmedia, wireless transmission, satellite communication), multiplexing (frequency divisionmultiplexing, time division multiplexing, wavelength division multiplexing

import math
import random
import time

# Define the physical layer components
class PhysicalLayer:
    def __init__(self):
        self.channel_bandwidth = 1000  # in Hz (Example: 1 KHz bandwidth)
        self.snr = 10  # Signal to Noise Ratio (in dB)
    
    # Modulation Techniques
    def ask_modulation(self, data):
        print("\nASK (Amplitude Shift Keying) Modulation:")
        modulated_signal = ''.join([str(int(bit) * random.choice([1, -1])) for bit in data])
        print(f"Original Data: {data}")
        print(f"Modulated Signal: {modulated_signal}")
    
    def psk_modulation(self, data):
        print("\nPSK (Phase Shift Keying) Modulation:")
        modulated_signal = ''.join([random.choice([1, -1]) if bit == '1' else random.choice([1, -1]) for bit in data])
        print(f"Original Data: {data}")
        print(f"Modulated Signal: {modulated_signal}")
    
    def qam_modulation(self, data):
        print("\nQAM (Quadrature Amplitude Modulation) Modulation:")
        modulated_signal = ''.join([str(random.choice([1, -1]) * random.choice([1, -1])) for _ in data])
        print(f"Original Data: {data}")
        print(f"Modulated Signal: {modulated_signal}")
    
    # Encoding Techniques
    def encoding_techniques(self, data):
        print("\nEncoding Techniques:")
        print(f"Original Data: {data}")
        # Here, let's use Manchester encoding (simple simulation)
        encoded_signal = ''.join(['10' if bit == '1' else '01' for bit in data])
        print(f"Manchester Encoded Signal: {encoded_signal}")
    
    # Maximum Data Rate of a Channel (Shannon's Formula)
    def max_data_rate(self):
        print("\nMaximum Data Rate (Shannon's Formula):")
        # Shannon's capacity formula: C = B * log2(1 + S/N)
        bandwidth = self.channel_bandwidth
        snr = 10 ** (self.snr / 10)
        max_rate = bandwidth * math.log2(1 + snr)
        print(f"Channel Bandwidth: {bandwidth} Hz, SNR: {self.snr} dB")
        print(f"Maximum Data Rate: {max_rate:.2f} bps")
    
    # Transmission Media
    def transmission_media(self):
        print("\nTransmission Media Options:")
        media_options = [
            "Guided Transmission Media (Fiber Optic, Copper Cables)",
            "Wireless Transmission (Radio waves, Microwaves, Infrared)",
            "Satellite Communication (Geostationary Satellites)"
        ]
        for media in media_options:
            print(f"- {media}")
    
    # Multiplexing Techniques
    def multiplexing(self):
        print("\nMultiplexing Techniques:")
        
        def fdm():
            print("Frequency Division Multiplexing (FDM): Different frequencies are allocated to different signals.")
        
        def tdm():
            print("Time Division Multiplexing (TDM): Different time slots are allocated to different signals.")
        
        def wdm():
            print("Wavelength Division Multiplexing (WDM): Different wavelengths of light are used to transmit multiple signals.")
        
        fdm()
        tdm()
        wdm()


# Simulation of Physical Layer
class PhysicalLayerSimulation:
    def __init__(self):
        self.physical_layer = PhysicalLayer()
    
    def simulate(self):
        # Sample data to simulate
        data = ''.join([random.choice(['0', '1']) for _ in range(10)])
        
        # Simulate ASK, PSK, and QAM modulation techniques
        self.physical_layer.ask_modulation(data)
        time.sleep(1)
        self.physical_layer.psk_modulation(data)
        time.sleep(1)
        self.physical_layer.qam_modulation(data)
        
        # Simulate Encoding Techniques
        self.physical_layer.encoding_techniques(data)
        time.sleep(1)
        
        # Calculate maximum data rate of the channel
        self.physical_layer.max_data_rate()
        time.sleep(1)
        
        # Display transmission media options
        self.physical_layer.transmission_media()
        time.sleep(1)
        
        # Display multiplexing techniques
        self.physical_layer.multiplexing()


# Main function to run simulation
def main():
    print("Physical Layer Simulation: Modulation, Encoding, and Multiplexing\n")
    
    # Run the simulation for Physical Layer components
    simulation = PhysicalLayerSimulation()
    simulation.simulate()


# Run the simulation
if __name__ == "__main__":
    main()
