# coding=UTF-8
"""
自定義函數

"""
from selenium.webdriver.firefox import options
from selenium.webdriver.support.wait import WebDriverWait    # 用於設置顯示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from numpy import NaN
from datetime import datetime
from appium import webdriver as appium_driver
from PIL import Image
from time import sleep
import allure
#import yaml
import os
class webdriver_base:
    # def __init__(self,drivers):
    #     self.driver = drivers
    #取得執行瀏覽器
    def Brower(Choose_brower):
        platform=os.name
        '''
        選取webdriver瀏覽器

        輸入
            Chrome / IE11 / Edge / Firefox
        輸出
            啟動指定瀏覽器
        '''
        if platform =="nt":
            if Choose_brower == 'Chrome':
                Chrome=webdriver.Chrome('.\webdriver\chromedriver.exe')#('D:\Python_Code\webdriver\chromedriver.exe')
                '''
                MAC/Windows 檔案路徑不同
                MAC:/Users/kimsu/Documents/python_code/webdriver/chromedriver
                Windows:.\webdriver\chromedriver.exe
                '''
                return Chrome
            elif Choose_brower =='IE11':
                IE11=webdriver.Ie() #('D:\Python_Code\webdriver\IEDriverServer3.exe')
                return IE11
            elif Choose_brower == 'Edge':
                Edge=webdriver.Edge()#('D:\Python_Code\webdriver\msedgedriver.exe')
                return Edge
            elif Choose_brower == 'Firefox':
                Firefox=webdriver.Firefox() #'D:\Python_Code\webdriver\geckodriver.exe'
                return Firefox
            else:
                print('判斷錯誤:請輸入正確瀏覽器名稱')

        elif platform=="posix":
            if Choose_brower == 'Chrome':
                Chrome=webdriver.Chrome(executable_path='./webdriver/chromedriver')
                return Chrome
            elif Choose_brower =='IE11':
                IE11=webdriver.Ie() 
                return IE11
            elif Choose_brower == 'Edge':
                # Edge=webdriver.Edge(executable_path='./webdriver/msedgedriver')
                service = Service(executable_path='./webdriver/msedgedriver')
                service.start()
                Edge = webdriver.Remote(service.service_url)
                return Edge
            elif Choose_brower == 'Firefox':
                #op='./webdriver/geckodriver',=op
                
                Firefox=webdriver.Firefox(executable_path='./webdriver/geckodriver')
                return Firefox
            else:
                print('判斷錯誤:請輸入正確瀏覽器名稱')
      
    def Mobile_Brower(hight,width):
        platform=os.name
        PIXEL_RATIO = 3.0
            # UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
        UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        mobileEmulation = {"deviceMetrics": {"width": width, "height": hight, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        if platform=='nt':
            driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        elif platform=="posix":
            driver = webdriver.Chrome(executable_path='./webdriver/chromedriver', chrome_options=options)
        driver.set_window_size(width,hight)
        return driver

    def execute_script2(driver,path):
        return webdriver_base.execute_script(path)

    #webdriver顯示等待
    def wait_element_by_css_selector(driver,path):
        '''
        find_element_by_find_element_by_css_selector 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.find_find_element_by_css_selector(path))

        '''
        return WebDriverWait(driver,200,0.5).until(lambda x: x.find_element_by_css_selector(path))
        
        
    def wait_element_by_xpath(driver,path):
        '''
        find_element_by_xpath 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.find_element_by_xpath(path))

        '''
        return WebDriverWait(driver,20,0.3).until(lambda x: x.find_element_by_xpath(path))

        #type='By.XPATH'
        #return WebDriverWait(driver,200,0.5).until(EC.presence_of_element_located(type, path))
    def wait_element_by_id(driver,path):
        '''
        wait_element_by_id 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.wait_element_by_id(path))
        '''
        return WebDriverWait(driver,20,0.3).until(lambda x: x.find_element_by_id(path))
    def wait_element_by_css_selector(driver,path):
        '''
        wait_element_by_id 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.wait_element_by_id(path))
        '''
        return WebDriverWait(driver,20,0.3).until(lambda x: x.find_element_by_css_selector(path))

    def wait_element_by_class_name(driver,path):
        '''
        find_element_by_class_name 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.find_element_by_class_name(path))
        '''
        return WebDriverWait(driver,20,0.3).until(lambda x: x.find_element_by_class_name(path))

    def wait_element_by_name(driver,path):
        '''
        find_element_by_class_name 顯示等待5秒

        輸入
            固定輸入變數driver,元素位置path
        輸出
            WebDriverWait(driver,20,0.5).until(lambda x: x.find_element_by_class_name(path))
        '''
        return WebDriverWait(driver,20,0.3).until(lambda x: x.find_element_by_name(path))

    def screen_shot(type,driver):
        '''

        type="allure" allure report attach png

        type="other" screenshot in .\screenshot
        '''
        CurrentTime=datetime.now().strftime('%Y_%m_%d_%H%M%S')
        image_name=str(CurrentTime) + '.png'
        if type == "allure":
            driver.save_screenshot("./screenshot.png")
            allure.attach.file("./screenshot.png",name='頁面截圖', attachment_type=allure.attachment_type.PNG)

            driver.find_element_by_tag_name('body').screenshot('.\\screenshot\\'+image_name)
        else:
            driver.save_screenshot("./"+image_name)

    def current_url(driver):
        driver.get


    