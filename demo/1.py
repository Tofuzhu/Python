import requests
import re

r = requests.get(r"https://movie.douban.com/top250?start=0")
w = open("1.txt",'w+',encoding="utf-8")
w.write(r.text)
w2 = open("2.txt",'w+',encoding="utf-8")
w.write(str(r.json))
w.close()
w2.close()

pattern = re.compile(r"<span class=\"title\">(.*?)</span>")
m = pattern.findall(r.text)
print(m)
n = m[:]
for i in m:
    if "nbsp" in i:
        n.remove(i)
m = n
# m = (i for i in m if "nbsp" not in i)
print(n,len(n))