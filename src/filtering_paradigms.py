#!/usr/bin/env python
# coding: utf-8
import argparse
from argparse import ArgumentParser
            
def Get_degree_num(input_list):
    d ={}
    for x in input_list:
        d[x[0]] = [int(x[1]),int(x[2])]
    return d

def Get_input_wordlist(input_list):
    aa = []
    for x in input_list:
        aa.append(x[0])
    return aa

def Find_med(L):
    l = len(L) 
    L.sort()
    if l%2 == 0:
        m = (L[int(l/2) - 1] + L[int(l/2)]) / 2 
        med = "%.1f" % m
        return med
    else: 
        m = L[int((l-1)/2)] 
        med = m
        return med 

def list_of_weight(listwords2,Weight_freq_list):
    all_words_each_group = []
    for words2 in listwords2:
        each_weight_num = Weight_freq_list.get(words2)[0]
        all_words_each_group.append(each_weight_num)
    return all_words_each_group

def qualify_candidate(paradigm_group,Weight_freq_list):
    candidate_words = []
    all_words_each_group = []
    for words2 in paradigm_group:
        each_weight_num = Weight_freq_list.get(words2)[0]
        all_words_each_group.append(each_weight_num)
    median = Find_med(all_words_each_group)
    for words2 in paradigm_group:
        each_degree_num = Weight_freq_list.get(words2)[1]
        each_weight_num = Weight_freq_list.get(words2)[0]
        if each_degree_num != None and each_degree_num > len(paradigm_group)/2 and each_weight_num > float(median):
            candidate_words.append(words2)
            if len(candidate_words) >=2:
                break         
    return candidate_words

from embeddings import load
emb = load("../embeddings/Language.bible.txt.vec")
import numpy as np
import scipy.spatial.distance

def load(fn):
    embedding = {}
    with open(fn, newline='') as f:
        for line in f:
            line = line.strip()
            if line:
                fields = line.split(" ")
                wf, vec = fields[0], fields[1:]
                embedding[wf] = np.array(vec, dtype=np.double)
    return embedding

def similarity(wf1,wf2,emb):
    if wf1 in emb and wf2 in emb:
        return 1 - scipy.spatial.distance.cosine(emb[wf1], emb[wf2])
    else:
        return 1

def main(language_name):
    file = open("../predictions/fst_rules/"+language_name+".5.preds.rp.top_n=500.tables",'r')
    lines = file.readlines()
    indexlist_id = []
    for index, line in enumerate(lines):
        if line == '\n':
            indexlist_id.append(index)

    big_cluster = []
    for i in range(1,len(indexlist_id)):
        if indexlist_id[i]-indexlist_id[i-1]-1 != 1 :
            group_cluster = []
            for n in range(len(lines)):
                if n> indexlist_id[i-1] and n <indexlist_id[i]:
                    word_string = lines[n].strip()
                    each_element = word_string.split('\t')
                    word = [each_element[0],each_element[1],each_element[2]]
                    group_cluster.append(word)
            big_cluster.append(group_cluster)
        if indexlist_id[i]-indexlist_id[i-1]-1 == 1 :
            group_cluster = []
            for n in range(len(lines)):
                if n> indexlist_id[i-1] and n <indexlist_id[i]:
                    word_string = lines[n].strip()
                    each_element = word_string.split('\t')
                    word = [each_element[0],each_element[1],each_element[2]]
                    group_cluster.append(word)
            big_cluster.append(group_cluster)
            
    with open('../predictions/fst_rules/"+language_name+"_fst_500_result.txt','w') as file_FST:
        removed_word = []
        for x in big_cluster:
            break_time = 0
            if len(x)>=20 and break_time == 0:
                break_time += 1
                degree_num_list = Get_degree_num(x)
                small_group = Get_input_wordlist(x)
                all_words_each_group = list_of_weight(small_group,degree_num_list)
                candidate_words = qualify_candidate(small_group,degree_num_list)
                median_num = Find_med(all_words_each_group)
                if len(candidate_words) >=2:
                    for each_word in small_group:
                        each_word_weight = degree_num_list.get(each_word)[0]
                        each_word_degree_num = degree_num_list.get(each_word)[1]
                        if each_word_degree_num != None and each_word_degree_num <=len(small_group)/3 and each_word_weight <= float(median_num):
                            cosine_sim1 = similarity(each_word,candidate_words[0],emb)
                            cosine_sim2 = similarity(candidate_words[0],candidate_words[1],emb)
                            if abs(cosine_sim1) > 0.5 and abs(cosine_sim2 - cosine_sim1) <= 0.3:
                                file_FST.write(each_word + '\n')
                            else:
                                removed_word.append(each_word)
                        else:
                            file_FST.write(each_word + '\n')
                else:
                    for each_word in small_group:  
                        file_FST.write(each_word + '\n')
                file_FST.write('\n')

            
            break_time = 0
            if len(x)<20 and break_time == 0:
                for each_word in x: 
                    file_FST.write(each_word[0] + '\n') 
                file_FST.write('\n')    

    print(removed_word) #print filtering words (words fail to pass the three tests)      

if __name__ == '__main__':
    parser = ArgumentParser(description='Filtering paradigms')
    parser.add_argument('--language',type=str, help='The ground truth file')
    args = parser.parse_args()
    main(args.language)            
       
