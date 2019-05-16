'''
Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um)
e por ele mesmo. 
Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 
e pelo número 7.

Entrada
A entrada contém vários casos de teste. 
A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100),
indicando o número de casos de teste da entrada. 
Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), 
que pode ser ou não, um número primo.

Saída
Para cada caso de teste de entrada, 
imprima a mensagem “X eh primo” ou “X nao eh primo”, 
de acordo com a especificação fornecida.
'''

def pr(num):
    for i in range(num):
        if i > 1 and num % i == 0:
            return False
    return True

def leia():
    leitura = int(input())
    if(pr(leitura)):
        print(str(leitura) + " eh primo")
    else:
        print(str(leitura) + " nao eh primo")
    return

quantidades = int(input())
for i in range(quantidades):
    leia()
