# Modulos
import pandas as pd
import re

#
corpusOriginal = pd.read_csv('corpora/corpus-q1-v2.csv', sep=',')

#regex P2_PERGUNTAR_1S para 2P_PERGUNTAR_1

#1.1
novoCorpus = corpusOriginal.replace(regex={r'P1_': '1P_', r'P2_': '2P_', r'P3_':'3P_'})
novoCorpus = novoCorpus.replace(regex={r'S1_': '1S_', r'S2_': '2S_', r'S3_':'3S_'})

#1.2
novoCorpus = corpusOriginal.replace(to_replace= r'\(\+{2,}\)', value = '(+)', regex =True)
#1.3
novoCorpus = novoCorpus.replace(to_replace= r'\s{1,}', value= ' ',regex=True)
#1.4
novoCorpus = novoCorpus.replace(to_replace= r'\b-{1,}\b', value='', regex=True)
#1.5 e 1.6
novoCorpus = novoCorpus.replace(to_replace= r'\s_', value='_', regex=True)
#1.7

#1.8
novoCorpus = novoCorpus.replace(to_replace= r'\s\(\+\)', value='(+)', regex=True)
#1.9
novoCorpus = novoCorpus.replace(to_replace=r'NÃO\s\b[A-Z]', value='NÃO_', regex=True)
#2.0
novoCorpus = novoCorpus.replace(to_replace=r'_FAMOSO', value='&FAMOSO', regex=True)
novoCorpus = novoCorpus.replace(to_replace=r'_FAMOSA', value='&FAMOSA', regex=True)
#2.1
novoCorpus = novoCorpus.replace(to_replace=r'[^\d]\.\b', value=' ', regex=True)
#2.2
novoCorpus = novoCorpus.replace(to_replace=r'\s\.', value='0.', regex=True)
#Gerando novo corpus

novoCorpus.to_csv("qs1_resposta.csv")