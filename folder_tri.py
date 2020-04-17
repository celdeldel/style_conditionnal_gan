import os
import shutil

root = "data_brands_modified"

listdir = os.listdir(root)
for x in listdir: 
    xlist = os.listdir(os.path.join(root, x))
    if len(xlist) == 1:
        shutil.rmtree(os.path.join(root, x))
        print('len xlist == 0')
        print(x)

