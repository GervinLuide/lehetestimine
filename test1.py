from selenium import webdriver
from selenium.webdriver import ActionChains
import time

# Looge uus Chrome brauseri sessioon
driver = webdriver.Chrome()

# Avage veebileht
driver.get("https://the-internet.herokuapp.com/")

# Klõpsake "Context Menu" lingil XPath-i abil
context_menu_link = driver.find_element("xpath", "//a[contains(text(), 'Context Menu')]")
context_menu_link.click()

# Leia lehe element, millele soovite teha parema hiireklõpsu
context_menu_area = driver.find_element("id", "hot-spot")

# Looge ActionChains objekt parema hiireklõpsu tegemiseks
action_chains = ActionChains(driver)
action_chains.context_click(context_menu_area).perform()

# Oodake mõni hetk, et tulemusi näha
time.sleep(2)

# Sulgege brauser pärast testimist
driver.quit()