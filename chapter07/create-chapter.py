#!/usr/bin/env python

width       = 80
chapter     = "chapter07 - lost and found"
description = """
Somewhere in the data directory resides the key you are looking for.

The file, which contains the key to the next chapter is owned by a
user who is just one chapter ahead of you. 

Now go and find(1) the file!
"""

# include different find examples, e.g. by owner, file size, etc..

import os
import random
import string

def generate_data():
    num_dirs = 100
    num_files = 100
    chars = string.ascii_letters

    if not os.path.exists('data'):
        os.mkdir('data')

    # create a hundred directories, each containing hundred files files each
    for i in xrange(num_dirs):
        random_dir = "".join(random.sample(chars, 5))
        os.mkdir(os.path.join('data', random_dir))
        for i in xrange(num_files):
            random_file = "".join(random.sample(chars, 5))
            with open(os.path.join('data', random_dir, random_file), 'w') as fobj:
                fobj.write("".join(random.sample(chars, 20)) + '\n')

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




