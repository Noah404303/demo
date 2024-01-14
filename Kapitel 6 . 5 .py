import time 
import sys
print("Benutzername: ", end="")
user = sys.stdin.readline()
user = user.strip()
for n in range(0, 10):
    zeit = time.asctime(time.localtime())
    print("[%s] %s> " % ( zeit, user), end="")
    nachricht = sys.stdin.readline()
    print("debug: nachricht: %s" % nachricht)
          
