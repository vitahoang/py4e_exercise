import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_382616.xml'
uh = urllib.request.urlopen(url, context=ctx).read()
data = uh.decode()
tree = ET.fromstring(data)
l_counts = tree.findall('.//count')
x_sum = 0
for count in l_counts:
	tpx = int(count.text)
	x_sum = x_sum + tpx
print(x_sum)
