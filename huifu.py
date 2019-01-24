import itchat
import requests
import json
#这个替换成自己的图灵机器人apikey
key = '1********************'
def liaotian(text):
    url = 'http://www.tuling123.com/openapi/api?key=' + key + '&info=' + text
    res = requests.get(url)
    res.encoding = 'utf-8'
    jd = json.loads(res.text)
    return jd['text']
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    messeg=liaotian(msg['Text'])
    sec=itchat.send_msg('［来自机器人］：'+messeg,msg['FromUserName'])
    if sec['BaseResponse']['Ret']!=1204:
        print('from:'+msg['User']['RemarkName'])
        print('sended:'+messeg)
    else:
        if not msg['User']['RemarkName']:
            print('failed from:Unkown user')
        else:
            print('failed from:'+msg['User']['RemarkName'])
    
itchat.auto_login(True)
itchat.run()
