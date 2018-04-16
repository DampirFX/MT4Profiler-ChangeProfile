from ctypes import *
from ctypes.wintypes import *
from enum import *
import time
import sys

# +------------------------------------------------------------------+
# |                        API Version                               |
# +------------------------------------------------------------------+


ManAPIProgramVersion = 400
ManAPIProgramBuild = 1045
ManAPIVersion =[ManAPIProgramBuild,ManAPIProgramVersion]

# +------------------------------------------------------------------+
# |                   Server Configurations                          |
# +------------------------------------------------------------------+
# | Configuration types                                              |
# +------------------------------------------------------------------+


class configuration_types(Enum):
    CONFIG_ALL = 0
    CONFIG_COMMON = 1
    CONFIG_ACCESS = 2
    CONFIG_SERVERS = 3
    CONFIG_TIME = 4
    CONFIG_HOLIDAYS = 5
    CONFIG_SYMBOLS = 6
    CONFIG_SYMB_GROUPS = 7
    CONFIG_GROUPS = 8
    CONFIG_MANAGERS = 9
    CONFIG_DATAFEEDS = 10
    CONFIG_BACKUP = 11
    CONFIG_LIVEUPDATE = 12
    CONFIG_SYNC = 13
    CONFIG_PLUGINS = 14
    CONFIG_GATEWAY_ACCOUNTS = 15
    CONFIG_GATEWAY_MARKUPS = 16
    CONFIG_GATEWAY_RULES = 17
    CONFIG_END = 255

# +------------------------------------------------------------------+
# | Configuration structures                                         |
# +------------------------------------------------------------------+
# | Common configuration                                             |
# +------------------------------------------------------------------+


class ConCommon(Structure):
    _fields_ = [
        ("owner", c_char * 128),
        ("name", c_char * 32),
        ("address", c_ulong),
        ("port", c_int),
        ("timeout", c_uint),
        ("typeofdemo", c_int),
        ("timeofdemo", c_int),
        ("daylightcorrection", c_int),
        ("internal", c_char * 60),
        ("timezone_real", c_int),
        ("timezone", c_int),
        ("timesync", c_char * 64),
        ("minclient", c_int),
        ("minapi", c_int),
        ("feeder_timeout", c_uint),
        ("keepemails", c_int),
        ("endhour", c_int),
        ("endminute", c_int),
        ("optimization_time", c_int),
        ("optimization_lasttime", c_int),
        ("optimization_counter", c_int),
        ("optimization_unused", c_int * 8),
        ("antiflood", c_int),
        ("floodcontrol", c_int),
        ("liveupdate_mode", c_int),
        ("lastorder", c_int),
        ("lastlogin", c_int),
        ("lostlogin", c_int),
        ("rollovers_mode", c_int),
        ("path_database", c_char * 256),
        ("path_history", c_char * 256),
        ("path_log", c_char * 256),
        ("overnight_last_day", c_uint),
        ("overnight_last_time", c_uint),
        ("overnight_prev_time", c_uint),
        ("overmonth_last_month", c_uint),
        ("adapters", c_char * 256),
        ("bind_adresses", c_ulong * 8),
        ("server_version", c_short),
        ("server_build", c_short),
        ("web_adresses", c_ulong * 8),
        ("statement_mode", c_int),
        ("monthly_state_mode", c_int),
        ("keepticks", c_int),
        ("statement_weekend", c_int),
        ("last_activate", c_uint),
        ("stop_last", c_uint),
        ("stop_delay", c_int),
        ("stop_reason", c_int),
        ("account_url", c_char * 128),
        ("reserved", c_int * 16)]

# --- demo-accounts type


class demo_account_type(Enum):
    DEMO_DISABLED = 0
    DEMO_PROLONG = 1
    DEMO_FIXED = 2

# --- rollover mode


class rollover_mode(Enum):
    ROLLOVER_NORMAL = 0
    ROLLOVER_REOPEN_BY_CLOSE_PRICE = 1
    ROLLOVER_REOPEN_BY_BID = 2

# --- LiveUpdate mode


class live_update_mode(Enum):
    LIVE_UPDATE_NO = 0
    LIVE_UPDATE_RELEASE = 1
    LIVE_UPDATE_NO_SERVER = 2
    LIVE_UPDATE_BETA = 3

# --- statement mode


class statement_mode(Enum):
    STATEMENT_END_DAY = 0
    STATEMENT_START_DAY = 1

# --- monthly statement mode


class monthly_statement_mode(Enum):
    MONTHLY_STATEMENT_END_MONTH = 0
    MONTHLY_STATEMENT_START_MONTH = 1

#--- server stop reason


class server_stop_reason(Enum):
    STOP_REASON_NONE = 0
    STOP_REASON_RESTART = 1
    STOP_REASON_SHUTDOWN = 2
    STOP_REASON_LIVEUPDATE = 3

# +------------------------------------------------------------------+
# | Access configuration                                             |
# +------------------------------------------------------------------+


class ConAccess(Structure):
    _fields_ = [("action", c_int),
                ("from", c_ulong),
                ("to", c_ulong),
                ("comment", c_char * 64),
                ("reserved", c_int * 17)]

# --- access action


class access_action(Enum):
    FW_BLOCK = 0
    FW_PERMIT = 1

# +------------------------------------------------------------------+
# | Data Servers configuration                                       |
# +------------------------------------------------------------------+


class ConDataServer(Structure):
    _fields_ = [
        ("server", c_char * 64),
        ("ip", c_ulong),
        ("description", c_char * 64),
        ("isproxy", c_int),
        ("priority", c_int),
        ("loading", c_uint),
        ("ip_internal", c_ulong),
        ("reserved", c_char * 2),
        ("next", c_uint64)
        ]

# +------------------------------------------------------------------+
# | Time configuration                                               |
# +------------------------------------------------------------------+


class ConTime(Structure):
    _fields_ = [
        ("days", POINTER(c_int) * 7),                        # может завалиться нужен массив скорее всего
        ("dayscontrol", c_int),
        ("reserved", POINTER(c_int) * 3)]

# +------------------------------------------------------------------+
# | Backup configuration                                             |
# +------------------------------------------------------------------+


class ConBackup(Structure):
    _fields_ = [
        ("fullbackup_path", POINTER(c_char) * 256),
        ("fullbackup_period", c_int),
        ("fullbackup_store", c_int),
        ("fullbackup_lasttime", c_uint),
        ("fullbackup_shift", c_short),
        ("external_path", POINTER(c_char) * 256),
        ("archive_period", c_int),
        ("archive_store", c_int),
        ("archive_lasttime", c_uint),
        ("export_securities", POINTER(c_char) * 512),
        ("export_path", POINTER(c_char) * 256),
        ("export_period", c_int),
        ("export_lasttime", c_uint),
        ("watch_role", c_int),
        ("watch_password", POINTER(c_char) * 16),
        ("watch_opposite", POINTER(c_char) * 24),
        ("watch_ip", c_int),
        ("archive_shift", c_char),
        ("watch_state", c_char),
        ("watch_failover", c_char),
        ("watch_timeout", c_char),
        ("watch_login", c_int),
        ("watch_timestamp", c_uint)
    ]

# --- server role


class server_role(Enum):
    WATCH_STAND_ALONE = 0
    WATCH_MASTER = 1
    WATCH_SLAVE = 2

# --- full backup execution periods: 1 hour, 4 hours, 1 day


