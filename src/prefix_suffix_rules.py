#!/usr/bin/env python
# coding: utf-8


import numpy as np
import copy
import collections
import argparse
from argparse import ArgumentParser
                    
def printLCSSubStr(X: str, Y: str, m: int, n: int): #get longest common substring
    LCSuff = [[0 for i in range(n + 1)] for j in range(m + 1)]
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


def combine(l, n): #generate two-word combination within one paradigm
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


def Generate(language_name):
  file = open("../data/"+language_name+"_remove_big.txt",'r')
  lines = file.readlines()
  datalists = []
  indexlist_id = []
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
   
  paradigm = []  #extract rules according to the longest common substring
  for n in all_list_all:
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

  overlap_para = collections.Counter(paradigm)
  x1= overlap_para.most_common(len(overlap_para))
  x2 = [key for (key, count) in x1]
  over_lap2 = x2

  all_of_the_word1 = []
  file_baseline = open("../data/"+language_name+".5.preds",'r')
  lines_baseline = file_baseline.readlines()
  for line in lines_baseline:
    if line != '\n':
      word = line.strip()
      all_of_the_word1.append(word)

  all_of_the_word_nodup = []
  for m in all_of_the_word1:
    if m not in all_of_the_word_nodup:
      all_of_the_word_nodup.append(m)
  all_of_the_word = all_of_the_word_nodup


  # Prefix-Sufix Using all rules
  with open ('../prediction/"+language_name+"_pairwise_all_rules.txt",'w') as file_generate:
    while len(all_of_the_word) != 0:
      for n in all_of_the_word:
        file_generate.write(n +'\n')
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
            new_item = prefix_right + n[yy:xx] + suffix_right #using this line if you want to apply all suffix rules: new_item = n[:xx] + suffix_right
            if new_item in all_of_the_word:
              file_generate.write(new_item +'\n')
              all_of_the_word.remove(new_item)
          if n.startswith(prefix_right) and n.endswith(suffix_right):
            yy = len(prefix_right)
            xx = n.rindex(suffix_right)
            new_item = prefix_left + n[yy:xx] + suffix_left # using this line if you want to apply all suffix rules: new_item = n[:xx] + suffix_left
            if new_item in all_of_the_word:
              file_generate.write(new_item +'\n')
              all_of_the_word.remove(new_item)
        file_generate.write('\n')

if __name__ == '__main__':
    parser = ArgumentParser(description='Generating new paradigms')
    parser.add_argument('--language',type=str, help='Choose the language file you want to process')
    args = parser.parse_args()
    Generate(args.language)       
