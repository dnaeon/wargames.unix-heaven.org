#!/usr/bin/env python

width       = 80
chapter     = "chapter15 - the end"
description = """
Every great journey comes to an end ...

... and so does ours in the Wargames.

Even though one journey ends, 
your journey in the UNIX/Linux world should not!

We hope that you have enjoyed the time while being here with us,
and also learned something new and interesting!

Before moving on there is one more thing to do ...

... welcome to the Hall Of Fame!

Login to the Wargames site and add your name to the Hall Of Fame!

Username: hof
Password: rockstar
URL     : http://wargames.unix-heaven.org/user/login
"""

# three daemons are running in the background
# each of them returns an encoded message, but only one of them
# will reveal you the secret key
# story is about the three brothers from indiana jones and the holy grail

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
