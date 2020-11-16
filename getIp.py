import urllib.request
import subprocess
import socket
import re
import time
 
child=subprocess.Popen("ifconfig", shell=True, stdout = subprocess.PIPE)
out=child.communicate()
ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
m=re.findall(ipv6_pattern,str(out));
address=m[1][0]
t=time.time()
print(t,m[0][0])
print(t,m[1][0])
