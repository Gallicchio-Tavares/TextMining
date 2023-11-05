import string

def processar_frase(frase):
    # Remove a pontuação da frase
    frase_sem_pontuacao = frase.translate(str.maketrans("", "", string.punctuation))
    
    # Divide a frase em palavras
    palavras = frase_sem_pontuacao.split()

    return palavras

# Exemplo de uso
frase = "Evan (Ashton Kutcher) é um jovem que luta para esquecer fatos de sua infância. Para tanto ele decide realizar uma regressão onde volta também fisicamente ao seu corpo de criança, tendo condições de alterar seu próprio passado. Porém, ao tentar consertar seus antigos problemas ele termina por criar novos, já que toda mudança que realiza gera consequências em seu futuro."
palavras_array = processar_frase(frase)
print(palavras_array)
print(string.punctuation)