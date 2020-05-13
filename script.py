import docker, json, time
from datetime import datetime

client = docker.from_env()

def main():
	service = client.services.list( filters= {'name':'exchange_barong_email'})[0]
	print('service found: ' + service.name)

	containers = [ n for n in client.containers.list() if 'barong_email' in n.name ]
	print(containers)
	# 2020-05-12 T 19:11:45 . 973516582Z
	for n in containers:
		print(n.name)
		datetime_str = n.attrs['Created'].split('.')[0]
		datetime_object = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S')
		now = datetime.now()
		time_limit = 20*60 #20 minutes
		diff_seconds = (now-datetime_object).seconds
		print("diff: "+ str(diff_seconds/60.0))
		if diff_seconds >= time_limit:
			print('scaling to 2 so it keeps running: ' + str(service.scale(2)))
			time.sleep(5)
			print("Removing oldest containers and creating new ones: " + n.name)
			s_containers = [ c for c in client.containers.list() if 'barong_email.1.' in c.name ]
			for c in s_containers: c.remove(force=True)
			time.sleep(10)
			service.reload()
			print('scaling service back to 1: ' + str(service.scale(1)))
			return


if __name__ == "__main__":
	while True:
		print("runnning script: " + str(datetime.now()))
		main()
		time.sleep(60)
