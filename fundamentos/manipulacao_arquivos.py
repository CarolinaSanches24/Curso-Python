file = './fundamentos/arquivo.txt';
# open -> abertura somente para leitura
arquivo_leitura = open(file, "r");
# abertura para escrita
arquivo_escrito = open(file,"w");
# abertura de arquivos binários
arquivo_binario = open(file, "wb");

# escrita
arquivo_escrita = open(file,"w");
arquivo_escrita.write("Texto a ser escrito");
arquivo_escrita.close();
# leitura
arquivo_leitura = open(file,"r");
leitura = arquivo_leitura.read();
print(leitura);
arquivo_leitura.close();