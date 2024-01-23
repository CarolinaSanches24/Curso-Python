bebida = 'refrigerante';
def cardapio():
    comida = 'hamburguer';
    global bebida;
    bebida = 'suco';
    # para identificar a variavel suco como
    # variavel global e nao uma nova variavel usamos 
    # palavra reservada global
    print(f'Exemplo variavel local: {comida}');
    print(f'Exemplo variavel global: {bebida}');
cardapio();
print(f'Exemplo variavel global: {bebida}');
