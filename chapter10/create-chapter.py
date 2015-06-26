#!/usr/bin/env python

width       = 80
chapter     = "chapter10 - the secret number"
description = """
A file is hidden somewhere in the /usr/share directory.

All that we know about it is that it is identified by the number XXX.

Find the file and retrieve the secret key!
"""

# file is identified by the inode number
# it's contents are encoded using xxd, the file's extention is the hint

def generate_data():
    data = """536f2c20796f
75277665206d
616465206974
212057656c6c
20646f6e6521
0a0a54686520
736563726574
206b65792066
6f7220746865
206e65787420
636861707465
722069733a20
41746c616e74
69730a0a4e6f
7720676f2c20
646f6e277420
6c6f73652070
726563696f75
732074696d65
2c20636f6e74
696e75652074
6f2074686520
6e6578742063
686170746572
21203a290a
"""

    with open('poseidon.xxd', 'w') as fobj:
        fobj.write(data)

def create_chapter():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'
    with open(chapter.split(' ')[0] + '.txt', 'w') as fobj:
        print >>fobj, line.center(width)
        print >>fobj, ('| ' + chapter.title() + ' |').center(width)
        print >>fobj, line.center(width)
        print >>fobj, description

def main():
    create_chapter()
    generate_data()
    
if __name__ == '__main__':
    main()