class full_backup_execution_periods(Enum):
    BACKUP_1HOUR = 0
    BACKUP_4HOURS = 1
    BACKUP_1DAY =2

# --- full backup store period: 1 month, 3 months, 6 months, 1 year


class full_backup_store_periods(Enum):
    BU_STORE_1MONTH = 0
    BU_STORE_3MONTHS = 1
    BU_STORE_6MONTHS = 2
    BU_STORE_1YEAR = 3

# --- arc. backup execution periods: 5 min, 15 min, 30 min, 1 hour


class arc_backup_execution_periods(Enum):
    ARC_BACKUP_DISABLED = 0
    ARC_BACKUP_5MIN = 1
    ARC_BACKUP_15MIN = 2
    ARC_BACKUP_30MIN = 3
    ARC_BACKUP_1HOUR = 4

# --- arc. backup store period: 1 day, 3 days, 1 week, 2 weeks, 1 month,3 months, 6 months,1 year


class arc_backup_store_periods(Enum):
    ARC_STORE_1DAY = 0
    ARC_STORE_3DAYS = 1
    ARC_STORE_1WEEK = 2
    ARC_STORE_2WEEKS = 3
    ARC_STORE_1MONTH = 4
    ARC_STORE_3MONTH = 5
    ARC_STORE_6MONTH = 6

# --- export execution period: 1 min, 5 min, 15 min, 30 min, 1 hour


class export_execution_period(Enum):
    EXPORT_1MIN = 0
    EXPORT_5MIN = 1
    EXPORT_15MIN = 2
    EXPORT_30MIN = 3
    EXPORT_1HOUR = 4

# --- watchdog state


class watchdog_state(Enum):
    WS_DISCONNECTED = 0
    WS_SYNCHRONIZING = 1
    WS_SYNCHRONIZED = 2

# --- watchdog failover mode


class watchdog_failover_mode(Enum):
    FAILOVER_OFF = 0
    FAILOVER_MOST = 1
    FAILOVER_FULL = 2

# +------------------------------------------------------------------+
# | Datafeed configuration                                           |
# +------------------------------------------------------------------+


class ConFeeder(Structure):
    _fields_ = [("name", POINTER(c_char) * 64),
                ("file", POINTER(c_char) * 256),
                ("server", POINTER(c_char) * 64),
                ("login", POINTER(c_char) * 32),
                ("pass", POINTER(c_char) * 32),
                ("keywords", POINTER(c_char) * 256),
                ("enable", c_int),
                ("mode", c_int),
                ("timeout", c_int),
                ("timeout_reconnect", c_int),
                ("timeout_sleep", c_int),
                ("attemps_sleep", c_int),
                ("news_langid", c_int),
                ("unused", POINTER(c_int) * 33)
                ]

# --- datafeed modes-receive quotes, receive news, receive quotes and news


class datafeed_modes(Enum):
    FEED_QUOTES = 0
    FEED_NEWS = 1
    FEED_QUOTESNEWS = 2
# +------------------------------------------------------------------+
# | Security group configuration for client group                    |
# +------------------------------------------------------------------+
MAX_SEC_GROUPS = (32)
MAX_SEC_GROPS_MARGIN = (128)


class ConGroupSec(Structure):
    _fields_ = [("show", c_int),
                ("trade", c_int),
                ("execution", c_int),
                ("comm_base", c_double),
                ("comm_type", c_int),
                ("comm_lots", c_int),
                ("comm_agent", c_double),
                ("comm_agent_type", c_int),
                ("spread_diff", c_int),
                ("lot_min", c_int),
                ("lot_max", c_int),
                ("lot_step", c_int),
                ("ie_deviation", c_int),
                ("confirmation", c_int),
                ("trade_rights", c_int),
                ("ie_quick_mode", c_int),
                ("autocloseout_mode", c_int),
                ("comm_tax", c_double),
                ("comm_agent_lots", c_int),
                ("freemargin_mode", c_int),
                ("reserved", POINTER(c_int) * 3)]

# +------------------------------------------------------------------+
# | Special securities configurations for client group               |
# +------------------------------------------------------------------+


class ConGroupMargin(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("swap_long", c_double),
                ("swap_short", c_double),
                ("margin_divider", c_double),
                ("reserved", POINTER(c_int) * 7)]

# --- dealing mode


class dealing_mode(Enum):
    EXECUTION_MANUAL = 0
    EXECUTION_AUTO = 1
    EXECUTION_ACTIVITY = 2

# --- commission type


class commision_type(Enum):
    COMM_TYPE_MONEY = 0
    COMM_TYPE_PIPS = 1
    COMM_TYPE_PERCENT = 2

# --- comission lots mode


class commision_lots_mode(Enum):
    COMMISSION_PER_LOT = 0
    COMMISSION_PER_DEAL = 1

# --- clients trade rights


class clients_trade_rights(Enum):
    TRADE_DENY_NONE = 0
    TRADE_DENY_CLOSEBY = 1
    TRADE_DENY_MUCLOSEBY = 2

# --- auto close-out method


class auto_close_out_method(Enum):
    CLOSE_OUT_NONE = 0
    CLOSE_OUT_HIHI = 1
    CLOSE_OUT_LOLO = 2
    CLOSE_OUT_HILO = 3
    CLOSE_OUT_LOHI = 4
    CLOSE_OUT_FIFO = 5
    CLOSE_OUT_LIFO = 6
    CLOSE_OUT_INTRDAY_FIFO = 7

# +------------------------------------------------------------------+
# | Client group configuration                                       |
# +------------------------------------------------------------------+


class ConGroup(Structure):
    _fields_ = [("group", POINTER(c_char) * 16),
                ("enable", c_int),
                ("timeout", c_int),
                ("otp_mode", c_int),
                ("company", POINTER(c_char) * 128),
                ("signature", POINTER(c_char) * 128),
                ("support_page", POINTER(c_char) * 128),
                ("smtp_server", POINTER(c_char) * 64),
                ("smtp_login", POINTER(c_char) * 32),
                ("smtp_password", POINTER(c_char) * 32),
                ("support_email", POINTER(c_char) * 64),
                ("templates", POINTER(c_char) * 32),
                ("copies", c_int),
                ("reports", c_int),
                ("default_leverage", c_int),
                ("default_deposit", c_double),
                ("maxsecurities", c_int),
                ("secgroups", POINTER(ConGroupSec) * MAX_SEC_GROUPS),
                ("secmargins", POINTER(ConGroupMargin) * MAX_SEC_GROPS_MARGIN),
                ("secmargins_total", c_int),
                ("currency", POINTER(c_char) * 12),
                ("credit", c_double),
                ("margin_call", c_int),
                ("margin_mode", c_int),
                ("margin_stopout", c_int),
                ("interestrate", c_double),
                ("use_swap", c_int),
                ("news", c_int),
                ("rights", c_int),
                ("check_ie_prices", c_int),
                ("maxpositions", c_int),
                ("close_reopen", c_int),
                ("hedge_prohibited", c_int),
                ("close_fifo", c_int),
                ("hedge_largeleg", c_int),
                ("unused_rights", POINTER(c_int) * 2),
                ("securities_hash", POINTER(c_char) * 16),
                ("margin_type", c_int),
                ("archive_period", c_int),
                ("archive_max_balance", c_int),
                ("stopout_skip_hedged", c_int),
                ("archive_pending_period", c_int),
                ("news_languages", POINTER(c_uint) * 8),
                ("news_languages_total", c_uint),
                ("reserved", POINTER(c_int) * 17)]

