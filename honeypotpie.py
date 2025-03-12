import socket
import threading
import logging

logging.basicConfig(filename='honeypotpiev1.log', level=logging.INFO, format='%(asctime)s:%(message)s')

server_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
server_listener.bind((host, port))
server_listener.listen(5)

user_dict = {}

def char_remove(data):
    return data.strip()

def write_log(addr, ctl_name, ctl_pass):
    log_message = f"Connection from {addr} with username: {ctl_name} and password: {ctl_pass}"
    #log_cmd_message = f"Command executed: {cmdTerm}"
    logging.info(log_message)
    #logging.info(log_cmd_message)


def send_cmds(user_type, c):
    if user_type ==0:
        commands = "Available commands: ls, pwd, whoami"
    else:
        commands = "Available commands: ls"

def store_commands(user_cmd, addr):
    if addr not in user_dict:
        user_dict[addr] = []
        user_dict[addr].append(user_cmd)
    pass

def threaded_client(c, addr):
    c.sendall(bytes("Kali GNU/Linux Rolling\n", "utf-8"))
    c.sendall(bytes('(', 'utf-8'))
    c.sendall(bytes(host, "utf-8"))
    c.sendall(bytes(') : kali\n', 'utf-8'))

    while True:
        ctl_name = c.recv(1024)
        ctl_pass = c.recv(1024)
        ctl_name = char_remove(ctl_name.decode('utf-8'))
        ctl_pass = char_remove(ctl_pass.decode('utf-8'))

        write_log(addr, ctl_name, ctl_pass)

        if 'admin' in ctl_name and 'admin' in ctl_pass:
            c.sendall(bytes('Welcome Admin\n', 'utf-8'))
            send_cmds(0, c)

            while True:
                user_cmd = c.recv(1024)
                user_cmd = char_remove(user_cmd.decode('utf-8'))
                store_commands(user_cmd, addr)
                cmdTerm(user_cmd, c, user_dict)
        else:
            c.sendall(bytes('Invalid Credentials\n', 'utf-8'))
            break

    c.close()

def cmdTerm(user_cmd, c, user_dict):
    if 'ls' in user_cmd:
        fake_output = b"bin boot dev etc home lib media mnt opt proc root run sbin srv sys tmp usr var"
        c.sendall(fake_output + b'\n')
    elif 'pwd' in user_cmd:
        fake_output = b"/home/user"
        c.sendall(fake_output + b'\n')
    elif 'whoami' in user_cmd:
        fake_output = b"kali"
        c.sendall(fake_output + b'\n')
    elif 'exit' in user_cmd:
        c.sendall(b'Goodbye\n')
        c.close()
    else:
        c.sendall(b'Invalid Command\n')
    return user_dict

while True:
    getCtl, addr = server_listener.accept()
    print("Connection Established with IP address :", addr)
    threading.Thread(target=threaded_client, args=(getCtl, addr)).start()
