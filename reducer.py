#!/usr/bin/env python3

import sys

current_pair = None
mutual_friends = []

for line in sys.stdin:
    line = line.strip()
    if line:
        pair, friends = line.split("\t")
        if current_pair != pair:
            if current_pair:
                print(f"{current_pair}\t{','.join(mutual_friends)}")
            current_pair = pair
            mutual_friends = []
        mutual_friends.append(friends)

if current_pair:
    print(f"{current_pair}\t{','.join(mutual_friends)}")
