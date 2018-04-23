from ChangeProfile_Request import *
from ReloadProfiles_Request import *
import allure
from Get_data_from_server import *
import time


#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
def wrong_request():
    allure.description("Check wrong request")
    data = {
        "tradingProfile":{
            "name":"Default",
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

    with allure.step('Get data from MT4_MARKET_REAL'):
        R2 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R3 = Get_data_from_server('172.16.1.51')
    return R1, R2, R3
#############################################################################
def request_without_platforms():
    allure.description("No parameter platforms on request")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{"name":"Default"}
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server('172.16.1.183')

    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server('172.16.1.184')

    with allure.step('Get data from MT4_RD_DEMO'):
        R4 = Get_data_from_server('172.16.1.132')

    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server('172.16.1.175')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server('172.16.1.51')

    with allure.step('Get data from MT4_RD_REAL'):
        R8 = Get_data_from_server('172.16.1.181')
    return R1, R2, R3, R4, R5, R6, R7, R8

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
                "name":"Crisis",
                "platforms":["MT4_INSTANT_REAL1", "MT4_MARKET_REAL"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server('172.16.1.183')

    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server('172.16.1.184')

    with allure.step('Get data from MT4_RD_DEMO'):
        R4 = Get_data_from_server('172.16.1.132')

    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server('172.16.1.175')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server('172.16.1.51')

    with allure.step('Get data from MT4_RD_REAL'):
        R8 = Get_data_from_server('172.16.1.181')
    return R1, R2, R3, R4, R5, R6, R7, R8

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
                "name":"Default",
                "platforms":[]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server('172.16.1.183')

    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server('172.16.1.184')

    with allure.step('Get data from MT4_RD_DEMO'):
        R4 = Get_data_from_server('172.16.1.132')

    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server('172.16.1.175')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server('172.16.1.51')

    with allure.step('Get data from MT4_RD_REAL'):
        R8 = Get_data_from_server('172.16.1.181')
    return R1, R2, R3, R4, R5, R6, R7, R8
#############################################################################
def value_to_platforms_not_str():
    allure.description("Value to platforms not str")
    data = {
        "tradingProfile":{
            "name":"Default",
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
                "name":"Crisis",
                "platforms":["MT4_INSTANT_DEMO"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server('172.16.1.183')

    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server('172.16.1.184')

    with allure.step('Get data from MT4_RD_DEMO'):
        R4 = Get_data_from_server('172.16.1.132')

    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server('172.16.1.175')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server('172.16.1.51')

    with allure.step('Get data from MT4_RD_REAL'):
        R8 = Get_data_from_server('172.16.1.181')
    return R1, R2, R3, R4, R5, R6, R7, R8
#############################################################################
def correct_value_to_platforms_two_servers():
    allure.description("Correct value to platforms")
    with allure.step('Sending a request'):
        data = {
            "tradingProfile":{
                "name":"Crisis",
                "platforms":["MT4_RD_REAL","MT4_RD_DEMO"]
            }
        }
        R1 = trueurl(data)
    time.sleep(2)

    with allure.step('Get data from MT4_INSTANT_REAL1'):
        R2 = Get_data_from_server('172.16.1.183')

    with allure.step('Get data from MT4_INSTANT_REAL2'):
        R3 = Get_data_from_server('172.16.1.184')

    with allure.step('Get data from MT4_RD_DEMO'):
        R4 = Get_data_from_server('172.16.1.132')

    with allure.step('Get data from MT4_MARKET_REAL'):
        R5 = Get_data_from_server('172.16.1.60')

    with allure.step('Get data from MT4_INSTANT_DEMO'):
        R6 = Get_data_from_server('172.16.1.175')

    with allure.step('Get data from MT4_MARKET_DEMO'):
        R7 = Get_data_from_server('172.16.1.51')

    with allure.step('Get data from MT4_RD_REAL'):
        R8 = Get_data_from_server('172.16.1.181')
    return R1, R2, R3, R4, R5, R6, R7, R8
#############################################################################
def value_to_platforms_two_servers_one_not_in_config():
    allure.description("Two server one not in the config")
    data = {
        "tradingProfile":{
            "name":"For_AutoTest",
            "platforms":["MT4_MARKET_DEMO","MT4_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult
#############################################################################
def not_found_platform_in_profile():
    allure.description("Not found platform in the profile")
    data = {
        "tradingProfile":{
            "name":"Default",
            "platforms":["MT4_TEST_DEMO"]
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
            "platforms":["MT5_TEST"]
        }
    }
    FinishResult = trueurl(data)
    return FinishResult

#############################################################################
#Check valid json
#############################################################################
def no_valid_json_1():
    allure.description("No valid json 1")
    data = '{"tradingProfile":{"name":"Default","platforms":["MT5_DEMO"]}}'
    FinishResult = trueurl(data)
    return FinishResult

def no_valid_json_2():
    allure.description("No valid json 2")
    data = "{\"tradingProfile:{\"name\":\"Default\",\"platforms\":[\"MT5_DEMO\"]}}"
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