import pytest
from Cases import *


@pytest.fixture(autouse=True)
def resource_setup(request):
    print("\nStart test")
    print(request.scope)
    print(request.cls)
    print('Description: ' +request.function.__name__)
    def resource_teardown():
        print("Finish test")
    request.addfinalizer(resource_teardown)
#############################################################################
#Проверка запроса ChangeProfile
#############################################################################
class Test_ChangeProfile():
    def test_wrong_request_changeprofile(resource_setup):
        assert wrong_request_changeprofile() == {'Description': 'invalid uri', 'Status': 3}

    def test_no_body_in_the_request_changeprofile(resource_setup):
        assert no_body_in_the_request_changeprofile() == {'Description': "can't find 'tradingProfile' param", 'Status': 4}

    def test_request_without_name_and_platform(resource_setup):
        assert request_without_name_and_platform() == {'Description': "can't find 'name' param", 'Status': 4}

    def test_request_without_name(resource_setup):
        assert request_without_name_for_profile() == {'Description': "can't find 'name' param", 'Status': 4}

    def test_request_without_platforms(resource_setup):
        finres = request_without_platforms()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL1'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL2'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL2'}],
                             'Status': 0}

        assert finres[1] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[2] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[3] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']
        assert finres[4] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']

    def test_no_value_to_name(resource_setup):
        assert no_value_to_name() == {'Description': "can't find profile ''", 'Status': 5}

    def test_value_to_name_not_str(resource_setup):
        assert value_to_name_not_str() == {'Description': "'name' param not a string", 'Status': 5}

    def test_correct_value_to_name(resource_setup):
        finres = correct_value_to_name()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT4_INSTANT_REAL1'},
                                        {'Description': 'Done', 'Status': 0, 'platform': 'MT4_MARKET_REAL'}],
                             'Status': 0}

        assert finres[1] == ['3', '3', '3', '3', '3', '5', '5', '5', '5', '5', '5', '3', '3', '4', '4', '3', '3', '5', '3', '3', '4']
        assert finres[2] == ['3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '3', '3', '3', '3', '3', '3', '3', '4']

    def test_not_found_profile_for_name_value(resource_setup):
        assert not_found_profile_for_name_value() == {'Description': "can't find profile 'for test'", 'Status': 5}

    def test_no_value_to_platforms(resource_setup):
        finres = request_without_platforms()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL1'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL2'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL2'}],
                             'Status': 0}

        assert finres[1] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[2] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[3] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']
        assert finres[4] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']

    def test_value_to_platforms_not_str(resource_setup):
        assert value_to_platforms_not_str() == {'Description': 'platform element not string', 'Status': 5}

    def test_correct_value_to_platforms_one_server(resource_setup):
        finres = correct_value_to_platforms_one_server()
        assert finres[0] == {'Description': 'Done', 'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT4_INSTANT_REAL1'}], 'Status': 0}

        assert finres[1] == ['3', '3', '3', '3', '3', '5', '5', '5', '5', '5', '5', '3', '3', '4', '4', '3', '3', '5', '3', '3', '4']

    def test_correct_value_to_platforms_two_servers(resource_setup):
        finres = correct_value_to_platforms_two_servers()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT4_MARKET_REAL'},
                                        {'Description': 'Done', 'Status': 0, 'platform': 'MT4_INSTANT_REAL1'}],
                             'Status': 0}

        assert finres[1] == ['3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '3', '3', '3', '3', '3', '3', '3', '4']
        assert finres[2] == ['3', '3', '3', '3', '3', '5', '5', '5', '5', '5', '5', '3', '3', '4', '4', '3', '3', '5', '3', '3', '4']

    def test_value_to_platforms_two_servers_one_no_connection(resource_setup):
        assert value_to_platforms_two_servers_one_no_connection() == {'Description': 'Some updates have failed',
                                                                      'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT4_INSTANT_REAL1'},
                                                                                 {'Description': 'No connection', 'Status': 6, 'platform': 'MT4_TEST'}],
                                                                      'Status': 7}

    def test_not_found_platform_in_profile(resource_setup):
        assert not_found_platform_in_profile() == {'Description': 'Some updates have failed',
                                                   'Result': [{'Description': 'No information in profile','Status': 2,'platform': 'MT4_INSTANT_DEMO'}],
                                                   'Status': 7}
