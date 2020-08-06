import os
import json
import glob

data = {}
data['frames'] = []

def getMid(point0, point1):
    return [(point0[0] + point1[0]) / 2, (point0[1] + point1[1]) / 2]

def read_file(filename):
    
    with open(filename) as f:
        d = json.load(f)
        shapes = d["shapes"]
        frame = []
        for x in range(len(shapes)):
            p = shapes[x]["points"]
            if len(p) != 0:
                frame.append({
                    'shape': shapes[x]['label'],
                    'mid': getMid(p[0], p[1])
                })

    data['frames'].append({
        'frame': filename,
        'frame_data': frame
    })        

# for subdir, dirs, files in os.walk(rootdir):
#     files.sort()
#     for file in files:
#         ext = os.path.splitext(file)[-1].lower()
#         if ext in extension:
#             file_path =  os.path.join(subdir, file)
#             print (file_path)
#             read_file(file_path) 

for file in sorted(glob.glob("./data/*.json")):
    read_file(file)

print(data)
with open('midpoints.json', 'w') as outfile:
    json.dump(data, outfile)