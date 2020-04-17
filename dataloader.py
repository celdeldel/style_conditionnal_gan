import os
import torch
import numpy as np
from io import BytesIO
import scipy.misc
#import tensorflow as tf
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from torch.autograd import Variable
from matplotlib import pyplot as plt
from PIL import Image
from dataset import CondDataset



def cycle(iterable):
    while True:
        for x in iterable:
            yield x




class dataloaderYes:
    def __init__(self, path, transform1, transform2, resolution=4):
        self.root = path
        self.batch_table = {4:400, 8:400, 16:400, 32:200, 64:100, 128:50, 256:15, 512:5 , 1024:1} # change this according to available gpu memory.
        self.batchsize = int(self.batch_table[pow(2,2)])        # we start from 2^2=4
        self.imsize = int(pow(2,2))
        self.num_workers = 2
        self.transform1 = transform1
        self.transform2 = transform2
        self.dataset = CondDataset(path, transform1,transform2, resolution)
        self.dataloader = DataLoader(
            dataset=self.dataset,
            batch_size=self.batchsize,
            shuffle=True,
            num_workers=self.num_workers)

        
    def renew(self, resl):
        print('[*] Renew dataloader configuration, load data from {}.'.format(self.root))
        
        self.batchsize = int(self.batch_table[resl])
        self.imsize = int(resl)
        print("renew resl")
        print(self.imsize)
        print(self.batchsize)
        self.dataset = CondDataset(self.root, self.transform1, self.transform2, resl)      

        self.dataloader = DataLoader(
            dataset=self.dataset,
            batch_size=self.batchsize,
            shuffle=True,
            num_workers=self.num_workers)
        

    def __iter__(self):
        return iter(cycle(self.dataloader))
    
    def __next__(self):
        return next(self.dataloader)

    def __len__(self):
        return len(self.dataloader.dataset)

      
    def get_batch(self, index):
        print("get batch ")
        print(self.batchsize)
        print(self.imsize)
         
        print("dataIter")

        #print(dataIter)
        return self.dataset.getitem2(index)#[0].mul(2).add(-1)         # pixel range [-1, 1]
    

        









