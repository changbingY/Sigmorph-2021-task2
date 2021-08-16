#!/usr/bin/env python
# coding: utf-8


import numpy as np
import copy
import collections
import argparse
from argparse import ArgumentParser

def Remove(language_name):
    file = open("../data/"+language_name+".5.preds",'r')
    lines = file.readlines()
    datalists = []
    indexlist_id = []
    for index, line in enumerate(lines):
        if line == '\n':
            indexlist_id.append(index)
    with open("../data/Language_remove_big.txt", "w") as f_new: ##remove big paradigms(equal to or larger than 20 words) 
        for i in range(1,len(indexlist_id)):
            if 1< indexlist_id[i]-indexlist_id[i-1]-1 <=20:
                for n in range(len(lines)):
                    if indexlist_id[i-1]<n<=indexlist_id[i]:
                        f_new.write(lines[n])
                    
if __name__ == '__main__':
    parser = ArgumentParser(description='Removing large paradigms')
    parser.add_argument('--language',type=str, help='The ground truth file')
    args = parser.parse_args()
    Remove(args.language)
