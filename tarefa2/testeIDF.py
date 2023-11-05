import string
import leArquivo

def processaTxt(frase):
    # Remove a pontuação da frase
    frase_sem_pontuacao = frase.translate(str.maketrans("", "", string.punctuation))
    
    # Divide a frase em palavras
    palavras = frase_sem_pontuacao.split()

    return palavras

def calculaDF(docs):
    df_mapa = dict.fromkeys(docs[0].keys(), 0) 
    
    for doc in docs:
        for p, valor in doc.items():
            if valor > 0:
                df_mapa[p] += 1
                
    return df_mapa

def calculaIDF(docs):
    import math
    N = len(docs) 
    
    idf_mapa = calculaDF(docs) 
    df = calculaDF(docs)
    
    print("Termo\tDF\tIDF")
    print("-"*30)
    for p, valor in idf_mapa.items():
        idf_mapa[p] = math.log(N / float(valor), 10)
        print(f"{p}\t{df[p]}\t{idf_mapa[p]}")      
    return idf_mapa

txt1 = leArquivo.leArquivo('1.txt').lower()
txt2 = leArquivo.leArquivo('2.txt').lower()

lista1 = processaTxt(txt1)
lista2 = processaTxt(txt2)

termosUnicos = set(lista1).union(set(lista2))
termosUnicos = sorted(termosUnicos)
numPalavras1 = dict.fromkeys(termosUnicos, 0) # mapeando o valor padrão 0 para todas as palavras
for palavra in lista1:
    numPalavras1[palavra] += 1 # para cada palavra da lista1 presente no bag of words, adiciono 1

numPalavras2 = dict.fromkeys(termosUnicos, 0)
for palavra in lista2:
    numPalavras2[palavra] += 1

idf = calculaIDF([numPalavras1, numPalavras2])