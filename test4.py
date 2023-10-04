from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select  # Importige Select klass

# Looge uus Chrome brauseri sessioon
driver = webdriver.Chrome()



driver.get("http://the-internet.herokuapp.com/inputs")

# Leidke sisestusväli, millel on tüüp "number"
number_input = driver.find_element("css selector", "input[type='number']")

# Sisestage number (nt 123) sisestusväljale
number_input.send_keys("123")
# Väljastage sisestatud number
entered_number = number_input.get_attribute("value")
print(f"Sisestatud number: {entered_number}")

# Oodake mõni hetk, et tulemusi näha
time.sleep(2)

# Sulgege brauser pärast testimist
driver.quit()