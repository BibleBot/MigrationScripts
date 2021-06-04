from re import IGNORECASE
from pymongo import MongoClient
from tinydb import TinyDB

client = MongoClient(port=27017)
db = client.BibleBotBackend

def ImportGuilds():
    mongoguilds = db.Guilds
    guilds = TinyDB("guilddb")

    for guild in guilds.all():
        guildId = str(guild["id"])
        version = "RSV"
        prefix = "+"
        ignoringBrackets = "<>"
        language = "english"

        if "version" in guild:
            if guild["version"] in ["KJVA", "FBV", "BSB", "NHEB", "WBT", "ELXX", "LXX", "NKJV"]:
                version = "RSV"
            else:
                version = guild["version"]
        
        if "language" in guild:
            language = guild["language"]

        mongoguilds.insert_one({
            "GuildId": guildId,
            "Version": version,
            "Language": language,
            "Prefix": prefix,
            "IgnoringBrackets": ignoringBrackets,
            "IsDM": False
        })
        
        print("processed guild - " + guildId)

ImportGuilds()