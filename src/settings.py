
if __name__ == "__main__":
    exit(1)


import json


class Settings(object):
    def __init__(self):
        self.settingsPath: str = "./settings"

    def readBaseSettings(self) -> dict:
        pass

    def readUserSettings(self, filename: str) -> dict:
        pass
