#!/usr/bin/env python3


if __name__ == "__main__":
    exit(1)


import json


class Settings(object):
    ACP_KEYS: list[str] = [
        "playerCount",
        "startingCards",
        "loopNullCard"
    ]

    def __init__(self):
        self.settingsPath: str = "./settings"

    def readBaseSettings(self) -> dict:
        data: dict = {}
        with open(f"{self.settingsPath}/baseSettings.json", 'r') as fp:
            data = json.load(fp.read())
        if not data:
            raise RuntimeError
        return data

    def readUserSettings(self, filename: str) -> dict:
        assert filename.endswith(".json"), "The filename must be a json file!"
        data: dict = self.readBaseSettings()
        with open(f"{self.settingsPath}/filename", 'r') as fp:
            tmpData: dict = json.load(fp.read())

        for key, val in tmpData.items():
            if key in data and key in ACP_KEYS:
                data[key] = val
            else:
                print(key, "is not a valid key")
        return data
