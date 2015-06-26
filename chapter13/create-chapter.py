#!/usr/bin/env python

width       = 80
chapter     = "chapter13 - the three brothers"
description = """
They swore to protect it with their lives.

And only one of them shall reveal the key to the noble ones.

---

Hints: netstat(1), sockstat(1), nc(1), bzip2(1), socket(2),
       base64(1), gzip(1), nmap(1), telnet(1), lsof(8), ss(8)
"""

# three daemons are running in the background
# each of them returns an encoded message, but only one of them
# will reveal you the secret key
# story is about the three brothers from indiana jones and the holy grail

def create_chapter():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'
    with open(chapter.split(' ')[0] + '.txt', 'w') as fobj:
        print >>fobj, line.center(width)
        print >>fobj, ('| ' + chapter.title() + ' |').center(width)
        print >>fobj, line.center(width)
        print >>fobj, description

def main():
    create_chapter()

if __name__ == '__main__':
    main()
