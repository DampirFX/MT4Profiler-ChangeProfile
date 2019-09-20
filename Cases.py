import requests_to_service
import Get_data_from_server
import time


MT4_INSTANT_REAL1 = 'mt4instantreal.mt.qa-env.com'
MT4_INSTANT_REAL2 = 'mt4instantreal2.mt.qa-env.com'
MT4_MARKET_REAL = 'mt4marketreal.mt.qa-env.com'
MT4_INSTANT_DEMO = 'mt4instantdemo.mt.qa-env.com'
MT4_MARKET_DEMO = 'mt4marketdemo.mt.qa-env.com'
MT4_MARKET_REAL2 = 'mt4marketreal2.mt.qa-env.com'
#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
def wrong_request_changeprofile():
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":["MT4_INSTANT_REAL1"]
        }
    }
    FinishResult = requests_to_service.change_profile_falseurl(data)
    return FinishResult
#############################################################################
def no_body_in_the_request_changeprofile():
    data = {}
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def request_without_name_and_platform():
    data = {"tradingProfile":{}}
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def request_without_name_for_profile():
    data = {
            "tradingProfile":{"platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]}
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    return R1
#############################################################################
def request_without_platforms():
    data = {
            "tradingProfile":{"name":"Default_autotest"}
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R3 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL2)
    R4 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)
    R5 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
#Проверка параметра Name
#############################################################################
def no_value_to_name():
    data = {
        "tradingProfile":{
            "name":"",
            "platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def value_to_name_not_str():
    data = {
        "tradingProfile":{
            "name":123456,
            "platforms":["MT4_MARKET_REAL", "MT4_MARKET_DEMO"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_name():
    data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_INSTANT_REAL1", "MT4_MARKET_REAL"]}}
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R3 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)

    return R1, R2, R3

#############################################################################
def not_found_profile_for_name_value():
    data = {
        "tradingProfile":{
            "name":"for test",
            "platforms":["MT4_INSTANT_REAL1", "MT4_MARKET_REAL"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult

#############################################################################
#Проверка параметра platforms
#############################################################################
def no_value_to_platforms():
    data = {
            "tradingProfile":{
                "name":"Default_autotest",
                "platforms":[]
            }
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R3 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL2)
    R5 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)
    R6 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_DEMO)
    R7 = Get_data_from_server.Get_data_from_server(MT4_MARKET_DEMO)
    R8 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R5, R6, R7, R8
#############################################################################
def value_to_platforms_not_str():
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":[123456]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def correct_value_to_platforms_one_server():
    data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_INSTANT_REAL1"]
            }
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)

    return R1, R2
#############################################################################
def correct_value_to_platforms_two_servers():
    data = {
            "tradingProfile":{
                "name":"Crisis_autotest",
                "platforms":["MT4_MARKET_REAL","MT4_INSTANT_REAL1"]
            }
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R3 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R2 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)
    return R1, R2, R3
#############################################################################
def value_to_platforms_two_servers_one_no_connection():
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT4_INSTANT_REAL1","MT4_TEST"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult
#############################################################################
def not_found_platform_in_profile():
    data = {
        "tradingProfile":{
            "name":"Default_autotest",
            "platforms":["MT4_INSTANT_DEMO"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult

#############################################################################
#Проверка кодов ответа
#############################################################################
def no_connection_with_server():
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT4_TEST"]
        }
    }
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult

#############################################################################
#Check valid json
#############################################################################
def no_valid_json_1():
    data = '{"tradingProfile":{"name":"Default_autotest","platforms":["MT4_MARKET_DEMO"]}}'
    FinishResult = requests_to_service.change_profile_trueurl(data)
    return FinishResult

def no_valid_json_2():
    data = "{\"tradingProfile:{\"name\":\"Default_autotest\",\"platforms\":[\"MT4_MARKET_DEMO\"]}}"
    FinishResult = requests_to_service.change_profile_trueurl_without_json(data)
    return FinishResult

#############################################################################
#Check request ReloadProfiles
#############################################################################
def true_reload():
    FinishResult = requests_to_service.reload_trueurl()
    return FinishResult
#############################################################################
def false_reload():
    FinishResult = requests_to_service.reload_falseurl()
    return FinishResult
#############################################################################
def All_Crisis():
    data = {
            "tradingProfile":{"name":"Crisis_autotest"}
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)
    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R3 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL2)
    R4 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)
    R5 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
def All_Default():
    data = {
            "tradingProfile":{"name":"Default_autotest"}
        }
    R1 = requests_to_service.change_profile_trueurl(data)
    time.sleep(2)

    R2 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL1)
    R3 = Get_data_from_server.Get_data_from_server(MT4_INSTANT_REAL2)
    R4 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL)
    R5 = Get_data_from_server.Get_data_from_server(MT4_MARKET_REAL2)

    return R1, R2, R3, R4, R5

#############################################################################
#check request ChangeServerSettings
#############################################################################
def wrong_request_change_settings():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_falseurl(data)
    return FinishResult

def no_body_request_change_settings():
    data = {}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def without_symbol():
    data = {"symbols":[{"trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def symbol_not_found():
    data = {"symbols":[{"symbol":"Test","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def invalid_value_for_symbol_trade():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL_TEST"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def server_not_found():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL_TEST"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def trade_full():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def trade_close():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_CLOSE"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def trade_no():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_NO"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def success_one_server():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def success_two_server():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL","MT4_INSTANT_REAL1"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def success_one_server_fail_one():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}],"platforms":["MT4_MARKET_REAL","MT4_INSTANT_TEST"]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult

def request_changesettings_without_platform():
    data = {"symbols":[{"symbol":"EURUSD","trade":"TRADE_FULL"}]}
    FinishResult = requests_to_service.server_settings_trueurl(data)
    return FinishResult