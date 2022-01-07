
if __name__ == "__main__":
    exit(1)


import json


class Settings(object):
    def __init__(self):
        self.settingsPath: str = "./settings"

    def readBaseSettings(self) -> dict:
        data: dict = {}
        with open(f"{self.settingsPath}/baseSettings.json") as fp:
            data = json.load(fp.read())
        if not data:
            raise RuntimeError
        return data


    def readUserSettings(self, filename: str) -> dict:
        pass
