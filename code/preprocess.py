# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:35:52 2020

@author: melan
"""
import pandas as pd
import re
import jieba
data=pd.read_csv('data.csv',encoding = 'utf8')
def stopwordslist():
    stopwords=[]
    for line in open('stopwords.txt',encoding='UTF-8'):
        stopwords.append( line.strip().replace(";",""))
    return stopwords
def seg_depart(s):
    sentence_depart = jieba.cut(s.strip())
    stopwords = stopwordslist()
    outstr = ''
    for word in sentence_depart:
        if word not in stopwords and len(word)>1:
                 if word != '\t':
                     outstr += word
                     outstr += " "
    return outstr
data_example=pd.DataFrame(columns=["content","time"])
#print(data.shape[0])
for i in range(60000,data.shape[0]):    
    try:
        print(i) 
        data.loc[i,'content']=re.sub('\\<.*?>|[\n\t\r]|&nbsp|[a-zA-Z0-9]','',data.loc[i,'content'])
        clean_content=seg_depart(data.loc[i,'content'])
        if len(clean_content)>10:
            data_example.loc[i,"content"]=seg_depart(data.loc[i,'content'])
            data_example.loc[i,"time"]=seg_depart(data.loc[i,'publishDate'])
    except TypeError:
        pass
    continue
#print(data.loc[0:10,'content'])
data_example.to_csv('data_example4.csv',index=None,encoding='gbk')


#print(data[0:10]['content'])
# =============================================================================
# pd.set_option('max_colwidth',100)
# print(data.columns.values)
# print(data.dtypes)
# data=data.sort_values(by = 'publishDate')
# data.reset_index(inplace=True)
# data[80325:176500].to_csv("data.csv",index=False)
# =============================================================================
# =============================================================================
# #print(data[100000:100010]['content'])
# for i in range(100000,100010):
#     data.loc[i,'content']=re.sub('\<.*\>|[\n\t\r]','',data.loc[i,'content'])
# #print(data[100000:100010]['content'])
# print(data[80325:176500]['publishDate'])
# 
# =============================================================================
