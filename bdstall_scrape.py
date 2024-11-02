from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import pandas as pd


driver = webdriver.Chrome()
driver.maximize_window()

all_product_list = []
all_data = []

for all_pages in range(1,22):
    driver.get(f"https://www.bdstall.com/laptop/{all_pages}/")
    
    url_elements = driver.find_elements(By.XPATH, "//div[@class='row popular-menu-effect']/a")
    
    for all_urls in url_elements:
        single_url = all_urls.get_attribute("href")
        all_product_list.append(single_url)


for demo_urls in all_product_list:
    driver.get(demo_urls)
    
    try:
        name = driver.find_element(By.XPATH, "//h1").text
    except:
        name = ""
        
    try:
        id = driver.find_element(By.XPATH, "(//div[@class='container product-desc']//div[@class='s-bottom']/span)[1]").text.strip()
        id = id.replace("ID: ", "")
    except:
        id = ""
        
    try:
        stock = driver.find_element(By.XPATH, "//div[@class='container product-desc']//div[@class='s-bottom']//span[@style='font-weight:bold']").text
    except:
        stock= ""

    try:
        image = driver.find_element(By.XPATH, "//div[@id='displayAvator']/img").get_attribute("src")
    except:
        image = ""
        
        
    try:
        price1 = driver.find_element(By.XPATH, "//div[@id='compare']//p/b").text
        price1 = re.sub(r"\D", "", price1)
    except:
        price1 = ""
        
    try:
        price2= driver.find_element(By.XPATH, "(//div[@class='product-desc-contact-price'])[1]").text.strip()
        price2 = price2.replace("৳ ", "")
    except:
        price2 = ""
        
    try:
        item = driver.find_element(By.XPATH, "(//table[@style='margin-bottom:0px']//td)[1]/a").text
    except:
        item = ""
        
    try:
        pbrands = driver.find_element(By.XPATH, "(//table[@style='margin-bottom:0px']//tbody//tr/td)[2]/a").text
    except:
        pbrands = ""
        
    try:
        description = driver.find_element(By.XPATH, "//div[@class='b-top']/p").text
    except:
        description = "" 
        
    product_details = {
        "name": name,
        "id": id,
        "stock": stock,
        "image": image,
        "price1": price1,
        "price2": price2,
        "item": item,
        "brand": pbrands,
        "description": description,    
    }
    
    all_data.append(product_details)
    print(f"Scrape done {len(all_data)}")
    
    # if(len(all_data)== 5): break
    
df = pd.DataFrame(all_data)
df.to_excel("bdstall.xlsx", index=False)
        

#Close driver
driver.quit()        