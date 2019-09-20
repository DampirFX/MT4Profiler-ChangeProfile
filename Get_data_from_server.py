import MT4ManagerAPI

def Get_data_from_server(server):
    Man = MT4ManagerAPI.CreateManagerInterface()
    MT4ManagerAPI.Connect(Man, server)
    MT4ManagerAPI.Login(Man, 61, "Ghtdtl71")
    result = MT4ManagerAPI.GetPluginParameterValue(Man,'Delay (1-10 sec, 0 - disable)')
    return(result)
    del Man

