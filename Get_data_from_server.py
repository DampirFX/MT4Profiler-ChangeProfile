from MT4ManagerAPI import *

def Get_data_from_server(server):
    Man = CreateManagerInterface()
    Connect(Man, server)
    Login(Man, 61, "Ghtdtl71")
    result = GetPluginParameterValue(Man,'Delay (1-10 sec, 0 - disable)')
    return(result)
    del Man

