import subprocess

def check_mac():
    cmd = subprocess.run('arp -a | findstr ""', shell=True)
    return print(cmd.returncode)

def msg():
    

if __name__ == '__main__':
    check_mac()