from utils import json_file_to_object

settings=json_file_to_object("./settings.json")

__MAX_THREADS=settings['__MAX_THREADS']
__MAX_HOSTS=settings['__MAX_HOSTS']
__HOSTS_PER_THREAD=settings['__HOSTS_PER_THREAD']
