import socket
import pandas as pd
df = pd.DataFrame(columns=['Temp', 'Humd', 'Label'])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")
host = '172.20.10.2'
port = 12345
s.bind((host, port))
print ("socket binded to %s" %(port))
s.listen(5)
print (f"socket is listening on {host}:{port}")
c, addr = s.accept()
print ('Got connection from', addr)

i = 1001
while i>=0:
    client = c.recv(1024)
    data = client.decode()
    temp = data.split(" ")[0]
    hum = data.split(" ")[1]
    new_data = {'Temp': temp, 'Humd': hum, 'Label': 1}
    df = df._append(new_data, ignore_index=True)
    print(data)
    i = i - 1
c.close()
df.to_csv('data_1.csv', index=False)