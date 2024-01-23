name_user = 'Nemo';

def imprimir_frase(texto, nivel):

    if nivel == 'info':
        print(f'[INFO] {texto}')
    elif nivel == 'alerta':
        print (f'[ALERTA]{texto}')
    elif nivel == 'erro':
        print(f'[ERRO]{texto}')