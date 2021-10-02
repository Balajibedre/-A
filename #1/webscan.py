from selenium import webdriver

driver = webdriver.Edge('D:\\SERVER\\mseddriver.exe')
driver.get("https://web.whatsapp.com")

print("Login now...\n")

name = input("Enter name:")
count = int(input("count:"))
msg = input("Message: ")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msgBox.send_key(msg)
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    sendButton.click()

    print("Mission Successsful")
    print(f"{count} message were sent to {name}")