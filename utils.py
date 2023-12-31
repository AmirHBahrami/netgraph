from json import load as json_load
from sys import exit as sys_exit, stderr as sys_stderr

global sigint_caught
sigint_caught=False

# global flags=dict()

def json_file_to_object(path):

	"""
		read a json file from path and convert it to an object
	"""

	obj=None
	with open(path) as jf:
		obj=json_load(jf)
	return obj

def is_sigint_met():
	global sigint_caught
	return sigint_caught == True

def handle_sigint(sig,frame):
	global sigint_caught
	sigint_caught=True

# flag handling across different modules - not used yet!
"""
def set_flag(flag,val=True):
	flags[flag]=val

def get_flag(flag):
	
	if flag not in flags:
		return None

	return flags[flag]
"""
