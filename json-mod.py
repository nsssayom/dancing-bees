import os
import glob
import cv2
import json
import numpy as np
import re
import sys
import math
import csv

# with open('midpoints.json') as f:
#     d = json.load(f)
# data = d['frames']

# for frame in data:
#     frame.pop('frame', None)

# with open('mid-mod.json', 'w') as data_file:
#     json.dump(d, data_file)

with open('mid-mod-3.json') as f:
    d = json.load(f)
frames = d['frames']

# print(data[0]['frame_data'][0])

#for frame in data:
#    frames[]

# with open('mid-mod-3.json', 'w') as data_file:
#     json.dump(d, data_file)

# with open('mid-mod-2.json') as f:
#     d = json.load(f)
# data = d['frames']

# print(data[0]['frame_data']['bee1'])

if 'bee2' in frames[0][0]:
    print("Found")