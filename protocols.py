# Protocols: FTP (File Transfer protocol), SMTP (Simple, Mail Transfer Protocol), Telnet andremote login protocol, WWW (World Wide Web), HTTP (Hyper Text Transfer protocol),Uniform Resource Locator, HTML and forms.

import smtplib
import socket
import os
import time
import urllib.parse
from ftplib import FTP
import webbrowser

# Protocols Class: Simulating various network protocols
class Protocols:
    def __init__(self):
        self.server_address = ('localhost', 21)  # FTP default port
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.ftp_server = 'ftp.dlptest.com'  # Public test FTP server

    # Simulate FTP (File Transfer Protocol)
    def ftp_protocol(self):
        print("\nFTP (File Transfer Protocol) Simulation")
        print("Connecting to FTP server...")
        ftp = FTP(self.ftp_server)
        ftp.login()  # Anonymous login
        print(f"Connected to {self.ftp_server}")
        
        # List files on the FTP server
        print("Listing files on the FTP server:")
        ftp.retrlines('LIST')
        
        # Download a file (simulate)
        print("Downloading test file from FTP server...")
        ftp.retrbinary('RETR README', open('README.txt', 'wb').write)
        print("File downloaded as 'README.txt'")
        
        # Upload a file (simulate)
        print("Uploading a new file to FTP server...")
        ftp.storbinary('STOR UPLOAD.txt', open('UPLOAD.txt', 'rb'))
        print("File uploaded successfully.")
        
        ftp.quit()
        time.sleep(1)
    
    # Simulate SMTP (Simple Mail Transfer Protocol) - Sending an Email
    def smtp_protocol(self):
        print("\nSMTP (Simple Mail Transfer Protocol) Simulation")
        from_email = 'your_email@gmail.com'  # Replace with your email
        to_email = 'receiver_email@example.com'  # Replace with receiver email
        subject = 'Test Email'
        body = 'This is a test email sent using SMTP protocol.'
        
        print(f"Sending email from {from_email} to {to_email}...")
        
        # Set up SMTP client
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()  # Start TLS for security
        server.login(from_email, 'your_password')  # Login (replace with actual password)
        
        message = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(from_email, to_email, message)
        server.quit()
        
        print("Email sent successfully.")
        time.sleep(1)
    
    # Simulate Telnet for remote login (simple mock of the process)
    def telnet_protocol(self):
        print("\nTelnet (Remote Login) Simulation")
        telnet_host = 'localhost'  # Simulating local machine for demo
        telnet_port = 23  # Default Telnet port
        
        print(f"Connecting to {telnet_host} on port {telnet_port}...")
        # Create a socket connection (simulating Telnet behavior)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((telnet_host, telnet_port))
            s.sendall(b'Username: demo_user\n')  # Simulating login prompt
            s.sendall(b'Password: demo_pass\n')  # Simulating password prompt
            s.sendall(b'Command: ls\n')  # Simulating command execution (e.g., 'ls')
            data = s.recv(1024)
            print(f"Received: {data.decode()}")
        time.sleep(1)

    # Simulate HTTP Protocol and WWW (World Wide Web)
    def http_protocol(self):
        print("\nHTTP (Hypertext Transfer Protocol) Simulation")
        url = "http://www.example.com"  # Simulate visiting a website
        print(f"Accessing URL: {url}")
        
        # Parse the URL
        parsed_url = urllib.parse.urlparse(url)
        print(f"Parsed URL: {parsed_url}")
        
        # Simulating an HTTP GET request using Python's built-in webbrowser library
        webbrowser.open(url)
        print(f"Web browser opened to {url}")
        time.sleep(1)
    
    # Simulate Uniform Resource Locator (URL) and HTML Basics
    def url_html_protocol(self):
        print("\nURL and HTML Basics Simulation")
        url = "http://www.example.com"
        html_content = """
        <html>
        <head><title>Example Page</title></head>
        <body>
        <h1>Welcome to Example Page</h1>
        <p>This is a sample HTML page.</p>
        <form action="/submit" method="POST">
            Name: <input type="text" name="username"><br>
            <input type="submit" value="Submit">
        </form>
        </body>
        </html>
        """
        print(f"URL: {url}")
        print("HTML Content: ")
        print(html_content)
        time.sleep(1)

# Main Simulation Class for Protocols
class ProtocolsSimulation:
    def __init__(self):
        self.protocols = Protocols()

    def simulate(self):
        # Simulate FTP, SMTP, Telnet, HTTP, URL, HTML protocols
        self.protocols.ftp_protocol()
        self.protocols.smtp_protocol()
        self.protocols.telnet_protocol()
        self.protocols.http_protocol()
        self.protocols.url_html_protocol()

# Main function to run the simulation
def main():
    print("Protocols Simulation (FTP, SMTP, Telnet, HTTP, URL, HTML)\n")
    
    # Run the simulation
    simulation = ProtocolsSimulation()
    simulation.simulate()

# Execute the simulation
if __name__ == "__main__":
    main()