#############################################################################
#Проверка кодов ответа
#############################################################################
class Test_response_code():
            def test_not_found_platform_in_profile_status_2_and_7(resource_setup):
                assert not_found_platform_in_profile() == {'Description': 'Some updates have failed',
                                                            'Result': [{'Description': 'No information in profile','Status': 2,'platform': 'MT4_INSTANT_DEMO'}],
                                                            'Status': 7}

            def test_wrong_request_status_3(resource_setup):
                assert wrong_request_changeprofile() == {'Description': 'invalid uri', 'Status': 3}

            def test_no_body_request_status_4(resource_setup):
                assert no_body_in_the_request_changeprofile() == {'Description': "can't find 'tradingProfile' param", 'Status': 4}

            def test_request_without_name_and_platform_status_4(resource_setup):
                assert request_without_name_and_platform() == {'Description': "can't find 'name' param", 'Status': 4}

            def test_request_without_name_status_4(resource_setup):
                assert request_without_name_for_profile() == {'Description': "can't find 'name' param", 'Status': 4}

            def test_value_to_name_not_str_status_5(resource_setup):
                assert value_to_name_not_str() == {'Description': "'name' param not a string", 'Status': 5}

            def test_no_value_to_name_status_5(resource_setup):
                assert no_value_to_name() == {'Description': "can't find profile ''", 'Status': 5}

            def test_not_found_profile_for_name_value_status_5(resource_setup):
                assert not_found_profile_for_name_value() == {'Description': "can't find profile 'for test'", 'Status': 5}

            def test_no_valid_json_2_status_5(resource_setup):
                assert no_valid_json_2() == {'Description': 'invalid json', 'Status': 5}

            def test_value_to_platforms_not_str_status_5(resource_setup):
                assert value_to_platforms_not_str() == {'Description': 'platform element not string', 'Status': 5}

            def test_no_connection_with_server_status_6_and_7(resource_setup):
                assert no_connection_with_server() == {'Description': 'Some updates have failed',
                                                       'Result': [{'Description': 'No connection', 'Status': 6, 'platform': 'MT4_TEST'}],
                                                       'Status': 7}

            def test_value_to_platforms_two_servers_one_no_connection_status_6_and_7(resource_setup):
                assert value_to_platforms_two_servers_one_no_connection() == {'Description': 'Some updates have failed',
                                                                              'Result': [{'Description': 'Done', 'Status': 0, 'platform': 'MT4_INSTANT_REAL1'},
                                                                                         {'Description': 'No connection', 'Status': 6, 'platform': 'MT4_TEST'}],
                                                                              'Status': 7}

#############################################################################
#Проверка запроса Reload
#############################################################################

class Test_ReloadProfiles():
    def test_true_reload(self):
        assert true_reload() == {'Description': 'Done', 'Status': 0}
    def test_false_reload(self):
        assert false_reload() == {'Description': 'invalid uri', 'Status': 3}

#############################################################################
#Check invalid json
#############################################################################

class Test_valid_json():
    def test_no_valid_json_1(resource_setup):
        assert no_valid_json_1() == {'Description': 'in Json::Value::find(key, end, found): requires objectValue or nullValue','Status': 1}
    def test_no_valid_json_2(resource_setup):
        assert no_valid_json_2() == {'Description': 'invalid json', 'Status': 5}

