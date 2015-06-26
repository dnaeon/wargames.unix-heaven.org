#!/usr/bin/env python

width       = 80
chapter     = "chapter12 - daemons"
description = """
The secret key is guarded by a daemon, be careful!

---

Hints: cat(1), awk(1), ls(1), tr(1), ps(1), top(1), strace(1),
       tty(1), pstree(1), daemon(3), lsof(8), tset(1), init(8)
"""

# a daemon runs in the background and holds a file opened
# every char in the file it holds is rotated by 13 (rot13) chars
# find the daemon, find the file and decode it
# how to build the daemon
#
#	gcc beastie.c -o beastie
#
# TODO: make sure you watch if the daemon dies to restart it

def generate_data():
    data = """"HAVK vf onfvpnyyl n fvzcyr bcrengvat flfgrz,
ohg lbh unir gb or n travhf gb haqrefgnaq gur fvzcyvpvgl."

        - Qraavf Evgpuvr

Gur frperg xrl lbh ner ybbxvat sbe vf "cyna9"
"""

    with open('frperg-xrl.13', 'w') as fobj:
        fobj.write(data)
    
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
