from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd

try:
    # Initialize the Safari driver
    driver = webdriver.Safari()

    # URL for the NSE Nifty Options Chain
    url = 'https://www.nseindia.com/option-chain'
    driver.get(url)
    driver.implicitly_wait(3)
    # time.sleep(5)
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "bg-yellow")))
    html_content=driver.page_source

    option_type=[]
    strike=[]
    oi=[]
    volume=[]
    ltp=[]


    soup = BeautifulSoup(html_content, 'lxml')
    table= soup.find('table',class_="common_table w-100")
    rows=table.find_all('tr')
    for i in range(2,len(rows)):
        row=rows[i]
        rowdata=row.find_all('td')
        calls_or_puts= rowdata[1].get('class')
        if 'bg-yellow' in calls_or_puts: 
            option_type.append("Calls")
        else:
            option_type.append("Puts")
        
        strike.append(rowdata[11].text)
        if option_type[-1]=="Calls":
            oi.append(rowdata[1].text)
            volume.append(rowdata[3].text)
            ltp.append(rowdata[5].text)

        else:
            oi.append(rowdata[21].text)
            volume.append(rowdata[19].text)
            ltp.append(rowdata[17].text)
            
        
    data=pd.DataFrame({
        'OPTION TYPE':option_type,
        'STRIKE PRICE':strike,
        'OPEN INTEREST':oi,
        'VOLUME':volume,
        'LTP':ltp
    })

    data.to_csv('final_assignment_optional.csv', index=False)
    print(data)
    
except:
    print("Problem in Data Retrieval. TRY AGAIN!")