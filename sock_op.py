from socket import socket as make_socket
from net_util import get_ips,get_ports
from sys import stderr as sys_stderr,exit as sys_exit
from utils import is_sigint_met

def __ping_sock(sock,host,port=80,time_out=0.5,port_alias=None,host_alias=None,verbose=False):
	"""
		connect a socket,  try-catch it and close it at the end
	"""
	result=False
	if host_alias==None: # for printing
		host_alias=sock.getpeername()
	try:
		sock.settimeout(time_out)
		sock.connect((host,port))
		result=True
		if verbose:
			print("[x] {} {} {}".format(port,port_alias,host_alias))
	except:
		if verbose:
			print("[ ] {} {} {}".format(port_alias,port,host_alias))
		pass
	sock.close()
	return result
			
def ping(ip='localhost',port=80,host=None,alias=None,verbose=False):
	"""
		Ping a server (ip/host) and report it!
		if host is set, ip is ignored and instead the ip location
		of the host is pinged
	"""

	# setting host
	host_alias=host # remember for verbosity
	if not host is None:
		host=get_ips(host)[0] # get the first ip that comes to mind
	else:
		host=ip

	# actual actual - this is the whole point of this program!
	with make_socket() as s:
		# s.setblocking(True)
		if is_sigint_met(): # for some resaon sockets won't let sigint in normal way to work
			# print('[SIGINT]')
			sys_exit(0)
		return __ping_sock(s,host,port,time_out=.3,port_alias=alias,host_alias=host_alias,verbose=verbose)

def ping_all(host,type="host",ports=None,verbose=False):
	"""
		ping all standard ports on host, and print it out
		ports is a list of dicts with:
			key(int) : { protocol:str , title:str  }
		example:
			[
				"2049":{"protocol":"tcp","title":"nfs"},
				"2049":{"protocol":"udp","title":"nfs"},
			]
	"""

	res=dict()

	# setting default values
	if ports is None:
		ports=get_ports()

	# getting ip, to prevent dns queries in ping()
	if type == "host":
		try:
			res['host']=host
			ip=get_ips(host)[0]
			res['ip']=ip
		except:
			# print("< {} > : NOT_RESOLVED".format(host))
			res['ip']='NOT_FOUND'
			return
	
	# prompting
	# print("< {} >".format(host))
	res['ports']=list()
	for i,j in ports.items():
		if ping(ip=ip,host=host,port=int(i),alias=j['title'],verbose=verbose):
			res['ports'].append(int(i))
	return res
