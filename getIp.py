import urllib.request
import subprocess
import socket
import re
 
child=subprocess.Popen("ifconfig", shell=True, stdout = subprocess.PIPE)
out=child.communicate();#保存 ipconfig 中的所有信息
 
ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
m=re.findall(ipv6_pattern,str(out));
address=m[1][0]
print(m[0][0])
print(m[1][0])