#!/usr/bin/env python3
import sys

parameters = sys.argv[1:]

# Check if there are any parameters
if not parameters:
    print("none")
else:
    # Iterate through each parameter using a for loop
    for param in parameters:
        # Check if the parameter already ends with "ism" (case-sensitive)
        if not param.endswith("ism"):
            # If it doesn't, append "ism" and print it
            print(param + "ism")