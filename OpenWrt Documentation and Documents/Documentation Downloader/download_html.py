# -*- coding: utf-8 -*-

import re
import os
import requests
from tqdm import tqdm

CMD = "?do=export_xhtml"
FOLDER = "OpenWrtWiki_QuickStart_Doku_xhtml"
TYPE = 'quick-start'

f = open("openwrt_org_all_links.txt", "r")
content = f.read()
f.close()

urls = list(set(re.findall(r'(https?://\S+)', content)))
urls = [url + CMD for url in urls if f"docs/guide-{TYPE}" in url]

try:
    os.mkdir(f"{os.getcwd()}/{FOLDER}")
except: 
    pass

for url in tqdm(urls):

    startpos = url.find(f"/guide-{TYPE}/") + len(f'/guide/{TYPE}/')
    filename = url[startpos: -len(CMD)]
    filename = filename.replace("/", "_")
    
    response = requests.get(url)
    
    try:
        with open(f"{FOLDER}/{filename}.html", "xb") as file:
            file.write(response.text.encode('UTF-8', "ignore"))
    except:
        continue