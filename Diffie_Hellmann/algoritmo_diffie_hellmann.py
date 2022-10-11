
numero_primo = int(input("Digite um numero primo: "))
verificador_numero_primo = True
base_usuario = 5

for i in range (2, numero_primo//2):
    if numero_primo % i == 0:
        verificador_numero_primo =  False

if verificador_numero_primo:
    alice_secret_key = int(input('Informe a chave secreta da Alice: '))
    bob_secret_key = int(input('Informe a chave secreta do Bob: '))
else:
    print("Erro! Não é um número primo, digite um numero correto.")
    exit()

resposta_alice = (base_usuario ** alice_secret_key) % numero_primo
resposta_bob =  (base_usuario ** bob_secret_key) % numero_primo

final_alice = (resposta_bob ** alice_secret_key) % numero_primo
final_bob = (resposta_alice ** bob_secret_key) % numero_primo

if final_alice == final_bob:
    print(f'\nAs respostas coincidem!\nResposta da Alice: {final_alice}\nResposta do Bob: {final_bob}\n')
else:
    print("Algo de inesperado aconteceu tente novamente mais tarde!")

