import string
import leArquivo

def processaTxt(frase):
    # Remove a pontuação da frase
    frase_sem_pontuacao = frase.translate(str.maketrans("", "", string.punctuation))
    
    # Divide a frase em palavras
    palavras = frase_sem_pontuacao.split()

    return palavras

def calculaDF(docs):
    df_dicio = dict.fromkeys(docs[0].keys(), 0) # vamos mapear o idf, com as chaves do primeiro doc e o valor padrão 0
    
    for doc in docs:
        for p, valor in doc.items(): # verificar chave (termo) e valor (freq) no doc
            if valor > 0:
                df_dicio[p] += 1
                
    return df_dicio

txt1 = leArquivo.leArquivo('1.txt').lower()
txt2 = leArquivo.leArquivo('2.txt').lower()

lista1 = processaTxt(txt1)
lista2 = processaTxt(txt2)

termosUnicos = set(lista1).union(set(lista2))
print(termosUnicos)

numPalavras1 = dict.fromkeys(termosUnicos, 0) # mapeando o valor padrão 0 para todas as palavras
for palavra in lista1:
    numPalavras1[palavra] += 1 # para cada palavra da lista1 presente no bag of words, adiciono 1
print("\n")
print(numPalavras1)

numPalavras2 = dict.fromkeys(termosUnicos, 0)
for palavra in lista2:
    numPalavras2[palavra] += 1
print("\n")
print(numPalavras2)
print("\n")
df = calculaDF([numPalavras1, numPalavras2])
print(df)
print("\n")
print(df.values())