# --- margin calculation mode


class margin_calculation_mode(Enum):
    MARGIN_MODE_DONT_USE = 0
    MARGIN_MODE_USE_ALL = 1
    MARGIN_MODE_USE_PROFIT = 2
    MARGIN_MODE_USE_LOSS = 3

# --- margin controlling type


class margin_controlling_type(Enum):
    MARGIN_TYPE_PERCENT = 0
    MARGIN_TYPE_CURRENCY = 1

# --- news mode-no news, only topics, full news (topic+body)


class news_mode(Enum):
    NEWS_NO = 0
    NEWS_TOPICS = 1
    NEWS_FULL = 2

# --- group rights


class group_rights(Enum):
    ALLOW_FLAG_EMAIL = 1
    ALLOW_FLAG_TRAILING = 2
    ALLOW_FLAG_ADVISOR = 4
    ALLOW_FLAG_EXPIRATION = 8
    ALLOW_FLAG_SIGNALS_ALL = 16
    ALLOW_FLAG_SIGNALS_OWN = 32
    ALLOW_FLAG_RISK_WARNING = 64
    ALLOW_FLAG_FORCED_OTP_USAGE = 128

# --- group one-time password mode


class group_one_time_password_mode(Enum):
    OTP_MODE_DISABLED = 0
    OTP_MODE_TOTP_SHA256 = 1

# +------------------------------------------------------------------+
# | Hollidays configuration                                          |
# +------------------------------------------------------------------+


class ConHoliday(Structure):
    _fields_ = [("year", c_int),
                ("month", c_int),
                ("day", c_int),
                ("from", c_int),
                ("to", c_int),
                ("symbol", POINTER(c_char) * 32),
                ("description", POINTER(c_char) * 128),
                ("enable", c_int),
                ("reserved", POINTER(c_int) * 13),
                ("next", c_uint64)
                 ]

# +------------------------------------------------------------------+
# | LiveUpdate configuration                                         |
# +------------------------------------------------------------------+
LIVE_FILES_MAX = (128)


class LiveInfoFile(Structure):
    _fields_ = [("file", POINTER(c_char) * 256),
                ("size", c_int),
                ("hash", POINTER(c_char) * 36),
                ("reserved", POINTER(c_int) * 10)]


class ConLiveUpdate(Structure):
    _fields_ = [("company", POINTER(c_char) * 128),
                ("path", POINTER(c_char) * 256),
                ("version", c_int),
                ("build", c_int),
                ("maxconnect", c_int),
                ("connections", c_int),
                ("type", c_int),
                ("enable", c_int),
                ("totalfiles", c_int),
                ("files", POINTER(LiveInfoFile) * LIVE_FILES_MAX),
                ("reserved", POINTER(c_int) * 16),
                ("next", c_uint64)
                ]

# --- LiveUpdate type


class LiveUpdate_type(Enum):
    LIVE_UPDATE_CLIENT = 0
    LIVE_UPDATE_MANAGER = 1
    LIVE_UPDATE_ADMIN = 2
    LIVE_UPDATE_DATACENTER = 3
    LIVE_UPDATE_CLIENT_PPC2002 = 4
    LIVE_UPDATE_CLIENT_PPC2003 = 5
    LIVE_UPDATE_MULTI = 6
    LIVE_UPDATE_WD = 7
    LIVE_UPDATE_CLIENT_PHONE = 8
    LIVE_UPDATE_LAST = 9

# +------------------------------------------------------------------+
# | Manager rights for security groups                               |
# +------------------------------------------------------------------+


class ConManagerSec(Structure):
    _fields_ = [("internal", c_int),
                ("enable", c_int),
                ("minimum_lots", c_int),
                ("maximum_lots", c_int),
                ("unused", POINTER(c_int) * 16)
                ]

# +------------------------------------------------------------------+
# | Manager configuration                                            |
# +------------------------------------------------------------------+


class ConManager(Structure):
    _fields_ = [("login", c_int),
                ("manager", c_int),
                ("money", c_int),
                ("online", c_int),
                ("riskman", c_int),
                ("broker", c_int),
                ("admin", c_int),
                ("logs", c_int),
                ("reports", c_int),
                ("trades", c_int),
                ("market_watch", c_int),
                ("email", c_int),
                ("user_details", c_int),
                ("see_trades", c_int),
                ("news", c_int),
                ("plugins", c_int),
                ("server_reports", c_int),
                ("techsupport", c_int),
                ("market", c_int),
                ("notifications", c_int),
                ("unused", POINTER(c_int) * 9),
                ("ipfilter", c_int),
                ("ip_from", c_ulong),
                ("ip_to", c_ulong),
                ("mailbox", POINTER(c_char) * 64),
                ("groups", POINTER(c_char) * 1024),
                ("secgroups", POINTER(ConManagerSec) * MAX_SEC_GROUPS),
                ("exp_time", c_uint),
                ("name", POINTER(c_char) * 32),
                ("info_depth", c_int),
                ("reserved", POINTER(c_int) * 22)]

# +------------------------------------------------------------------+
# | Symbol configurations                                            |
# +------------------------------------------------------------------+
# | Symbol sessions configurations                                   |
# +------------------------------------------------------------------+


class ConSession(Structure):            #32 байта
    _fields_ = [("open_hour", c_short),
                ("open_min", c_short),
                ("close_hour", c_short),
                ("close_min", c_short),
                ("open", c_int),
                ("close", c_int),
                ("align", c_short * 7)]


class ConSessions(Structure):
    _fields_ = [("quote", ConSession * 3),
                ("trade", ConSession * 3),
                ("quote_overnight", c_int),
                ("trade_overnight", c_int),
                ("reserved", c_int * 2)]


# +------------------------------------------------------------------+
# | Symbol configuration                                             |
# +------------------------------------------------------------------+

MAX_SYMBOLS  = 1024


class ConSymbol(Structure):
    _fields_ = [# //--- общие настройки
                ("symbol", c_char * 12),
                ("description", c_char * 64),
                ("source", c_char * 12),
                ("currency", c_char * 12),
                ("type", c_int),
                ("digits", c_int),
                ("trade", c_int),
        # //--- параметры представления
                ("background_color", c_uint),
                ("count", c_int),
                ("count_original", c_int),
                ("external_unused", c_int * 7),
        # //--- сессии
                ("realtime", c_int),
                ("starting", c_uint),
                ("expiration", c_uint),
                ("sessions", ConSessions * 7),
        # //--- расчет прибыли
                ("profit_mode", c_int),
                ("profit_reserved", c_int),
        # //--- фильтрация котировок
                ("filter", c_int),
                ("filter_counter", INT),
                ("filter_limit", c_double),
                ("filter_smoothing", c_int),
                ("filter_reserved", c_float),
                ("logging", c_int),
        # //--- спреды и свопы
                ("spread", c_int),
                ("spread_balance", c_int),
                ("exemode", c_int),
                ("swap_enable", c_int),
                ("swap_type", c_int),
                ("swap_long", c_double),
                ("swap_short", c_double),
                ("swap_rollover3days", c_int),
                ("contract_size", c_double),
                ("tick_value", c_double),
                ("tick_size", c_double),
                ("stops_level", c_int),
                ("gtc_pendings", c_int),
        # //--- расчет маржи
                ("margin_mode", c_int),
                ("margin_initial", c_double),
                ("margin_maintenance", c_double),
                ("margin_hedged", c_double),
                ("margin_divider", c_double),
        # //--- расчетные данные (для внутреннего использования)
                ("point", c_double),
                ("multiply", c_double),
                ("bid_tickvalue", c_double),
                ("ask_tickvalue", c_double),
        # //---
                ("long_only", c_int),
                ("instant_max_volume", c_int),
        # //---
                ("margin_currency", c_char * 12),
                ("freeze_level", c_int),
                ("margin_hedged_strong", c_int),
                ("value_date", c_uint),
                ("quotes_delay", c_int),
                ("swap_openprice", c_int),
                ("swap_variation_margin", c_int),
        # //---
                ("unused", c_int * 21)]


