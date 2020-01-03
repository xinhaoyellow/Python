import json
import requests

'''
    向机器人发送消息
'''
def get_requests(msg):
    apiurl='https://api.ownthink.com/bot'
    appid='06a76a20d94db1094ec2f3cd54de33f4'
    data={
        'spoken':msg,
        'appid':appid,
        'userid':'xiaohuang'

    }
    header={'content-type':'application/json'}

    try:
        req=requests.post(apiurl,headers=header,data=data)
        return req.json()
    except:
        return 
    

'''
    获取机器人回复消息
'''
def reciver_msg(msg):
    #戻り値
    return_msg='我是小黄，我的CPU好像挂了~_~[自动回复]'
    replayjson=get_requests(msg)
    if replayjson['message']=='success':
        return_msg=replayjson['data']['info']['text'].replace('小思','伦家~').replace('思知机器人','伦家~')
        print('AI机器人回答：',return_msg)
    return return_msg

msg=input()
while msg!='exit':
    reciver_msg(msg)
    msg=input()
