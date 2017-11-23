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
            return(True, print(ip))
        except ValueError:
            # If ValueError exception is raised, value for ip is invalid
            return(False, 'Address {} is invalid!'.format(ip_address))

    def check_port(self, port):
        pass
        
    def create_socket(self):
        pass
        
    def connect(self):
        pass
        
    def send(self):
        pass
        
    def receive(self):
        pass
        
    def disconnect(self):
        pass
