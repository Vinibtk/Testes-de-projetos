from inventario import Armamento, Espada, Cajado, ArcoeFlecha, EspadaMagica

#Primeiro definimos a classe Raca com o objetivo de criar atributos necessários que possam ser herdados pelas SubRaças
#Aqui vamos ter os seguintes atributos Nome, bônus de força, agilidade e inteligência
class Raca:
    def __init__(self, nome, bonus_forca=0, bonus_agilidade=0, bonus_inteligencia=0):
        self._nome = nome
        self._bonus_forca = bonus_forca
        self._bonus_agilidade = bonus_agilidade
        self._bonus_inteligencia = bonus_inteligencia
    #Aqui temos ter um método para aplicar os bônus da raça ao personagem, espécie de função que vai pegar os atributos da Class Personagem e vai somar com os bônus
    def aplicar_bonus(self, personagem):
        personagem.set_forca(personagem.get_forca() + self._bonus_forca)
        personagem.set_agilidade(personagem.get_agilidade() + self._bonus_agilidade)
        personagem.set_inteligencia(personagem.get_inteligencia() + self._bonus_inteligencia)  

#Abaixo temos as SubRaças que vão herdar a class Raça e modificam os atributos para gerar uma variação em cada Raça
class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", bonus_forca=2, bonus_agilidade=2, bonus_inteligencia=2) 

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", bonus_agilidade=4, bonus_inteligencia=2)

class Anao(Raca):
    def __init__(self):
        super().__init__("Anão", bonus_forca=4, bonus_agilidade=1)

class vampiro(Raca):
    def __init__(self):
        super().__init__("Vampiro", bonus_forca=3, bonus_inteligencia=3)

#Abaixo temos a classe Personagem que é a classe base para todas as SubClasses de personagens do jogo
#Aqui temos os atributos básicos como nome, classe, raça, armamento, vida, mana, força, agilidade e inteligência
#Esses atributos serão importantes para o desenvolvimento do jogo pois além de permitir a criação dos métodos de ataque e habilidades especiais, também possibilitam o encapsulamento dos dados através de Getters e Setters
class Personagem:
    def __init__(self, nome, classe, raca: Raca, armamento: Armamento):
        #Aqui inicializamos os atributos básicos do personagem, onde o atributo raça é do tipo Raca e armamento do tipo Armamento, classes que criamos anteriormente
        self._nome = nome
        self._classe = classe
        self._raca = raca
        self._armamento = armamento
        self._vida = 100
        self._mana = 50
        self._forca = 10
        self._agilidade = 10
        self._inteligencia = 10
        self._inventario = None
        self._raca.aplicar_bonus(self)

    # Encapsulamento utilizando Getters e Setters
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_classe(self):
        return self._classe
    
    def set_classe(self, classe):
        self._classe = classe

    def get_raca(self) -> Raca:
        return self._raca

    def set_raca(self, raca: Raca):
        if isinstance(raca, Raca):
            self._raca = raca
            self._raca.aplicar_bonus(self)

    def get_armamento(self) -> Armamento:
        return self._armamento
    
    def set_armamento(self, armamento: Armamento):
        if isinstance(armamento, Armamento):
            self._armamento = armamento

    def get_vida(self):
        return self._vida

    def set_vida(self, vida):
        self._vida = vida

    def get_mana(self):
        return self._mana

    def set_mana(self, mana):
        self._mana = mana

    def get_forca(self):
        return self._forca

    def set_forca(self, forca):
        self._forca = forca

    def get_agilidade(self):
        return self._agilidade

    def set_agilidade(self, agilidade):
        self._agilidade = agilidade

    def get_inteligencia(self):
        return self._inteligencia

    def set_inteligencia(self, inteligencia):
        self._inteligencia = inteligencia

#Aqui começa as subclasses: Guerreiro, Mago, Arqueiro, MagoGuerreiro(sendo que este possui uma herença multipla da class Paladino e Mago)
class Guerreiro(Personagem):
    def __init__(self, nome, raca: Raca):
        super().__init__(nome, "Guerreiro", raca, Espada())
        self._vida = 120
        self._forca = 15

class Mago(Personagem):
    def __init__(self, nome, raca: Raca):
        super().__init__(nome, "Mago", raca, Cajado())
        self._mana = 80
        self._inteligencia = 20

class Arqueiro(Personagem):
    def __init__(self, nome, raca: Raca):
        super().__init__(nome, "Arqueiro", raca, ArcoeFlecha())
        self._agilidade = 20
        
class Paladino:
    def __init__(self):
        self._forca = 15

#Abaixo criamos a classe GuerreiroMago que possui hereança multipla de Mago e Paladino, combinando atributos de ambas as classes
class GuerreiroMago(Mago, Paladino):
    def __init__(self, nome, raca: Raca):
        Mago.__init__(self, nome, raca)
        Paladino.__init__(self)
        self._classe = "Guerreiro-Mago"
        self._armamento = EspadaMagica()
        self._vida = 110
