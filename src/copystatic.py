import os
import shutil

def copy_directory(source, destination, erase=True):
    if erase and os.path.exists(destination):
        print(f"Deleting {destination}...")
        shutil.rmtree(destination)
    if not os.path.exists(destination):
        os.makedirs(destination)
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        print("copying", s, "to", d)
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)