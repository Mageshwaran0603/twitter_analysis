#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        tweet = json.loads(line)
        if 'user' in tweet and 'friends' in tweet['user']:
            user = tweet['user']['screen_name']
            friends = tweet['user']['friends']
            for friend in friends:
                if user < friend:
                    print(f"{user},{friend}\t{friends}")
                else:
                    print(f"{friend},{user}\t{friends}")
    except Exception as e:
        sys.stderr.write(f"Error processing JSON: {e}\n")
        continue
