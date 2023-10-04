from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select  # Importige Select klass

# Looge uus Chrome brauseri sessioon
driver = webdriver.Chrome()

# Avage veebileht "https://the-internet.herokuapp.com/"
driver.get("https://the-internet.herokuapp.com/")


driver.get("https://the-internet.herokuapp.com/dropdown")

# Leidke dropdown-element
dropdown = driver.find_element("id", "dropdown")

# Looge Select-objekt
select = Select(dropdown)

# Vali Option 1 (või Option 2, kui soovite)
select.select_by_value("1")

# Väljastage valitud option
selected_option = select.first_selected_option.text
print(f"Valitud valik: {selected_option}")

# Oodake mõni hetk, et tulemusi näha
time.sleep(2)

# Sulgege brauser pärast testimist
driver.quit()