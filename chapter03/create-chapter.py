#!/usr/bin/env python

width       = 80
chapter     = "chapter03 - more counting"
description = """
The sum of all bytes in the data files minus all
lines will give you the key to the next chapter.

---

Hints: echo, ls(1), cat(1), wc(1), awk(1), bc(1), sed(1), pipe(7), diff(1)

Useful links:

* http://tldp.org/LDP/abs/html/arithexp.html
* http://www.gnu.org/software/bash/manual/html_node/Pipelines.html
"""

import string
import random

def generate_data(path, lines):
    chars = string.ascii_letters + string.digits
    
    with open(path, 'w') as fobj:
        for i in xrange(lines):
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

    for f in ('data1.txt', 'data2.txt'):
        generate_data(f, random.randrange(1500))
    
if __name__ == '__main__':
    main()