# +------------------------------------------------------------------+
# | Symbols enumeration                                              |
# +------------------------------------------------------------------+
# --- symbol execution mode


class symbol_execution_mode(Enum):
    EXE_REQUEST = 0
    EXE_INSTANT = 1
    EXE_MARKET = 2

# --- trade mode


class trade_mode(Enum):
    TRADE_NO = 0
    TRADE_CLOSE = 1
    TRADE_FULL = 2

# --- swap type


class swap_type(Enum):
    SWAP_BY_POINTS = 0
    SWAP_BY_DOLLARS = 1
    SWAP_BY_INTEREST = 2
    SWAP_BY_MARGIN_CURRENCY = 3

# --- profit calculation mode


class profit_calculation_mode(Enum):
    PROFIT_CALC_FOREX = 0
    PROFIT_CALC_CFD = 1
    PROFIT_CALC_FUTURES = 2

# --- margin calculation mode


class margin_calculation_mode(Enum):
    MARGIN_CALC_FOREX = 0
    MARGIN_CALC_CFD = 1
    MARGIN_CALC_FUTURES = 2
    MARGIN_CALC_CFDINDEX = 3
    MARGIN_CALC_CFDLEVERAGE = 4

# --- GTC mode


class gtc_mode(Enum):
    ORDERS_DAILY = 0
    ORDERS_GTC = 1
    ORDERS_DAILY_NO_STOPS = 2

# +------------------------------------------------------------------+
# | Symbol groups                                                    |
# +------------------------------------------------------------------+
MAX_SEC_GROUP = (32)


class ConSymbolGroup(Structure):
    _fields_ = [("name", POINTER(c_char) * 16),
                ("description", POINTER(c_char) * 64)
                ]

# +------------------------------------------------------------------+
# | Synchronization configuration                                    |
# +------------------------------------------------------------------+


class ConSync(Structure):
    _fields_ = [("server", POINTER(c_char) * 64),
                ("unusedport", c_int),
                ("login", POINTER(c_char) * 32),
                ("password", POINTER(c_char) * 32),
                ("enable", c_int),
                ("mode", c_int),
                ("from", c_uint),
                ("to", c_uint),
                ("securities", POINTER(c_char) * 1024),
                ("timecorrection", c_int),
                ("reserved", POINTER(c_int) * 13),
                ("next", c_uint64)]

# --- synchronization mode


class synchronization_mode(Enum):
    HB_ADD = 0
    HB_UPDATE = 1
    HB_INSERT = 2
    HB_DELETE = 3
    HB_LAST = 4

# +------------------------------------------------------------------+
# | Plugin configuration                                             |
# +------------------------------------------------------------------+
# | Plugin description                                               |
# +------------------------------------------------------------------+


class PluginInfo(Structure):
    _fields_ = [("name", c_char * 128),
                ("version", c_uint),
                ("copyright", c_char * 128),
                ("reserved", c_int * 32)]


class PluginCfg(Structure):
    _fields_ = [("name", c_char * 32),
                ("value", c_char * 128),
                ("reserved", c_int * 16)]


class ConPlugin(Structure):
    _fields_ = [("file", c_char * 256),
                ("info", PluginInfo),
                ("enabled", c_int),
                ("configurable", c_int),
                ("manager_access", c_int),
                ("reserved", c_int * 62)]

# --- plugin with parameters


class ConPluginParam(Structure):
    _fields_ = [("plugin", ConPlugin),
                ("params", POINTER(PluginCfg)),
                ("total", c_int)]
# +------------------------------------------------------------------+
# | Gateway configuration                                            |
# +------------------------------------------------------------------+
# +------------------------------------------------------------------+
# | Gateway account configuration                                    |
# +------------------------------------------------------------------+


class ConGatewayAccount(Structure):
    _fields_ = [("enable", c_int),
                ("name", POINTER(c_char) * 64),
                ("id", c_int),
                ("type", c_int),
                ("login", c_int),
                ("address", POINTER(c_char) * 64),
                ("password", POINTER(c_char) * 64),
                ("notify_logins", POINTER(c_int) * 8),
                ("flags", c_int),
                ("reserved", POINTER(c_int) * 23)]

# --- gateway account flags


class EnGatewayAccountFlags(Enum):
    GATEWAY_FLAG_NONE = 0
    GATEWAY_FLAG_QUOTES = 1

# +------------------------------------------------------------------+
# | Gateway markup configuration                                     |
# +------------------------------------------------------------------+


class ConGatewayMarkup(Structure):
    _fields_ = [("enable", c_int),
                ("source", POINTER(c_char) * 128),
                ("symbol", POINTER(c_char) * 12),
                ("account_name", POINTER(c_char) * 64),
                ("account_id", c_int),
                ("bid_markup", c_int),
                ("ask_markup", c_int),
                ("reserved", POINTER(c_int) * 16)]

# +------------------------------------------------------------------+
# | Gateway rules configuration                                     |
# +------------------------------------------------------------------+


class ConGatewayRule(Structure):
    _fields_ = [("enable", c_int),
                ("name", POINTER(c_char) * 64),
                ("request_symbol", POINTER(c_char) * 128),
                ("request_group", POINTER(c_char) * 128),
                ("request_reserved", POINTER(c_int) * 32),
                ("exe_account_name", POINTER(c_char) * 64),
                ("exe_account_id", c_int),
                ("exe_max_deviation", c_int),
                ("exe_max_profit_slippage", c_int),
                ("exe_max_profit_slippage_lots", c_int),
                ("exe_max_losing_slippage", c_int),
                ("exe_max_losing_slippage_lots", c_int),
                ("exe_account_pos", c_int),
                ("exe_volume_percent", c_int),
                ("exe_reserved", POINTER(c_int) * 26)
                ]

# +------------------------------------------------------------------+
# |                           Result codes                           |
# +------------------------------------------------------------------+


