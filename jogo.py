from personagem import Personagem, Guerreiro, Mago, Arqueiro, GuerreiroMago, Humano, Elfo, Anao, vampiro, Raca
from inimigo import Goblin
from inventario import Armamento, Espada, Cajado, ArcoeFlecha, EspadaMagica

#Abaixo temos a classe JogoRPG que gerencia a criação do personagem, inimigo e o sistema de combate
class JogoRPG:
    #Aqui inicializamos os atributos do jogo
    def __init__(self):
        self.personagem = None
        self.inimigo = None
    
    #Método para criar o personagem com base na classe e raça selecionada
    def criar_personagem(self, nome, classe, raca: Raca,):
        """Cria um personagem com base na classe selecionada"""
        # Mapeamento de raça para classe
        raca_map = {
            "Humano": Humano(),
            "Elfo": Elfo(),
            "Anão": Anao(),
            "Vampiro": vampiro()
        }

        raca = raca_map.get(raca,  Humano())  # Padrão Humano se inválido

        if classe == "Guerreiro":
            self.personagem = Guerreiro(nome, raca)
        elif classe == "Mago":
            self.personagem = Mago(nome, raca)
        elif classe == "Arqueiro":
            self.personagem = Arqueiro(nome, raca)
        elif classe == "Guerreiro-Mago":
            self.personagem = GuerreiroMago(nome, raca)

        return self.personagem

    #Abaixo temos o método para atacar o inimigo
    def atacar(self):
        #criamos uma variável dano que recebe o dano do armamento do personagem
        dano = self.personagem.get_armamento().dano
        #Abaixo criamos a condição para verificar se o inimigo ainda está vivo, caso esteja, o inimigo recebe o dano do personagem, até que a sua vida tenha acabo e será exibido a vitória do usuário
        if self.inimigo.vida > 0:
            self.inimigo.vida -= dano
            if self.inimigo.vida <= 0:
                return f"{self.personagem.get_nome()} venceu a batalha!"
            else:
                return f"{self.personagem.get_nome()} atacou {self.inimigo.nome} utilizando {self.personagem.get_armamento().nome} causando {dano} de dano.\nVida do inimigo: {self.inimigo.vida}\n"
        else:
            return f"{self.personagem.get_nome()} venceu a batalha!"
