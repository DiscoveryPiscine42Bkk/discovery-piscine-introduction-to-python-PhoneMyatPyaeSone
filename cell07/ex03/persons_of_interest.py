#!/usr/bin/env python3

def famous_births(people):
    sorted_list = sorted(
        people.values(),
        key=lambda info: int(info['date_of_birth'])
    )

    for info in sorted_list:
        name = info['name']
        dob  = info['date_of_birth']
        print(f"{name} is a great scientist born in {dob}.")


women_scientists = {
    "ada":     {"name": "Ada Lovelace",   "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne",   "date_of_birth": "1900"},
    "lise":    {"name": "Lise Meitner",   "date_of_birth": "1878"},
    "grace":   {"name": "Grace Hopper",   "date_of_birth": "1906"}
}

famous_births(women_scientists)