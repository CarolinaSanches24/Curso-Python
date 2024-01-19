def divisao(a, b):
    try:
        resultado = a/b;
        print(resultado);
        
    except ZeroDivisionError:
        print("Erro:Impossível dividir um valor por zero");
    except TypeError as e:
        print(f'Erro: O tipo do dado informado está incorreto.\n Detalhes: {e}');
    else:
        print('sem exceções');
divisao(10, 0);
divisao(10,'womakerscode');