# função para calcular o TF (Term Frequency)

def calculaTF(termo, doc):
    tf_mapa = {}
    tamanho = len(doc) # qtd de palavras no documento
    for t, c in termo.items(): # t corresponde ao termo em questão; c corresponde a qtd de vezes que esse termo ocorre
        tf_mapa[t] = c / float(tamanho) # fórmla do tf
        
    print("Termo\tTF")
    print("-"*30)
    for termo, frequencia in tf_mapa.items():
        if frequencia != 0:
            print(f"{termo}\t{frequencia:.5f}")
        else:
            print(f"{termo}\t{int(frequencia)}")
    print("\n")
    return tf_mapa # retorno meu tf mapeado (termo -> frequencia do termo)

# função para calcular o DF (Document Frequency)

def calculaDF(docs):
    df_mapa = dict.fromkeys(docs[0].keys(), 0) 
    
    for doc in docs:
        for p, valor in doc.items():
            if valor > 0:
                df_mapa[p] += 1
                
    return df_mapa

#função para calcular o IDF (Inverse Document Frequency) de um conjunto de documentos

def calculaIDF(docs):
    import math
    N = len(docs) 
    
    idf_mapa = calculaDF(docs) 
    df = calculaDF(docs)
    
    print("Termo\tDF\tIDF")
    print("-"*30)
    for p, valor in idf_mapa.items():
        idf_mapa[p] = round(math.log(N / float(valor), 10), 6)
        print(f"{p}\t{df[p]}\t{idf_mapa[p]}")      
    return idf_mapa

