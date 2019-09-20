from ChangeProfile_Request import *
from ReloadProfiles_Request import *
import allure
from Get_data_from_server import *
import time
import ChangeServerSettings_Request

MT4_INSTANT_REAL1 = 'mt4instantreal.mt.qa-env.com'
MT4_INSTANT_REAL2 = 'mt4instantreal2.mt.qa-env.com'
MT4_MARKET_REAL = 'mt4marketreal.mt.qa-env.com'
MT4_INSTANT_DEMO = 'mt4instantdemo.mt.qa-env.com'
MT4_MARKET_DEMO = 'mt4marketdemo.mt.qa-env.com'
MT4_MARKET_REAL2 = 'mt4marketreal2.mt.qa-env.com'
#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
def wrong_request():
    allure.description("Check wrong request")
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":["MT4_INSTANT_REAL1"]
        }
    }
    FinishResult = falseurl(data)
    return FinishResult
#############################################################################
def no_body_request():
    allure.description("No body on request")
    data = {}
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_name_and_platform():
    allure.description("No parameters name and platform on request")
    data = {"tradingProfile":{}}
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def request_without_name():
    allure.description("No parameter name on request")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{"platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]}
        }
        R1 = trueurl(data)
    return R1
#############################################################################
def request_without_platforms():
    allure.description("No parameter platforms on request")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{"name":"Default_autotest"}
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)
    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server(MT4_INSTANT_REAL2)
    with allure.step('Get data from MT4_MARKET_REAL'):
        R4 = Get_data_from_server(MT4_MARKET_REAL)
    with allure.step('Get data from MT4_MARKET_REAL2'):
        R5 = Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
#Проверка параметра Name
#############################################################################
def no_value_to_name():
    allure.description("No value to name")
    data = {
        "tradingProfile":{
            "name":"",
            "platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def value_to_name_not_str():
    allure.description("Value to name not str")
    data = {
        "tradingProfile":{
            "name":123456,
            "platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_name():
    allure.description("Correct value to name")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_INSTANT_REAL1", "MT4_MARKET_REAL"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)

    with allure.step('Get data from MT4_MARKET_REAL'):
        R3 = Get_data_from_server(MT4_MARKET_REAL)

    return R1, R2, R3

#############################################################################
def not_found_profile_for_name_value():
    allure.description("Not found profile for name value")
    data = {
        "tradingProfile":{
            "name":"for test",
            "platforms":["MT4_INSTANT_REAL1", "MT4_MARKET_REAL"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Проверка параметра platforms
#############################################################################
def no_value_to_platforms():
    allure.description("No value to platforms")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{
                "name":"Default_autotest",
                "platforms":[]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)
    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server(MT4_INSTANT_REAL2)
    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server(MT4_MARKET_REAL)
    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server(MT4_INSTANT_DEMO)
    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server(MT4_MARKET_DEMO)
    with allure.step('Get data from MT4_MARKET_REAL2'):
        R8 = Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R5, R6, R7, R8
#############################################################################
def value_to_platforms_not_str():
    allure.description("Value to platforms not str")
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":[123456]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_platforms_one_server():
    allure.description("Correct value to platform")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_INSTANT_REAL1"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)

    return R1, R2
#############################################################################
def correct_value_to_platforms_two_servers():
    allure.description("Correct value to platforms")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_MARKET_REAL","MT4_INSTANT_REAL1"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R3 = Get_data_from_server(MT4_INSTANT_REAL1)

    with allure.step('Get data from MT4_MARKET_REAL'):
        R2 = Get_data_from_server(MT4_MARKET_REAL)
    return R1, R2, R3
#############################################################################
def value_to_platforms_two_servers_one_no_connection():
    allure.description("Two server one not in the config")
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT4_INSTANT_REAL1","MT4_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def not_found_platform_in_profile():
    allure.description("Not found platform in the profile")
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":["MT4_INSTANT_DEMO"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Проверка кодов ответа
#############################################################################
def no_connection_with_server():
    allure.description("No connection with server")
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT4_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Check valid json
#############################################################################
def no_valid_json_1():
    allure.description("No valid json 1")
    data = '{"tradingProfile":{"name":"Default_autotest","platforms":["MT4_MARKET_DEMO"]}}'
    FinishResult = trueurl(data)
    return FinishResult

def no_valid_json_2():
    allure.description("No valid json 2")
    data = "{\"tradingProfile:{\"name\":\"Default_autotest\",\"platforms\":[\"MT4_MARKET_DEMO\"]}}"
    FinishResult = trueurl_without_json(data)
    return FinishResult

#############################################################################
#Check request ReloadProfiles
#############################################################################
def true_reload():
    allure.description('Check true request ReloadProfiles')
    FinishResult = reload_trueurl()
    return FinishResult
#############################################################################
def false_reload():
    allure.description('Check false request ReloadProfiles')
    FinishResult = reload_falseurl()
    return FinishResult
#############################################################################
def All_Crisis():
    allure.description("All Crisis mode")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{"name":"Crisis_autotest"}
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)
    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server(MT4_INSTANT_REAL2)
    with allure.step('Get data from MT4_MARKET_REAL'):
        R4 = Get_data_from_server(MT4_MARKET_REAL)
    with allure.step('Get data from MT4_MARKET_REAL2'):
        R5 = Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
def All_Default():
    allure.description("All Default mode")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{"name":"Default_autotest"}
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server(MT4_INSTANT_REAL1)
    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server(MT4_INSTANT_REAL2)
    with allure.step('Get data from MT4_MARKET_REAL'):
        R4 = Get_data_from_server(MT4_MARKET_REAL)
    with allure.step('Get data from MT4_MARKET_REAL2'):
        R5 = Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
#check request ChangeServerSettings
#############################################################################
def wrong_request_change_settings():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_falseurl(data)
    return FinishResult

def no_body_request_change_settings():
    data = {}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def without_symbol():
    data = {"symbols":[{"trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def symbol_not_found():
    data = {"symbols":[{"symbol":"Test","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def invalid_value_for_symbol_trade():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL_TEST"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def server_not_found():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL_TEST"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def trade_full():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def trade_close():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_CLOSE"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult

def trade_no():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_NO"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = ChangeServerSettings_Request.server_settings_trueurl(data)
    return FinishResult