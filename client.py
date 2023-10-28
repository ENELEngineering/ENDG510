import socket
import time
import Adafruit_DHT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
# connect to the server on local computer
s.connect(('172.20.10.2', port)) #use your laptop IP
while True:
	# read from sensor
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	#prepare data
	data = str(temperature) + " " + str(humidity)
	print (data)
	# send data to the server
	s.send(data.encode())
	# pause for 1 seconds
	time.sleep(0.1)
#close the channel
s.close()
