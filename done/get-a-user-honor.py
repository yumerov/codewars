# https://www.codewars.com/kata/get-a-users-honor/train/python

import requests as r
import re

def get_honor(username):
    r.packages.urllib3.disable_warnings()
    url = "https://www.codewars.com/users/" + username
    content = r.get(url, verify=False).content
    pattern = '<div class="stat"><b>Honor:</b>(\d*,?\d+)</div>'
    points_in_raw = re.search(pattern, content, flags=re.M).group(1)
    return int(points_in_raw.replace(",", ""))