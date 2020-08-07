import os
import glob
import cv2
import json
import numpy as np
import re

extension = ('.jpg')


def create_frame(frame_name):
    # Loading image data from file
    img = cv2.imread(frame_name, 1)
    # img = cv2.imread("black.jpg", 1)

    filenum = int(re.search(r'\d+', frame_name).group())

    print (filenum)

    for x in range(filenum, 1, -1):

        bees_in_frame = d['frames'][x-1]['frame_data']
        bees_in_prev_frame = d['frames'][x-2]['frame_data']

        list_prev_bees = []
        for bee in bees_in_prev_frame:
            list_prev_bees.append(bee['shape'])

        for bee in bees_in_frame:
            # print ("Parsing ", bee['shape'], " of frame ", filenum)
            if bee['shape'] in list_prev_bees:

                prev_bee = bees_in_prev_frame[list_prev_bees.index(
                    bee['shape'])]

                # print(bee['mid'], prev_bee['mid'])

                point0 = round(bee['mid'][0]), round(bee['mid'][1])
                point1 = round(prev_bee['mid'][0]), round(prev_bee['mid'][1])

                # cv2.line(img, tuple(point0), tuple(point1),
                #          tuple(colors[bee['shape']]), 3)

                cv2.line(img, tuple(point0), tuple(point1),
                           tuple(colors[bee['shape']]), 3)

                # cv2.namedWindow('image',cv2.WINDOW_NORMAL)
                # cv2.resizeWindow('image', 800,450)
                # cv2.imshow('image', img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
        cv2.imwrite("./modified_frames/" + str(filenum).zfill(3) + ".jpg", img)


with open('midpoints.json') as f:
    d = json.load(f)

with open('./colors.json') as q:
    c = json.load(q)

os.chdir(".")
colors = c['colors']

for file in sorted(glob.glob("./data/*.jpg")):
    filename = file.split('.')[0]
    if filename != "001":                   # Skipping the first image
        print (file)
        create_frame(file)

    frameSize = (1920, 1088)
    out = cv2.VideoWriter('output_video.avi',
                          cv2.VideoWriter_fourcc(*'DIVX'), 3, frameSize)

for filename in sorted(glob.glob('./modified_frames/*.jpg')):
    img = cv2.imread(filename)
    out.write(img)

out.release()
