def soma(): #definição da função soma
    calculo = 10+2;
    print(f'O resultado da soma é :{calculo}');
    
soma() # chamada da função

# Função com parametro
num1 = int (input('Digite o primeiro número: '));
num2 = int (input('Digite o segundo número:'));

def multiplicacao (num1, num2):
    multi = num1*num2;
    print(f'O resultado da multiplicação é {multi}');
    
multiplicacao(num1, num2);