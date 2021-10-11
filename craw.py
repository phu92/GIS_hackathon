#-*- coding:utf-8 -*-
#기본버젼
from urllib.request import urlopen
from urllib.parse import quote_plus
import time
import pandas as pd
from selenium import webdriver
import chromedriver_autoinstaller

path = chromedriver_autoinstaller.install()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--no-sandbox')
#--disable-extensions 확장프로그램 무력화
chrome_options.add_argument('window-size=1920x1080') # 창크기 조절
chrome_options.add_argument("disable-gpu") #gpu 사용X
chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument("User_Agent: Mozilla/5.0 \(Windows NT 6.1\) AppleWebKit/537.36 \(KHTML, like Gecko\) Chrome/41.0.2228.0 Safari/537.36")

driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)

url = 'http://bd.kma.go.kr/kma2020/fs/energySelect1.do?pageNum=5&menuCd=F050701000'
driver.get(url)
today = driver.find_element_by_id("thToday").text
# print(today)
element = driver.find_element_by_xpath('//*[@id="toEnergy"]/tr[1]').text.split()

# print(element)

times_1 = []
elects_1 = []
elect_1 =[]
sun_1 = []
tempe = []
time.sleep(1)
for i in range(5,22):
    tr = str(i)
    string = driver.find_element_by_xpath(f'//*[@id="toEnergy"]/tr[{i}]').text.split()
    times_1.append(string[0])
    elect_1.append(string[1]+'   ')
    elects_1.append(string[2]+'      ')
    sun_1.append(string[3]+'      ')
    tempe.append(string[4])

my_dict = {"발전량(KW)":elect_1,"누적발전량(KWh)":elects_1,"일사량(W/㎡)":sun_1,"기온(℃)":tempe}
my_df = pd.DataFrame(my_dict,index=times_1).rename_axis(today)
#===========================지역정보=======================================
서울특별시     = '//*[@id="info_1100000000"]/span' 
경기도         = '//*[@id="info_4100000000"]/span'
인천광역시     = '//*[@id="info_2800000000"]/span'
대전광역시     = '//*[@id="info_3000000000"]/span'
세종특별자치시 = '//*[@id="info_3600000000"]/span'
광주광역시     = '//*[@id="info_2900000000"]/span'
대구광역시     = '//*[@id="info_2700000000"]/span'
울산광역시     = '//*[@id="info_3100000000"]/span'
부산광역시     = '//*[@id="info_2600000000"]/span'
제주특별자치도 = '//*[@id="info_5000000000"]/span'
강원도         = '//*[@id="info_4200000000"]/span'
# 충청북도       = '//*[@id="info_4300000000"]/span'
충청남도       = '//*[@id="info_4400000000"]/span'
경상북도       = '//*[@id="info_4700000000"]/span'
경상남도       = '//*[@id="info_4800000000"]/span'
전라북도       = '//*[@id="info_4500000000"]/span'
전라남도       = '//*[@id="info_4600000000"]/span'

def information(area):
    reset = driver.find_element_by_xpath('//*[@id="map"]/div[1]')
    driver.execute_script("arguments[0].click();", reset)
    button = driver.find_element_by_xpath(area)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(0.8)
    # button.click()
    
        
    times = []
    elect = []
    elects = []
    sun = []
    tempe = []
    for i in range(5,22):

        tr = str(i)
        string = driver.find_element_by_xpath(f'//*[@id="toEnergy"]/tr[{i}]').text.split()
        times.append(string[0])
        elect.append(string[1]+'   ')
        elects.append(string[2]+'      ')
        sun.append(string[3]+'     ')
        tempe.append(string[4])

    
    today = driver.find_element_by_id("thToday").text       #오늘 정보
    area_name = driver.find_element_by_id("areaName").text  #지역 이름

    my_dict = {"발전량(KW)":elect,"누적발전량(KWh)":elects,"일사량(W/㎡)":sun,"기온(℃)":tempe}
    area_my_df = pd.DataFrame(my_dict,index=times).rename_axis(f"{area_name}:{today}")

    return area_my_df
time.sleep(1)

서울 = information(서울특별시)
경기 = information(경기도)
인천 = information(인천광역시)
대전 = information(대전광역시)
세종 = information(세종특별자치시)
광주 = information(광주광역시)
대구 = information(대구광역시)
울산 = information(울산광역시)
부산 = information(부산광역시)
제주 = information(제주특별자치도)
강원 = information(강원도)
충남 = information(충청남도)
경북 = information(경상북도)
경남 = information(경상남도)
전북 = information(전라북도)
전남 = information(전라남도)

# print(서울)
driver.quit()