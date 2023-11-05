def array_para_txt(arquivo_saida, lista):
    with open(arquivo_saida, 'w') as arquivo:
        for elemento in lista:
            arquivo.write(str(elemento) + '\n')