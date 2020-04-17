from io import BytesIO
import os
from PIL import Image
from torch.utils.data import Dataset
import utils

class MultiResolutionDataset(Dataset):
    def __init__(self, path, transform, resolution=8):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.dir = [os.path.join(path,x ) for x in os.listdir(path)]

        #print(dir_path)
        self.files = [os.path.join(y,os.listdir(y)[0]) for y in self.dir]

        #print(self.files)
        self.path = path
        #self.data = datasets.ImageFolder(path, transform)
        #self.env = lmdb.open(
        #    path,
        #    subdir=True,
        #    max_readers=32,
        #    readonly=True,
        #    lock=False,
        #    readahead=False,
        #    meminit=False,
        #)
        #if not self.env:
        #    raise IOError('Cannot open lmdb dataset', path)
        #with self.env.begin(write=False) as txn:
        self.walk = os.walk(path)
        self.length = len(self.files)
        #int(txn.get('length'.encode('utf-8')).decode('utf-8'))
        self.resolution = resolution
        self.transform = transform

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        #with self.env.begin(write=False) as txn:
        #    key = f'{self.resolution}-{str(index).zfill(5)}'.encode('utf-8')
        #    img_bytes = txn.get(key)
        img = Image.open(self.files[index])
        img = self.transform(img)
        return img

class CondDataset(Dataset):
    def __init__(self, path, transform1, transform2, resolution=8):
        self.dir = [os.path.join(path,x ) for x in os.listdir(path)]
        #print(len (self.dir))
        #print("directory")
        #print(self.dir)
        self.path = path
        self.transform1 = transform1
        self.transform2 = transform2
        self.resl = resolution
        self.lenght = len(self.dir)
    
    def __len__(self):
        return len(self.dir)

    def __getitem__(self, index):
        #print("effefefefeffefefefefefef")
        #print(index)
        folder_i = self.dir[index]
        #print("folder i ")

        #print(folder_i)
        folder_list = [os.path.join(folder_i, x) for x in os.listdir(folder_i)]
        #print("1")
        if len(folder_list) <= 0 :
            #print("remove")
            os.rmdir(folder_i) 
        #print("2")
        folder_list_input = folder_list[-1]
        #print("3")
        folder_list_output = folder_list[:-1]
        #print("4")
        img_input = self.transform1(Image.open(folder_list_input))
        #print("5")
        img_output_list = [self.transform2(Image.open(x)) for x in folder_list_output]
        #img = self.transform(img)
        #print("6")
        return {"input" : img_input, "output" : img_output_list}



    def getitem2(self, index):

        #print("ababababbabbbaababababab")
        #print(index)
        folder_i = self.dir[index]
        #print("folder i ")

        #print(folder_i)
        folder_list = [os.path.join(folder_i, x) for x in os.listdir(folder_i)]
        #print("1")
        if len(folder_list) <= 0 :
            #print("remove")
            os.rmdir(folder_i) 
        #print("2")
        folder_list_input = folder_list[-1]
        #print("3")
        folder_list_output = folder_list[:-1]
        #print("4")
        img_input = self.transform1(Image.open(folder_list_input))
        #print("5")
        img_output_list = [self.transform2(Image.open(x)) for x in folder_list_output]
        #img = self.transform(img)
        #print("6")
        return {"input" : img_input, "output" : img_output_list}


