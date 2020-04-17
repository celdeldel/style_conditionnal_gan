import os
import cv2
import random

def get_all_files(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))
    return files



def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation) for im in im_list]
    return cv2.hconcat(im_list_resize)

def get_concat_h(img_list, size, nb=1): 
    len_img = len(img_list)
    for i in range(nb):
        if len_img <= i:
            img_list.append(img_list[int(random.random()*len_img)])
    img_list = [cv2.resize(x, size, interpolation = cv2.INTER_AREA) for x in img_list]    
    new_im =  hconcat_resize_min(img_list, interpolation=cv2.INTER_CUBIC)
    final_size = (size[0],nb*size[1] )
    new_im = new_im[0:final_size[0], 0:final_size[1]]
    return new_im


