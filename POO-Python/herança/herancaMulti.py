class Logavel:
    def __init__(self):
        self.nome_da_classe = 'login'
    def logar(self, mensagem):
        print('Mensagem da classe ' + self.nome_da_classe + ': ' + mensagem);
login = Logavel();
print(login.nome_da_classe)
login.logar('Acesso Negado');

class Conexao:
    def __init__(self):
        self.servidor ='';
    def conectar (self):
        print('Conectando ao banco de dados no servidor:' + self.servidor);
conect = Conexao();
conect.servidor='servidor';
conect.conectar();

class MySqlDatabase(Conexao,Logavel):
    def __init__(self):
        super().__init__()
        self.nome_da_classe = 'MySqlDatabase';
        self.servidor = 'Meu servidor';
def framework(objeto):
    if isinstance(objeto, Conexao):
        objeto.conectar()
    if isinstance(objeto, Logavel):
        mensagem = 'Usuaario autenticado.'
        objeto.logar(mensagem)

conexao_mysql = MySqlDatabase()
framework(conexao_mysql)