import urllib.request, urllib.parse, urllib.error
import json
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_382617.json"
print("Enter location:", url)
uh = urllib.request.urlopen(url, context=ctx).read()
print("Retrieving", url)
dc = uh.decode()
print("Retrieved", len(dc), "characters")
data = json.loads(dc)
x_sum = 0
for comment in data["comments"]:
	x_sum = comment["count"] + x_sum
print(x_sum)
