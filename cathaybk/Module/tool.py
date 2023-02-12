"""
自定義函數
"""
from collections import defaultdict
from email import header
from aiohttp import Payload
#from matplotlib.font_manager import json_dump
from numpy import NaN
from PIL import Image
from time import sleep
import requests
#import pymssql
import pytesseract
import pandas
import os,shutil
from pathlib import Path
import time
import datetime
import json
import sys,os

#取得資料庫特定資料
'''
def DB_Link(SQL):
    
    #以sql指令查詢資料表，以單欄位/單筆資料為主
    #輸入
    #    sql  EX : select name from customer where id='a123456789'
    #輸出
    #    顯示查詢結果
    

    conn=pymssql.connect(
    server='127.0.0.1'
    ,port='1433'
    ,user='Admin'
    ,password='admin1982'
    ,database='Master'
    ,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(SQL)
    row_1 = cursor.fetchone()
    return row_1


 #取得資料庫中簡訊密碼值,簡訊未產生時間隔5秒查詢10次
def OTP(verify_code):

    #查詢簡訊密碼

    #輸入
        #輸入密碼關鍵字，ex:ATX-568695， 輸入ATX
    #輸出
        #簡訊密碼


    verify_code=verify_code.upper()
    A="select * from message where message like"+" '%" + verify_code +"%'"
    result=DB_Link(A)
    for i in range(0,10,1):
        if result is None:
            sleep(5)
            result=DB_Link(A)
        else:
            str1=str(result[1])
            str2=str1.find(verify_code)
            OTP_Code=str1[str2+4:str2+10]
            return OTP_Code
'''

#儲存網頁圖檔
def save_img(url):
    '''
    儲存網頁圖檔
    '''
    file_name='ocr_code.jpg'
    res=requests.get(url)
    with open(file_name,'wb') as f:
        f.write(res.content)

#OCR辨識
def OCR(file_path):
    '''
    圖像辨識，用於圖形驗證碼

    輸入
        辨識圖檔路徑
    輸出
        字串型態辨識結果
    '''

    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = Image.open(file_path)
    return pytesseract.image_to_string(img,lang='eng')

#取得csv變數
def CSV(file_path:str,column1:str,column2:str,column3:str,column4:str,column5:str,column6:str):
    '''
    取得CSV檔案內容

    輸入
        檔案路徑、欄位名1、欄位名2、欄位名3、欄位名4、欄位名5、欄位名6
        若欄位為空值則輸入''
    輸出
        以列表型態顯示結果
    '''

    file=pandas.read_csv(file_path)
    A=[]
    B=[]
    C=[]
    D=[]
    E=[]
    F=[]
    if column1 != '':
        for i in  file[column1]:
            if i is not NaN:
                A.append(i)
    if column2 != '':
        for j in  file[column2]:
            if j is not NaN:
                B.append(j)
    if column3 != '':
        for k in  file[column3]:
            if k is not NaN:
                C.append(k)
    if column4 != '':
        for l in  file[column4]:
            if l is not NaN:
                D.append(l)
    if column5 != '':
        for m in  file[column5]:
            if m is not NaN:
                E.append(m)
    if column6 != '':
        for n in  file[column6]:
            if n is not NaN:
                F.append(n)

    return(A,B,C,D,E,F)

#清除並重建暫存檔
def clean_temp_file(file_path):
    '''
    輸入暫存資料夾的路徑
    如不存在建立資料夾
    若存在則先刪除資料夾在建立
    '''
    if os.path.isdir(file_path):
        shutil.rmtree(str(Path(file_path)))
        os.mkdir(str(Path(file_path)))
    else:
        os.mkdir(str(Path(file_path)))

#自動轉換路徑
def path_modify(path):
    '''
    自動依照運行環境切換路徑／
    '''
    return str(Path(path))

