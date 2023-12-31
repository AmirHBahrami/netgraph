from sys import argv, exit as sys_exit
from sock_op import ping,ping_all
from utils import handle_sigint
from json import dumps as json_dumps
from net_util import get_ports

import signal as sig
import datetime
import argparse

p=argparse.ArgumentParser(
	prog="scandude",
	description="usage: python3 . (<ip/host>)+ [-v] [-f csv/json/graph]",
	epilog="\nexample:\tpython3 . irnik.ir -e json\n\t\tpython3 . 4.4.4.4 -v"
)

p.add_argument(
	"hosts",
	nargs='+',
	help='host/ip or a list of them'
)

p.add_argument(
	'-v','--verbose',
	default=False,
	help='write closed ports as well as open ports',
	action=argparse.BooleanOptionalAction
)

p.add_argument(
	'-f','--format',
	choices=['graph','json','csv'],
	default='graph',
	help='graph(default)/json/csv '
)

args=p.parse_args()

# uncomment for production
# TODO handle this fucker: -v -e some_format (maybe csv?)
# TODO make sure the output is convertable to some garph-thing
# TODO multi-threading for fuck_up

#"""
# test=False for production
ports=get_ports(test=True)

# setting sigint handler
sig.signal(sig.SIGINT,handle_sigint)

# getting port (optional)
dt=datetime.datetime.now()
res=dict()
res['scan']=list()
res['unix_time']=dt.timestamp()
res['datetime']=dt.strftime('%Y-%M-%d %H:%m')
for host in args.hosts:
	# TODO use regex to check if it's an ipv4, ipv6 or a hostname
	res['scan'].append(ping_all(host,ports=ports,verbose=args.verbose))
print(json_dumps(res,indent=2))
#"""
