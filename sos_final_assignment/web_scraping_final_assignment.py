from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

# Initialize the Safari driver
driver = webdriver.Safari()
try:
    # Open the webpage
    url = "https://www.nseindia.com/market-data/live-equity-market"
    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()
    # tbody = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    # )

    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "freezed-row")))
    # time.sleep(5)
    html_content=driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')
    # tags=soup.find_all('div',class_="tbl_leftcol_fix")
    tags=soup.find('tbody')

    rows = tags.find_all('tr')


    stock_name=[]
    open=[]
    high=[]
    low=[]
    prclose=[]
    ltp=[]
    change=[]
    changeper=[]
    volume=[]
    value=[]
    week_high=[]
    week_low=[]
    perchange_D=[]
    uni_list=[stock_name,open,high,low,prclose,ltp,change,changeper,volume,value,week_high,week_low,perchange_D]




    # for row in rows:
    #     print(row)
    for i in range(4,204,4):
        row = rows[i]
        
        stock_detail=row.find_all('td')
        
        
        for j in range(13):
            # print(stock_detail[j].text,end="  ")
            uni_list[j].append(stock_detail[j].text)
        
    # print(stock_name)
    # print(len(stock_name))

    data = pd.DataFrame({
        'STOCK NAME' : stock_name,
        'OPEN': open,
        'HIGH':high,
        'LOW':low,
        'PREV. CLOSE':prclose,
        'LTP':ltp,
        'CHNG':change,
        '%CHNG':changeper,
        'VOLUME':volume,
        'VALUE':value,
        '52W HIGH':week_high,
        '52W LOW':week_low,
        '30D %CHNG':perchange_D
    })

    data.to_csv('final_assignment.csv', index=False)

    print(data)


except:
    print("Problem in Data Retrieval. TRY AGAIN!")




