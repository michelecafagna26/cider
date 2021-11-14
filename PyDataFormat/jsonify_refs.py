"""
Code to convert mat file with structures into json files
Created on : 5/18/15 3:27 PM by rama
"""

import scipy.io as io
import os
import json

pathToMat = '/Users/rama/Research/data/pyCider/'
mat_file = 'pascal_cands.mat'
json_file = 'pascal_cands'

data = io.loadmat(os.path.join(pathToMat, mat_file))
refs = list(data['cands'][0])

A = []
B = []

for image in refs:
    for sentences in image[1]:
        for i, sent in enumerate(sentences):
            sent_struct = {}
            imname = str(image[0][0]).split('/')[-1]
            sent_struct['image_id'] = imname
            string_sent = sent[0].strip().split('\\')
            if len(string_sent) == 1:
                sent_struct['caption'] = string_sent[0]
            else:
                sent_struct['caption'] = ' '.join(string_sent[:-1])
            if i == 1:
                A.append(sent_struct)
            else:
                B.append(sent_struct)

with open(os.path.join(pathToMat, json_file + 'A.json'), 'w') as outfile:
    json.dump(A, outfile)

with open(os.path.join(pathToMat, json_file + 'B.json'), 'w') as outfile:
    json.dump(B, outfile)
