import pandas as pd
import leArquivo
import calcula
import string

def processaTxt(frase): # fase de pré-processamento: tirar pontuação e tokenizar
    fraseNova = frase.translate(str.maketrans("", "", string.punctuation))
    palavras = fraseNova.split()

    return palavras

arquivos = ['tarefa2/1.txt', 'tarefa2/2.txt', 'tarefa2/3.txt', 'tarefa2/4.txt', 'tarefa2/5.txt', 'tarefa2/6.txt', 'tarefa2/7.txt', 'tarefa2/8.txt', 'tarefa2/9.txt', 'tarefa2/10.txt', 'tarefa2/11.txt', 'tarefa2/12.txt']
textos = []

for arquivo in arquivos:
    textos.append(leArquivo.leArquivo(arquivo).lower())

listas = [processaTxt(texto) for texto in textos]

termosUnicos = set()

for lista in listas:
    termosUnicos.update(lista)

termosUnicos = sorted(termosUnicos)

# Criar um dicionário para contar a ocorrência de palavras únicas em cada um dos arquivos:
freqs = [dict.fromkeys(termosUnicos, 0) for _ in range(len(listas))]

for i, lista in enumerate(listas):
    for palavra in lista:
        freqs[i][palavra] += 1
    
# Calcular os Term Frequencies (TF) para cada documento:
tfs = [calcula.calculaTF(freq, lista) for freq, lista in zip(freqs, listas)]

df = calcula.calculaDF(freqs)

idf = calcula.calculaIDF(freqs)

tfidfs = [calcula.calculaTFxIDF(tf, idf) for tf in tfs]

dadosTFIDFs = [pd.DataFrame(list(tfidf.values()), index=tfidf.keys()) for tfidf in tfidfs]
dadosTFIDF = pd.concat(dadosTFIDFs, axis=1)
calcula.similaridade(dadosTFIDF)

dadosTF = pd.DataFrame(tfs)
dadosTF.to_excel('tarefa2/dados-TF-Doc.xlsx')

dadosDF = pd.DataFrame({'Termo': list(df.keys()), 'DF':list(df.values())})

dadosIDF = pd.DataFrame({'Termo': list(idf.keys()), 'IDF':list(idf.values())})

dadosDFxIDF = dadosDF.merge(dadosIDF, on='Termo')
dadosDFxIDF.to_excel('tarefa2/dados-DF-IDF.xlsx', index=True)


dadosTFIDF.to_excel('tarefa2/dados-TF-IDF.xlsx', index=True)

