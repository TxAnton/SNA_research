import requests

from config.config import Config

r = requests.get("http://example.com/foo/bar")

Config.token

for i,j in enumerate(r.__dict__):
    print(i,j)

# print(r.__dict__)