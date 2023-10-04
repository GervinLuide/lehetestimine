from selenium import webdriver
import time

# Looge uus Chrome brauseri sessioon
driver = webdriver.Chrome()

# Avage veebileht
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

# Leia nupp "Add Element" ja vajuta seda
add_button = driver.find_element("xpath", "//button[@onclick='addElement()']")
add_button.click()

# Oodake, kuni ilmub nupp "Delete" ja seejärel vajuta seda
delete_button = driver.find_element("xpath", "//button[@class='added-manually' and @onclick='deleteElement()']")
delete_button.click()

# Oodake paar sekundit, et tulemusi näha
time.sleep(2)

# Kontrolli, kas nuppu "Add Element" ja "Delete" on vajutatud ja väljasta vastavad sõnumid
if "Add Element" in driver.page_source:
    print("Nupp 'Add Element' on vajutatud.")
else:
    print("Nupp 'Add Element' ei ole vajutatud.")

if "Delete" in driver.page_source:
    print("Nupp 'Delete' on vajutatud.")
else:
    print("Nupp 'Delete' ei ole vajutatud.")

# Sulgege brauser pärast testimist
driver.quit()
