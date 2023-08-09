# Função com parâmetros e retorno
def square(number):
    squared = number ** 2
    return squared

# Solicitando um número ao usuário
num = float(input("Digite um número: "))

# Chamando a função para calcular o quadrado do número e exibindo o resultado
result = square(num)
print(f"O quadrado de {num} é {result}")
