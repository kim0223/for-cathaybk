import pytest
import sys,os
sys.path.append(os.getcwd())
from Module.base import webdriver_base
from selenium.webdriver.common.by  import Ｂy
from Module.tool import *
from time import sleep

# logictest_01
default_num = [35, 46, 57, 91, 29]
change_num = []
x = 0
while  x < len(default_num):
    y = str(default_num[x])
    change_num.append(y[::-1])
    x = x +1
print (change_num)

#logictest_02
default_string = "Hello welcome to Cathay 60th year anniversary"
match_string = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

z = 0
while z < len(match_string):
    match = match_string[z]
    count_num = default_string.upper().count(str(match))
    if count_num > 0 :
        print (match_string[z],count_num)
    z = z + 1
            
#logictest_03
try:
    start_num = int(input("請輸入0-100正整數:"))
    sort_count = 0
    i = 1
    if start_num >0 and start_num <=101:
        while i <= start_num:
            match = str(i).count("3")
            i = i + 1
            if match == 0:
                sort_count = sort_count + 1

        print("第 "  + str(sort_count) + " 順位")
    else:
        print("輸入錯誤，請重新執行")
except:
    print("輸入錯誤，請重新執行")