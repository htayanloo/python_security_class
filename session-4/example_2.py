import dns
import dns.resolver


host = "xenonserver.ir"
record= ["A","AAAA","NS","SOA","MX","TXT"]
for rec in record:
    print(f"------------------{rec}--------------------------")
    try:
        temp = dns.resolver.resolve(host,rec)
        for item in temp:
            print(item)
    except:
        print("")
