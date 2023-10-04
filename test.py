from selenium import webdriver
import time

# Looge uus Chrome brauseri sessioon
driver = webdriver.Chrome()

# Avage veebileht
driver.get("https://the-internet.herokuapp.com/")

# Klõpsake "Checkboxes" lingil XPath-i abil
checkbox_link = driver.find_element("xpath", "//a[contains(text(), 'Checkboxes')]")
checkbox_link.click()

# Leia kõik checkboxid vormist
checkbox_form = driver.find_element("id", "checkboxes")
checkboxes = checkbox_form.find_elements("tag name", "input")

# Kontrolli esimest checkboxi ja eemalda märkeruut teiselt
if checkboxes[0].is_selected():
    print(f"Checkbox 1 on juba valitud.")
else:
    checkboxes[0].click()
    print(f"Checkbox 1 on nüüd valitud.")

if checkboxes[1].is_selected():
    checkboxes[1].click()
    print(f"Checkbox 2 on nüüd mitte valitud.")

# Oodake mõni hetk, et tulemusi näha
time.sleep(2)

# Sulgege brauser pärast testimist
driver.quit()