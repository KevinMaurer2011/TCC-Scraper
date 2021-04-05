from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
import time
from datetime import datetime
import winsound


def ShowTime():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return current_time


def GetPrices(item_ID):
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("headless")
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('C:/Users/kevin/Documents/PyCharmProjects/pythonProject/msedgedriver.exe',
                              options=options)
    driver.get(
        f'https://us.tamrieltradecentre.com/pc/Trade/SearchResult?ItemID={item_ID}&SortBy=Price&Order=asc&page=1')

    dict_price = {}
    dict_time = {}
    item_name = driver.find_element_by_xpath('//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[1]/td[1]/div[1]')

    duration = 1000
    freq = 440

    for i in range(1, 20, 2):
        dict_price[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[4]/span[1]'
        dict_time[i] = f'//*[@id="search-result-view"]/div[1]/div/table/tbody/tr[{i}]/td[5]'

    for i in range(1, 20, 2):
        price = driver.find_element_by_xpath(dict_price[i])
        price_str = (price.text.replace(',', ''))
        price_float = float(price_str)
        price_int = int(price_float)
        age = driver.find_element_by_xpath(dict_time[i])
        # print(f'{item_name.text}: $',price.text,'Posted:',age.text)
        # print(price_int)
        # print(type(price_int))

        if '1 Minute ago' == age.text or '2 Minute ago' == age.text or '3 Minute ago' == age.text:
            if item_name.text == 'Aetherial Dust' and price_int < 300000:
                print(f'{item_name.text}: {price.text} , Posted: {age.text}')
                # winsound.Beep(freq,duration)
            if item_name.text == 'Dreugh Wax' and price_int < 7000:
                print(f'{item_name.text}: {price.text} , Posted: {age.text}')
                # winsound.Beep(freq,duration)

    print(f'Price Checked for: {item_name.text},', 'at', ShowTime(), 'PM', '- Waiting 10 Seconds')
    time.sleep(10)


while True:
    try:
        GetPrices(11807)  # Aetherial Dust
        GetPrices(211)  # Dreugh Wax
        GetPrices(6132)  # Perfect Roe
        GetPrices(5687)  # Tempering Alloy
        GetPrices(17927)  # Chromium Grains

    except:
        print('We got an error on out hands BOIIISSS')
        pass
