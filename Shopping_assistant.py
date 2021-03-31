#! /usr/bin/python3
import os
def shopping():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import requests
    import bs4
    import os
    import time
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    global browser
    #browser = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
    browser = webdriver.Chrome('/usr/bin/chromedriver')
    song_base_url = "https://www.flipkart.com"
    #ong_base_url = str(song_base_url)
    song_url = os.path.join(song_base_url)
    song_url = song_url.replace("\\","")
    browser.get(song_url)

def search_product(product):
    
    base_url = "https://www.flipkart.com/search?q="
    product = str(product)
    base_url1 = "&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    song_url = os.path.join(base_url,product,base_url1)
    song_url = song_url.replace("\\","")
    browser.get(song_url)

def scroll_down():
    import time
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)

def scroll_down_continuous():
    import time
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)
    browser.execute_script("window.scrollTo(0, window.scrollY + 200)")
    time.sleep(4)





