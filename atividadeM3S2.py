# Decorador Imprimir
def decorator_imprimir(func):
    # Define uma função recebe wrapper` que recebe três argumentos: `capital`, `taxa` e `tempo`
    def wrapper(capital, taxa, tempo):
        # Chama a função `func` passando os argumentos `capital`, `taxa` e `tempo` e armazena o resultado na variável `resultado`
        resultado = func(capital, taxa, tempo)
        # Imprime o valor de capital
        print(f"Capital: {capital}")
        # Imprime o valor de taxa`
        print(f"Taxa: {taxa}")
        # Imprime o valor do argumento `tempo`
        print(f"Tempo: {tempo}")
        # Imprime o valor da variável `resultado`
        print(f"Resultado: {resultado}")
        # Retorna o valor da variável `resultado`
        return resultado
    # Retorna a função interna `wrapper`
    return wrapper

# Importa a função `juros_simples` do módulo `funcoes`
from funcoes import juros_simples

# Aplica o decorador `decorator_imprimir` à função `juros_simples` e armazena o resultado na variável `juros_simples`
juros_simples = decorator_imprimir(juros_simples)

