#!/usr/bin/env python

width       = 80
chapter     = "chapter09 - differences"
description = """
files differ from each other with just one line.

putting these differences together you will find ...

---

Hints: ls(1), cat(1), uniq, sort, find
"""

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




