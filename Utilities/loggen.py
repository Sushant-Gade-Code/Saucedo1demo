import inspect
import logging

class LoGenretor:
    @staticmethod
    def getLoggen():
        name=inspect.stack()[1][3]
        logger=logging.getLogger(name)
        File=logging.FileHandler("C:\\Users\\Admin\\PycharmProjects\\Saucedo1demo\Log\\automation.log")
        Formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s :%(lineno)s: %(message)s")
        File.setFormatter(Formatter)
        logger.addHandler(File)
        logger.setLevel(logging.DEBUG)
        return logger

