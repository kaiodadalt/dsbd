"""
    *** WORD COUNTER ***
    
    Obtenha um texto qualquer e crie um dicionário contendo quantas vezes
    determinada palavra apareceu.
"""
import re
from collections import Counter

base_text = open('base_text.txt').read()
words = re.findall(r"[a-zA-Z'0-9]+", base_text)
word_counts_sorted = Counter(words).most_common()

print(dict(word_counts_sorted))