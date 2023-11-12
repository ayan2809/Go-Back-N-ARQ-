# Receiver.py
import time, socket, sys
import random

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nYou will receie messages from", s_name)

while True:

    try:
        m = s.recv(1024)
    except:
        break
    m=m.decode()
    try:
        k = s.recv(1024)
    except:
        break
    k=k.decode()
    try:
        k = int(k)
    except:
        print('The sender', s_name, 'has left the chat room. Terminating the program...')
    i=0
    a=""
    b=""
    f=random.randint(0,1)
    message=""
    while i!=k:
       
       
       f=random.randint(0,1)
       if(f==0):
          b="ACK Lost"
          try: 
              message = s.recv(1024)
          except:
              break
          message = message.decode()
          s.send(b.encode())
         
       elif(f==1):
          b="ACK "+str(i)
          try:
              message = s.recv(1024)
          except:
              break
          message = message.decode()
          
          s.send(b.encode())
          a=a+message
          i=i+1
          
       
    
    if(m != "[e]"):
        print("The message received is :", m)
   
