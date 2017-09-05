#!/usr/bin/env python3

import json

import requests

def login():
    with open('password.json', 'r') as f:
        j = json.load(f)
        username = j['username']
        password = j['password']
    res = requests.post('http://p.nju.edu.cn/portal_io/login', 
            data = {'username': username, 'password': password})
    data = res.json()
    reply = {
        'code': data['reply_code'],
        'msg': data['reply_msg']
    }
    isSuccess = reply['code'] in (1, 6)
    reply_string = '[{code}] {msg}'.format(**reply)
    return isSuccess, reply_string

def logout():
    res = requests.post('http://p.nju.edu.cn/portal_io/logout')
    print(res.text)

if __name__ == '__main__':
    isSuccess, reply_string = login()
    print(reply_string)
