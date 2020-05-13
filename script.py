import docker, json, time
from datetime import datetime

client = docker.from_env()

def main():
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
			n.remove(force=True)
			print("Removing container: " + n.name)
			break


if __name__ == "__main__":
	while True:
		print("runnning script: " + str(datetime.now()))
		main()
		time.sleep(60)
