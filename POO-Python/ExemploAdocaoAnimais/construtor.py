class PersonagemAnime:
    def __init__(self, nome, poder, habilidade):
        self.nome = nome
        self.poder = poder
        self.habilidade = habilidade

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}!")
        print(f"Meu poder é {self.poder} e minha habilidade especial é {self.habilidade}.")

# Criando objetos para alguns personagens de anime
goku = PersonagemAnime(nome="Goku", poder="Super Saiyajin", habilidade="Kamehameha")
luffy = PersonagemAnime(nome="Luffy", poder="Gomu Gomu no Mi", habilidade="Gear Second")
sakura = PersonagemAnime(nome="Sakura", poder="Força física", habilidade="Jutsus médicos")

# Apresentando os personagens
goku.apresentar()
luffy.apresentar()
sakura.apresentar()