class result_code(Enum):
    RET_OK = 0
    RET_OK_NONE = 1
    RET_ERROR = 2
    RET_INVALID_DATA = 3
    RET_TECH_PROBLEM = 4
    RET_OLD_VERSION = 5
    RET_NO_CONNECT = 6
    RET_NOT_ENOUGH_RIGHTS = 7
    RET_TOO_FREQUENT = 8
    RET_MALFUNCTION = 9
    RET_GENERATE_KEY = 10
    RET_SECURITY_SESSION = 11
    RET_ACCOUNT_DISABLED = 64
    RET_BAD_ACCOUNT_INFO = 12                       # возможна нумерация продолжается с 65
    RET_PUBLIC_KEY_MISSING = 13
    RET_TRADE_TIMEOUT = 128
    RET_TRADE_BAD_PRICES = 14
    RET_TRADE_BAD_STOPS = 15
    RET_TRADE_BAD_VOLUME = 16
    RET_TRADE_MARKET_CLOSED = 17
    RET_TRADE_DISABLE = 18
    RET_TRADE_NO_MONEY = 19
    RET_TRADE_PRICE_CHANGED = 20
    RET_TRADE_OFFQUOTES = 21
    RET_TRADE_BROKER_BUSY = 22
    RET_TRADE_REQUOTE = 23
    RET_TRADE_ORDER_LOCKED = 24
    RET_TRADE_LONG_ONLY = 25
    RET_TRADE_TOO_MANY_REQ = 26
    RET_TRADE_ACCEPTED = 27
    RET_TRADE_PROCESS = 28
    RET_TRADE_USER_CANCEL = 29
    RET_TRADE_MODIFY_DENIED = 30
    RET_TRADE_CONTEXT_BUSY = 31
    RET_TRADE_EXPIRATION_DENIED = 32
    RET_TRADE_TOO_MANY_ORDERS = 33
    RET_TRADE_HEDGE_PROHIBITED = 34
    RET_TRADE_PROHIBITED_BY_FIFO = 35

# +------------------------------------------------------------------+
# | Pumping mode flags                                               |
# +------------------------------------------------------------------+


class pumping_mode_flags(Enum):
    CLIENT_FLAGS_HIDETICKS = 1
    CLIENT_FLAGS_HIDENEWS = 2
    CLIENT_FLAGS_HIDEMAIL = 4
    CLIENT_FLAGS_SENDFULLNEWS = 8
    CLIENT_FLAGS_RESERVED = 16
    CLIENT_FLAGS_HIDEONLINE = 32
    CLIENT_FLAGS_HIDEUSERS = 64

# +------------------------------------------------------------------+
# |  Server datafeed descritopn                                      |
# +------------------------------------------------------------------+


class FeedDescription(Structure):
    _fields_ = [("version", c_int),
                ("name", POINTER(c_char) * 128),
                ("copyright", POINTER(c_char) * 128),
                ("web", POINTER(c_char) * 128),
                ("email", POINTER(c_char) * 128),
                ("server", POINTER(c_char) * 128),
                ("username", POINTER(c_char) * 32),
                ("userpass", POINTER(c_char) * 32),
                ("modes", c_int),
                ("description", POINTER(c_char) * 512),
                ("module", POINTER(c_char) * 32),
                ("reserved", POINTER(c_int) * 54)]

# --- feeder modes


class FeederModes(Enum):
    modeOnlyQuotes = 0
    modeOnlyNews = 1
    modeQuotesAndNews = 2
    modeQuotesOrNews = 3

# --- server datafeed


class ServerFeed(Structure):
    _fields_ = [("file", POINTER(c_char) * 256),
                ("feed", FeedDescription)]

# +------------------------------------------------------------------+
# |                           Charts                                 |
# +------------------------------------------------------------------+
# | Request chart history struct                                     |
# +------------------------------------------------------------------+


class ChartInfo(Structure):
    _field_ = [("symbol", POINTER(c_char) * 12),
               ("period", c_int),
               ("start", c_uint),
               ("end", c_uint),
               ("timesign", c_uint),
               ("mode", c_int)]

# --- chart period


class chart_period(Enum):
    PERIOD_M1 = 1
    PERIOD_M5 = 5
    PERIOD_M15 = 15
    PERIOD_M30 = 30
    PERIOD_H1 = 60
    PERIOD_H4 = 240
    PERIOD_D1 = 1440
    PERIOD_W1 = 10080
    PERIOD_MN1 = 43200

# --- request mode


class request_mode(Enum):
    CHART_RANGE_IN = 0
    CHART_RANGE_OUT = 1
    CHART_RANGE_LAST = 2

# +------------------------------------------------------------------+
# | Rate the in chart base                                           |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class RateInfoOld(Structure):
    _fields_ = [("ctm", c_uint),
                ("open", c_int),
                ("high", c_short),
                ("low", c_short),
                ("close", c_short),
                ("vol", c_double)]


class RateInfo(Structure):
    _fields_ = [("ctm", c_uint),
                ("open", c_int),
                ("high", c_int),
                ("low", c_int),
                ("close", c_int),
                ("vol", c_double)]

# pragma pack(pop)
# +------------------------------------------------------------------+
# | Tick record in base                                              |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class TickRecord(Structure):
    _fields_ = [("ctm", c_uint),
                ("bid", c_double),
                ("ask", c_double),
                ("datafeed", c_int),
                ("flags", c_char)]

# pragma pack(pop)


class tick_flag(Enum):
    TICK_FLAG_RAW = 1
    TICK_FLAG_NORMAL = 2
    TICK_FLAG_ALL = TICK_FLAG_RAW + TICK_FLAG_NORMAL

# +------------------------------------------------------------------+
# | Tick request                                                     |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class TickRequest(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("from", c_uint),
                ("to", c_uint),
                ("flags", c_char)]

# pragma pack(pop)
# +------------------------------------------------------------------+
# | Performance information                                          |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class PerformanceInfo(Structure):
    _field_ = [("ctm", c_uint),
               ("users", c_short),
               ("cpu", c_short),
               ("freemem", c_int),
               ("network", c_int),
               ("sockets", c_int)]

# pragma pack(pop)
# +------------------------------------------------------------------+
# | Backup file information                                          |
# +------------------------------------------------------------------+


class BackupInfo(Structure):
    _fields_ = [("file", POINTER(c_char) * 256),
                ("size", c_int),
                ("time", c_uint),
                ("reserved", POINTER(c_int) * 6)]

# --- backup mode


class backup_mode(Enum):
    BACKUPS_ALL = 0
    BACKUPS_PERIODICAL = 1
    BACKUPS_STARTUP = 2
    BACKUPS_DELETE = 3

# +------------------------------------------------------------------+
# |                        Databases                                 |
# +------------------------------------------------------------------+
# | Transaction types                                                |
# +------------------------------------------------------------------+


class transaction_types(Enum):
    TRANS_ADD = 0
    TRANS_DELETE = 1
    TRANS_UPDATE = 2
    TRANS_CHANGE_GRP = 3

# +------------------------------------------------------------------+
# | User Record                                                      |
# +------------------------------------------------------------------+


PUBLIC_KEY_SIZE = 272
USER_COLOR_NONE = (0xFF000000)


