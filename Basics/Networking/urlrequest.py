from urllib.request import *
from urllib.error import *

try:
 urlrequest = urlopen("https://www.python.org/")
 content = urlrequest.read()
except HTTPError:
    print("can't open website")
    exit()


f = open("pythonorg.html","wb")
f.write(content)
f.close()

urlretrieve("https://www.python.org/static/img/python-logo@2x.png","python.png")
