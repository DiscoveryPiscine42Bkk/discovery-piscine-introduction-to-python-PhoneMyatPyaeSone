#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    target_string = sys.argv[2]
    matches = re.findall(keyword, target_string)
    count = len(matches)

    if count == 0:
        print("none")
    else:
        print(count)