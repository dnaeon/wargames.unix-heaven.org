#!/usr/bin/env python

width       = 80
chapter     = "chapter08 - x marks the spot"
description = """
Hmm, no hints in here..?
"""

# might want to set grep = "export GREP_COLOR='3;32'"

import string
import random

def generate_data(path, data):
    with open(path, 'w') as f:
        # the evil number... 
        for i in xrange(666):
            f.write(data[random.randrange(1000) % len(data)])

def create_chapter():
    line = '+' + ('-' * (len(chapter) + 2)) + '+'
    with open(chapter.split(' ')[0] + '.txt', 'w') as fobj:
        print >>fobj, line.center(width)
        print >>fobj, ('| ' + chapter.title() + ' |').center(width)
        print >>fobj, line.center(width)
        print >>fobj, description

def main():
    data = ['AcWDmsYbf39eJx6wKZy7UIAouNj8tdLF0qgcMa5v4kG2HVrTQEpihOl1RPnS\n',
            'Cf2XXXXXXX9IVXXvAgomX0jXXX2sXXXXXXXrUXXM2IcizXXJOfxpXXlasj87\n',
            'FaxXL3xMPazUOXXLcaUVXILGXC46XJCtb9af8XkX01YxXUXLeJGXQGiX31ba\n',
            'MuIXDuSvVREChXGXcDIwXv1oXcAOXdCQE15ZWXZ8XlfXOlXpjvX3orzaX0a1\n',
            'CaqZUy28ps96ThQC1aSfjWDPd9NAOH0cx7lzVvuFoMe3IbimLYrBGn5Jk4RK\n',
            'PzxX8MqtFdKAHXvPdXmVXiT2Xz6VXmKrKfXIPXYmsQF87MX0LDXXXXXXXman\n',
            'SkfXai19IaswbXcLQwXtX3pzXzs5XpG7biXNEXOQY8ncaZXUBJXadRs8X0zx\n',
            'Z2874jhnabsfjhjas09g8aAhjagJBsoLDGJuSAFAsmnmmnasf9ak124jazxc\n',
            'T9pXXXXXXXyCsXmWEvFXXVuXXXexXXXXXXXWfXUFMvpZm2XCaoXcu6raXhag\n',
            'YGkI7F28D3Jrhj4T6xbzC1anS9OudN9L0BcU5KPMQqsHpgvVZRiwteEWmlfA\n',
            'NhaXXXXXXX5kNX4SXtIyXT0iX6F0XM4XXXXGcXwNzXXAYNXKWTXHUp9AXlda\n']

    create_chapter()

    generate_data('data1.txt', data[:3])
    generate_data('data2.txt', data[3:7])
    generate_data('data3.txt', data[7:])
    
if __name__ == '__main__':
    main()




