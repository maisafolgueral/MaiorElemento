import random

def criaMatriz(l,c):
    A = []
    for i in range(l):
        linha = [] # lista vazia
        for j in range(c):        
            linha.append(random.randint(1,100))
        A.append(linha)
    return A

def descobreMaior(A):    
    maior = 0
    for i in range(len(A)):        
        for j in range(len(A[0])):            
            if A[i][j] > maior:                
                maior = A[i][j]
    return maior  

def imprime(A):
    for i in range(len(A)):            
        print(A[i])

def main():
    l=int(input("Linha: "))
    c=int(input("Coluna: "))
    A = criaMatriz(l,c)
    imprime(A)
    print("Maior elemento:", descobreMaior(A))

main()
            
