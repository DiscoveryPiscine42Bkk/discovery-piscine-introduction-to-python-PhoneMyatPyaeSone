#!/usr/bin/env python3

import sys

def shrink(s):
    print(s[:8]) 
def enlarge(s):
    num_z_to_add = 8 - len(s) 
    print(s + ('Z' * num_z_to_add))

parameters = sys.argv[1:]

if not parameters:
    print("none")
else:
    for param in parameters:
        param_length = len(param)

        if param_length > 8:
            shrink(param)
        elif param_length < 8:
            enlarge(param)
        else:
            print(param)