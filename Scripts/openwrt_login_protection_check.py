# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:42:42 2020

@author: Henry Weckermann (henry.weckermann@smail.inf.h-brs.de)

A script to visualize the behavior of OpenWrt when faced with multiple
wrong login attempts. Uses linear regresion to fit a line in the response 
data of the server. 
"""

import re
import time
import pprint
import requests
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy import stats

# -------------------------------------------------------------------------- #

# Define global parameters
username = "root"
password = "imawrongpassword"
correct_pw = "123"

# Change this if you want more or less connection attempts
no_of_requests = 100

# Change this if your router is in another castle
URL = f"http://192.168.1.1/cgi-bin/luci/admin/status?luci_username={username}&luci_password={password}"

# -------------------------------------------------------------------------- #

# Check if Webserver is alive and connection is possible
tmp = requests.post(URL.replace(password, correct_pw))
if tmp.status_code == 200 and "Invalid username and/or password!" not in tmp.text:
    print(f"Status code {tmp.status_code} -> Webserver found and is accessable via password {correct_pw}")
else:
    print(f"Error. Please check if the webserver is accessable at the specified URL \n {URL[:URL.find('?')+1]} ")

# -------------------------------------------------------------------------- #

# Making the requests to the OpenWrt login page
times = []
for _ in tqdm(range(no_of_requests)):
    start = time.time()
    r = requests.post(URL)
    stop = time.time()
    if r.status_code == 403:
        times.append(stop - start)
    elif r.status_code == 200:
        print("This should not happen if you set a wrong password")
    else:
        print(f"Status Code: {r.status_code}. Please seek help.")

assert len(times) == no_of_requests

# -------------------------------------------------------------------------- #

# Plotting part

# Define x values as the number of requests (so 1, 2, ..., x)
x = range(1, no_of_requests+1)

# Calculate the linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, times)

# Define the matplotlib figure
fig = plt.figure()
ax1 = fig.add_subplot(111)

# Define plots
ax1.scatter(x, times)
ax1.plot(x, intercept + slope*x, 'black', label='Regression line')

# Define looks 
plt.xlabel('Number of POST requests to the OpenWrt webserver')
plt.ylabel('Time to complete the request (sec)')
plt.legend()
plt.grid(True)

plt.show()

# -------------------------------------------------------------------------- #

# Define results
results = {'Mean' : np.round(np.mean(times),3),
           'Median' : np.round(np.median(times),3),
           'Regression coefficient' : str(np.round(r_value,5)) + f" (p = {np.round(p_value,3)})",
           'Standard error' : np.round(std_err, 3)
           }

# Plot results in a nice way. You don't have to understand the print statement. It justs looks better
myStr = pprint.pformat(results)
print(myStr.translate(myStr.maketrans("'{},", "    ")))

# -------------------------------------------------------------------------- #

# Checking if the webserver still responds to a correct login attempt
id_string = "Invalid username and/or password! Please try again."

URL = URL.replace(password, correct_pw)
r = requests.post(URL)
sessionID, token = re.findall("[a-zA-Z0-9]{32}", r.text)

if id_string not in r.text:
    print(f""""Successfully logged in with user {username}. Got Session-ID {sessionID} and token {token}.
           The IP does not seem to be blacklisted by the DUT.""")

# -------------------------------------------------------------------------- #

browser_open = input("Do you want to open the OpenWrt web-interface in your browser (y / n): ")
if browser_open.lower() == "y":
    webbrowser.open_new(URL)
