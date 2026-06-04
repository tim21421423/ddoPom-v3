import os
import sys
import subprocess

def install(package):
    print(f"Ima installing a package please wait {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        print(f"Installed {package}")
    except:
        print(f"im falied im idk why and cant install {package}")

print("starting library installation...")

packages = ["requests", "colorama", "fake-useragent"]

for p in packages:
    install(p)

print("\nIm installed all the packages")
print("Now you can run the ddoPom")

input("Press Enter to exit...")