from config.config import *
import json
import os
import requests

def print_dict(d):
    for i, j in enumerate(d):
        print(i, j)
        print("\t", d[j])

offset = 0
step = 4900

while(True):

    files = os.listdir('./data/users/')

    response = requests.get("https://api.vk.com/method/friends.get",
                            {"user_id": id,
                             "count":step
                             "offset": offset,
                             "count": step,
                             "fields": "nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig, has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message, can_see_all_posts, can_post, universities",
                             "v": "5.130",
                             "access_token": Config.token})
    r = R(response)
    if (not r):
        print("members' friends ended unexpectedly")