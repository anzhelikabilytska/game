from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service('https://qauto2.forstudy.space')
driver = webdriver.Chrome(service=service)

Name = "Marry"
last_name = "Queen"
email = "test1@test.com"
Password = "Testing123"
Car_brand = "Audi"
Car_model = "TT"
Car_Mileage = "12000"

expense_description = "23"
expense_amount = "50"


    driver.get("https://qauto2.forstudy.space//button[@type='signup]")

    driver.find_element(By.NAME, "Name").send_keys(Name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "Password").send_keys(Password)
    driver.find_element(By.XPATH, "//button[@type='Register']").click()


    profile_name = driver.find_element(By.ID, "profileName").text
    profile_last_name = driver.find_element(By.ID, "profileLastName").text

    assert profile_name == Name, "First name does not match"
    assert profile_last_name == last_name, "Last name does not match"


    driver.find_element(By.ID, "addCarButton").click()
    driver.find_element(By.NAME, "Brand").send_keys(car_brand)
    driver.find_element(By.NAME, "Model").send_keys(car_model)
    driver.find_element(By.NAME, "Mileage").send_keys(Car_Mileage)
    driver.find_element(By.XPATH, "//button[@type='Add']").click()

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, f"//td[text()='{Audi TT}']"))
    )

    driver.find_element(By.XPATH, f"//td[text()='{Audi TT}']/../td/button[text()='Add Fuel Expense']").click()
    driver.find_element(By.NAME, "Number of liters").send_keys(expense_description)
    driver.find_element(By.NAME, "Total cost").send_keys(expense_amount)
    driver.find_element(By.XPATH, "//button[@type='Add']").click()


    driver.find_element(By.ID, "deleteAccountButton").click()
    driver.find_element(By.XPATH, "//button[text()='Confirm']").click()

    WebDriverWait(driver, 7).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Account Deleted']"))
    )

    print("All test steps passed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
