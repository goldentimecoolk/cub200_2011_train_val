'''
=========================
IMAGES AND CLASS LABELS:
=========================
Images are contained in the directory images/, with 200 subdirectories (one for each bird species)

------- List of image files (images.txt) ------
The list of image file names is contained in the file images.txt, with each line corresponding to one image:

<image_id> <image_name>
------------------------------------------


------- Train/test split (train_test_split.txt) ------
The suggested train/test split is contained in the file train_test_split.txt, with each line corresponding to one image:

<image_id> <is_training_image>

where <image_id> corresponds to the ID in images.txt, and a value of 1 or 0 for <is_training_image> denotes that the file is in the training or test set, respectively.
------------------------------------------------------


------- List of class names (classes.txt) ------
The list of class names (bird species) is contained in the file classes.txt, with each line corresponding to one class:

<class_id> <class_name>
--------------------------------------------


------- Image class labels (image_class_labels.txt) ------
The ground truth class labels (bird species labels) for each image are contained in the file image_class_labels.txt, with each line corresponding to one image:

<image_id> <class_id>

where <image_id> and <class_id> correspond to the IDs in images.txt and classes.txt, respectively.
---------------------------------------------------------
'''

import os
import shutil
import math


file_root = '/home/jsk/s/prcv/dataset/cub200/raw/CUB_200_2011'
image_root = os.path.join(file_root,'images')
split_image_root = '/home/jsk/s/prcv/dataset/cub200/split'

# read label, split, name information.
filename = 'images.txt'
f = open(file_root+'/'+filename)
info_id_name = f.readlines()
f.close()

filename = 'train_test_split.txt'
f = open(file_root+'/'+filename)
info_id_cls = f.readlines()
f.close()

assert len(info_id_name) == len(info_id_cls)

num_images = len(info_id_name)
for i in range(num_images):
    id_name = info_id_name[i]
    id_cls = info_id_cls[i]

    id_name = id_name.split()
    id_cls = id_cls.split()
    #print(id_name)
    #print(id_cls)

    id1, id2 = id_name[0], id_cls[0]
    assert id1 == id2

    name = id_name[1]
    cls = id_cls[1]
    # establish source image path
    image_src = os.path.join(image_root,name)

    # establish destination image path
    label = name.split('/')[0].split('.')[0]
    img_name = name.split('/')[1]

    for split in ['train','val']:
        folder = os.path.join(split_image_root,split,label)
        if not os.path.exists(folder):
            os.mkdir(folder)

    if cls == '0':
        image_dst = os.path.join(split_image_root,'val',label,img_name)
    elif cls == '1':
        image_dst = os.path.join(split_image_root,'train',label,img_name)

    #print(image_src,image_dst)
    shutil.copyfile(image_src,image_dst)
