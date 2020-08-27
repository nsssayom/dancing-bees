import os
import glob
import cv2
import json
import numpy as np
import re
import sys
import math
import csv


def euclidian_distance(point_1, point_2):
    return math.sqrt(pow(point_2[1] - point_1[1], 2) +
                     pow(point_2[0] - point_1[0], 2))


with open('mid-mod-3.json') as f:
    d = json.load(f)
frames = d['frames']

target_bees = ['bee7', 'bee14', 'bee16', 'bee17', 'bee18',
               'bee19', 'bee23', 'bee24', 'bee28', 'bee30']

bee_dict = {}

fieldnames = ['bee', 'frame-1', 'frame-2', 'frame-3', 'frame-4', 'frame-5', 'frame-6',
                'frame-7', 'frame-8', 'frame-9', 'frame-10', 'frame-11', 'frame-12',
                'frame-13', 'frame-14', 'frame-15']


for target_bee in target_bees:

    file_csv = open('distance/distance-' + str(target_bee) + '.csv', mode='w')
    with file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=fieldnames)
        writer.writeheader()

    for bee_num in range(1, 102):
        object_bee = "bee" + str(bee_num)
        bee_dict['bee'] = object_bee

        frame_count = 1
        for frame in frames:
            for bee in frame:
                if target_bee in bee:
                    center = bee[target_bee]
                    break
            for bee in frame:
                if object_bee in bee:
                    bee_dict['frame-' + str(frame_count)] = euclidian_distance(center, bee[object_bee])
            
            frame_count = frame_count + 1
        
        with open('distance/distance-' + str(target_bee) + '.csv','a+') as fd:
            writer = csv.DictWriter(fd, fieldnames)
            writer.writerow(bee_dict)
            
        print(bee_dict)
        print ("-----------------------")
        bee_dict.clear()
            
