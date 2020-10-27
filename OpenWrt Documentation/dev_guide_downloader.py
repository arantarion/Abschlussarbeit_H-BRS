# -*- coding: utf-8 -*-
"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import re
import os
import requests
from tqdm import tqdm

CMD = "?do=export_raw"
FOLDER = "OpenWrtWiki_Dev_Doku"

f = open("sitemap.xml", "r")
content = f.read()
f.close()

urls = list(set(re.findall(r'(https?://\S+)', content))) # get all urls from sitemap
urls = [url[:-6] for url in urls] # remove </loc> at the end
urls = [url + CMD for url in urls if "docs/guide-developer" in url] # extract only the user guide urls

try:
    os.mkdir(f"{os.getcwd()}/{FOLDER}")
except: 
    pass

for url in tqdm(urls):

    startpos = url.find("/guide-user/") + len('/guide/user/')
    filename = url[startpos: -len(CMD)]
    filename = filename.replace("/", "_")
    
    response = requests.get(url)
    
    try:
        with open(f"{FOLDER}/{filename}.txt", "xb") as file:
            file.write(response.text.encode('UTF-8', "ignore"))
    except:
        continue