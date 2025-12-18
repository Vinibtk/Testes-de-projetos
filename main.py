import customtkinter as ctk
from typing import Dict, Any
from jogo import JogoRPG
from personagem import Humano, Elfo, Anao, vampiro
from inimigo import Goblin

# Configuração inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RPGCharacterSheet:
    def __init__(self):
        #Cria a janela principal
        self.window = ctk.CTk()
        self.window.title("Ficha de RPG - Personagem")
        self.window.geometry("1100x600")
        # Criação dos frames principais
        #Cria o frame esquerdo ao qual condiz com a parte esquerda da janela principal
        self.esquerda_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.esquerda_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        #Cria o frame direito ao qual condiz com a parte direita da janela principal
        self.direita_frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.direita_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        #Estilização da janela principal
        self.window.grid_columnconfigure(0, weight=0)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_rowconfigure(1, weight=1)
        #Estilização da parte direita da janela
        self.direita_frame.grid_columnconfigure((0,1),weight=1)
        self.direita_frame.grid_rowconfigure((1,4),weight=1)
        self.direita_frame.grid_columnconfigure((0,1),weight=1)
        #Inicia as funções para cada sessão ser criada na ui
        self.create_section_informacoes()
        self.create_section_atributos()
        self.create_section_inventario()
        self.create_section_combate()
        self.create_section_inimigo()
        self.create_buttons()
        
    def create_section_informacoes(self):
        #Cria o frame das informações
        informacoes_frame = ctk.CTkFrame(self.esquerda_frame, fg_color="transparent")
        informacoes_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
        #Cria a label das informações
        informacoes_label = ctk.CTkLabel(informacoes_frame, text="Informações básicas", font=("Arial", 20, "bold"))
        informacoes_label.grid(row=0, column=0, pady=5, sticky="w",padx=5)
        #Faz com que as informações se ajustem ao tamanho da coluna
        informacoes_frame.grid_columnconfigure(0, weight=1)
        #Permite a digitar o nome do personagem
        self.nome_personagem = ctk.StringVar()
        self.name_entry = ctk.CTkEntry(informacoes_frame, placeholder_text="Nome do Personagem", textvariable=self.nome_personagem)
        self.name_entry.grid(row=1, column=0, pady= 5, sticky="nsew",padx=(0,10))
        #Permite a escolha da raça
        self.raca_personagem = ctk.StringVar(value="Vampiro")
        self.raca_combobox = ctk.CTkComboBox(informacoes_frame, values=["Humano", "Elfo", "Anão", "Vampiro"], variable=self.raca_personagem)
        self.raca_combobox.grid(row=2, column=0, pady=5, sticky="nsew", padx=(0,10))
        #Permite a escolha da classe
        self.classe_personagem = ctk.StringVar(value="Mago")
        self.classe_combobox = ctk.CTkComboBox(informacoes_frame, values=["Guerreiro", "Mago", "Arqueiro", "Guerreiro-Mago"], variable=self.classe_personagem)
        self.classe_combobox.grid(row=3, column=0, pady=5, sticky="nsew", padx=(0,10))


    def create_section_atributos(self):
        #Cria o frame para o status
        atributos_frame = ctk.CTkFrame(self.esquerda_frame,fg_color="transparent")
        atributos_frame.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        #Cria a label para o status
        atributos_label = ctk.CTkLabel(atributos_frame, text="Status", font=("Arial", 20, "bold"))
        atributos_label.grid(row=0, column=0, pady=5, sticky="w",padx=10)
        #Cria a area de informações do status
        self.info_text = ctk.CTkTextbox(atributos_frame, height=300, width=300, fg_color="#2b2b2b", text_color="white", font=("Arial", 15, "bold"))
        self.info_text.grid(row=1, column=0, columnspan=1, pady=(0, 20))


    def create_section_combate(self):
        #Cria o frame para seção de combate
        combate_frame = ctk.CTkFrame(self.direita_frame)
        combate_frame.grid(row=1,column=0, sticky="nsew", padx=10, pady=5, columnspan=2)
        #Cria a label para Interface do sistema
        combate_label=ctk.CTkLabel(self.direita_frame, text="Interface do sistema", font=("Arial", 20, "bold"))
        combate_label.grid(row=0,column=0,  pady=5, sticky="w", padx="5")
        #Cria a area para mostrar as informações do combate
        self.info_combate_text = ctk.CTkTextbox(combate_frame, fg_color="#2b2b2b", height=300, width=5000, text_color="white", font=("Arial", 22, "bold"))
        self.info_combate_text.grid(row=1, column=0, columnspan=1, pady=(0, 20))
        
    def create_buttons(self):
        #Cria o frame para criação dos botões
        buttons_frame=ctk.frame = ctk.CTkFrame(self.direita_frame, fg_color="transparent")
        buttons_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5, columnspan=2)
        #Cria o botão para Criar personagem
        personagem_button = ctk.CTkButton(buttons_frame, text='Criar personagem', width=80, height=28, fg_color="blue",command=self.criar_personagem)
        personagem_button.grid(row=2,column=0, pady=10, sticky="ew")
        #Cria o botão para Iniciar a batalha
        batalha_button = ctk.CTkButton(buttons_frame, text='Iniciar batalha', width=80, height=28, fg_color="red",
        command=self.iniciar_batalha)
        batalha_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        #Cria o botão para Atacar
        atacar_button = ctk.CTkButton(buttons_frame, text='Atacar', width=80, height=28, fg_color="orange",
        command=self.atacar_inimigo)
        atacar_button.grid(row=2,column=2, pady=10, sticky="ew")
        
    def create_section_inventario(self):
        #Cria o frame para aba de inventario
        inventario_frame = ctk.CTkFrame(self.direita_frame)
        inventario_frame.grid(row=4,column=0, sticky="nsew", padx=10, pady=5)
        #Cria a label para aba de inventario
        inventario_label=ctk.CTkLabel(self.direita_frame, text="Inventario", font=("Arial", 20, "bold"))
        inventario_label.grid(row=3,column=0,  pady=5, sticky="w", padx="5")
        #Exibe as informações do inventario
        self.info_inventario_text=ctk.CTkTextbox(inventario_frame,fg_color="#2b2b2b", text_color="white", font=("Arial", 16, "bold"))
        self.info_inventario_text.grid(row=1,column=0,  pady=5, sticky="w", padx="5")
    
    def create_section_inimigo(self):
        #Cria o frame para aba de inimigo
        status_inimigo_frame = ctk.CTkFrame(self.direita_frame)
        status_inimigo_frame.grid(row=4,column=1, sticky="nsew", padx=10, pady=5)
        #Cria a label para aba de inimigo
        status_inimigo_label=ctk.CTkLabel(self.direita_frame, text="Inimigo", font=("Arial", 20, "bold"))
        status_inimigo_label.grid(row=3,column=1,  pady=5, sticky="w", padx="5")
        #Exibe as informações do inimigo
        self.info_inimigo_text=ctk.CTkTextbox(status_inimigo_frame,fg_color="#2b2b2b", text_color="white", font=("Arial", 16, "bold"))
        self.info_inimigo_text.grid(row=1,column=0,  pady=5, sticky="w", padx="5")


    def criar_personagem(self):
        #Cria o personagem com base nas entradas do usuário
        nome = self.nome_personagem.get().strip()
        classe = self.classe_personagem.get()
        raca = self.raca_personagem.get()
        jogo = JogoRPG()
        personagem = jogo.criar_personagem(nome, classe, raca)
        
        #Armazenar e exibir na UI os dados preenchidos e os atributos do personagem que variam conforme a raça e classe
        info = f"Personagem Criado:\nNome: {personagem.get_nome()}\nClasse: {personagem.get_classe()}\nRaça: {personagem.get_raca()._nome}\nVida: {personagem.get_vida()}\nMana: {personagem.get_mana()}\nForça: {personagem.get_forca()}\nAgilidade: {personagem.get_agilidade()}\nInteligência: {personagem.get_inteligencia()}"
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, info)
        #Armazena e exibi os dados do inventário do personagem
        self.info_inventario_text.delete(1.0, tk.END)
        self.info_inventario_text.insert(tk.END, f"Arma Equipada:\n{personagem.get_armamento().nome}\nDano: {personagem.get_armamento().dano}")
        #Informa na tela de combate a informação de criação do personagem
        self.info_combate_text.delete(1.0, tk.END)
        self.info_combate_text.insert(tk.END, "Personagem criado.\nPrepare-se para a batalha!\nOu\nCrie um novo personagem.")

    def iniciar_batalha(self):
        #Crie uma instância única do jogo
        if not hasattr(self, 'jogo'):
            self.jogo = JogoRPG()
        #Cria o personagem
        personagem = self.jogo.criar_personagem(
            self.nome_personagem.get().strip(), 
            self.classe_personagem.get(), 
            self.raca_personagem.get()
        )
        #Criamos um inimigo para a batalha (não precisa criar novamente)
        self.jogo.inimigo = Goblin()
        #Exibe as informações iniciais da batalha na interface
        self.info_combate_text.delete(1.0, tk.END)
        self.info_combate_text.insert(tk.END, "Batalha Iniciada!\nUm Goblin apareceu!\nInicie o ataque!")
        #Exibe as informações do inimigo na interface Nome, vida e ataque
        self.info_inimigo_text.delete(1.0, tk.END)
        self.info_inimigo_text.insert(tk.END, f"Inimigo: {self.jogo.inimigo.nome}\nVida: {self.jogo.inimigo.vida}\nAtaque: {self.jogo.inimigo.ataque}")
    
    def atacar_inimigo(self):
        #Garantimos que a instância do jogo exista
        if not hasattr(self, 'jogo'):
            self.jogo = JogoRPG()
            
        #Aqui verificamos se o personagem existe. caso não será impresso erro
        if not hasattr(self.jogo, 'personagem') or self.jogo.personagem is None:
            self.info_combate_text.delete(1.0, tk.END)
            self.info_combate_text.insert(tk.END, "Erro: Personagem não criado!")
            return
        #Chamada para o método Atacar que veio do Jogo
        ataque = self.jogo.atacar()
        #Exibe as informações sobre ataque e vida do inimigo
        self.info_combate_text.delete(1.0, tk.END)
        self.info_combate_text.insert(tk.END, ataque)
        #Atualiza a vida do inimigo 
        self.info_inimigo_text.delete(1.0, tk.END)
        self.info_inimigo_text.insert(tk.END, f"Inimigo: {self.jogo.inimigo.nome}\nVida: {self.jogo.inimigo.vida}\nAtaque: {self.jogo.inimigo.ataque}")
    
    def run(self):
        self.window.mainloop()

import tkinter as tk
from tkinter import ttk

# Executar a aplicação
if __name__ == "__main__":
    app = RPGCharacterSheet()
    app.run()