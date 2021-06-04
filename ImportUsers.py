from pymongo import MongoClient
from tinydb import TinyDB

client = MongoClient(port=27017)
db = client.BibleBotBackend

def ImportUsers():
    mongousers = db.Users
    users = TinyDB("db")

    for user in users.all():
        userId = str(user["id"])
        version = "RSV"
        inputMethod = "default"
        language = "english"
        titlesEnabled = True
        verseNumbersEnabled = True
        displayStyle = "embed"

        if "version" in user:
            if user["version"] in ["KJVA", "FBV", "BSB", "NHEB", "WBT", "ELXX", "LXX", "NKJV"]:
                version = "RSV"
            else:
                version = user["version"]
        
        if "language" in user:
            language = user["language"]
        
        if "headings" in user:
            if user["headings"] in ["enable", "disable"]:
                if user["headings"] == "disable":
                    titlesEnabled = False
        
        if "verseNumbers" in user:
            if user["verseNumbers"] in ["enable", "disable"]:
                if user["verseNumbers"] == "disable":
                    verseNumbersEnabled = False
        
        if "mode" in user:
            if user["mode"] in ["embed", "code", "blockquote"]:
                displayStyle = user["mode"]

        mongousers.insert_one({
            "UserId": userId,
            "Version": version,
            "InputMethod": inputMethod,
            "Language": language,
            "TitlesEnabled": titlesEnabled,
            "VerseNumbersEnabled": verseNumbersEnabled,
            "DisplayStyle": displayStyle
        })
        
        print("processed user - " + userId);

ImportUsers()