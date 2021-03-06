#!/usr/bin/env python3

import socket
import ipaddress

class SimpleSocket(object):

    def __init__(self, ip_address, port):
        self.ip_address = self.check_ip(ip_address)
        self.port = self.check_port(port)
        self.socket = self.create_socket()
        self.connection_status = False
        self.connection_message = None
        self.received_data = None
        
    def check_ip(self, ip_address):
        try:
            # Trying to create a ip_address object
            ip = ipaddress.ip_address(ip_address)
            # Printing de ip_address object to get the ip value instead of the object
            return(ip.__str__())
        except ValueError:
            # If ValueError exception is raised, value for ip is invalid
            return(False)

    def check_port(self, port):
        # Checks if is a int and a valid port number
        if (type(port) == int) and (port > 0 and port < 65536):
            return(port)
        else:
            return(False)
        
    def create_socket(self):
        # Checks if everything is right with ip address and port
        if (self.ip_address == False) or (self.port == False):
            return(False)
        else:
            # Creating a TCP Socket
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return(my_socket)
        
    def connect(self):
        # If a socket don't exist
        if self.socket == False:
            return(False)
        else:
            try:
                self.socket.connect((self.ip_address, self.port))
                self.connection_status = True
                self.connection_message = "Connected"
                return(True)
            # If connection is refused
            except ConnectionRefusedError:
                self.connection_message = "Connection Refused"
                return(False)
            # Other exception happened, so fuck it
            self.connection_message = "Unknow error in connection"
            return(False)
        
    def send(self, data):
        # Check if it is connected
        if self.connection_status == False:
            return(False)
        else:
            # The method sendall will return 'None' if the data was sent
            if self.socket.send(data.encode('ascii')) == None:
                return(True)
            else:
                return(False)
                
    def receive(self):
        # Check if it is connected
        if self.connection_status == False:
            return(False)
        else:
            self.received_data = self.socket.recv(1024)
            return(True)
        
    def disconnect(self):
        # Check if it is connected
        if self.connection_status == False:
            return(False)
        else:
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
            self.connection_status = False
