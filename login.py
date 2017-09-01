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
    print(res.text)

def logout():
    res = requests.post('http://p.nju.edu.cn/portal_io/logout')
    print(res.text)

if __name__ == '__main__':
    login()