class UserRecord(Structure):
    _fields_ = [("login", c_int),
                ("group", POINTER(c_char) * 16),
                ("password", POINTER(c_char) * 16),
                ("enable", c_int),
                ("enable_change_password", c_int),
                ("enable_read_only", c_int),
                ("enable_otp", c_int),
                ("enable_reserved", POINTER(c_int) * 2),
                ("password_investor", POINTER(c_char) * 16),
                ("password_phone", POINTER(c_char) * 32),
                ("name", POINTER(c_char) * 128),
                ("country", POINTER(c_char) * 32),
                ("city", POINTER(c_char) * 32),
                ("state", POINTER(c_char) * 32),
                ("zipcode", POINTER(c_char) * 16),
                ("address", POINTER(c_char) * 16),
                ("lead_source", POINTER(c_char) * 32),
                ("phone", POINTER(c_char) * 32),
                ("email", POINTER(c_char) * 48),
                ("comment", POINTER(c_char) * 64),
                ("id", POINTER(c_char) * 32),
                ("status", POINTER(c_char) * 16),
                ("regdate", c_uint),
                ("lastdate", c_uint),
                ("leverage", c_int),
                ("agent_account", c_int),
                ("timestamp", c_uint),
                ("last_ip", c_int),
                ("balance", c_double),
                ("prevmonthbalance", c_double),
                ("prevbalance", c_double),
                ("credit", c_double),
                ("interestrate", c_double),
                ("taxes", c_double),
                ("prevmonthequity", c_double),
                ("prevequity", c_double),
                ("reserved2", POINTER(c_double) * 2),
                ("otp_secret", POINTER(c_char) * 32),
                ("secure_reserved", POINTER(c_char) * 240),
                ("send_reports", c_int),
                ("mqid", c_uint),
                ("user_color", c_uint),              # исходный тип COLORREF может не взлететь
                ("unused", POINTER(c_char) * 40),
                ("api_data", POINTER(c_char) * 16)]

# +------------------------------------------------------------------+
# | Users group operation                                            |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class GroupCommandInfo(Structure):
    _fields_ = [("len", c_int),
                ("command", c_char),
                ("newgroup", POINTER(c_char) * 16),
                ("leverage", c_int),
                ("reserved", POINTER(c_int) * 8)]

# pragma pack(pop)

# --- group commands


class group_commands(Enum):
    GROUP_DELETE = 0
    GROUP_ENABLE = 1
    GROUP_DISABLE = 2
    GROUP_LEVERAGE = 3
    GROUP_SETGROUP = 4

# +------------------------------------------------------------------+
# | Online user description                                          |
# +------------------------------------------------------------------+


class OnlineRecord(Structure):
    _fields_ = [("counter", c_int),
                ("reserved", c_int),
                ("login", c_int),
                ("ip", c_uint),
                ("group", c_char * 16)]

# +------------------------------------------------------------------+
# | Trade Record                                                     |
# +------------------------------------------------------------------+
# pragma pack(push,1)


class TradeRecord(Structure):
    _fields_ = [("order", c_int),
                ("login", c_int),
                ("symbol", POINTER(c_char) * 12),
                ("digits", c_int),
                ("cmd", c_int),
                ("volume", c_int),
                ("open_time", c_uint),
                ("state", c_int),
                ("open_price", c_double),
                ("sl", c_double),
                ("tp", c_double),
                ("close_time", c_uint),
                ("gw_volume", c_int),
                ("expiration", c_uint),
                ("reason", c_char),
                ("conv_reserv", POINTER(c_char) * 3),
                ("conv_rates", POINTER(c_double) * 2),
                ("commission", c_double),
                ("commission_agent", c_double),
                ("storage", c_double),
                ("close_price", c_double),
                ("profit", c_double),
                ("taxes", c_double),
                ("magic", c_int),
                ("comment", POINTER(c_char) * 32),
                ("gw_order", c_int),
                ("activation", c_int),
                ("gw_open_price", c_short),
                ("gw_close_price", c_short),
                ("margin_rate", c_double),
                ("timestamp", c_uint),
                ("api_data", POINTER(c_int) * 4),
                ("next", c_uint64)         # исходный тип указатель на класс
                ]

# pragma pack(pop)
# --- trade commands


class trade_commands(Enum):
    OP_BUY = 0
    OP_SELL = 1
    OP_BUY_LIMIT = 2
    OP_SELL_LIMIT = 3
    OP_BUY_STOP = 4
    OP_SELL_STOP = 5
    OP_BALANCE = 6
    OP_CREDIT = 7

# --- trade record state


class trade_record_state(Enum):
    TS_OPEN_NORMAL = 0
    TS_OPEN_REMAND = 1
    TS_OPEN_RESTORED = 2
    TS_CLOSED_NORMAL = 3
    TS_CLOSED_PART = 4
    TS_CLOSED_BY = 5
    TS_DELETED = 6

# --- trade record reasons


class trade_record_reasons(Enum):
    TR_REASON_CLIENT = 0
    TR_REASON_EXPERT = 1
    TR_REASON_DEALER = 2
    TR_REASON_SIGNAL = 3
    TR_REASON_GATEWAY = 4
    TR_REASON_MOBILE = 5
    TR_REASON_WEB = 6
    TR_REASON_API = 7

# --- activation types
# --- *_ROLLBACK=current price roll back from activation price level


class activation_types(Enum):
    ACTIVATION_NONE = 0
    ACTIVATION_SL = 1
    ACTIVATION_TP = 2
    ACTIVATION_PENDING = 3
    ACTIVATION_STOPOUT = 4
    ACTIVATION_SL_ROLLBACK = -ACTIVATION_SL
    ACTIVATION_TP_ROLLBACK = -ACTIVATION_TP
    ACTIVATION_PENDING_ROLLBACK = -ACTIVATION_PENDING
    ACTIVATION_STOPOUT_ROLLBACK = -ACTIVATION_STOPOUT

# +------------------------------------------------------------------+
# | TradeRecord restoring from backup result                         |
# +------------------------------------------------------------------+

# pragma pack(push,1)


class TradeRestoreResult(Structure):
    _fields_ = [("order", c_int),
                ("res", c_char_p)]

# pragma pack(pop)

# +------------------------------------------------------------------+
# | Trade transaction                                                |
# +------------------------------------------------------------------+

# pragma pack(push,1)


class TradeTransInfo(Structure):
    _fields_ = [("type", c_char_p),
                ("flags", c_char),
                ("cmd", c_short),
                ("order", c_int),
                ("orderby", c_int),
                ("symbol", POINTER(c_char) * 12),
                ("volume", c_int),
                ("price", c_double),
                ("sl", c_double),
                ("tp", c_double),
                ("ie_deviation", c_int),
                ("comment", POINTER(c_char) * 32),
                ("expiration", c_uint),
                ("crc", c_int)]

# pragma pack(pop)

# --- trade transaction types


class trade_transaction_types(Enum):
    TT_PRICES_GET = 0
    TT_PRICES_REQUOTE = 1
    TT_ORDER_IE_OPEN = 64
    TT_ORDER_REQ_OPEN = 2
    TT_ORDER_MK_OPEN = 3
    TT_ORDER_PENDING_OPEN = 4
    TT_ORDER_IE_CLOSE = 5
    TT_ORDER_REQ_CLOSE = 6
    TT_ORDER_MK_CLOSE = 7
    TT_ORDER_MODIFY = 8
    TT_ORDER_DELETE = 9
    TT_ORDER_CLOSE_BY = 10
    TT_ORDER_CLOSE_ALL = 11
    TT_BR_ORDER_OPEN = 12
    TT_BR_ORDER_CLOSE = 13
    TT_BR_ORDER_DELETE = 14
    TT_BR_ORDER_CLOSE_BY = 15
    TT_BR_ORDER_CLOSE_ALL = 16
    TT_BR_ORDER_MODIFY = 17
    TT_BR_ORDER_ACTIVATE = 18
    TT_BR_ORDER_COMMENT = 19
    TT_BR_BALANCE = 20

# --- trade request flags


class EnReqFlags(Enum):
    TT_FLAG_NONE = 0x00000000
    TT_FLAG_SIGNAL = 0x00000001
    TT_FLAG_EXPERT = 0x00000002
    TT_FLAG_GATEWAY = 0x00000004
    TT_FLAG_MOBILE = 0x00000008
    TT_FLAG_WEB = 0x00000010
    TT_FLAG_API = 0x00000020

