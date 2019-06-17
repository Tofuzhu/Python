import requests
import re

r = requests.get(r"https://movie.douban.com/top250?start=0")
w = open("1.txt", 'w+', encoding="utf-8")
w.write(r.text)
w.write(str(r.json))
w.close()
# 获取本页的电影名称
pattern_Name = re.compile(r"<span class=\"title\">(.*?)</span>")
m = pattern_Name.findall(r.text)
film_Name = m[:]
for i in m:
    if "nbsp" in i:
        film_Name.remove(i)
print(film_Name)
# 获取本页的评分
pattern_Rating = re.compile((r"<span class=\"rating_num\" property=\"v:average\">(.*?)</span>"))
film_Rating = pattern_Rating.findall(r.text)
print(film_Rating)
# 获取观看人数
pattern_People = re.compile((r"<span>(.*?)人评价</span>"))
film_People = pattern_People.findall(r.text)
print(film_People)
# 获取影片短评
pattern_Quote = re.compile((r"<span class=\"inq\">(.*?)</span>"))
film_Quote = pattern_Quote.findall(r.text)
print(film_Quote)