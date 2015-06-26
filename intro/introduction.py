#!/usr/bin/env python

width       = 80
chapter     = "introduction"
quote       = '"SHALL WE PLAY A GAME?"'
description = """

## Welcome

Welcome to the Unix/Linux Wargames!

This game is about Unix/Linux, and more precisely how to use Unix/Linux!

The goal of the game is to teach you how to use Unix and solve
real-world problems that Unix/Linux sysadmins face every day.

The approach we take to teaching you some Unix is by playing a game,
where you, the player would have to solve a task using the Unix
command-line tools, thus getting you familiar with the Unix system,
the tools, and the philosophy of Unix!

Working on Unix/Linux is supposed to be fun, and by this game
we try to bring some fun and entertainment in your journey with Unix/Linux!

Hope you enjoy it! :)

## Recommended reading

Before starting off with the game it is recommended that you read the FAQ.

The Unix Wargames FAQ can be found on the link below and contains important
information about the game itself and how to look for help in case you need it.

* http://wargames.unix-heaven.org/faq

You can also join the discussion on our forums where you can look for help,
or help others by giving them some hints. 

* http://wargames.unix-heaven.org/forums/index.php

## Getting started

Enough of the boring stuff already, let's play a game!

To approach your first challenge, login to chapter00 using these details:

Username: chapter00
Password: skuvdogboocKasginkeyctof
Hostname: wargames.unix-heaven.org
SSH Port: 1337

And remember, this is a game, so make sure you enjoy it while playing it! :)
"""

def main():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'
    fobj = open(chapter.split(' ')[0] + '.txt', 'w')
    
    print >>fobj, line.center(width)
    print >>fobj, ('| ' + chapter.title() + ' |').center(width)
    print >>fobj, line.center(width)

    print >>fobj, "\n"
    print >>fobj, quote.center(width)
    
    print >>fobj, description

    fobj.close()

if __name__ == '__main__':
    main()




