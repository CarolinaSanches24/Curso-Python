import colorama;

colorama.init(); # inicializa a lib

name_user = 'Dori';

def imprimir_cores (texto, nivel):

    if nivel.lower() == 'info':
        print(colorama.Fore.LIGHTBLUE_EX+ 'Info:', end='');
        print(colorama.Style.RESET_ALL+texto);
    elif nivel.lower() == 'aviso':
        print(colorama.Fore.YELLOW+ 'Aviso:');
        print(colorama.Style.RESET_ALL+texto);
    elif nivel.lower() == 'erro':
        print(colorama.Fore.RED+ 'Erro:', end='');
        print(colorama.Style.RESET_ALL+texto);
    else:
        print(colorama.Fore.RED+'Erro interno - nível desconhecido'+ colorama.Style.RESET_ALL);
    