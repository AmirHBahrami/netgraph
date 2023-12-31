import socket
from utils import json_file_to_object

def get_ports(test=False):
	"""
		get all ports with their corresponding protocols names 
		(like icmp, http, etc) and expected transport layer 
		protocol (tcp/udp) in a dictionary (check ports.json)
	"""
	if test:
		return json_file_to_object("./data/test.json")
	else:
		return json_file_to_object("./data/ports.json")

def get_ips(hostname):
	"""
		Get ipv4's of a hostname
	"""
	addr=list()
	results=socket.getaddrinfo(hostname, None, socket.AF_UNSPEC)
	for r in results:
		family,_,_,_,sockaddr=r
		addr.append(sockaddr[0])
	return addr
