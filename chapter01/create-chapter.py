#!/usr/bin/env python

width       = 80
chapter     = "chapter01 - dashified"
description = """
Retrieve the secret key from the file!

---

Hints: ls(1), sed(1), more(1), less(1), cat(1), awk(1)
"""

def generate_key():
    secret = "OkOigTekUvOd4osdawyetKar\n"
    
    with open('-secret-key', 'w') as key:
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




