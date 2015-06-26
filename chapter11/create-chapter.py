#!/usr/bin/env python

width       = 80
chapter     = "chapter11 - the librarian"
description = """
In your home directory you will find a program.

Executing this program will reveal you the secret key to the
next chapter, but... there is just one issue with it...

... an important piece of it is missing and you need to fix that.

You will have to fix the program first to make it run!

---

Hints: file(1), nm(1), ldd(1), objdump(1), ldconfig(8), ld.so(8)
"""

# find the shared library and run the program
# decode the returned message
# how to build the code:
#
# 	gcc -c -Wall -Werror -fpic junto.c
#	gcc -shared -o libjunto.so junto.o
#	gcc benjamin.c -L. -ljunto -o benjamin
#
# Install the shared library and object files in /usr/lib/philly,
# Philladelphia, where the Junto club was established by Benjamin Franklin

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
