# -*- encoding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

### get Twitter pass from filename
sshpass_path = "/etc/fbpass"
fo = open(sshpass_path, "r")

username = "neonigmatests"
password = fo.readline().replace("\n","")
 
url = "https://www.twitter.com/login"
tweet = "Hola BetaBeers ODB!"

### load automatization driver
driverpath = "/Users/jialvarez/Dropbox/charlas/BetaBeers/20180316/demo/"

### configure headless options
options = Options()
options.add_argument("--headless")

### open browser
#driver = webdriver.Chrome(driverpath)
driver = webdriver.Firefox(firefox_options=options)

### open url 
driver.get(url)
driver.maximize_window()

### get username and password fields
username_field = driver.find_element_by_class_name("js-username-field")
password_field = driver.find_element_by_class_name("js-password-field")

### type username
username_field.send_keys(username)
time.sleep(1)

### type password
password_field.send_keys(password)
time.sleep(1)

### click login button
driver.find_element_by_class_name("EdgeButtom--medium").click()

### type tweet message
tweetbox = driver.find_element_by_id("tweet-box-home-timeline")
tweetbox.send_keys(tweet)
time.sleep(5)

### click Tweet button
tweetbtn = driver.find_element_by_class_name("tweeting-text")
tweetbtn.click()
