#!/usr/bin/env python
# coding: utf-8


import numpy as np
import copy
import collections

file = open("../data/Language.5.preds",'r')
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
