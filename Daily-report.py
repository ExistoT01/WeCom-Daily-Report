import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import date

# SMTP config
mail_user = ""  # username
mail_pass = ""  # token

sender = ''
receiver = ''

def getHeaders():
    headers = {
        'Host': 'pingan.ouc.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '2356',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': '', # edit this
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://pingan.ouc.edu.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://pingan.ouc.edu.cn/ncov/wap/default/index',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en,en-US;q=0.9',
        'Cookie': '' # edit this
    }
    return headers

def getData(today):
    data = {
        'uid': '', # edit this
        'tw': '10',
        'szxqsfyqzbl': '0',
        'szsqsfybl': '0',
        'szsqfsyq': '0',
        'sfzx': '0',
        'sfzhbsxsx': '0',
        'sfzgsxsx': '0',
        'sfyyjc': '0',
        'sfygtjzzfj': '0',
        'sftjwh': '0',
        'sftjhb': '0',
        'sfsqhzjkk': '0',
        'sfqrxxss': '1',
        'sfjtfxdq': '0',
        'sfjcwhry': '0',
        'sfjcqzfyyshz': '0',
        'sfjchbry': '0',
        'sfjchbjwry': '0',
        'sfjcfrhxdbr': '0',
        'sfjcfjry': '0',
        'sfjcbh': '0',
        'sfcyglq': '0',
        'sfcxzysx': '0',
        'sfcxtz': '0',
        'sfbqzwhz': '0',
        'province': '', # edit this
        'oucyzjzpp': '3',
        'oucsfyjzjqz': '1',
        'oucsfjzym': '1',
        'ouchsjcqk': '1',
        'oucezjzwcsj': '2021-07-17',
        'oucezjzpp': '3',
        'oucezjzdd': '1',
        'jcjgqr': '0',
        'ismoved': '0',
        'id': '', # edit this
        'geo_api_info': , # edit this
        'date': today,
        'created': '', # edit this
        'city': '', # edit this
        'area': '', # edit this
        'address': '' # edit this
    }
    return data
    
def sendEmail(msg):
    message = MIMEText(msg, 'plain', 'utf-8')

    message['From'] = Header(sender, 'utf-8')  # 发送者
    message['Subject'] = Header('「每日上报」结果', 'utf-8')

    # sending process
    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
    smtp.login(mail_user, mail_pass)
    smtp.sendmail(sender, receiver, message.as_string())
    

def main():
    # 上报api接口
    url = 'https://pingan.ouc.edu.cn/ncov/wap/default/save'
    # 今日日期
    today = date.today()
    # format
    today = today.strftime('%Y%m%d')
    # send request
    r = requests.post(url=url, headers=getHeaders(), data=getData(today))
    # send email
    sendEmail(r.json()['m'])
    
    

if __name__ == '__main__':
    main()
