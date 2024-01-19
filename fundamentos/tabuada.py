numero_tabuada = int (input("Digite qual número deseja construir a tabuada: "));
limite = int(input("Digite qual o limite para tabuada:"));

def tabuada(numero, limite):
    print(f'Tabuada do {numero}');
    
    for i in range(1, limite+1):
        resultado = numero*i;
        print(f'{numero} x {i} = {resultado}');
        
tabuada(numero_tabuada, limite);

'''for itera de 1 até o limite, 
multiplicando o número pelo iterador 
atual do loop para gerar os resultados.'''