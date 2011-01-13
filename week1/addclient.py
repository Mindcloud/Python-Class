import socket

#host = 'block115382-xkb.blueboxgrid.com'
host = 'localhost'

port = 50000 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect((host,port))
s.send("1, 2")
data = s.recv(size)
print 'Received:', data
s.close()

