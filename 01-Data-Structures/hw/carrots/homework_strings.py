""""
Задание 1
0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)
1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])
2) Перевод последовательности ДНК в РНК (окей, Гугл)
3) Перевод последовательности РНК в протеин*
*В папке files вы найдете файл rna_codon_table.txt - 
в нем содержится таблица переводов кодонов РНК в аминокислоту, 
составляющую часть полипептидной цепи белка.
Вход: файл dna.fasta с n-количеством генов
Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена
 ** Если вы умеете в matplotlib/seaborn или еще что, 
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)
P.S. За незакрытый файловый дескриптор - караем штрафным дезе.
"""

import numpy as np
import re
import matplotlib.pyplot as plt

import time

dna = None


def read_dna():
	"""Считать из файла dna.fasta"""
	st = ['',''] 
	i = -1
	f = open("files\dna.fasta", 'r')
	for line in f:
		if line.startswith('>'):
			i += 1
		else:
			st[i] += line
	print(st)
	f.close()
	return st



def count_nucleotides(dna):
	"""Cтатистикf по входящим в последовательность ДНК нуклеотидам для каждого гена"""
	print("Первое задание")
	first, second, gen = [], [], ['A','C','G','T']
	first.extend((dna[0].count('A'), dna[0].count('C'), dna[0].count('G'), dna[0].count('T')))
	second.extend((dna[1].count('A'), dna[1].count('C'), dna[1].count('G'), dna[1].count('T')))
	print('Первый ген: A, C, G, T ', first)
	print('Второй ген: A, C, G, T ', second)
	plt.plot(gen, first, 'g') #гистограммы здесь получились не очень имхо, заменила на график
	plt.plot(gen, second, 'r')
	plt.legend(['2 gen', '1 gen'])
	plt.title("Cтатистики по входящим нуклеотидам для каждого гена")
	plt.show()
	f = open('count_nucleotides.txt', 'w')
	f.write(str(first))
	f.write(str(second))
	f.close()
	#return num_of_nucleotides
	

def translate_from_dna_to_rna(dna):
    """Поменять тимин(Т) на урацил (U)"""
    print("Второе задание")
    st = ['','']
    st[0] = dna[0].replace('T','U')
    st[1] = dna[1].replace('T','U')
    st[0] = st[0].replace('\n','')
    st[1] = st[1].replace('\n','')
    print(st)
    f = open('rna.txt', 'w')
    f.write(str(st))
    f.close()
    return st


def translate_rna_to_protein(rna):
	"""Перевод последовательности РНК в протеин"""
	print("Третье задание")
	#print(rna)
	st, protein = '', ['','']
	
	f = open("files\\rna_codon_table.txt", 'r')
	for line in f:
		st += line

	for ind in range(0,len(rna)):
		i = 0
		while i < len(rna[ind])-3:
			index = st.find(rna[ind][i:i+3])
			protein[ind] += st[index+4]
			i += 3
	print(protein)
	f = open('protein.txt', 'w')
	f.write(str(protein))
	f.close()
	return protein
	
	
dna = read_dna()
count_nucleotides(dna) #1)
rna = translate_from_dna_to_rna(dna) #2
protein = translate_rna_to_protein(rna) #3
