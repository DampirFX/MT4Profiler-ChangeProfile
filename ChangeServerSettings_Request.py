import requests
import json

def server_settings_trueurl(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettings'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def trueurl_without_json(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettings'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=data, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def server_settings_falseurl(data):
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettingstst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult