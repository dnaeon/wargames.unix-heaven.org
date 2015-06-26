#!/usr/bin/env python

width       = 80
chapter     = "chapter08 - the epoch"
description = """
mtime

---

Hints: ls(1), cat(1), awk(1), stat(1), grep(1),
       cut(1), file(1), date(1), touch(1), strftime(3)
"""

# make sure to have different atime, ctime and mtime

def generate_data():
    with open('password.txt', 'w') as fobj:
        fobj.write("I'm not exactly what you are looking for!\n")

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




