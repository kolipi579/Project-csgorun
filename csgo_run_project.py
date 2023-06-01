from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import time 
o = Options()
o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)
driver.get("https://csgo3.run/")
time.sleep(20)
"""exchange = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[3]/button[1]')
exchange.click()
input_cost = driver.find_element(By.XPATH, '//*[@id="exchange-filter-maxPrice-field"]')
input_cost.send_keys('0.1')
time.sleep(2)
button_item = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[1]/div[2]/div/div[2]/div[3]/button[1]')
button_item.click()
time.sleep(2)
button_item = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[1]/div[2]/div/div[2]/div[1]/button')
button_item.click()"""

def if_crash(x_num):
    if x_num < 1.2:
        return True
    else:
        return False

def analyze_last_bet(last_bet_element):
    outer_html = last_bet_element.get_attribute('outerHTML')
    last_x = outer_html[:len(outer_html)-5]
    g = 0
    for i in range(7,3,-1):
        l = last_x[len(last_x)-i:]
        arr_l = l.split('.')
        for i in arr_l:
            if i.isdigit():
                g += 1
        if g == len(arr_l):
            g = 0
            break
        g = 0
    last_x_num = float(l)
    return last_x_num

def make_bet_func():
    try:
        select_item = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/button')
        select_item.click()
        input_bet = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div/input[2]')
        input_bet.click()
        """input_x = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/label/input')
        input_x.send_keys('1.2')"""
        make_bet = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/button')
        make_bet.click()
        time.sleep(5)
    except NoSuchElementException:
        print('make_bet')
        buy_item()

def buy_item():
    try:
        exchange = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[3]/button[1]')
        exchange.click()
        time.sleep(4)
        input_cost = driver.find_element(By.XPATH, '//*[@id="exchange-filter-maxPrice-field"]')
        input_cost.send_keys('0.1')
        time.sleep(4)
        button_item = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[4]/div[2]/div/div[2]/div[3]/button[1]')
        button_item.click()
        time.sleep(4)
        item_accept = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[4]/div[2]/div/div[2]/div[1]/button')
        item_accept.click()
        close_buy_screen = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[3]/div[2]/div/div[1]/button')
        close_buy_screen.click()
    except NoSuchElementException:
        print("buy_item")
        pass

def change_item():
    try:
        select_item = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/button')
        select_item.click()
        exchange = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[3]/button[1]')
        exchange.click()
        time.sleep(4)
        input_cost = driver.find_element(By.XPATH, '//*[@id="exchange-filter-maxPrice-field"]')
        input_cost.send_keys('0.1')
        time.sleep(4)
        button_item = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[4]/div[2]/div/div[2]/div[3]/button[1]')
        button_item.click()
        time.sleep(4)
        item_accept = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[4]/div[2]/div/div[2]/div[1]/button')
        item_accept.click()
        close_buy_screen = driver.find_element(By.XPATH, '//*[@id="modal-portal"]/div[3]/div[2]/div/div[1]/button')
        close_buy_screen.click()
    except NoSuchElementException:
        print('change_item')
        pass

last_bet = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/a[1]')
crash_arr = [0]*15
lastx1 = analyze_last_bet(last_bet)
number_of_crash = 0
number_of_x = 0
five_bets = 0

while True:
    time.sleep(3)
    last_bet = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/a[1]')
    if analyze_last_bet(last_bet) != lastx1:
        lastx1 = analyze_last_bet(last_bet)
        if if_crash(last_bet):
            crash_arr[number_of_x] = 1
            number_of_crash += 1
        else: 
            crash_arr[number_of_x] = 0
        if five_bets >= 5:
            time.sleep(4)
            five_bets = 0
            change_item()
        if sum(crash_arr) >= 4:
            time.sleep(4)
            five_bets += 1
            make_bet_func()
        number_of_x += 1
        if number_of_x == 15:
            number_of_x = 0
            number_of_crash = 0
    
