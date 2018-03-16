# -*- encoding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "https://www.dominospizza.es"

### load automatization driver
driverpath = "/Users/jialvarez/Dropbox/charlas/BetaBeers/20180316/demo/geckodriver"

profile = webdriver.FirefoxProfile()
profile.set_preference("geo.prompt.testing", False)
profile.set_preference("geo.prompt.testing.allow", False)

### open browser
#driver = webdriver.Chrome(driverpath)
#driver = webdriver.Firefox(driverpath)
driver = webdriver.Firefox(firefox_profile=profile, executable_path=driverpath)

### open url 
driver.get(url)
driver.maximize_window()

### clic order button
button = driver.find_element_by_class_name("red.border")
button.click()
time.sleep(3)

### select city
city = u'CÓRDOBA'
cityselect = driver.find_element_by_xpath("//select[@id='IdProvinciaSeleccionada']/option[text()='" + city + "']")
cityselect.click()
time.sleep(3)

### select street
street = "Calle Secretario Carretero"
streetinput = driver.find_element_by_id("1tags")
streetinput.click()
streetinput.send_keys(street)
time.sleep(3)

streetselect = driver.find_element_by_xpath("//span[@class='autocomplete-highlight-element']")
streetselect.click()

### select number
number = driver.find_element_by_id("Direccion_NumeroPortal")
number.click()
number.send_keys("7")

### click Search store
store = driver.find_element_by_xpath("//button[@class='green fr']")
store.click()
time.sleep(3)

### click At Home
home = driver.find_element_by_xpath("//button[@class='green fr' and @name='domicilio']")
home.click()
time.sleep(8)

### First Pizza!
# hover into div
pizza1Name = "Queso de cabra y espinacas"
pizza1 = driver.find_element_by_xpath("//div[@class='owl-item']//li[@data-name='" + pizza1Name + "']")
hover = ActionChains(driver).move_to_element(pizza1)
hover.perform()

# click Add button
pizza1Btn = driver.find_element_by_xpath(".//button[contains(@onclick, '" + pizza1Name + "')]")
pizza1Btn.click()

pizza1Add = driver.find_element_by_id("add-pizza")
hover = ActionChains(driver).move_to_element(pizza1Add)
hover.perform()
time.sleep(4)
pizza1Add.click()
time.sleep(3)

### Add promotion
# @TO-DO

### Close promotion
promotion = driver.find_element_by_class_name("ico.ico-close-gray")
promotion.click()
time.sleep(3)

### Send order
shoppingCart = driver.find_element_by_class_name("icon.mini-carrito")
shoppingCart.click()
