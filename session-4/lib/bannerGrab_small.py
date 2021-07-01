#	Python FTP banner Grabbing script
#
#	this python script will scan and check for
#	matching vulnarablities from a given text
#	list of Vulnarable banners.
#
#	Void .inc
#	bekidelta@protonmail.com
#		oct 21, 2018

import socket

socket.setdefaulttimeout(2)


def ReturnBanner(ip, port):
    try:
        sock = socket.socket()
        sock.connect((ip, port))
        banner = sock.recv(1024)
        print(banner)
        return banner
    except Exception as e:
        print('Error : ' + str(e))
        return True


# check for vulnarability on known server names
def checkVulns(banner):
    VulnarableFTPlist = open("vulnbanners.txt", 'r')
    for line in VulnarableFTPlist.readlines():
        if line.strip('\n') in banner:
            print("[ + ] server is Vulnarable: " + banner.strip('\n'))


def main():
    print('Welcome to FTP Banner grabbing script')
    IP = input('Host IP : ')

    PortList = [21, 22, 23, 25, 80, 110, 443]
    PortNames = {21: 'ftp', 22: 'ssh', 23: 'Telnet', 25: 'smtp', 80: 'HTTP', 110: 'POP3', 443: 'HTTPS'}

    for port in PortList:
        banner = str(ReturnBanner(IP, port))
        print(banner)
        if banner:
            print('[ + ] ' + IP + ': ' + str(banner))
            c = checkVulns(banner)
            print('\t %s' % (c))
        else:
            print('[ - ] CANT CONNECT ' + IP + ' ON PORT ' + str(PortNames[port]))


if __name__ == '__main__':
    main()
