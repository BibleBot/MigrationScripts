from pymongo import MongoClient
from tinydb import TinyDB

client = MongoClient(port=27017)
db = client.BibleBotBackend

def ImportVersions():
    mongoversions = db.Versions
    versions = TinyDB("versiondb")

    for version in versions.all():
        source = "bg"

        if version["abbv"] in ["BSB", "NHEB", "WBT", "ELXX", "LXX", "NKJV"]:
            continue
        elif version["abbv"] in ["KJVA", "FBV"]:
            source = "ab"

        mongoversions.insert_one({
            "Name": version["name"],
            "Abbreviation": version["abbv"],
            "Source": source,
            "SupportsOldTestament": version["hasOT"],
            "SupportsNewTestament": version["hasNT"],
            "SupportsDeuterocanon": version["hasDEU"]
        })
        
        print("processed version - " + version["name"])

ImportVersions()
