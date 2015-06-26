#!/usr/bin/env python

width       = 80
chapter     = "chapter05 - unique among many"
description = """
Find the one and true key!

---

Hints: ls(1), cat(1), awk(1), sort(1), uniq(1)
"""

import random

def generate_data():
    lines = ['wekGannOapjayGhobcir',
             'PygOjkiebchivyinEdEu',
             'MyecyachSyGhourJorm6',
             'egavodirbofIdCaveigh',
             'BlooddIajVuvEinnuryi',
             'BonDeijvubCuotuckBem',
             'OrhiafAweidcaytGapki',
             'RedHybphejorGhayctOy',
             'alranianhewnucsalvOa',
             'ceacGueljevdunqualho',
             'RodNeomBarvyeshviark',
             'EpyeecThipCekopemth5',
             'Eetpaj7slucfecIpMig4',
             'NoidofuccaunApEerdad',
             'IgEecWobHougsyownunt',
             'AnHypMockNijpelatPej',
             'jeptojeypshothbatKie',
             '5FricgassIvCualickjo',
             'guKnuAthejDacKorvupp',
             'creykAxTyboptyethpea',
             'frewthoivledudMoffuj',
             'eshtic8ovThugBastas3',
             'nadNefwydzadtywutog2',
             'GejquenJifeevnejrohy',
             'FugWyQuoodebyoHastib',
             'oijmaktyejFofNedutag',
             'quetjaupCeCistachIm$',
             'TiHobEfyakbuhajtaWri']

    num_lines = len(lines)
    with open('data.txt', 'w') as data:
        for i in xrange(1000):
            data.write(lines[random.randrange(100) % num_lines] + '\n')

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