#gmail發信
def send_email_from_google(to_b,subject,content):
    '''
    透過gmail發送信件與附加檔案
    '''
    #載入模組
    import email.message
    from email.mime.application import MIMEApplication
    #建立訊息物件
    msg=email.message.EmailMessage()
    #利用物件建立基本設定
    msg["From"]='kim19820223@gmail.com'
    msg["To"]=to_b
    msg["Subject"]=subject
    #寄送郵件主要內容
    #msg.set_content("測試郵件純文字內容") #純文字信件內容
    msg.add_alternative(content) #HTML信件內容
    #構建郵件附件
    attach_file = '/Users/kimsu/Documents/python_code/practice/python_demo/crawler_website/official_crawler_report.csv'           #獲取檔案路徑
    part_attach1 = MIMEApplication(open(attach_file,'rb').read())   #開啟附件
    part_attach1.add_header('Content-Disposition','attachment',filename='attach_file') #為附件命名
    msg.attach(part_attach1)   #新增附件

    #登入資訊
    acc='kim19820223@gmail.com'
    password='ttbfgovymxjvjuaa' #使用google應用程式密碼、App Password密碼

    #連線到SMTP Sevver
    import smtplib
    #可以從網路上找到主機名稱和連線埠
    server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
    server.login(acc,password)
    server.send_message(msg)
    server.close() #發送完成後關閉連線

    #LineBot通知機器人
def linebot(message):
    from linebot import LineBotApi, WebhookHandler
    from linebot.exceptions import InvalidSignatureError
    from linebot.models import MessageEvent, TextMessage, TextSendMessage

    line_bot_api = LineBotApi('iQDlTHlwIVAvvITW2f+EdDXf6Q+k6Lx3sS4l0S4Q64FU1LR1l0YGuyJ+pwzkjcDFE6iV66mgzVmDlfHsH7IgFEtVYnxLKM/RrzRxHvbaG0ZdJofj+BJnWXhD5FRh+9lf/rh1MyaLBsHglFxV1wFAqwdB04t89/1O/w1cDnyilFU=')
    handler = WebhookHandler('28867c681d4ef4eeaffd2bffcf1ff1c4')

    line_bot_api.push_message('U5da618bb5f0debd8568142696439be59', TextSendMessage(text=message))

def order_date(order_date_type):
    mid_datetime=str(datetime.date.today())+'-12-00'
    mid_datetime=datetime.datetime.strptime(mid_datetime,"%Y-%m-%d-%H-%M")
    if order_date_type=='today':
        if datetime.datetime.today() > mid_datetime:
            order_date = datetime.date.today() + datetime.timedelta(days = 1)
        else:
            order_date=datetime.date.today()
    elif order_date_type=='tomorrow':
        order_date = datetime.date.today() + datetime.timedelta(days = 1)
    elif order_date_type=='yesterday':
        order_date = datetime.date.today() + datetime.timedelta(days = -1)
    return str(order_date)

def get_datetime():
    localtime = time.localtime()
    result = time.strftime("_%m%d_%I%M%S", localtime)
    return result


def get_api(api_url,payload,token):
    headers={'Authorization': 'Bearer ' + token}
    result= requests.get(api_url,params = payload , headers = headers)
    log_body = 'POST[status_code:',result.status_code,'][response_time:',result.elapsed.total_seconds(),'] ',api_url
    log_api(log_body)
    return result

def put_api(api_url,api_body,token):
    headers={'Authorization': 'Bearer ' + token}
    result= requests.put(api_url,json = api_body , headers = headers)
    log_body = 'POST[status_code:',result.status_code,'][response_time:',result.elapsed.total_seconds(),'] ',api_url
    log_api(log_body)
    return result

def post_api_json(api_url,api_body,token):
    headers={'Authorization': 'Bearer ' + token}
    #json.load型態轉換
    result= requests.post(api_url,json = json.loads(api_body) , headers = headers)
    log_body = 'POST[status_code:',result.status_code,'][response_time:',result.elapsed.total_seconds(),'] ',api_url
    log_api(log_body)
    return result
def post_api_data(api_url,api_body,token):
    headers={'Authorization': 'Bearer ' + token}
    #json.load型態轉換
    result= requests.post(api_url,data = api_body , headers = headers)
    log_body = 'POST[status_code:',result.status_code,'][response_time:',result.elapsed.total_seconds(),'] ',api_url
    log_api(log_body)
    return result

def log_api(log_body):
    current_time = datetime.datetime.now()
    file_date = current_time.strftime("%Y%m%d_")
    file_path = './Tsaitung/log/' + file_date + 'api_log.txt'
    with open(file_path, 'a+') as f:
        content =current_time.strftime("%Y/%m/%d %H:%M:%S  ") + str(log_body) + '\n'
        f.write(content)

