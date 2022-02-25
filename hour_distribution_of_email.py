# findout the distribution of hours of messages/emails by pulling hours from
# the 'From 'line

import re

hours_dict = dict()
fname = input('Enter filename: ')

with open(fname) as f:
    for l in f:
        #only return the lines that match format 'From '
        if not l.startswith('From '):
            continue
        raw_line = l.rstrip()
        #finds the regex time pattern from raw_line
        #and return the 1st position (namely the hour)
        hours = re.findall(r"([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]",raw_line)

        for h in hours:
            hours_dict[h] = hours_dict.get(h,0) + 1

#Option 1: 
    for k,v in sorted(hours_dict.items()):
        print(k,v)

#Option 2:    
    # for key, value in hours_dict.items():
    #     hours_list.append((key,value))
    # hours_list = sorted(hours_list)
    
    # print('H_List:',hours_list)
    # for k,v in hours_list:
    #     print(k,v)