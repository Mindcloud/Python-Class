import socket
import time

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

while True:
	client, address = s.accept()
	data = client.recv(size)

	print data
	nums = data.split(",")
	total = int(nums[0]) + int(nums[1])
	if data:
		client.send(str(total))

	client.close()

