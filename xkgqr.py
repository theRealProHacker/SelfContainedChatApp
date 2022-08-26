# TODO: add gui and or asyncconsole and maybe 
import os
import time
import re

file = os.path.abspath(__file__)
author = os.path.basename(os.environ["USERPROFILE"])
print(f"{author=}")

def write(msg):
    with open(file, "a") as f:
        print(f"# {author}:{int(time.time())}:{msg}", file=f)

pattern = re.compile(r'# (.+):(\d+):(.+)')

def read():
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            match = pattern.match(line)
            if match:
                print(match.groups())

read()

# Here should be an event loop that checks for both user input as well as file changes.


# Rashid:1661541411:hello
