import sys
import socket
import subprocess
from datetime import datetime

remoteServer = input("Enter a remote host to scan: ")
scan_rng = input("Enter a port range to scan: ")
remoteHostIP = socket.gethostbyname(remoteServer)

print("-" * 60)
print("Please wait, scanning remote host", remoteHostIP)
print("-" * 60)

t1 = datetime.now()

try:
    for port in range(1, int(scan_rng)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteHostIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Exiting... ")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved... ")
    sys.exit()

except socket.error:
    print("Couldn't connect to server... ")
    sys.exit()

t2 = datetime.now()

total = t2 - t1

print("Scanning Completed in: ", total)