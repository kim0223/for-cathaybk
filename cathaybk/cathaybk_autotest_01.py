import pytest
import sys,os
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from selenium.webdriver.common.by  import Ｂy
from Module.tool import *
from time import sleep

'''globe var'''

class Test_001:
    def setup(self):
        self.driver=webdriver_base.Brower('Firefox')
    def teardown(self):
        self.driver.quit()
        sleep(1)
    
    def test_01(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        self.driver.set_window_size(200,800)
        self.driver.get_screenshot_as_file("./screenshot/test_01.jpg")
        
    
    def test_02(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        self.driver.set_window_size(200,800)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/a/img[2]").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/div").click()
        self.driver.get_screenshot_as_file("./screenshot/test_02.jpg")
        sleep(1)
        list = self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]").text
        print("信用卡選單數有：" + str(list.count("\n")) + "個")
    
    def test_03(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        self.driver.set_window_size(200,800)
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/a/img[2]").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[1]/div").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[1]/div").click()
        self.driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[3]/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div[2]/a[1]").click()
        sleep(1)
        self.driver.find_element(By.XPATH,"//*[text()='停發卡']").click()
        sleep(1)
        try:
            i = 1
            while i > 0:
                xpath_path = "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[" + str(i) + "]"
                self.driver.find_element(By.XPATH,xpath_path).click()
                file_name = "test_03_" + str(i) + ".jpg"
                self.driver.get_screenshot_as_file("./screenshot/" + file_name)
                i = i+1
        except:
            
            j = 0
            path="./screenshot/"
            for lists in os.listdir(path):
                sub_path = os.path.join(path, lists)
                if os.path.isfile(sub_path):
                    if "test_03"in sub_path:
                        j = j + 1 
            #count_slide 扣除最後一次錯誤連結  
            count_slide = i - 1    
            file_count = j
            if count_slide == file_count:
                print("卡片數" + str(count_slide) + "與截圖數" + str(file_count) + "相符")
            else:
                print("卡片數" + str(count_slide) + "與截圖數" + str(file_count) + "不相符")
            

    pytest.main(['-reruns 2','-s',path_modify("./cathaybk_autotest_01.py")])