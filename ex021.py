nome = input("Digite seu nome completo: ")
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_sem_espaco = nome.replace(" ","")
caracteres_nome = len(nome_sem_espaco)
primeiro_nome = nome.split()
mostrando_primeiro_nome = len(primeiro_nome[0])
print("nome em maiusculo é {}\n nome em minusculo é {}\n seu nome sem espaço tem o tamanho de {}\n seu primeiro nome tem o tamanho de {}".format(nome_maiusculo, nome_minusculo, caracteres_nome, mostrando_primeiro_nome))