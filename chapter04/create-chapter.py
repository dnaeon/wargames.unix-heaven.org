#!/usr/bin/env python

width       = 80
chapter     = "chapter04 - strings"
description = """
While performing an audit of our UNIX systems,
one of our security engineers discovered a
serious bug in one of the programs that is used for authentication.

He discovered that the programmer has carelessly
left the password in the program unencrypted!

Retrieve the password from the program in order to
advance to the next chapter!
"""

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




