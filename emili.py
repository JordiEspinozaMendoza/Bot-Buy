import time
# import selenium
from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:\\Users\\dell\\Documents\\Emiliano Bot\\chromedriver.exe")
browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440&intl=nosplash")
buyButton = False

while not buyButton:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button isnt ready yet")

        time.sleep(1)
        browser.refresh()
    
    except :
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
        print("Button was clicked")

        addToCartBtn.click()
        buyButton =  True