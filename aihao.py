from urllib import request, parse

cookie = ""
push_key = ""

if(cookie == ""):
   cookie = input("cookie:")
   push_key = input("push:")

url = 'https://www.aihao.cc/plugin.php?id=daka'
push = 'https://sc.ftqq.com/' + push_key + '.send?text=aihao_checkin_error'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}

# --------
params = {
    # button1 button2 button3 button4
    # 8~9     13~14   18~19   >60
    'button1': ''
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
req.add_header('Cookie', cookie)
response = request.urlopen(req)
if response.status == 200:
    print("上午打卡成功")
else:
    request.urlopen(push)
    print("上午打卡失败")

# --------
params = {
    # button1 button2 button3 button4
    # 8~9     13~14   18~19   >60
    'button2': ''
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
req.add_header('Cookie', cookie)
response = request.urlopen(req)
if response.status == 200:
    print("中午打卡成功")
else:
    request.urlopen(push)
    print("中午打卡失败")

# --------
params = {
    # button1 button2 button3 button4
    # 8~9     13~14   18~19   >60
    'button3': ''
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
req.add_header('Cookie', cookie)
response = request.urlopen(req)
if response.status == 200:
    print("下午打卡成功")
else:
    request.urlopen(push)
    print("下午打卡失败")

# --------
params = {
    # button1 button2 button3 button4
    # 8~9     13~14   18~19   >60
    'button4': ''
}

data = bytes(parse.urlencode(params), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
req.add_header('Cookie', cookie)
response = request.urlopen(req)
if response.status == 200:
    print("打卡领奖成功")
else:
    print("打卡领奖失败")
