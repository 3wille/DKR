#/usr/env/python3
import sys
import socket
import dns.resolver
import re

def isAddr(addr):
    regex = re.compile('^([0-9]{1,3}\.){3}[0-9]{1,3}$')
    return regex.match(addr) is not None

def getName(input):
    name = socket.gethostbyaddr(input)
    return name

def getAddr(input):
    addr = socket.gethostbyname(input)
    return addr

def dayTime(addr):
    soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    soc.bind((addr,13))
    MESSAGE = b"asdf"
    BUFFER_SIZE= 1024
    soc.sendto(MESSAGE,(addr,13))
    answer = soc.recv(1024)
    return answer

def main():
    # name = dns.resolver.query('uni-hamburg.de')[0]
    if len(sys.argv)>1:
        input = sys.argv[1]
        if isAddr(input):
            name, alias, addr = getName(input)
            print(name)
        else:
            addr = getAddr(input)
            print(addr)
    else:
        print(dayTime("tkrn6.informatik.uni-hamburg.de"))
if __name__ == "__main__":
    main()
