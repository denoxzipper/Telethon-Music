import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29797352"))
    API_HASH = os.environ.get("API_HASH", "24bf545ecf9ea682c67c236d1e51e947")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958376911:AAHqRJcLuhmNWLitFnUc2h_v_whPDgaMD3Q")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu6d6BsJkoT8ZPmCzu24tJ959Fk9pYr2P0pw6TvretzIlshSIormp0W0YCHS_PJ0hC5rEfcL9THDDGblBua2o041IlNsy7zXbpmmMe9z76NHg-kx6xdzrIjt_k4fgyaqv8dNcLZgF_-ns2ecxSC-hymb6en6n52MTNM3jyQT-ID2ahZ3sMPoL5hpgt7_iAujmhVT0Y3CXdpabsCwWXuJkJHt7xNsM5Rp6rAYWRU7ocSbOSLYSoeAOfhXF-VWLk0ganB_Qmnn-7OU5Nj-_-cTQDuIGnFog2K1ILPOLrA4gpO7M1RjgvoVw1bOgN4EGKJIGxZEHkYRkTgAmrKuH2Lfsygw=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "TRUE")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "N4musicV3_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6176726691")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "TRUE") # Change it to "True"
