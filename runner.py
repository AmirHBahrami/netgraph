from sock_op import ping_all
from utils import join_worker_threads

import constants
import threading
import datetime

def __init_profile():
	dt=datetime.datetime.now()
	res=dict()
	res['scan']=list()
	res['unix_time']=str(dt.timestamp())
	res['datetime']=dt.strftime('%Y-%M-%d %H:%m')
	return res

def __run_ping_all(hosts,ports,buffer,tno,verbose=False):
	"""buffer is a normal list()"""
	for h in hosts:
		buffer.append(ping_all(host=h,ports=ports,verbose=verbose))

def __split_hosts(hosts):
	"""
		since the program decides to distribute workload, a list of
		hosts are split into different segments, and then each segment
		is done in a thread of it's own.
		this function does the splitting part!
	"""
	res=list()
	temp=list()
	for i in range(len(hosts)):
		temp.append(hosts.pop())
		if len(temp) - constants.__HOSTS_PER_THREAD >=0:
			res.append(temp)
			temp=list() # re-assign

	# remanants
	if len(temp) >0:
		res.append(temp)
	return res

# TODO make sure {hosts,ports}+ are given 
# and each set of hosts get their own ports
# to be scanned
def distribute_workload(hosts,ports,verbose=False):
	"""
		distribute workload of ping_all across multiple
		threads and return reduced results as an object:
		{
			scans:[
				{
					host:<str>,
					ip:<str>,
					port:<str>
				}+
			],
			unix_time:<long>,
			datetime:<str>
		}
	"""
	
	# initialize things...
	buffer=__init_profile() # save results here
	threads_limit=constants.__HOSTS_PER_THREAD % len(hosts)
	hosts=__split_hosts(hosts)
	threads_pool=list()

	# manage threadings and joining them and all
	tno=0
	for h_set in hosts:
		
		# create and start threads
		t=threading.Thread(target=(__run_ping_all),args=(h_set,ports,buffer['scan'],tno,verbose))
		t.name='t_{}'.format(tno)
		threads_pool.append(t)
		threads_pool[tno].start()
		tno+=1

		# limit reached for active threads, 
		# wait until all of them are free (yeah, I know!)
		# TODO this makes a HUGE overhaed ffs!
		if tno == threads_limit:
			join_worker_threads(threads_pool)
			threads_pool.clear()
			tno=0;
	
	join_worker_threads(threads_pool)
	return buffer
