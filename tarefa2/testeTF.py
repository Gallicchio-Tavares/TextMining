import string
from calcula import calculaTF
import leArquivo

def processaTxt(frase):
    # Remove a pontuação da frase
    frase_sem_pontuacao = frase.translate(str.maketrans("", "", string.punctuation))
    
    # Divide a frase em palavras
    palavras = frase_sem_pontuacao.split()

    return palavras

def calculaTF(termo, doc):
    tf_mapa = {}
    tamanho = len(doc) # qtd de palavras no documento
    for t, c in termo.items(): # t corresponde ao termo em questão; c corresponde a qtd de vezes que esse termo ocorre
        tf_mapa[t] = c / float(tamanho) # fórmla do tf
    return tf_mapa

txt1 = leArquivo.leArquivo('1.txt').lower()
txt2 = leArquivo.leArquivo('2.txt').lower()

lista1 = processaTxt(txt1)
lista2 = processaTxt(txt2)

termosUnicos = set(lista1).union(set(lista2))

numPalavras1 = dict.fromkeys(termosUnicos, 0) # mapeando o valor padrão 0 para todas as palavras

for palavra in lista1:
    numPalavras1[palavra] += 1 # para cada palavra da lista1 presente no bag of words, adiciono 1

tf1 = calculaTF(numPalavras1, lista1)
print(tf1)