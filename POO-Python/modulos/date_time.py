from datetime import datetime;

# O módulo datetime fornece classes para trabalhar com datas e horas em Python. 
now = datetime.now();
print(now);

# importa somente a data atual
from datetime import date;
data_atual = date.today();
print(data_atual);

#importa somente a hora atual 
from datetime import time;
hora_atual = datetime.now().time();
print(hora_atual);

# Formatação de Data/Hora: Você pode formatar objetos datetime em strings usando o método strftime

from datetime import datetime;

agora = datetime.now();

formatado = agora.strftime("%Y-%m-%d");
print(formatado);

# Você pode realizar operações aritméticas com datas e 
# usar objetos timedelta para representar diferenças de tempo:



from datetime import datetime, timedelta

hoje = datetime.now()
amanha = hoje + timedelta(days=1)
diferenca = amanha - hoje

print("Amanhã:", amanha)
print("Diferença de Dias:", diferenca.days)

from datetime import datetime;

data_aniversario = datetime(2024,9,17);
hoje = datetime.now();
diferenca = data_aniversario- hoje;
print(f'Faltam {diferenca.days} dias para seu aniversario');

from datetime import date;

# dia é um objeto instancia da classe date

dia = date(2024,1,23);
print('Dia da semana:', dia.weekday());