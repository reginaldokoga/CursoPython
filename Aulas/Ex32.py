numero_str = input("Digite um número: ")
if numero_str.isdigit():
    numero = int(numero_str)
    num_par = numero % 2 == 0
    if num_par:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("O valor digitado não é um número inteiro.")

hora_str = input("Digite a hora atual (0-23): ")
if hora_str.isdigit():
    hora = int(hora_str)
    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24:
        print("Boa noite!")
    else:
        print("Hora inválida. Digite um valor entre 0 e 23.")
else:
    print("Hora deve ser um número inteiro entre 0 e 23.")

nome = input("Digite seu primeiro nome: ")
nome_tamanho = len(nome)
if nome_tamanho > 0 and nome_tamanho <= 4:
    print(f"Seu nome é curto.")
elif nome_tamanho >= 5 and nome_tamanho <= 6: 
    print(f"Seu nome é normal.")
elif nome_tamanho > 6:
    print(f"Seu nome é muito grande.")  
else:
    print("O nome digitado é inválido.")
 