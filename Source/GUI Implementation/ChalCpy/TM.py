import os
import subprocess

def TM(self):
    path = os.getcwd() + "\Challenges\TM\Cipher.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = b'x64\x71\x73\x20\x69\x63\x78\x7A\x69\x71\x20\x31\x20\x77\x79\x76\x6E\x74\x69\x20\x6B\x6B\x76\x69\x74\x6B\x61\x20\x77\x6A\x6D\x20\x63\x73\x6D\x76\x20\x74\x6C\x6D\x6D\x75\x72\x6F\x71\x20\x6A\x63\x66\x71\x65\x78\x7A\x6D\x64\x61\x78\x65\x2C\x20\x65\x62\x69\x72\x75\x6B\x73\x2C\x20\x6E\x63\x7A\x65\x72\x72\x69\x77\x77\x20\x68\x6C\x6E\x7A\x6B\x79\x63\x6F\x78\x63\x69\x69\x20\x66\x62\x70\x75\x20\x64\x67\x79\x72\x20\x62\x6F\x6E\x72\x68\x71\x73\x68\x20\x74\x66\x70\x72\x20\x63\x20\x6F\x74\x79\x65\x6D\x69\x20\x28\x7A\x66\x73\x69\x6C\x6A\x69\x71\x7A\x6D\x20\x62\x6D\x64\x62\x68\x6C\x69\x20\x70\x20\x61\x76\x6A\x6C\x77\x6A\x74\x70\x6C\x29\x20\x65\x63\x77\x78\x20\x62\x20\x6E\x71\x6B\x61\x70\x75\x20\x70\x68\x20\x75\x71\x75\x6B\x63\x76\x72\x20\x75\x20\x65\x6D\x68\x20\x69\x61\x63\x77\x6E\x67\x70\x2E\x0D\x0A\x63\x74\x62\x65\x7B\x66\x70\x73\x5F\x6C\x6D\x6B\x66\x77\x7D\x0D\x0A\x2D\x20\x74\x6B\x6B\x66\x20\x77\x79\x6D\x6B'
    with open(path, 'wb') as f:
        f.write(data)
    f.close()
    subprocess.Popen(r'explorer /select,' + path)
    print(path)