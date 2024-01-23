from Televisao import Televisao;
tv_sala = Televisao(); #instanciando um objeto

# Exibindo estado inicial
print(f'TV Ligada: {tv_sala.ligada}');
print(f'Canal: {tv_sala.canal}');

tv_sala.ligar();
print(f'TV Ligada: {tv_sala.ligada}');
print(f'Canal: {tv_sala.canal}');
tv_sala.canal = 4;
print(f'TV Ligada: {tv_sala.ligada}');
print(f'Canal: {tv_sala.canal}');
tv_sala.desligar();
print(f'TV Ligada: {tv_sala.ligada}');
print(f'Canal: {tv_sala.canal}');
