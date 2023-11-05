# Nesse trabalho, nenhuma biblioteca de mineração de texto pode ser utilizada. 
# os calculos todos devem ser implementados. Façam a remoção de pontuação (aqui pode usar o NLTK) e
# transformem todo o texto para letras minúsculas.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def lerArquivo(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        return conteudo
    except FileExistsError:
        print(f"O arquivo '{file_path}' não foi encontrado.\n")
        return None
    except Exception as e:
        print(f"Um erro ocorreu ao ler o arquivo: {e}")
        return None
    
frase = lerArquivo('1.txt')
tokens = word_tokenize(frase)
print(frase)
print("\n")
print(tokens)
print("\n")
stopWords = set(stopwords.words("portuguese"))
print(stopWords)