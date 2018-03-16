# -*- encoding: utf-8 -*-
import time
from selenium import webdriver

### get Twitter pass from filename
sshpass_path = "/etc/fbpass"
fo = open(sshpass_path, "r")

username = "neonigmatests"
password = fo.readline().replace("\n","")
 
url = "https://www.twitter.com/login"
tweet = "Hola BetaBeers ODB!"

### load automatization driver
driverpath = "/Users/jialvarez/Dropbox/charlas/BetaBeers/20180316/demo/"

### open browser
#driver = webdriver.Chrome(driverpath)
driver = webdriver.Firefox(driverpath)

### open url 
driver.get(url)
driver.maximize_window()

