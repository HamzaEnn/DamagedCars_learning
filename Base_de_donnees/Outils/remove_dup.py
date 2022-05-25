# Programme pour éliminer les doublons en comparant les HashCodes de chacune des images avec les autres
# et supprimant ainsi les images présents plusieurs fois dans le fichier.

import hashlib
from imageio import imread
import cv2
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os

def file_hash(filename):
    with open(filename,'rb') as f:
        return md5(f.read()).hexdigest()
os.getcwd()

os.chdir(r'/home/cross/Hamza/pare-brise/')
os.getcwd()
files_list = os.listdir('.')
print (len(files_list))
duplicates=[]
hash_keys=dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=index
        else:
            duplicates.append((index,hash_keys[filehash]))
print(duplicates)

for index in duplicates:
    os.remove(files_list[index[0]])
