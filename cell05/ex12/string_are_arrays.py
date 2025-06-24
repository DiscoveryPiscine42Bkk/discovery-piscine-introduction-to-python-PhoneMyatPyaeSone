#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]

    z_count = 0
    for char in input_string:
        if char == 'z':
            z_count += 1

    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")