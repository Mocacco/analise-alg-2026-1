import sys
import time

sys.setrecursionlimit(2000)

def calcular_fatorial(n):
    # Caso base: o fatorial de 0 ou 1 é 1.
    # Isso é essencial para que a recursão não continue infinitamente.
    if n == 0 or n == 1:
        return 1
    # Passo recursivo: n! = n * (n-1)!
    else:
        return n * calcular_fatorial(n - 1)
try:
    numero_usuario = int(input("Digite um número inteiro n: "))
    if numero_usuario < 0:
        print("Fatorial não é definido para números negativos.\n")
    else:
        resultado = calcular_fatorial(numero_usuario)
        print(f"O fatorial de {numero_usuario} é {resultado}\n")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.\n")

print("-" * 30)
print("Resultados do Tempo de Execução:")
valores_teste = [10, 100, 500, 1000]

for valor in valores_teste:
    # time.perf_counter() é utilizado por ter maior precisão para blocos de código rápidos
    inicio = time.perf_counter()    
    # Executa a função recursiva 
    calcular_fatorial(valor)   
    fim = time.perf_counter() 
    tempo_execucao = fim - inicio
    # Exibe o resultado com formatação de precisão (casas decimais)
    print(f"Tempo para n={valor:4}: {tempo_execucao:.8f} segundos")\
    

"""
 A complexidade assintótica de tempo do algoritmo de fatorial recursivo é $O(n)$, caracterizando uma complexidade linear.

Para calcular o fatorial de um número $n$, a função realiza uma chamada a si mesma para n-1, que por sua vez chama para n-2, 
e assim por diante, até atingir o caso base onde n = 1 ou n = 0.Isso significa que, para uma entrada de tamanho n, a 
função será invocada exatamente n vezes (ou n+1 vezes se contar o zero). Como o número de operações dentro de cada chamada 
da função (uma verificação de condição if/else, uma multiplicação e um retorno) é constante e não depende de n — ou seja,
eva um tempo O(1) —, o tempo total de execução é o número de chamadas multiplicado pelo tempo de cada chamada: n x O(1) = 
O(n).Portanto, o tempo de execução cresce de forma diretamente proporcional ao tamanho da entrada n.

tempos de execução:
Tempo para n=  10: 0.00000540 segundos
Tempo para n= 100: 0.00001830 segundos
Tempo para n= 500: 0.00015700 segundos
Tempo para n=1000: 0.00038220 segundos
"""