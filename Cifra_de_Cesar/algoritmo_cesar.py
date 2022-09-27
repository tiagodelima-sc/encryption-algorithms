
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
resultado_criptografia = ''


while True:
    if resultado_criptografia == '':
        print("Selecione uma opção:\n")
        opcao = int(input("1) Criptografar 2) Descriptografar: "))

        if opcao == 1:
            palavra = input("Digite uma palavra para Criptografar:\n")
            palavra = palavra.lower()
            chave_codificacao = int(input("Digite o número da chave de codificação: "))

            for letra in palavra:
                indice = alfabeto.find(letra)
                indice = indice + chave_codificacao
                if (indice >= len(alfabeto)):
                    indice = indice - len(alfabeto)
                    resultado_criptografia = resultado_criptografia + alfabeto[indice]

        elif opcao == 2:
            palavra = input("Digite uma palavra para Descriptografar: \n")
            palavra = palavra.lower()
            chave_codificacao = int(input("Digite o número da chave de codificação: "))

            for letra in palavra:
                indice = alfabeto.find(letra)
                indice = indice - chave_codificacao
                resultado_criptografia = resultado_criptografia + alfabeto[indice]
        else:
            print("\nPor favor, digite uma opção correta!\n")

    else:
        print("\nSeu Resultado Final é:\n" + resultado_criptografia)
        break






