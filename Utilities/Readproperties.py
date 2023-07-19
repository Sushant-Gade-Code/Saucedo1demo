import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\Admin\\PycharmProjects\\Saucedo1demo\\Configuration\\config.ini")

class Readproperties:
    @staticmethod
    def getUrl():
        url=config.get("LogIn Info","url")
        return url

    @staticmethod
    def getUsername():
        Username=config.get("LogIn Info","username")
        return Username

    @staticmethod
    def getPassword():
        Password = config.get("LogIn Info", "password")
        return Password

    @staticmethod
    def getList():
        aList=config.get("LogIn Info", "aList")
        return aList

