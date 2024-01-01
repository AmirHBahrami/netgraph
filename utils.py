from json import load as json_load
from sys import exit as sys_exit, stderr as sys_stderr

global sigint_caught
sigint_caught=False

def json_file_to_object(path):
	"""read a json file from path and convert it to an object"""
	obj=None
	with open(path) as jf:
		obj=json_load(jf)
	return obj

def is_sigint_met():
	"""use this function in order to check for interrupts"""
	global sigint_caught
	return sigint_caught == True

def handle_sigint(sig,frame):
	"""do not call this function, it's only assigned as a handler for sigint (hence the name)"""
	global sigint_caught
	sigint_caught=True

def join_worker_threads(threads):
	# TODO make this based! (right now it's just accessing
	# threads based on the index in the list. make it access
	# them in a pool. maybe re-do the whole program
	"""
		WARNING: ONLY use when all the workers have the same
		priority and none of them is inherently
	"""
	for t in threads:
		# print(t.name)
		t.join()


# flag handling across different modules - not used yet!
# TODO make a flag system for global access (instead of 
# passing down arguments)
"""
def set_flag(flag,val=True):
	flags[flag]=val

def get_flag(flag):
	
	if flag not in flags:
		return None

	return flags[flag]
"""
