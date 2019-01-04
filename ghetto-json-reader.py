
# Code from Mils Werner
# Found on the website: https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file

import json
from pprint import pprint

filename = input("Name of file:\n")

with open(filename + '.json') as f:
    print(f)
    data = json.load(f)
    
pprint(data)
