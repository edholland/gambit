#!/usr/bin/env python

import requests
import re

def f(x):
    return (int(x) + mod) % 1000 #dirty use of global for lazyness

r = requests.get('http://quiz.gambitresearch.com/')
mod = int(re.search( "parseInt.x. . (\d+)", r.text ).group(1))
match = re.search( "(\d+) (.) (\d+) (.) (\d+)", r.text )
expression = [ f(match.group(1)), match.group(2), f(match.group(3)), match.group(4), f(match.group(5)) ]
result = eval(''.join(map(str,expression))) #This is fairly safe due to the regex validation
r2 = requests.get('http://quiz.gambitresearch.com/job/%s' % result, cookies=r.cookies)
print r2.text