class change_profile_for_all_server():
    def test_all_crisis(resource_setup):
        finres = All_Crisis()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL1'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL2'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL2'}],
                             'Status': 0}

        assert finres[1] == ['3', '3', '3', '3', '3', '5', '5', '5', '5', '5', '5', '3', '3', '4', '4', '3', '3', '5', '3', '3', '4']
        assert finres[2] == ['3', '3', '3', '3', '3', '5', '5', '5', '5', '5', '5', '3', '3', '4', '4', '3', '3', '5', '3', '3', '4']
        assert finres[3] == ['3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '3', '3', '3', '3', '3', '3', '3', '4']
        assert finres[4] == ['3', '3', '3', '3', '3', '3', '3', '3', '3', '4', '4', '3', '3', '3', '3', '3', '3', '3', '4']

    def test_all_default(resource_setup):
        finres = All_Default()
        assert finres[0] == {'Description': 'Done',
                             'Result': [{'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL1'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_INSTANT_REAL2'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL'},
                                        {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL2'}],
                             'Status': 0}

        assert finres[1] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[2] == ['2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2']
        assert finres[3] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']
        assert finres[4] == ['2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '3', '2', '2', '2', '2', '4']


class Test_request_ChangeServerSettings():
    def test_wrong_request_change_settings(self):
        assert wrong_request_change_settings() == {'Description': 'invalid uri', 'Status': 3}

    def test_no_body_request(resource_setup):
        assert no_body_request_change_settings() == {"Description":"Done",
                                                     "Result":[{"Description":"Done","Status":0,"platform":"MT4_INSTANT_DEMO"},
                                                               {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL1"},
                                                               {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL2"},
                                                               {"Description":"Done","Status":0,"platform":"MT4_MARKET_DEMO"},
                                                               {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"},
                                                               {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL2"}],
                                                     "Status":0}

    def test_without_symbol(resource_setup):
        assert without_symbol() == {"Description":"Symbols element not contain 'symbol' element","Status":4}

    def test_symbol_not_found(resource_setup):
        assert symbol_not_found() == {"Description":"Some updates have failed",
                                      "Result":[{"Description":" failed to get symbol info 'Test'","Status":7,"platform":"MT4_MARKET_REAL"}],
                                      "Status":7}

    def test_invalid_value_for_symbol_trade(resource_setup):
        assert invalid_value_for_symbol_trade() == {"Description":"Invalid value for symbol trade.","Status":5}

    def test_server_not_found(resource_setup):
        assert server_not_found() == {"Description":"Some updates have failed",
                                      "Result":[{"Description":"No information in config","Status":2,"platform":"MT4_MARKET_REAL_TEST"}],
                                      "Status":7}

    def test_trade_close(resource_setup):
        assert trade_full() == {"Description":"Done","Result":[{"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"}],"Status":0}

    def test_trade_no(resource_setup):
        assert trade_full() == {"Description":"Done","Result":[{"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"}],"Status":0}

    def test_trade_full(resource_setup):
        assert trade_full() == {"Description":"Done","Result":[{"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"}],"Status":0}

    def test_success_one_server(resource_setup):
        assert success_one_server() == {"Description":"Done","Result":[{"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"}],"Status":0}

    def test_success_two_server(resource_setup):
        assert success_two_server() == {"Description":"Done",
                                        "Result":[{"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL1"},
                                                  {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"}],
                                        "Status":0}

    def test_success_one_server_fail_one(resource_setup):
        assert success_one_server_fail_one() == {'Description': 'Some updates have failed',
                                                 'Result': [{'Description': 'No information in config','Status': 2,'platform': 'MT4_INSTANT_TEST'},
                                                            {'Description': 'Done','Status': 0,'platform': 'MT4_MARKET_REAL'}],
                                                 'Status': 7}

    def test_request_changesettings_without_platform(resource_setup):
        assert request_changesettings_without_platform() == {"Description":"Done",
                                                             "Result":[{"Description":"Done","Status":0,"platform":"MT4_INSTANT_DEMO"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL1"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL2"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_DEMO"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL2"}],
                                                             "Status":0}


    def test_request_changesettings_two_symbols(resource_setup):
        assert request_changesettings_two_symbols() == {"Description":"Done",
                                                             "Result":[{"Description":"Done","Status":0,"platform":"MT4_INSTANT_DEMO"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL1"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_INSTANT_REAL2"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_DEMO"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL"},
                                                                       {"Description":"Done","Status":0,"platform":"MT4_MARKET_REAL2"}],
                                                             "Status":0}