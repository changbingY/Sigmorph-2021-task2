#!/usr/bin/env python
# coding: utf-8


import numpy as np

all_word = []
file = open("Language.5.preds",'r')
lines = file.readlines()
datalists = []
indexlist_id = []

for index, line in enumerate(lines):
    if line == '\n':
        indexlist_id.append(index)

with open("Language_just20_remove_big.txt", "w") as f29:
    for i in range(1,len(indexlist_id)):
        if 1< indexlist_id[i]-indexlist_id[i-1]-1 <=20:
            for n in range(len(lines)):
                if indexlist_id[i-1]<n<=indexlist_id[i]:
                    f29.write(lines[n])
                    



def printLCSSubStr(X: str, Y: str,
                 m: int, n: int):


    LCSuff = [[0 for i in range(n + 1)]
                for j in range(m + 1)]

    length = 0
    row, col = 0, 0


    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                if length < LCSuff[i][j]:
                    length = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0


    if length == 0:
        return 0,0,0


    resultStr = ['0'] * length


    while LCSuff[row][col] != 0:
        length -= 1
        resultStr[length] = X[row - 1] # or Y[col-1]


        row -= 1
        col -= 1


    return(''.join(resultStr), row, len(''.join(resultStr))+row)



import copy

def combine(l, n): 
    answers = []
    one = [0] * n 
    def next_c(li = 0, ni = 0): 
        if ni == n:
            answers.append(copy.copy(one))
            return
        for lj in range(li, len(l)):
            one[ni] = l[lj]
            next_c(lj + 1, ni + 1)
    next_c()
    return answers


import numpy as np

all_word = []
file = open("Language_just20_remove_big.txt",'r')
lines = file.readlines()
datalists = []
indexlist_id = []
indexlist_ref = []
indexlist_mb = []
indexlist_tx = []

for index, line in enumerate(lines):
    if line == '\n':
        indexlist_id.append(index)

all_list = []
for i in range(len(indexlist_id)):
    word_list = []
    if i == len(indexlist_id) - 1:
        current_lines = lines[indexlist_id[i]:]
    else:
        current_lines = lines[indexlist_id[i]: indexlist_id[i + 1]]
    for line in current_lines:
        if line != '\n':
            word = line.split("\n")
            word_list.append(word[0])
    all_list.append(word_list)
           


paradigm = []
for n in all_list:
    if len(n)>= 2:
        for i in combine(n, 2):
            str1 = i[0]
            str2 = i[1]
            X = i[0]
            Y = i[1]
            m = len(X)
            n = len(Y)
            s = (printLCSSubStr(X, Y, m, n))
            if s[0] != 0:
                extra_str1_1 = str1[0:s[1]]
                extra_str1_2 = str1[s[2]:]
                extra_str1 = (extra_str1_1+extra_str1_2)
                extra_str2_1 = str2[0:s[1]]
                extra_str2_2 = str2[s[2]:]
                extra_str2 = extra_str2_1+extra_str2_2
                paradigm.append(extra_str1_1 +"->"+extra_str2_1+"+"+extra_str1_2 +"->"+extra_str2_2)


all_list = []
for i in range(len(indexlist_id)):
    word_list = []
    if i == len(indexlist_id) - 1:
        current_lines = lines[indexlist_id[i]:]
    else:
        current_lines = lines[indexlist_id[i]: indexlist_id[i + 1]]
    for line in current_lines:
        if line != '\n':
            word = line.split("\n")
            word_list.append(word[0])
    all_list.append(word_list)

           


import collections
overlap_para = collections.Counter(paradigm)



x1= overlap_para.most_common(len(overlap_para))
x2 = [key for (key, count) in x1]


over_lap2 = x2



all_of_the_word1 = []
file88 = open("Language.5.preds",'r')
lines88 = file88.readlines()
for line in lines88:
    if line != '\n':
        word = line.strip()
        all_of_the_word1.append(word)



all_of_the_word_nodup = []
for m in all_of_the_word1:
    if m not in all_of_the_word_nodup:
        all_of_the_word_nodup.append(m)


all_of_the_word = all_of_the_word_nodup


# Prefix-Sufix Using all rules

with open ('Language_pairwise_all_rules.txt','w') as file50:
    while len(all_of_the_word) != 0:
        for n in all_of_the_word:
            file50.write(n +'\n')
            all_of_the_word.remove(n)
            for m in over_lap2:
                prefix = m.split("+")[0]
                suffix = m.split("+")[1]
                prefix_left = prefix.split("->")[0]
                prefix_right = prefix.split("->")[1]
                suffix_left = suffix.split("->")[0]
                suffix_right = suffix.split("->")[1]
                if n.startswith(prefix_left) and n.endswith(suffix_left):
                    yy = len(prefix_left)
                    xx = n.rindex(suffix_left)
                    new_item = prefix_right + n[yy:xx] + suffix_right
#                         new_item = n[:xx] + suffix_right
                    if new_item in all_of_the_word:
                       file50.write(new_item +'\n')
                       all_of_the_word.remove(new_item)
                if n.startswith(prefix_right) and n.endswith(suffix_right):
                    yy = len(prefix_right)
                    xx = n.rindex(suffix_right)
                    new_item = prefix_left + n[yy:xx] + suffix_left
#                         new_item = n[:xx] + suffix_left
                    if new_item in all_of_the_word:
                       file50.write(new_item +'\n')
                       all_of_the_word.remove(new_item)
            file50.write('\n')


# Prefix-Sufix Using all suffix rules

with open ('Language_pairwise_all_suffix.txt','w') as file50:
    while len(all_of_the_word) != 0:
        for n in all_of_the_word:
            file50.write(n +'\n')
            all_of_the_word.remove(n)
            for m in over_lap2:
                prefix = m.split("+")[0]
                suffix = m.split("+")[1]
                prefix_left = prefix.split("->")[0]
                prefix_right = prefix.split("->")[1]
                suffix_left = suffix.split("->")[0]
                suffix_right = suffix.split("->")[1]
                if n.startswith(prefix_left) and n.endswith(suffix_left):
                    yy = len(prefix_left)
                    xx = n.rindex(suffix_left)
#                     new_item = prefix_right + n[yy:xx] + suffix_right
                    new_item = n[:xx] + suffix_right
                    if new_item in all_of_the_word:
                       file50.write(new_item +'\n')
                       all_of_the_word.remove(new_item)
                if n.startswith(prefix_right) and n.endswith(suffix_right):
                    yy = len(prefix_right)
                    xx = n.rindex(suffix_right)
#                     new_item = prefix_left + n[yy:xx] + suffix_left
                    new_item = n[:xx] + suffix_left
                    if new_item in all_of_the_word:
                       file50.write(new_item +'\n')
                       all_of_the_word.remove(new_item)
            file50.write('\n')





