#!/usr/bin/env python
# Randon six digits + letters
from random import choice
from string import digits,ascii_letters

code = list()
for i in range(6):
    code.append(choice(ascii_letters))
    code.append(choice(digits))
print ''.join(code)
