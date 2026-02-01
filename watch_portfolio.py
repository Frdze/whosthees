import time
import os
import subprocess

def generate_json():
    subprocess.run(['python', 'generate_portfolio.py'])

# Initial generation
generate_json()

# Watch for changes (simple polling)
last_mtimes = {}
categories = ['design', 'development', 'illustration', 'photography', '3d']

while True:
    changed = False
    for cat in categories:
        folder = os.path.join('portfolio', cat)
        if os.path.exists(folder):
            for file in os.listdir(folder):
                filepath = os.path.join(folder, file)
                if os.path.isfile(filepath):
                    mtime = os.path.getmtime(filepath)
                    if filepath not in last_mtimes or last_mtimes[filepath] != mtime:
                        last_mtimes[filepath] = mtime
                        changed = True
    if changed:
        generate_json()
        print("Portfolio updated")
    time.sleep(1)
