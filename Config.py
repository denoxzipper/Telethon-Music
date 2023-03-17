import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29797352"))
    API_HASH = os.environ.get("API_HASH", "24bf545ecf9ea682c67c236d1e51e947")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958376911:AAHqRJcLuhmNWLitFnUc2h_v_whPDgaMD3Q")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQC8-IWmBHvVOq0axdXKv4hVdqbl9nKKXLvbHfsngSr5qa14gWFJ8GOF_ujDakpFiYWgU25AXzB4xLrklPU6Vbf5DJs2a--kMukuu6BNx6_Ia76_zkOM3rO7b-JojVz309UAXWKOExUWJ1lSzzy9GI-VafZ2Ncu9SEmur3KsAI_JYBm-HOYeC4KsFBAfkjMt4IAfqq8lYjDu0PEqvj-XTuDaow_hOaCSdnwH2MBIWja9CXh6oko51OZVNrIgIRcA0PL7z8QeV9kZwR27aGl2G_Bwr9r_J87iMnGq8ZbHEdF5-zWXtgf5Dpks1Cds1fgOc0VJRBPCiNpSzL6ZTHBBp7mvAAAAAXApXqMA")
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
