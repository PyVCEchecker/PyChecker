#!/usr/bin/env python

from __future__ import print_function

# make sure we're testing colors module in this dir, not system
import sys, os
sys.path.insert(0, os.path.abspath('.'))

from colors import color, COLORS, STYLES

def test_styles(bg, fg):
    for style in (None,) + STYLES:
        cname = fg or 'default'
        # renamed None color to default to avoid confusion wiht normal style
        if cname.startswith('bright'):
            cname = cname[6:].upper()
        text = cname[:5].ljust(6)
        print(color(text, fg=fg, bg=bg, style=style), end=' ')
    print()

# doubled number of colors, so have to split test into halves to
# test on standard 80-column terminal

colors  = [None,] + list(COLORS[:8])
brights = list(COLORS[8:])

for bg in colors:
    for fg in colors:
        test_styles(bg, fg)
    for fg in brights:
        test_styles(bg, fg)
for bg in brights:
    for fg in colors:
        test_styles(bg, fg)
    for fg in brights:
        test_styles(bg, fg)
        
for i in range(256):
    if i % 64 == 0:
        print()
    print(color(' ', bg=i), end='')

print()
