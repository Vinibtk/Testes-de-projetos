#Classe base para todos os armamentos do jogo que serão distribuido entre os personagens
class Armamento:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

#Subclasses específicas de armamentos com atributos pré-definidos que são herdados da Classe Armamento
class Espada(Armamento):
    def __init__(self):
        super().__init__("Espada", 10)

class Cajado(Armamento):
    def __init__(self):
        super().__init__("Cajado", 8)

class ArcoeFlecha(Armamento):
    def __init__(self):
        super().__init__("Arco e Flecha", 9)

class EspadaMagica(Armamento):
    def __init__(self):
        super().__init__("Espada Mágica", 15)