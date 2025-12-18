#Abaixo temos a classe Inimigo que representa os inimigos no jogo, com atributos básicos como nome, vida e ataque
class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

#Criamos apenas 1 inimigo que herda da classe Inimigo, o Goblin
class Goblin(Inimigo):
    def __init__(self):
        super().__init__("Goblin", 30, "machado de duas mãos")