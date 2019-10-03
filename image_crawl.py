from bs4 import *
import requests as rq
import os
import ssl

# Ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


r1 = rq.get("https://www.pexels.com/@hiteshchoudhary")
soup1 = BeautifulSoup(r1.text,"html.parser")


links = []
#https://images.pexels.com/photos/
# 2756843/pexels-photo-2756843.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500
x = soup1.select('img[src^="https://images.pexels.com/photos"]')


for img in x:
    links.append(img['src'])

for link in links:
    print(link)
