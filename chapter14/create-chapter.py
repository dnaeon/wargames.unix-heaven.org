#!/usr/bin/env python

width       = 80
chapter     = "chapter14 - down the rabbit hole"
description = """

An authorative name server for the wargames.local domain is
running at 10.10.144.10 IP address.

You will find your next clue to this challenge there.

---

Hints: resolver(3), host(1), dig(1), nmap(1), hosts(5),
       nslookup(1), tcpdump(8), ftp(1), resolv.conf(5)
"""

# how the challenge should be approached:
# 
# * perform a DNS zone transfer for wargames.local
# * perform a DNS zone transfer for 144.10.10.in-addr.arpa zone
# * connect to the anon-ftp server and retrieve the tcpdump
# * connect to the private-ftp server using teh tcpdump login details
def main():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'
    fobj = open(chapter.split(' ')[0] + '.txt', 'w')
    
    print >>fobj, line.center(width)
    print >>fobj, ('| ' + chapter.title() + ' |').center(width)
    print >>fobj, line.center(width)
    print >>fobj, description

    fobj.close()

if __name__ == '__main__':
    main()




