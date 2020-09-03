# Sender.py
import time, socket, sys

def decimalToBinary(n):  
    return n.replace("0b", "")

def binarycode(s):
    a_byte_array = bytearray(s, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(decimalToBinary(binary_representation))

    #print(byte_list)
    a=""
    for i in byte_list:
        a=a+i
    return a

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))
           
s.listen(1)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    conn.send(message.encode())
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    message=binarycode(message)
    f=str(len(message))
    conn.send(f.encode())
   
    i=0
    j=0
    j=int(input("Enter the window size -> "))
    
   
    b=""
   
    j=j-1
    f=int(f)
    k=j
    while i!=f:
        while(i!=(f-j)):
            conn.send(message[i].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k+1)+" Now sending the next packet")
                i=i+1
                k=k+1
                time.sleep(1)
            else:
                time.sleep(1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k+1)+" Now Resending the same packet")
                time.sleep(1)
        while(i!=f):
            
            conn.send(message[i].encode())
            b=conn.recv(1024)
            b=b.decode()
            print(b)
            if(b!="ACK Lost"):
                time.sleep(1)
                print("Acknowledgement Received! The sliding window is in the range "+(str(i+1))+" to "+str(k)+" Now sending the next packet")
                i=i+1
                time.sleep(1)
            else:
                time.sleep(1)
                print("Acknowledgement of the data bit is LOST! The sliding window remains in the range "+(str(i+1))+" to "+str(k)+" Now Resending the same packet")
                time.sleep(1)
            
     
