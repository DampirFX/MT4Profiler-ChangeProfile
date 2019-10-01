import requests
import json

##############################################################################################################
#запросы для перечитывания профилей
##############################################################################################################
def reload_trueurl():
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ReloadProfiles'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.get(url, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def reload_falseurl():
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ReloadProfilestst'
    headers = {'Content-type': 'application/json',
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
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfile'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def change_profile_trueurl_without_json(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfile'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=data, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def change_profile_falseurl(data):
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeProfiletst'
    headers = {'Content-type': 'application/json',
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
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettings'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult

def server_settings_without_json(data):
    st = ''
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettings'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=data, headers=headers)
    FinishResult = answer.json()
    return FinishResult

def server_settings_falseurl(data):
    url = 'http://mt4sharedservices.mt.qa-env.com:9977/ChangeServerSettingstst'
    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    FinishResult = answer.json()
    return FinishResult