import urllib.request
import subprocess
import socket
import re
import time
import json

 
#child=subprocess.Popen("ifconfig", shell=True, stdout = subprocess.PIPE)
#out=child.communicate()
#ipv6_pattern='(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4})'
#m=re.findall(ipv6_pattern,str(out));
#address=m[1][0]
#t=time.strftime('%Y/%m/%d %H:%M:%S')
#print(t,m[0][0])
#print(t,m[1][0])


import urllib.request
import json
response = urllib.request.urlopen('http://[2001:470:1:18::115]/ip/?callback=c')
html = response.read()
s = str(html[2:-2],'utf-8')
j = json.loads(s)
t=time.strftime('%Y/%m/%d %H:%M:%S')
p = j['ip'].split(',')

#print(t,j['ip'])

#print(t,'http://[%s]:8081'%p[0])

jj={}
jj['t']=t
jj['a']=j['ip']
jj['b']='http://[%s]:8081'%p[0]

print(json.dumps(jj))
