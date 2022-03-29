import matplotlib.pyplot as plt
import os
import shutil

import numpy as np
import PIL
from PIL import Image
import os, sys
from scipy.io import loadmat

# !git clone https://github.com/HamzaEnn/DamagedCars_learning.git
path = "./DamagedCars_learning/Base de donnees//"



def load_data(data_path, classes, dataset='Entrainement', image_size=64):

    num_images = 0
    for i in range(len(classes)):
        dirs = sorted(os.listdir(data_path + dataset + '/' + classes[i]))
        num_images += len(dirs)
                                
    x = np.zeros((num_images, image_size, image_size, 3))
    y = np.zeros((num_images, 1))
    
    current_index = 0
    
    # Parcours des différents répertoires pour collecter les images
    for idx_class in range(len(classes)):
        dirs = sorted(os.listdir(data_path + dataset + '/' + classes[idx_class]))
        num_images += len(dirs)
        # Chargement des images, 
        for idx_img in range(len(dirs)):
            item = dirs[idx_img]
            if os.path.isfile(data_path + dataset + '/' + classes[idx_class] + '/' + item):
                try :
                    # Ouverture de l'image
                    img = Image.open(data_path + dataset + '/' + classes[idx_class] + '/' + item)
                    # Conversion de l'image en RGB
                
                    img = img.convert('RGB')
                
                    # Redimensionnement de l'image et écriture dans la variable de retour x 
                    img = img.resize((image_size,image_size))
                    x[current_index] = np.asarray(img)
                    # Écriture du label associé dans la variable de retour y
                    y[current_index] = idx_class
                    current_index += 1
                except :
                    pass
    return x, y


labels = ['pare-brise', 'Front', 'Porte', 'pare_chocs']

x_train, y_train = load_data(path, labels, dataset='Entrainement', image_size=64)
print(x_train.shape, y_train.shape)

x_val, y_val = load_data(path, labels, dataset='Validation', image_size=64)
print(x_val.shape, y_val.shape)

x_test, y_test = load_data(path, labels, dataset='Test', image_size=64)
print(x_test.shape, y_test.shape)



plt.figure(figsize=(12, 12))
shuffle_indices = np.random.permutation(9)
for i in range(0, 9):
    plt.subplot(3, 3, i+1)
    image = x_train[shuffle_indices[i]]
    plt.title(labels[int(y_train[shuffle_indices[i]])])
    plt.imshow(image/255)

plt.tight_layout()
plt.show()