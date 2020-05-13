import docker, json
from datetime import datetime

client = docker.from_env()
containers = [ n for n in client.containers.list() if 'barong_email' in n.name ]

print(containers)
# 2020-05-12 T 19:11:45 . 973516582Z
for n in containers:
	print(n.name)
	print(n.attrs['Created'])
	datetime_str = n.attrs['Created'].split('.')[0]
	datetime_object = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
	print(datetime_object)
	#n.stop()
	n.remove(force=True)
