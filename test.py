import requests
import json

import os


print(os.listdir("./miner/data/users"))
exit(0)
r = requests.get("http://example.com/foo/bar")


for i,j in enumerate(r.__dict__):
    print(i,j)
    print("\t",r.__dict__[j])


print(s)


import sys

print("\n".join(sys.argv))
