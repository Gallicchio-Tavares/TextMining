'''
1 - crie o código para produzir a matriz de document frequency (DF) e 
(Inverse Document Frequency) – IDF -conforme a fórmula com log: 

--- idf = log(N/df) ---

Em seguida, gere um arquivo pdf com o resultado da matriz DF-IDFx Termo.
Não precisa gerar o pdf com python. Pode fazer print e colar.

2 - crie o código para produzir a matriz de Termfrequency (TF) x Documento, 
conforme a fórmula com log: 

    | 1 + log tf ( if tf > 0)
w = | 
    | 0 ( else )
    
Em seguida, insira no arquivo pdf o resultado da matriz TF x Documento. 

3 - Crie o código para produzir a matriz de TF*IDF 

4 - Utilizando a similaridade por cosseno, imprima a lista dos 4 documentos 
mais similares e a similaridade
'''
import leArquivo
import calcula
import string

# ler os arquivos:
txt1 = leArquivo.leArquivo('TextMining/tarefa2/1.txt').lower()
txt2 = leArquivo.leArquivo('TextMining/tarefa2/2.txt').lower()
txt3 = leArquivo.leArquivo('TextMining/tarefa2/3.txt').lower()
txt4 = leArquivo.leArquivo('TextMining/tarefa2/4.txt').lower()
txt5 = leArquivo.leArquivo('TextMining/tarefa2/5.txt').lower()
txt6 = leArquivo.leArquivo('TextMining/tarefa2/6.txt').lower()
txt7 = leArquivo.leArquivo('TextMining/tarefa2/7.txt').lower()
txt8 = leArquivo.leArquivo('TextMining/tarefa2/8.txt').lower()
txt9 = leArquivo.leArquivo('TextMining/tarefa2/9.txt').lower()
txt10 = leArquivo.leArquivo('TextMining/tarefa2/10.txt').lower()
txt11 = leArquivo.leArquivo('TextMining/tarefa2/11.txt').lower()
txt12 = leArquivo.leArquivo('TextMining/tarefa2/12.txt').lower()

def processaTxt(frase): # fase de pré-processamento: tirar pontuação e tokenizar
    fraseNova = frase.translate(str.maketrans("", "", string.punctuation))
    palavras = fraseNova.split()

    return palavras

lista1 = processaTxt(txt1)
lista2 = processaTxt(txt2)
lista3 = processaTxt(txt3)
lista4 = processaTxt(txt4)
lista5 = processaTxt(txt5)
lista6 = processaTxt(txt6)
lista7 = processaTxt(txt7)
lista8 = processaTxt(txt8)
lista9 = processaTxt(txt9)
lista10 = processaTxt(txt10)
lista11 = processaTxt(txt11)
lista12 = processaTxt(txt12) # Avatar

# pegar as palavras únicas dos documentos -> Bag Of Words:
termosUnicos = set(lista1).union(set(lista2)).union(set(lista3)).union(set(lista4)).union(set(lista5)).union(set(lista6)).union(set(lista7)).union(set(lista8)).union(set(lista9)).union(set(lista10)).union(set(lista11)).union(set(lista12))
termosUnicos = sorted(termosUnicos)
# transformaEmTxt.array_para_txt("bagOfWords.txt", termosUnicos)

#criar um dicionario para contar a ocorrencia de palavras únicas em cada um dos arquivos:
numPalavras1 = dict.fromkeys(termosUnicos, 0) # mapeando o valor padrão 0 para todas as palavras

for palavra in lista1:
    numPalavras1[palavra] += 1 # para cada palavra da lista1 presente no bag of words, adiciono 1

numPalavras2 = dict.fromkeys(termosUnicos, 0)
for palavra in lista2:
    numPalavras2[palavra] += 1
    
numPalavras3 = dict.fromkeys(termosUnicos, 0)
for palavra in lista3:
    numPalavras3[palavra] += 1

numPalavras4 = dict.fromkeys(termosUnicos, 0)
for palavra in lista4:
    numPalavras4[palavra] += 1
    
numPalavras5 = dict.fromkeys(termosUnicos, 0)
for palavra in lista5:
    numPalavras5[palavra] += 1

numPalavras6 = dict.fromkeys(termosUnicos, 0)
for palavra in lista6:
    numPalavras6[palavra] += 1

numPalavras7 = dict.fromkeys(termosUnicos, 0)
for palavra in lista7:
    numPalavras7[palavra] += 1

numPalavras8 = dict.fromkeys(termosUnicos, 0)
for palavra in lista8:
    numPalavras8[palavra] += 1

numPalavras9 = dict.fromkeys(termosUnicos, 0)
for palavra in lista9:
    numPalavras9[palavra] += 1

numPalavras10 = dict.fromkeys(termosUnicos, 0)
for palavra in lista10:
    numPalavras10[palavra] += 1

numPalavras11 = dict.fromkeys(termosUnicos, 0)
for palavra in lista11:
    numPalavras11[palavra] += 1

numPalavras12 = dict.fromkeys(termosUnicos, 0)
for palavra in lista12:
    numPalavras12[palavra] += 1
    
tf1 = calcula.calculaTF(numPalavras1, lista1)
tf2 = calcula.calculaTF(numPalavras2, lista2)
tf3 = calcula.calculaTF(numPalavras3, lista3)
tf4 = calcula.calculaTF(numPalavras4, lista4)
tf5 = calcula.calculaTF(numPalavras5, lista5)
tf6 = calcula.calculaTF(numPalavras6, lista6)
tf7 = calcula.calculaTF(numPalavras7, lista7)
tf8 = calcula.calculaTF(numPalavras8, lista8)
tf9 = calcula.calculaTF(numPalavras9, lista9)
tf10 = calcula.calculaTF(numPalavras10, lista10)
tf11 = calcula.calculaTF(numPalavras11, lista11)
tf12 = calcula.calculaTF(numPalavras12, lista12)


df = calcula.calculaDF([numPalavras1, numPalavras2, numPalavras3, numPalavras4, numPalavras5, numPalavras6, numPalavras7, numPalavras8, numPalavras9, numPalavras10, numPalavras11, numPalavras12])
idf = calcula.calculaIDF([numPalavras1, numPalavras2, numPalavras3, numPalavras4, numPalavras5, numPalavras6, numPalavras7, numPalavras8, numPalavras9, numPalavras10, numPalavras11, numPalavras12])
