import os
import subprocess

def Julius(self):
    path = os.getcwd() + "\Challenges\Julius\Cipher.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = "rxms{VgXUg5OqmE4d}"
    with open(path, 'w') as f:
        f.write(data)
    f.close()
    subprocess.Popen(r'explorer /select,' + path)
    print(path)