# +------------------------------------------------------------------+
# | Margin level of the user                                         |
# +------------------------------------------------------------------+


class MarginLevel(Structure):
    _fields_ = [("login", c_int),
                ("group", POINTER(c_char) * 16),
                ("leverage", c_int),
                ("updated", c_int),
                ("balance", c_double),
                ("equity", c_double),
                ("volume", c_int),
                ("margin", c_double),
                ("margin_free", c_double),
                ("margin_level", c_double),
                ("margin_type", c_int),
                ("level_type", c_int)]

# --- margin level type


class margin_level_type(Enum):
    MARGINLEVEL_OK = 0
    MARGINLEVEL_MARGINCALL = 1
    MARGINLEVEL_STOPOUT = 2

# +------------------------------------------------------------------+
# | Trade request                                                    |
# +------------------------------------------------------------------+


class RequestInfo(Structure):
    _fields_ = [("id", c_int),
                ("status", c_char),
                ("time", c_uint),
                ("manager", c_int),
                ("login", c_int),
                ("group", POINTER(c_char) * 16),
                ("balance", c_double),
                ("credit", c_double),
                ("prices", POINTER(c_double) * 2),
                ("trade", TradeTransInfo),
                ("gw_volume", c_int),
                ("gw_order", c_int),
                ("gw_price", c_short),
                ("prev", c_uint64),
                ("next", c_uint64)]

# --- trade request status


class trade_request_status(Enum):
    DC_EMPTY = 0
    DC_REQUEST = 1
    DC_LOCKED = 2
    DC_ANSWERED = 3
    DC_RESETED = 4
    DC_CANCELED = 5

# --- time conversion ratio
TIME_RATE = (1.6777216)
# --- conversion from our time to standard __time32_t
# define STDTIME(custom_time) ((DWORD)((double)(custom_time)*TIME_RATE))
# --- conversion from standard __time32_t to our time
# define OURTIME(stdtime)     ((DWORD)((double)(stdtime)/TIME_RATE))

# --- request confirmation modes


class EnConfirmModes(Enum):
    CONFIRM_MODE_ADD_PRICES = 0x00000001
    CONFIRM_MODE_PACKET = 0x00000002

# +------------------------------------------------------------------+
# | Daily report                                                     |
# +------------------------------------------------------------------+


class DailyReport(Structure):
    _fields_ = [("login", c_int),
                ("ctm", c_uint),
                ("group", POINTER(c_char) * 16),
                ("bank", POINTER(c_char) * 64),
                ("balance_prev", c_double),
                ("balance", c_double),
                ("deposit", c_double),
                ("credit", c_double),
                ("profit_closed", c_double),
                ("profit", c_double),
                ("equity", c_double),
                ("margin", c_double),
                ("margin_free", c_double),
                ("next", c_int),
                ("reserved", c_int)]

# +------------------------------------------------------------------+
# | Reports request                                                  |
# +------------------------------------------------------------------+

# pragma pack(push,1)


class ReportGroupRequest(Structure):
    _fields_ = [("name", POINTER(c_char) * 32),
                ("from", c_uint),
                ("to", c_uint),
                ("total", c_int)]

# pragma pack(pop)

# +------------------------------------------------------------------+
# | Daily reports request                                            |
# +------------------------------------------------------------------+


class DailyGroupRequest(Structure):
    _fields_ = [("name", POINTER(c_char) * 32),
                ("from", c_uint),
                ("to", c_uint),
                ("total", c_int),
                ("reserved", c_int)]

# +------------------------------------------------------------------+
# | Selected symbol information                                      |
# +------------------------------------------------------------------+


class SymbolInfo(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("digits", c_int),
                ("count", c_int),
                ("visible", c_int),
                ("type", c_int),
                ("point", c_double),
                ("spread", c_int),
                ("spread_balance", c_int),
                ("direction", c_int),
                ("updateflag", c_int),
                ("lasttime", c_uint),
                ("bid", c_double),
                ("ask", c_double),
                ("high", c_double),
                ("low", c_double),
                ("commission", c_double),
                ("comm_type", c_int)]

# --- symbol price direction


class symbol_price_direction(Enum):
    SDIR_UP = 0
    SDIR_DOWN = 1
    SDIR_NONE = 2

# +------------------------------------------------------------------+
# | Symbol summary                                                   |
# +------------------------------------------------------------------+


class SymbolSummary(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("count", c_int),
                ("digits", c_int),
                ("type", c_int),
                ("orders", c_int),
                ("buylots", c_int64),
                ("selllots", c_int64),
                ("buyprice", c_double),
                ("sellprice", c_double),
                ("profit", c_double),
                ("covorders", c_int),
                ("covbuylots", c_int64),
                ("covselllots", c_int64),
                ("covbuyprice", c_double),
                ("covsellprice", c_double),
                ("covprofit", c_double)]

# +------------------------------------------------------------------+
# | Currence exposure                                                |
# +------------------------------------------------------------------+


class ExposureValue(Structure):
    _fields_ = [("currency", POINTER(c_char) * 4),
                ("clients", c_double),
                ("coverage", c_double)]

# +------------------------------------------------------------------+
# | Symbol properties                                                |
# +------------------------------------------------------------------+

# pragma pack(push,1)


class SymbolPropertiesOld(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("color", c_uint),                   #COLORREF
                ("spread", c_int),
                ("spread_balance", c_int),
                ("stops_level", c_int),
                ("exemode", c_int)]

# pragma pack(pop)

# pragma pack(push,1)


class SymbolProperties(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("color", c_uint),                   #COLORREF
                ("spread", c_int),
                ("spread_balance", c_int),
                ("stops_level", c_int),
                ("smoothing", c_int),
                ("exemode", c_int),
                ("reserved", POINTER(c_int) * 8)]

# pragma pack(pop)
# +------------------------------------------------------------------+
# | Symbol tick                                                      |
# +------------------------------------------------------------------+


class TickInfo(Structure):
    _fields_ = [("symbol", POINTER(c_char) * 12),
                ("ctm", c_uint),
                ("bid", c_double),
                ("ask", c_double)]

# +------------------------------------------------------------------+
# | Mail                                                             |
# +------------------------------------------------------------------+


class MailBox(Structure):
    _fields_ = [("time", c_uint),
                ("sender", c_int),
                ("from", POINTER(c_char) * 64),
                ("to", c_int),
                ("subject", POINTER(c_char) * 128),
                ("readed", c_int),
                ("body", c_char),                               #char* __ptr32
                ("bodylen", c_int),
                ("build_min", c_short),
                ("build_max", c_short),
                ("reserved", c_int)]

# +------------------------------------------------------------------+
# | News topic                                                       |
# +------------------------------------------------------------------+


class NewsTopic(Structure):
    _fields_ = [("key", c_ulong),
                ("time", c_int),
                ("ctm", c_char),
                ("topic", c_char),
                ("category", c_char),
                ("keywords", c_char),
                ("body", c_char_p),                   #char* __ptr32
                ("bodylen", c_int),
                ("readed", c_int),
                ("priority", c_int),
                ("langid", c_int),
                ("reserved", POINTER(c_int) * 1)]

# +------------------------------------------------------------------+
# | Extended news structure                                          |
# +------------------------------------------------------------------+

# pragma pack(push,1)
# --- constants


