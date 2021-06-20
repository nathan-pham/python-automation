from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from options import default_options

driver = webdriver.Chrome(
    executable_path="C:/Users/nathan-pham/python-scripts/chromedriver.exe", 
    options=default_options
)

manga_site = "https://mangakakalot.com/" 
manga_selector = "#contentstory > div > div.itemupdate > ul > li:nth-child(1) > h3 > a"

driver.get(manga_site)

manga_elements = driver.find_elements_by_css_selector(manga_selector)
for element in manga_elements:
    print(element.text)

driver.quit()