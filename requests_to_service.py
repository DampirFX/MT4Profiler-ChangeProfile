import requests
import json

##############################################################################################################
#запросы для перечитывания профилей
##############################################################################################################
def reload_trueurl():
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ReloadProfiles'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def reload_falseurl():
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ReloadProfilestst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers=headers)
    FinishResult = answer.json()
    return FinishResult

##############################################################################################################
#запросы для смены профилей
##############################################################################################################
def change_profile_trueurl(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfile'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def change_profile_trueurl_without_json(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfile'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=data, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def change_profile_falseurl(data):
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfiletst'       #MT5 - .42:9966  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult
##############################################################################################################
#запросы для изменения настроек сервера
##############################################################################################################

def server_settings_trueurl(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettings'       #MT5 - .42:9968  MT4 - .135:9967
    headers = {'Content-type': 'application/json',    # Определение типа данных
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def server_settings_without_json(data):
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