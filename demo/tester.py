import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

driver = webdriver.Chrome()

# #get cookies
# driver.get('https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20')
# driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("zzy19860808@gmail.com")
# driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys("68mbH4OL")
# driver.find_element_by_xpath('//*[@id="ap_password"]').submit()
# cookie = driver.get_cookies()
# #save to txt
# w = open("imdb_cookies.txt","w+",encoding="utf-8")
# w.write(json.dumps(cookie))
# w.close()

driver.get('https://www.imdb.com/title/tt3741700/')
w1 = open('imdb_cookies.txt')
cookie = w1.read()
cookie =json.loads(cookie)
for c in cookie:
    driver.add_cookie(c)
driver.refresh()
# inputtoolbar = driver.find_element_by_xpath('//*[@id="navbar-query"]')
# inputtoolbar.send_keys("batman")
# inputtoolbar.submit()


# w = open("1.txt", 'w+', encoding="utf-8")
# w.write(driver.page_source)
# w.close()


ratings_button = driver.find_element_by_xpath('//*[@id="star-rating-widget"]/div/button/span[1]')
stars = driver.find_element_by_class_name('star-rating-stars').find_elements_by_tag_name('a')
star_index = 7
builder = ActionChains(driver)
builder.move_to_element(ratings_button).click(ratings_button).move_to_element(stars[star_index]).click(stars[star_index]).perform()

