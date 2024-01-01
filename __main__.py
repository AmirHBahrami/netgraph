from sys import argv, exit as sys_exit
from sock_op import ping,ping_all
from utils import handle_sigint
from json import dumps as json_dumps
from net_util import get_ports
from runner import distribute_workload

import signal as sig
import argparse

p=argparse.ArgumentParser(
	prog="netgraph",
	description="from terminal: python3 . (<ip/host>)+ [-v] [-f csv/json/graph]",
	epilog="\nexample:\tpython3 . irnik.ir -f json\n\t\tpython3 . 4.4.4.4 -v"
)

p.add_argument(
	"hosts",
	nargs='+',
	help='host/ip or a list of them'
)

p.add_argument(
	'-v' ,
	default=False,
	help='write closed ports as well as open ports',
	action=argparse.BooleanOptionalAction
)

p.add_argument(
	'-f',
	choices=['json','csv'],
	default='json',
	help='graph(default)/json/csv '
)

p.add_argument(
	"-o",
	nargs='?',
	help='path to save the output to (default= LOG_PATH in settings.json)'
)

p.add_argument(
	"-dl",
	default=False,
	help="disable logging the output (beside writing to stdout) check settings.json for LOG_PATH",
	action=argparse.BooleanOptionalAction
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

# actual functionality
results=distribute_workload(hosts=args.hosts,ports=ports,verbose=args.verbose)
print(json_dumps(results,indent=2))
#"""
