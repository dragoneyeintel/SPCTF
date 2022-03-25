import os
import subprocess

def Dictionary(self):
    path = os.getcwd() + "\Challenges\Dictionary\Dictionary.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = "AF4DFE88F24D551E445C4688413C9F7BBB2D016B9E2F70C987B5CEE21FD6DAF4"
    with open(path, 'w') as f:
        f.write(data)
    f.close()
    subprocess.Popen(r'explorer /select,' + path)
    print(path)