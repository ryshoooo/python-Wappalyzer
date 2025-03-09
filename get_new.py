# https://github.com/enthec/webappanalyzer/tree/main

# Categories
# https://raw.githubusercontent.com/enthec/webappanalyzer/refs/heads/main/src/categories.json

# Apps
# https://raw.githubusercontent.com/enthec/webappanalyzer/refs/heads/main/src/technologies/_.json

import requests
import json

LETTERS = [x for x in "abcdefghijklmnopqrstuvwxyz_"]

categories = requests.get(
    "https://raw.githubusercontent.com/enthec/webappanalyzer/refs/heads/main/src/categories.json",
    timeout=10,
).json()

for v in categories.values():
    del v["groups"]

apps = {}
for letter in LETTERS:
    apps_x = requests.get(
        f"https://raw.githubusercontent.com/enthec/webappanalyzer/refs/heads/main/src/technologies/{letter}.json",
        timeout=10,
    ).json()
    apps.update(apps_x)

with open("Wappalyzer/data/apps.json", "w") as fd:
    json.dump({"categories": categories, "apps": apps}, fd, indent=2)
