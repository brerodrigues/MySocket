#!/usr/bin/env python3

import socket
import ipaddress

class SimpleSocket(object):

    def __init__(self, ip_address, port):
        self.ip_address = self.check_ip(ip_address)
        self.port = self.check_port(port)
        self.socket = self.create_socket()
        self.connection_status = False
        
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
        pass
        
    def send(self):
        pass
        
    def receive(self):
        pass
        
    def disconnect(self):
        pass
