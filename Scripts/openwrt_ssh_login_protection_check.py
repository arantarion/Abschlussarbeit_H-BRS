# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:34:27 2020

@author: Henry Weckermann (henry.weckermann@smail.inf.h-brs.de)

A script to visualize the behavior of OpenWrt when faced with multiple
wrong login attempts to the ssh server. 
Uses linear regresion to fit a line in the response data of the server. 
"""

import time
import pprint
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy import stats
from SSHLibrary import SSHLibrary

# -------------------------------------------------------------------------- #

# Global parameters
IP = '192.168.1.1'
PORT = 22

USERNAME = "root"
PASSWORD = "imawrongpw"
CORR_PW = "123"

# Number of login attempts
# the ssh test is relatively slow so keep that in mind
no_of_requests = 40

# initalize ssh lib object
ssh = SSHLibrary()

# -------------------------------------------------------------------------- #

# Sanity checks
connection_status = ssh.open_connection(IP, port=PORT)

if connection_status != 1:
    print("The SSH Server is not reachable. Please try something different")
    exit(0)


openwrt_banner = ssh.login(USERNAME, CORR_PW)
if "built-in shell (ash)" not in openwrt_banner:
    print("Server is reachable but no login is possible.")
    exit(0)

# -------------------------------------------------------------------------- #

# Testing
times = []
for _ in tqdm(range(no_of_requests)):
    failed = False
    start = time.time()
    try:
        ssh.open_connection(IP, port=PORT)
        ssh.login(USERNAME, PASSWORD)
    except:
        ssh.close_connection()
        failed = True    
    stop = time.time()
    
    if failed:
        times.append(stop-start)
    else:
        print("This should not happen.")
        exit(0)

# Checking if all login attempts have been made.
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
plt.xlabel('Number of login attempts at the ssh server')
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

# Final login to see if login is still possible
print("\n\nThis should print the OpenWrt Banner if the ssh server did not block the IP\n")
ssh.open_connection(IP, port=PORT)
openwrt_banner_new = ssh.login(USERNAME, CORR_PW)
print(openwrt_banner_new)