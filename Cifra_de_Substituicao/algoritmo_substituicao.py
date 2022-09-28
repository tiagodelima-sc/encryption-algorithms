alfabeto_normal = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
     "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alfabeto_cifragem = ["Q", "W", "E", "R", "T", "Y", "U" ,"I", "O", "P", "A", "S",
     "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]

resultado_criptografia = ''

while True:
	print("Selecione uma opção:\n")
	opcao = int(input("1) Criptografar 2) Descriptografar: "))

	if opcao == 1:
		palavra = input("Digite uma palavra ou frase para Criptografar:").upper()
		for letra in palavra:
			if letra in alfabeto_normal:
				palavra_indice = alfabeto_normal.index(letra)
				resultado_criptografia = resultado_criptografia + alfabeto_cifragem[palavra_indice]
		print(f"O texto criptografado é {resultado_criptografia}")

	elif opcao == 2:
		resultado_criptografia = ''
		palavra = input("Digite uma palavra ou frase para Descriptografar:").upper()
		for letra in palavra:
			if letra in alfabeto_cifragem:
				palavra_indice = alfabeto_cifragem.index(letra)
				resultado_criptografia = resultado_criptografia + alfabeto_normal[palavra_indice]
		print(f"O seu texto descriptografado é: {resultado_criptografia}")

	else:
		print("\nPor favor, digite uma opção correta!\n")

