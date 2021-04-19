# import sys
# print("\n".join(sys.argv))

from config.config import *
import json

import requests

def print_dict(d):
    for i, j in enumerate(d):
        print(i, j)
        print("\t", d[j])

offset = 0
step = 900

while(True):
    response = requests.get("https://api.vk.com/method/groups.getMembers",
                 {"group_id":Config.sel,
                  "sort":"id_asc",
                  "offset":offset,
                  "count":step,
                  "fields":"sex, bdate, city, country, photo_50, photo_100, photo_200_orig, photo_200, photo_400_orig, photo_max, photo_max_orig, online, online_mobile, lists, domain, has_mobile, contacts, connections, site, education, universities, schools, can_post, can_see_all_posts, can_see_audio, can_write_private_message, status, last_seen, common_count, relation, relatives",
                  "v":"5.130",
                  "access_token":Config.token})
    r = R(response)
    if(not r):
        print("'grop members' ended unexpectedly")

    print("MEMBERS: ",offset,'-',offset+r["count"])

    for user in r["items"]:
        with open(f'./data/users/{user["id"]}.json', 'w') as fp:
            json.dump(user,fp,indent=2,ensure_ascii=False)

    if(r["count"] == step):
        offset+=step

    else:
        break

