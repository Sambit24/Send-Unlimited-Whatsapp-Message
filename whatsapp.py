from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter the name of the person you want to send the message to \n")
msg = input("Enter the message: \n")
count = int(input("Enter number of times to send message \n"))

input("Enter anything after scan QR code")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msgbox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")


for i in range (count):
    msgbox.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Success")




# //span[@title="Aziz Bhai"]
# //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
# //*[@id="main"]/footer/div[1]/div[3]/button

# //span[@title="Saroj N"]