# função para calcular o TF (Term Frequency)

def calculaTF(freq, doc):
    import math
    tf_mapa = {}
    tamanho = len(doc) # qtd de palavras no doc
    for termo, c in freq.items(): #c corresponde a qtd de vezes que o termo ocorre
        if c > 0:
            tf_mapa[termo] = 1 + math.log10(freq[termo])
        else:
            tf_mapa[termo] = 0

    return tf_mapa # retorno meu tf mapeado (freq -> frequencia do freq)

# função para calcular o DF (Document Frequency)

def calculaDF(docs):
    df_mapa = dict.fromkeys(docs[0].keys(), 0) 
    
    for doc in docs:
        for p, valor in doc.items():
            if valor > 0:
                df_mapa[p] += 1
                
    return df_mapa

#função para calcular o IDF (Inverse Document Frequency) de um conjunto de docs

def calculaIDF(docs):
    import math
    N = len(docs) 
    
    idf_mapa = calculaDF(docs) 
    df = calculaDF(docs)
    
    for p, valor in idf_mapa.items():
        idf_mapa[p] = round(math.log(N / float(valor), 10), 6)
     
    return idf_mapa

#função para calcular TF x IDF 
def calculaTFxIDF(tf_mapa, idfs):
    tfidf = {}
    for p, valor in tf_mapa.items():
        tfidf[p] = valor * idfs[p]
    return tfidf 

#função para calcular a similaridade por cosseno
def similaridade(dados):
    import math
    similaridade = {}
    for i in range(0, 12):
        for j in range(i + 1, 12):
            cos = 0
            produto = 0
            A = 0
            B = 0

            for k in range(len(dados)):
                produto += (dados.iloc[k, i]) * (dados.iloc[k, j])
                A += (dados.iloc[k, i] ** 2)
                B += (dados.iloc[k, j] ** 2)

            if A > 0 and B > 0:
                cos = produto / (math.sqrt(A) * math.sqrt(B))

            doc_i = i + 1
            doc_j = j + 1
            similaridade[f'{doc_i}.txt - {doc_j}.txt -'] = cos

    print('Os docs mais similares são')
    for i in sorted(similaridade, key=similaridade.get, reverse=True)[:4]:
        print(i, round(similaridade[i], 5))
