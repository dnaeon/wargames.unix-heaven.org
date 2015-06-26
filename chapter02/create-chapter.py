#!/usr/bin/env python

width       = 80
chapter     = "chapter02 - learning to count"
description = """
The number of lines in data.txt will give you the key.

---

Hints: ls(1), cat(1), wc(1), awk(1)
"""

import string
import random

def generate_data():
    chars = string.ascii_letters + string.digits
    
    with open('data.txt', 'w') as fobj:
        for i in xrange(1337):
            fobj.write("".join(random.sample(chars, 60)) + '\n')
            
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




