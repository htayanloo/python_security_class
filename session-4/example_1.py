import socket
socket.setdefaulttimeout(2)
def get_banner(target,port):
    try:
        sock = socket.socket()
        sock.connect((target,port))
        query = "GET /HTTP/1.1\nHost: 192.168.3.110"
        http_query = bytes(query,'utf-8')
        sock.sendall(http_query)
        banner = sock.recvfrom(1024)

    except :
        return ""
    else:
        return banner[0]


temp = get_banner(target="192.168.3.110",port=80)
vul = open("vulnbanners.txt","r")
for line in vul.readlines():
    line = line.split(" ")
    for item in temp.splitlines():
        if line[0] in str(item):
            print("Detect : %s" % line[1])
