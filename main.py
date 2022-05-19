import csv
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
driver.get('https://pchome.megatime.com.tw/stock/sto0/ock3/sid2330.html')
table = driver.find_element_by_xpath("//table[@id='tb_chart']")
with open('eggs.csv', 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)
    for row in table.find_elements_by_css_selector('tr'):
        wr.writerow([d.text for d in row.find_elements_by_css_selector('td')])
