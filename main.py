import json
import os

file = "task.json"
file_exist = True

if not os.path.isfile(file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump({}, f)
    file_exist = False


if __name__ == "__main__":
    if file_exist:
        pass
    else:
        pass