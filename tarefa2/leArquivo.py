def leArquivo(file_path):
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
