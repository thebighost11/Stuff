import socket
import threading

from queue import Queue

target="choose" #target ip
queue=Queue()
open_ports=[]


def scanport(port)
  try:
  so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  so.connect((target,port))
    return True
  except:
    return False
def fillqueue(port_list):
    for port in port_list:
    queue.put(port)
def adder():
   while not queue.empty():
        port=queue.get()
        if scanport(port):
            print("port {} is oen".format(port))
            open_ports.append(port)            
port_list = range(1, 1024)
fillqueue(port_list)


thread_list=[]
 for t in range(10):
  thread = threading.thread(target=adder)
  thread_list.append(thread)
  
 
for thread in thread_list:
 thread.start()

for thread in thread_list:
 thread.join()

print ("open ports are : ',open_ports) 