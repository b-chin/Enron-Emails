#!/usr/bin/env python3


import json
with open('csc-485-enron-emails-export.json') as json_data:
    d = json.load(json_data)
    


emails = {}
for key, value in d.items():
    #print(key, len([item for item in value if item]))
    count=0
    for i in value:
        for pkey in i:
            if pkey == "X-To":
                emails[key] = (i[pkey], count)
                
        count+=1
print(emails)
                
                
                
    
    
