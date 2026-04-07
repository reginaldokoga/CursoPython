def imprimir_mensagem(a, b):
    return a[:2] + '  ' + b[2:]

def calcular_soma(x, y):
    return x + y

resultado = calcular_soma(5, 3)
mensagem = imprimir_mensagem("Alice", "Bobbrown")
print(f"A soma de 5 e 3 é: {resultado}")    
print(f"A mensagem é: {mensagem}")