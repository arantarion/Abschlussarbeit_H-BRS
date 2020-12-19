# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:45:16 2020

@author: hweck
"""

import os
import pandas as pd
import re
from collections import Counter

#os.chdir('Desktop')


# /releases/19.07.4/targets/x86/generic/openwrt-19.07.4-x86-generic-combined-ext4.img.gz
def find_target(firmwares):
    reg = "/targets/.*/"
    result = [re.findall(reg, firmware) for firmware in firmwares]
    result = [item for sublist in result for item in sublist]
    return [item[9:] for item in result]


def find_version(firmwares):
    reg = "(\d{2}\.\d{2}\.\d{1})"
    result = [re.findall(reg, firmware) for firmware in firmwares]
    result = [lst for lst in result if lst != []]
    result = [lst[0] for lst in result]
    return result


df = pd.read_csv('stats.csv', sep=";")
df2 = pd.read_csv('stats2.csv', sep=";")

firmwares1 = list(df['Image'])
firmwares2 = list(df2['Firmware'])


targets = find_target(firmwares1)
targets2 = find_target(firmwares2)

version = find_version(firmwares1)
version2 = find_version(firmwares2)


target1_counter = Counter(targets)
target2_counter = Counter(targets2)

version1_counter = Counter(version)
version2_counter = Counter(version2)