class constant(Enum):
    MAX_NEWS_BODY_LEN = 15*1024*1024

# --- news topic flags


class EnNewsFlags(Enum):
    FLAG_PRIORITY = 1
    FLAG_CALENDAR = 2
    FLAG_MIME = 4
    FLAG_ALLOW_DEMO = 8


class NewsTopicNew(Structure):
    _fields_ = [
                #("constant", constant),
                #("EnNewsFlags", EnNewsFlags),
                ("key", c_ulong),
                ("language", c_uint),
                ("subject", POINTER(c_wchar_p) * 256),
                ("category", POINTER(c_wchar_p) * 256),
                ("flags", c_uint),
                ("body", c_wchar_p),                   #wchar_t* __ptr32
                ("body_len", c_uint),
                ("languages_list", POINTER(c_uint) * 32),
                ("datetime", c_int64),
                ("reserved", POINTER(c_uint) * 30)]

# pragma pack(pop)

# +------------------------------------------------------------------+
# | Server journal record                                            |
# +------------------------------------------------------------------+


class ServerLog(Structure):
    _fields_ = [("code", c_int),
                ("time", POINTER(c_char) * 24),
                ("ip", POINTER(c_char) * 256),
                ("message", POINTER(c_char) * 512)]

# --- log record codes


class EnErrLogTypes(Enum):
    CmdOK = 0
    CmdTrade = 1
    CmdLogin = 2
    CmdWarn = 3
    CmdErr = 4
    CmdAtt = 5

# --- request logs type


class EnLogType(Enum):
    LOG_TYPE_STANDARD = 0
    LOG_TYPE_LOGINS = 1
    LOG_TYPE_TRADES = 2
    LOG_TYPE_ERRORS = 3
    LOG_TYPE_FULL = 4
    LOG_TYPE_UPDATER = 16
    LOG_TYPE_SENDMAIL = 17
    LOG_TYPE_FAILOVER = 18

# --- request logs type


class EnLogMode(Enum):
    LOG_MODE_ENABLED = 0
    LOG_MODE_DISABLED = 1

# +------------------------------------------------------------------+
# | Balance check                                                    |
# +------------------------------------------------------------------+

# pragma pack(push,1)


class BalanceDiff(Structure):
    _fields_ = [("login", c_int),
                ("diff", c_double)]

# pragma pack(pop)

# +------------------------------------------------------------------+
# | Pumping notification codes                                       |
# +------------------------------------------------------------------+


class pumping_notification_codes(Enum):
    PUMP_START_PUMPING = 0
    PUMP_UPDATE_SYMBOLS = 1
    PUMP_UPDATE_GROUPS = 2
    PUMP_UPDATE_USERS = 3
    PUMP_UPDATE_ONLINE = 4
    PUMP_UPDATE_BIDASK = 5
    PUMP_UPDATE_NEWS = 6
    PUMP_UPDATE_NEWS_BODY = 7
    PUMP_UPDATE_MAIL = 8
    PUMP_UPDATE_TRADES = 9
    PUMP_UPDATE_REQUESTS = 10
    PUMP_UPDATE_PLUGINS = 11
    PUMP_UPDATE_ACTIVATION = 12
    PUMP_UPDATE_MARGINCALL = 13
    PUMP_STOP_PUMPING = 14
    PUMP_PING = 15
    PUMP_UPDATE_NEWS_NEW = 16

# +------------------------------------------------------------------+
# | Dealing notification codes                                       |
# +------------------------------------------------------------------+


class dealing_notification_codes(Enum):
    DEAL_START_DEALING = 0
    DEAL_REQUEST_NEW = 1
    DEAL_STOP_DEALING = 2

# +------------------------------------------------------------------+
# | Class CManager                                                   |
# +------------------------------------------------------------------+
# Подгружаем враппер
#lib = ctypes.CDLL("E:/for_work/MT4ManPythonWrapper/_output/bin/Win32/Debug/MT4ManPythonWrapper.dll")
lib = ctypes.CDLL("D:/Visual Studio/Projects/MT4ManPythonWrapper/_output/bin/Win32/Debug/MT4ManPythonWrapper.dll")
#функции враппера
########################################################################################################################
# создание менеджерского интерфейса
########################################################################################################################
def CreateManagerInterface():
    return lib.MT4Man_New()

########################################################################################################################
# коннект к серверу, параметры: интерфейс менеджера, IP адрес
########################################################################################################################
def Connect(ManInt,server):
    if lib.MT4Man_Connect(ManInt,server.encode("ascii")) == 0:
        return 0
    else:
        sys.exit()



########################################################################################################################
# отключение от сервера, параметр интерфейс менеджера
########################################################################################################################
def Disonnect(ManInt):
    return lib.MT4Man_Disconnect(ManInt)

########################################################################################################################
# проверка коннекта с сервером, параметр интерфейс менеджера
########################################################################################################################
def IsConnected(ManInt):
    lib.MT4Man_Ping(ManInt)
    return lib.MT4Man_IsConnected(ManInt)

########################################################################################################################
#авторизация, параметры: интерфейс менеджера, логин, пароль
########################################################################################################################
def Login(ManInt,Login,Password):
    return lib.MT4Man_Login(ManInt,Login,Password.encode("ascii"))

########################################################################################################################
#авторизация, параметры: интерфейс менеджера, логин, пароль
########################################################################################################################
def Ping(ManInt):
    return lib.MT4Man_Ping(ManInt)

########################################################################################################################
# перезагрузка торгового сервера, параметр интерфейс менеджера
########################################################################################################################
def Restart(ManInt):
    return lib.MT4Man_SrvRestart(ManInt)

########################################################################################################################
# обновление информации по инструментам, параметр интерфейс менеджера
########################################################################################################################
def SymbolsRefresh(ManInt):
    return lib.MT4Man_SymbolsRefresh(ManInt)

def OnlineRecord(ManInt):
    Total = c_int(0)
    Result = ARRAY(OnlineRecord, 10000)()
    lib.MT4Man_OnlineRequest(ManInt, pointer(Total), pointer(Result))
    return Result

def CfgRequestSymbol(ManInt):
    Total = c_int(0)
    Result = ARRAY(ConSymbol, 300)()
    lib.MT4Man_CfgRequestSymbol(ManInt, pointer(Total), pointer(Result))
    #print(Total.value)
    return Result

def PluginsGet(ManInt):
    Total = c_int(0)
    Result = ARRAY(ConPlugin, 50)()
    lib.MT4Man_PluginsGet(ManInt, pointer(Total), pointer(Result))
    return Result
########################################################################################################################
#CfgRequestPlugin процедура и методы для нее
########################################################################################################################
def CfgRequestPlugin(ManInt):
    Total = c_int(0)
    Result = ARRAY(ConPluginParam, 50)()
    lib.MT4Man_CfgRequestPlugin(ManInt, pointer(Total), pointer(Result))
    return Result
####
# Процедура получения массива значений по имени параметра (например значения однотипных параметров плагина Routing)
####
def GetPluginParameterValue(ManInt, ParameterName):
    Result = CfgRequestPlugin(ManInt)
    ResArr = []
    i = 0
    while i < len(Result):
        j = 0
        while j < Result[i].total:
            if (Result[i].params[j].name == ParameterName.encode("ascii")):
               ResArr.append( Result[i].params[j].value.decode())
            j = j + 1
        i = i + 1
    return (ResArr)
########################################################################################################################