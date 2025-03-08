import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Agafonov Artem
#Задание "Практикум SDET:тестовое задание"



link = 'https://practice-automation.com/form-fields/'
driver = webdriver.Chrome()
driver.get(link)
time.sleep(3)
name = driver.find_element(By.XPATH, '//*[@id="feedbackForm"]/label[1]')
print(name)
name.send_keys("test")

html = driver.find_element(By.CSS_SELECTOR, "html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

password = driver.find_element(By.XPATH, '//*[@id="feedbackForm"]/label[2]')
print(password)
password.send_keys("qwerty")
time.sleep(3)

choice1 = driver.find_element(By.ID, 'drink2').click()
print(choice1)

choice2 = driver.find_element(By.ID, 'drink3').click()
print(choice2)

choice3 = driver.find_element(By.ID, 'color3').click()
print(choice3)
time.sleep(3)

html = driver.find_element(By.CSS_SELECTOR, "html")
html.send_keys(Keys.PAGE_DOWN)
time.sleep(2)

select = driver.find_element(By.CSS_SELECTOR, '#automation > option:nth-child(2)').click()
print(select)

mail = driver.find_element(By.ID, 'email')
print(mail)
mail.send_keys("name@example.com")

tools = driver.find_elements(By.CSS_SELECTOR, "#feedbackForm > ul")
spisok = []
for i in tools:
    spisok.append(i.text)
myspisok = [x.split('\n') for x in spisok][0]
number = len(myspisok)
longest = max(myspisok, key=len)
message = driver.find_element(By.ID, 'message')
message.send_keys(str(number) + "\n" + longest)
print(message)

btn = driver.find_element(By.CSS_SELECTOR, '#submit-btn').click()
time.sleep(2)
driver.quit()
