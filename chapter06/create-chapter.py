#!/usr/bin/env python

width       = 80
chapter     = "chapter06 - know your neighbors"
description = """
Joshua has decided to take a long vacation and travel in
the country-side and visit places he have never been before.

But before Joshua went on vacation he gave the keys from his home to
the neighbors, who live across the street, so they can give the keys to
Joshua's brother who should be coming back from work soon.

Help Joshua's brother to retrieve the keys from the neighbors,
while Joshua is on vacation.

---

Hints: ls(1), cat(1), awk(1), cut(1), grep(1)
"""

import string
import random

def generate_data():
    chars = string.ascii_letters + string.digits

    with open('data.txt', 'w') as data:
        for i in xrange(1337):
            line = '%s %s %s %s %s\n' % ("".join(random.sample(chars, 6)),
                                         "".join(random.sample(chars, 7)),
                                         "".join(random.sample(chars, 8)),
                                         "".join(random.sample(chars, 9)),
                                         "".join(random.sample(chars, 10)))
            data.write(line)

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




