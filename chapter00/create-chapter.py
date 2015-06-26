#!/usr/bin/env python

width       = 80
chapter     = "chapter00 - the secret key"
description = """

Welcome to the first chapter of the Unix/Linux wargames!

In this chapter you will have to find the secret key,
which is hidden somewhere in your home directory.

Find the secret key in order to advance to the next chapter!

---

Hints: ls(1), more(1), less(1), cat(1)
"""

def generate_key():
    secret = "cajRewgUvVicpebtijBoinIa\n"
    
    with open('.secret-key', 'w') as key:
        key.write(secret)

def create_chapter():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'

    with open(chapter.split(' ')[0] + '.txt', 'w') as fobj:
        print >>fobj, line.center(width)
        print >>fobj, ('| ' + chapter.title() + ' |').center(width)
        print >>fobj, line.center(width)
        print >>fobj, description

def main():
    create_chapter()
    generate_key()

if __name__ == '__main__':
    main()




