#!/usr/bin/env python3
#########################################
# ToxicBomber
# A Bangladeshi SMS Bomber Tool
# Author: ToxicNoob Inc.
# GitHub: https://github.com/Toxic-Noob
# Version: 4.1.0 (Python 3 Compatible)
#########################################

import time
import requests
import sys
import os
import shutil
import json

# Get Rows and Columns of Screen
columns = shutil.get_terminal_size().columns


def psb(z, end="\n"):
    for e in z + end:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def checkPy():
    major = sys.version_info.major
    minor = sys.version_info.minor
    if (major != 3) or (minor < 8):
        print(f"\n[\033[92m*\033[37m] Your Python Version ({major}.{minor}) is not supported!")
        print("[\033[92m*\033[37m] Update your Python using the command below:\n\n    pkg reinstall python\n")
        sys.exit()


def showAuthorMsg(msg):
    print()
    print("\033[94m-" * columns)
    print("\033[92mMessage From Author".center(columns + 4))
    print("\033[95m-" * columns)
    psb("\n\033[37m    " + msg + "\n")
    print("\033[94m-" * columns)
    print()
    os.makedirs("./more", exist_ok=True)
    with open("./more/.msg", "w") as f:
        f.write(msg)
    time.sleep(1)
    input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
    logo()


def update():
    try:
        toolVersion = json.loads(open("./more/.version", "r").read())["version"]
    except Exception:
        toolVersion = "ToxicNoob"

    try:
        authorMsg = open("./more/.msg", "r").read().strip()
    except Exception:
        authorMsg = "None"

    try:
        parsedData = requests.get(
            "https://raw.githubusercontent.com/Toxic-Noob/ToxicBomber/main/more/.version"
        ).json()
    except Exception:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Connect To The Internet!")
        input("\n    \033[92m[\033[37m*\033[92m] \033[37mPress Enter To Continue...")
        return update()

    mainVersion = parsedData["version"]
    newMsg = parsedData["message"]

    if toolVersion != mainVersion:
        psb("\n    \033[92m[\033[37m!\033[92m] \033[37mTool Update Found!")
        time.sleep(0.5)
        psb("    \033[92m[\033[37m!\033[92m] \033[37mUpdating Tool: ", end="")

        os.system("cd .. && rm -rf ToxicBomber && git clone https://github.com/Toxic-Noob/ToxicBomber > /dev/null 2>&1")

        print("\033[37mDone")
        psb("\n    \033[92m[\033[37m*\033[92m] \033[37mStarting Tool...")
        time.sleep(0.8)
        os.system("cd .. && cd ToxicBomber && python3 Tbomb.py")
    else:
        if (authorMsg != newMsg) and (newMsg != "blank"):
            showAuthorMsg(newMsg)


def logo():
    os.system("clear")
    print("\033[94m┌────────────────────────────────────────┐".center(columns + 5))
    print("\033[94m│     \033[92m▀▛▘     ▗    ▛▀▖       ▌        \033[94m   │".center(columns + 15))
    print("\033[94m│     \033[92m ▌▞▀▖▚▗▘▄ ▞▀▖▙▄▘▞▀▖▛▚▀▖▛▀▖▞▀▖▙▀▖\033[94m   │".center(columns + 15))
    print("\033[94m│     \033[92m ▌▌ ▌▗▚ ▐ ▌ ▖▌ ▌▌ ▌▌▐ ▌▌ ▌▛▀ ▌  \033[94m   │".center(columns + 15))
    print("\033[94m│     \033[92m ▘▝▀ ▘ ▘▀▘▝▀ ▀▀ ▝▀ ▘▝ ▘▀▀ ▝▀▘▘  \033[94m   │".center(columns + 15))
    print("\033[94m│                              \033[94m          │".center(columns + 9))
    print("\033[94m│ \033[95mAuthor : ToxicNoob Inc.                \033[94m│".center(columns + 15))
    print("│ \033[95mTool   : Unlimited SMS Bomber          \033[94m│".center(columns + 9))
    print("│ \033[95mGitHub : https://github.com/Toxic-Noob \033[94m│".center(columns + 9))
    print("│ \033[95mCoder  : HunterSl4d3              \033[37mV4.1 \033[94m│".center(columns + 15))
    print("\033[94m└────────────────────────────────────────┘".center(columns + 5))


def banner():
    amount = str(main.amount)
    amount = amount + (" " * (21 - len(amount)))

    print("\033[95m-" * columns)
    print(("\033[92mTarget  : \033[37m0" + main.number).center(columns + 10))
    print(("\033[92mAmount  : \033[37m" + amount).center(columns + 10))
    print("\033[92mProcess : \033[37mStarted".center(columns + 10))
    print("\033[92mNote    : \033[37mPress ctrl + z To Stop".center(columns + 10))
    print("\033[95m-" * columns)
    print("\n")


def check(sent):
    amount = main.amount
    delay = main.delay
    localTime = time.localtime()
    current_time = time.strftime("%I:%M:%S", localTime)
    print(f"\r\033[92m    [\033[94m {current_time} \033[92m] Message Sent : \033[94m[\033[37m{sent}\033[94m]\033[37m", end="")
    if sent == amount:
        psb("\n\n\033[92m    [\033[37m*\033[92m] Bombing Finished!")
        psb(f"\033[92m    [\033[37m*\033[92m] Amount : \033[37m{amount}")
        psb(f"\033[92m    [\033[37m*\033[92m] Target : \033[37m0{main.number}")
        psb("\033[92m    [\033[37m*\033[92m] From   : \033[37mToxicBomber\n")
        time.sleep(0.6)
        print("\033[92m[\033[93m★\033[92m] Thanks For Using Our Tool \033[92m[\033[93m★\033[92m]".center(columns + 30))
        print("\033[37m")
        return True
    else:
        time.sleep(delay)
        return False


def getNumber():
    number = input("\n    \033[92m[\033[37m*\033[92m] \033[37mEnter Target (\033[92mWithout +88\033[37m):> \033[37m")
    if not number.isdigit():
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter a Correct Number!")
        return getNumber()
    if len(number) != 11:
        psb("\n    \033[92m[\033[91m!\033[92m] \033[37mPlease Enter 11 Digit Number!")
        return getNumber()
    return number


def main():
    number = getNumber()
    number = number[-10:]
    main.number = number

    try:
        amount = int(input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Amount (Default: 10):> \033[37m") or 10)
    except ValueError:
        amount = 10
    main.amount = amount

    try:
        delay = int(input("    \033[92m[\033[37m*\033[92m] \033[37mEnter Time(Sec) Delay (Default: 2s):> \033[37m") or 2)
    except ValueError:
        delay = 2
    main.delay = delay

    time.sleep(1)
    logo()
    banner()

    sent = 0
    finished = False

    items = globals().get("RUNNABLE_ITEMS", 0)
    allFuncs = globals()

    if check(sent):
        sys.exit()

    while True:
        for i in range(1, items + 1):
            api_func = allFuncs.get(f"api_{i}")
            if callable(api_func):
                success = api_func(number)
                if success:
                    sent += 1
                    if check(sent):
                        finished = True
                        break
        if finished:
            break


if __name__ == "__main__":
    checkPy()
    logo()
    update()
    main()
