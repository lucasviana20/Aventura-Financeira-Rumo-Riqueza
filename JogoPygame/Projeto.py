import pygame
import random

pygame.init()
pygame.mixer.init()

class Jogador:

    Dinheiro = 0

    Score = 1000

    Rodada = 1

    despesas = [["Luz", "50", False, pygame.Rect(270, 200, 20, 20)],
                ["Agua", "50", False, pygame.Rect(270, 230, 20, 20)],
                ["Internet/Telefone/TV/Celular", "300", False, pygame.Rect(270, 260, 20, 20)],
                ["Aluguel", "1150", False, pygame.Rect(270, 290, 20, 20)],
                ["Comida", "400", False, pygame.Rect(270, 320, 20, 20)],
                ["Transporte", "200", False, pygame.Rect(270, 350, 20, 20)],
                ["Plano de saude", "150", False, pygame.Rect(270, 380, 20, 20)],
                ["Dividas", "0", False, pygame.Rect(270, 410, 20, 20)],
                ["Total", "2300", False, pygame.Rect(270, 440, 20, 20)]]

    Investimentos = [["", False, "0"], ["", False, "0"], ["", False, "0"]]
    
    Bens = [["Educação", False, "Vantagem: Aumento de 10% nas chances de sucesso dos investimentos", "2000"],
            ["Abrir negócio próprio", False, "Vantagem: Aumento de 1000,00 no salário", "2000"],
            ["Comprar um imóvel", False, "Vantagem: Exclusão da despesa aluguel", "3000"],
            ["Seguro", False, "Vantagem: Ao receber um evento aleatorio, o seguro pagará metade do valor", "100"],
            ["Consultoria de Investimentos", False, "Vantagem: Aumenta a porcentagem de retorno dos seus investimentos em 10%", "2000"],
            ["Parceria Bancária", False, "Vantagem: Diminuição da taxa de juros dos emprestimos em 33%", "2000"],
            ["Comprar uma Bike", False, "Vantagem: Exclusão da despesa de transporte", "500"]]

    BensComprados = []

    Emprestimos = [["", False], ["", "", "", False], ["", "", "", False], ["", "", "", False]]

    def PagarDespesas(self):

        ValorASerPago = 0
        
        for i in range(8):

            if self.despesas[i][2]:
                ValorASerPago = ValorASerPago + int(self.despesas[i][1])

        if self.Dinheiro >= ValorASerPago:

            for i in range(8):

                if self.despesas[i][2]:
                    self.Dinheiro = self.Dinheiro - int(self.despesas[i][1])
                    self.despesas[i][1] = "0"

            self.despesas[8][1] = str(int(self.despesas[0][1]) + int(self.despesas[1][1]) + int(self.despesas[2][1]) + int(self.despesas[3][1]) +
                             int(self.despesas[4][1]) + int(self.despesas[5][1]) + int(self.despesas[6][1]) + + int(self.despesas[7][1]))

    def PassarRodada(self):

        self.CalculaDespesas()

        self.CalculaEmprestimos()

        AntesTesouroDireto = "0"
        DepoisTesouroDireto = "0"

        AntesAcoes = "0"
        DepoisAcoes = "0"

        AntesCriptoMoedas = "0"
        DepoisCriptoMoedas = "0"

        if "Consultoria de Investimentos" in self.BensComprados:
            Incremento = 0.1
            
        else:
            Incremento = 0
            
        for i in range(3):

            if int(self.Investimentos[i][2]) > 0:
                
                NumeroSorteado = random.randint(1,10)

                if i == 0:

                    AntesTesouroDireto = self.Investimentos[i][2]
                    
                    if "Educação" in self.BensComprados:
                        Falhas = []
                    else:
                        Falhas = [7]
                        
                    if NumeroSorteado in Falhas:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.1))
                        DepoisTesouroDireto = str(int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.1 + Incremento)))
                        self.Investimentos[i][2] = "0"
                        
                    else:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.1 + Incremento))
                        DepoisTesouroDireto = str(int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.1 + Incremento)))
                        self.Investimentos[i][2] = "0"

                if i == 1:

                    AntesAcoes = self.Investimentos[i][2]

                    if "Educação" in self.BensComprados:
                        Falhas = [3, 7]
                    else:
                        Falhas = [3, 5, 7]
                        
                    if NumeroSorteado in Falhas:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.3))
                        DepoisAcoes = str(int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.3 + Incremento)))
                        self.Investimentos[i][2] = "0"
                        
                    else:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.3 + Incremento))
                        DepoisAcoes = str(int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.3 + Incremento)))
                        self.Investimentos[i][2] = "0"

                if i == 2:

                    AntesCriptoMoedas = self.Investimentos[i][2]

                    if "Educação" in self.BensComprados:
                        Falhas = [1, 3, 7, 9]
                    else:
                        Falhas = [1, 3, 5, 7, 9]
                        
                    if NumeroSorteado in Falhas:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.5))
                        DepoisCriptoMoedas = str(int(self.Investimentos[i][2]) - round(int(self.Investimentos[i][2]) * (0.5 + Incremento)))
                        self.Investimentos[i][2] = "0"
                        
                        
                    else:
                        self.Dinheiro = self.Dinheiro + int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.5 + Incremento))
                        DepoisCriptoMoedas = str(int(self.Investimentos[i][2]) + round(int(self.Investimentos[i][2]) * (0.5 + Incremento)))
                        self.Investimentos[i][2] = "0"

                        
        self.Feedback(AntesTesouroDireto, DepoisTesouroDireto, AntesAcoes, DepoisAcoes, AntesCriptoMoedas, DepoisCriptoMoedas)

        if self.Rodada == 11:

            valorEmprestimo = 0

            for i in range(3):
                
                if self.Emprestimos[i + 1][0] != "":
                    valorEmprestimo = valorEmprestimo + int(self.Emprestimos[i + 1][0])


            if (self.Dinheiro - int(self.despesas[7][1]) - valorEmprestimo) > 10000:
                display.blit(Vitoria, (0,0))
                display.blit(fonteGrande.render("Parabéns!!!, você salvou a vila do Chaves", True, BRANCO), (200, 10))
                
            else:
                display.blit(Derrota, (0,0))
                display.blit(fonteGrande.render("Infelizmente o Chaves não conseguiu salvar a vila!", True, BRANCO), (110, 10))

            
            pygame.display.flip()
            pygame.time.wait(7000)
            pygame.quit()
            quit()

        self.CalculaSalario()

    def CalculaSalario(self):

        display.blit(Salario_Imagem, (0,0))
        
        if "Abrir negócio próprio" in self.BensComprados:
            self.Dinheiro = self.Dinheiro + 4000
            display.blit(fonteGrande.render("4000", True, PRETO), (580, 243))
            
        else:
            self.Dinheiro = self.Dinheiro + 3000
            display.blit(fonteGrande.render("3000", True, PRETO), (580, 243))

        pygame.display.flip()

        pygame.time.wait(3000)

    def CalculaDespesas(self):

        self.despesas[7][1] = str(round((int(self.despesas[0][1]) + int(self.despesas[1][1]) + int(self.despesas[2][1]) + int(self.despesas[3][1]) +
                         int(self.despesas[4][1]) + int(self.despesas[5][1]) + int(self.despesas[6][1]) + int(self.despesas[7][1])) * 1.15))
        self.despesas[7][2] = False
        
        self.despesas[0][1] = "50"
        self.despesas[0][2] = False
        
        self.despesas[1][1] = "50"
        self.despesas[1][2] = False
        
        self.despesas[2][1] = "300"
        self.despesas[2][2] = False

        if "Comprar um imóvel" in self.BensComprados:
            self.despesas[3][1] = "0"
        else:
            self.despesas[3][1] = "1150"
    
        self.despesas[3][2] = False
        
        self.despesas[4][1] = "400"
        self.despesas[4][2] = False

        if "Comprar uma Bike" in self.BensComprados:
            self.despesas[5][1] = "0"
        else:
            self.despesas[5][1] = "200"

        self.despesas[5][2] = False
        
        self.despesas[6][1] = "150"
        self.despesas[6][2] = False

        self.despesas[8][1] = str(int(self.despesas[0][1]) + int(self.despesas[1][1]) + int(self.despesas[2][1]) + int(self.despesas[3][1]) +
                         int(self.despesas[4][1]) + int(self.despesas[5][1]) + int(self.despesas[6][1]) + int(self.despesas[7][1]))
        self.despesas[8][2] = False

    def CalculaEmprestimos(self):

        for i in range(3):
            if self.Emprestimos[i + 1][0] != "":
                if "Parceria Bancária" in self.BensComprados:
                    juros = 1 + (float(self.Emprestimos[i + 1][1]) / 150)
                    self.Emprestimos[i + 1][0] = str( round((int(self.Emprestimos[i + 1][0]) * juros) ) )
                else:
                    juros = 1 + (float(self.Emprestimos[i + 1][1]) / 100)
                    self.Emprestimos[i + 1][0] = str( round((int(self.Emprestimos[i + 1][0]) * juros) ) )
                  
    def Feedback(self, AntesTesouroDireto, DepoisTesouroDireto, AntesAcoes, DepoisAcoes, AntesCriptoMoedas, DepoisCriptoMoedas):
        
        display.fill(BRANCO)
        display.blit(fonteGrande.render("FEEDBACK DA RODADA", True, PRETO), (300, 30))
        display.blit(fonte.render("Esse foi o desempenho dos seus investimentos, emprestimos e dívidas fixas.", True, PRETO), (200, 90))
        
        pygame.draw.rect(display, CINZA, pygame.Rect(70, 150, 800, 90))
        pygame.draw.rect(display, BRANCO, pygame.Rect(70, 140, 110, 30))
        display.blit(fonte.render("Investimentos", True, PRETO), (70, 140))
        display.blit(fonteGrande.render("|", True, PRETO), (350, 150))
        display.blit(fonteGrande.render("|", True, PRETO), (350, 188))
        display.blit(fonteGrande.render("|", True, PRETO), (600, 150))
        display.blit(fonteGrande.render("|", True, PRETO), (600, 188))

        if int(DepoisTesouroDireto) > int(AntesTesouroDireto):
            pygame.draw.circle(display, VERDE, (100,200), 20)
            
        elif int(AntesTesouroDireto) > int(DepoisTesouroDireto):
            pygame.draw.circle(display, VERMELHO, (100,200), 20)
            
        else:
            pygame.draw.circle(display, PRETO, (100,200), 20)
        
        display.blit(fonte.render("TESOURO DIRETO", True, PRETO), (185, 150))
        display.blit(fonte.render("Aplicado: R$ " + AntesTesouroDireto, True, PRETO), (135, 178))
        display.blit(fonte.render("Retirado: R$ " + DepoisTesouroDireto, True, PRETO), (135, 203))

        if int(DepoisAcoes) > int(AntesAcoes):
            pygame.draw.circle(display, VERDE, (390,200), 20)

        elif int(AntesAcoes) > int(DepoisAcoes):
            pygame.draw.circle(display, VERMELHO, (390,200), 20)

        else:
            pygame.draw.circle(display, PRETO, (390,200), 20)
        
        display.blit(fonte.render("AÇÕES", True, PRETO), (440, 150))
        display.blit(fonte.render("Aplicado: R$ " + AntesAcoes, True, PRETO), (425, 178))
        display.blit(fonte.render("Retirado: R$ " + DepoisAcoes, True, PRETO), (425, 203))

        if int(DepoisCriptoMoedas) > int(AntesCriptoMoedas):
            pygame.draw.circle(display, VERDE, (640,200), 20)

        elif int(AntesCriptoMoedas) > int(DepoisCriptoMoedas):
            pygame.draw.circle(display, VERMELHO, (640,200), 20)

        else:
            pygame.draw.circle(display, PRETO, (640,200), 20)
            
        display.blit(fonte.render("CRIPTO MOEDAS", True, PRETO), (660, 150))
        display.blit(fonte.render("Aplicado: R$ " + AntesCriptoMoedas, True, PRETO), (675, 178))
        display.blit(fonte.render("Retirado: R$ " + DepoisCriptoMoedas, True, PRETO), (675, 203))

        SaldoEmprestimo = 0
        for i in range(3):
            if self.Emprestimos[i + 1][0] != "":
                SaldoEmprestimo = SaldoEmprestimo + int(self.Emprestimos[i + 1][0])
        
        pygame.draw.rect(display, CINZA, pygame.Rect(70, 265, 800, 90))
        pygame.draw.rect(display, BRANCO, pygame.Rect(70, 265, 110, 30))
        display.blit(fonte.render("Emprestimos", True, PRETO), (70, 265))
        display.blit(fonte.render("Saldo devedor:", True, PRETO), (200, 305))
        display.blit(fonteGrande.render("R$ " + str(SaldoEmprestimo), True, PRETO), (400, 295))
        
        pygame.draw.rect(display, CINZA, pygame.Rect(70, 390, 800, 90))
        pygame.draw.rect(display, BRANCO, pygame.Rect(70, 390, 110, 30))
        display.blit(fonte.render("Dívidas Fixas", True, PRETO), (70, 390))
        display.blit(fonte.render("Saldo devedor:", True, PRETO), (200, 430))
        display.blit(fonteGrande.render("R$ " + self.despesas[7][1], True, PRETO), (400, 420))

        display.blit(fonteGrande.render("Score: " + str(self.Score), True, PRETO), (720, 485))
         
        pygame.display.flip()

        pygame.time.wait(5000)
                        
fps = pygame.time.Clock()

fonte = pygame.font.SysFont("Arial", 20)
fonteGrande = pygame.font.SysFont("Arial", 40)
fontePequena = pygame.font.SysFont("Arial", 15)

display = pygame.display.set_mode((960,540))

Musica = pygame.mixer.music.load('03. Earth.mp3')
pygame.mixer.music.play(-1,0.0)

#Cores
CINZA = (234,233,233)
PRETO = (0,0,0)
BRANCO = (255,255,255)
AZUL = (0,0,255)
AZUL_CLARO = (185,191,241)
VERDE = (0,255,0)
VERDE_ESCURO = (0,100,0)
VERDE_CLARO = (203, 241, 185)
VERDE_2 = (168, 220, 189)
VERMELHO = (255,0,0)
ROXO = (107, 63, 160)
AMARELO = (255, 255, 0)
LARANJA = (241, 202, 185)

#Rects
SideBar = pygame.Rect(0, 0, 150, 600)
Botao_Investimentos = pygame.Rect(20, 150, 110, 50)
Botao_Bens = pygame.Rect(20, 230, 110, 50)
Botao_Emprestimos = pygame.Rect(20, 310, 110, 50)
Botao_Despesas = pygame.Rect(20, 390, 110, 50)
Botao_Noticias = pygame.Rect(20, 470, 110, 50)
Botao_Dinheiro = pygame.Rect(180, 20, 110, 50)
Botao_FimRodada = pygame.Rect(800, 20, 150, 50)
Botao_X = pygame.Rect(910, 30, 20, 20)
Botao_TrocaPaginas = pygame.Rect(890, 510, 20, 20)
Botao_Pagar = pygame.Rect(475, 480, 160, 30)
PopUp = pygame.Rect(150, 0, 810, 540)
Botao_Investir = pygame.Rect(760, 480, 120, 30)
Text_Box_TesouroDireto = pygame.Rect(215, 420, 120, 30)
Text_Box_Acoes = pygame.Rect(385, 420, 120, 30)
Text_Box_CriptoMoedas = pygame.Rect(555, 420, 120, 30)
Text_Box_PedirEmprestimo = pygame.Rect(235, 305, 120, 30)
Text_Box_PagarEmprestimo1 = pygame.Rect(700, 300, 100, 20)
Text_Box_PagarEmprestimo2 = pygame.Rect(700, 335, 100, 20)
Text_Box_PagarEmprestimo3 = pygame.Rect(700, 370, 100, 20)
PagarEmprestimo1 = pygame.Rect(815, 297, 55, 25)
PagarEmprestimo2 = pygame.Rect(815, 332, 55, 25)
PagarEmprestimo3 = pygame.Rect(815, 367, 55, 25)
ComprarBens_0 = pygame.Rect(800, 185, 90, 30)
ComprarBens_1 = pygame.Rect(800, 275, 90, 30)
ComprarBens_2 = pygame.Rect(800, 365, 90, 30)
ComprarBens_3 = pygame.Rect(800, 455, 90, 30)
PedirEmprestimo = pygame.Rect(250, 345, 85, 30)

#Bolleanos

Tela_Inicial = True
Tela_Investimentos = False
Tela_Bens = False
Tela_Emprestimos = False
Tela_Despesas = False
Tela_Noticias = False
TrocaPaginas = False

#Imagens
Chaves = pygame.image.load('chaves.png')
AdventureCapitalist = pygame.image.load('AdventureCapitalist.png')
TioPatinhas = pygame.image.load('TioPatinhas.png')
SeuSirigueijo = pygame.image.load('SeuSirigueijo.png')
Burns = pygame.image.load('Burns.png')
monopoly = pygame.image.load('monopoly.png')
Jornal = pygame.image.load("Jornal.png")
NotStonks = pygame.image.load("not-stonks.png")
Salario_Imagem = pygame.image.load("Salario.png")
Vitoria = pygame.image.load("Vitoria.png")
Derrota = pygame.image.load("Derrota.png")

jogador = Jogador()
jogador.CalculaSalario()

while True:
    
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if jogador.Investimentos[0][1]:

                if event.unicode and event.unicode.isdigit() and len(jogador.Investimentos[0][0]) < 10:
                    jogador.Investimentos[0][0] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Investimentos[0][0] = jogador.Investimentos[0][0][:-1] 

                if event.key == pygame.K_RETURN:
                    jogador.Investimentos[0][1] = False
                    
            if jogador.Investimentos[1][1] and len(jogador.Investimentos[1][0]) < 10:

                if event.unicode and event.unicode.isdigit():
                    jogador.Investimentos[1][0] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Investimentos[1][0] = jogador.Investimentos[1][0][:-1]

                if event.key == pygame.K_RETURN:
                    jogador.Investimentos[1][1] = False
                    
            if jogador.Investimentos[2][1] and len(jogador.Investimentos[2][0]) < 10:

                if event.unicode and event.unicode.isdigit():
                    jogador.Investimentos[2][0] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Investimentos[2][0] = jogador.Investimentos[2][0][:-1]

                if event.key == pygame.K_RETURN:
                    jogador.Investimentos[2][1] = False

            if jogador.Emprestimos[0][1]:

                if event.unicode and event.unicode.isdigit() and len(jogador.Emprestimos[0][0]) < 10:
                    jogador.Emprestimos[0][0] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Emprestimos[0][0] = jogador.Emprestimos[0][0][:-1] 

                if event.key == pygame.K_RETURN:
                    jogador.Emprestimos[0][1] = False

            if jogador.Emprestimos[1][3]:
                
                if event.unicode and event.unicode.isdigit() and len(jogador.Emprestimos[1][2]) < 10:
                    jogador.Emprestimos[1][2] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Emprestimos[1][2] = jogador.Emprestimos[1][2][:-1] 

                if event.key == pygame.K_RETURN:
                    jogador.Emprestimos[1][3] = False

            if jogador.Emprestimos[2][3]:
                
                if event.unicode and event.unicode.isdigit() and len(jogador.Emprestimos[2][2]) < 10:
                    jogador.Emprestimos[2][2] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Emprestimos[2][2] = jogador.Emprestimos[2][2][:-1] 

                if event.key == pygame.K_RETURN:
                    jogador.Emprestimos[2][3] = False

            if jogador.Emprestimos[3][3]:
                
                if event.unicode and event.unicode.isdigit() and len(jogador.Emprestimos[3][2]) < 10:
                    jogador.Emprestimos[3][2] += event.unicode

                if event.key == pygame.K_BACKSPACE:
                    jogador.Emprestimos[3][2] = jogador.Emprestimos[3][2][:-1] 

                if event.key == pygame.K_RETURN:
                    jogador.Emprestimos[3][3] = False
                    
        if event.type == pygame.MOUSEBUTTONUP:
            
            if Tela_Inicial:
                if Mouse.colliderect(Botao_Investimentos) and not Tela_Investimentos and not Tela_Bens and not Tela_Emprestimos and not Tela_Despesas and not Tela_Noticias:
                    Tela_Investimentos = True
                    Tela_Inicial = False
                if Mouse.colliderect(Botao_Bens) and not Tela_Investimentos and not Tela_Bens and not Tela_Emprestimos and not Tela_Despesas and not Tela_Noticias:
                    Tela_Bens = True
                    Tela_Inicial = False
                if Mouse.colliderect(Botao_Emprestimos) and not Tela_Investimentos and not Tela_Bens and not Tela_Emprestimos and not Tela_Despesas and not Tela_Noticias:
                    Tela_Emprestimos = True
                    Tela_Inicial = False
                if Mouse.colliderect(Botao_Despesas) and not Tela_Investimentos and not Tela_Bens and not Tela_Emprestimos and not Tela_Despesas and not Tela_Noticias:
                    Tela_Despesas = True
                    Tela_Inicial = False
                if Mouse.colliderect(Botao_Noticias) and not Tela_Investimentos and not Tela_Bens and not Tela_Emprestimos and not Tela_Despesas and not Tela_Noticias:
                    Tela_Noticias = True
                    Tela_Inicial = False
                    
                if Mouse.colliderect(Botao_FimRodada):
                    jogador.Rodada = jogador.Rodada + 1
                    jogador.PassarRodada()
            

            if Tela_Investimentos:

                if Mouse.colliderect(Botao_X):
                    Tela_Investimentos = False
                    Tela_Inicial = True
                    
                if Mouse.colliderect(Text_Box_TesouroDireto) and not jogador.Investimentos[1][1] and not jogador.Investimentos[2][1]:
                    jogador.Investimentos[0][1] = True
                if Mouse.colliderect(Text_Box_Acoes) and not jogador.Investimentos[2][1] and not jogador.Investimentos[0][1]:
                    jogador.Investimentos[1][1] = True
                if Mouse.colliderect(Text_Box_CriptoMoedas) and not jogador.Investimentos[0][1] and not jogador.Investimentos[1][1]:
                    jogador.Investimentos[2][1] = True
                    
                if Mouse.colliderect(Botao_Investir) and not jogador.Investimentos[0][1] and not jogador.Investimentos[1][1] and not jogador.Investimentos[2][1]:
                    Valor = 0
                    for i in range(3):
                        try:
                            Valor = Valor + int(jogador.Investimentos[i][0])
                        except:
                            pass
                    
                    if jogador.Dinheiro >= Valor:

                        jogador.Dinheiro = jogador.Dinheiro - Valor

                        for inv in jogador.Investimentos:
                            try:
                                inv[2] = str(int(inv[2]) + int(inv[0]))
                                inv[0] = ""
                            except:
                                pass
                                                    
            elif Tela_Bens:

                if Mouse.colliderect(Botao_X):
                    Tela_Bens = False
                    Tela_Inicial = True
                    
                if Mouse.colliderect(Botao_TrocaPaginas):
                    TrocaPaginas = not TrocaPaginas

                if Mouse.colliderect(ComprarBens_0):
                    if not TrocaPaginas: 
                        if  not jogador.Bens[0][1] and jogador.Dinheiro >= int(jogador.Bens[0][3]):
                            jogador.Bens[0][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[0][3])
                            Bem_Comprado = jogador.Bens.pop(0)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                    else:
                        if not jogador.Bens[4][1] and jogador.Dinheiro >= int(jogador.Bens[4][3]):
                            jogador.Bens[4][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[4][3])
                            Bem_Comprado = jogador.Bens.pop(4)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                    
                if Mouse.colliderect(ComprarBens_1) :
                    if not TrocaPaginas:
                        if not jogador.Bens[1][1] and jogador.Dinheiro >= int(jogador.Bens[1][3]):
                            jogador.Bens[1][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[1][3])
                            Bem_Comprado = jogador.Bens.pop(1)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                    else:
                        if not jogador.Bens[5][1] and jogador.Dinheiro >= int(jogador.Bens[5][3]):
                            jogador.Bens[5][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[5][3])
                            Bem_Comprado = jogador.Bens.pop(5)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                        
                if Mouse.colliderect(ComprarBens_2):
                    if not TrocaPaginas:
                        if not jogador.Bens[2][1] and jogador.Dinheiro >= int(jogador.Bens[2][3]):
                            jogador.Bens[2][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[2][3])
                            Bem_Comprado = jogador.Bens.pop(2)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                    else:
                        if not jogador.Bens[6][1] and jogador.Dinheiro >= int(jogador.Bens[6][3]):
                            jogador.Bens[6][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[6][3])
                            Bem_Comprado = jogador.Bens.pop(6)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                        
                if Mouse.colliderect(ComprarBens_3):
                    if not TrocaPaginas:
                        if not jogador.Bens[3][1] and jogador.Dinheiro >= int(jogador.Bens[3][3]):
                            jogador.Bens[3][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[3][3])
                            Bem_Comprado = jogador.Bens.pop(3)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])
                    else:
                        if not jogador.Bens[7][1] and jogador.Dinheiro >= int(jogador.Bens[7][3]):
                            jogador.Bens[7][1] = True
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Bens[7][3])
                            Bem_Comprado = jogador.Bens.pop(7)
                            jogador.Bens.append(Bem_Comprado)
                            jogador.BensComprados.append(Bem_Comprado[0])

            elif Tela_Emprestimos:

                if Mouse.colliderect(Botao_X):
                    Tela_Emprestimos = False
                    Tela_Inicial = True

                if Mouse.colliderect(Text_Box_PedirEmprestimo):
                    jogador.Emprestimos[0][1] = True

                if Mouse.colliderect(Text_Box_PagarEmprestimo1):
                    jogador.Emprestimos[1][3] = True
                    
                if Mouse.colliderect(Text_Box_PagarEmprestimo2):
                    jogador.Emprestimos[2][3] = True
                    
                if Mouse.colliderect(Text_Box_PagarEmprestimo3):
                    jogador.Emprestimos[3][3] = True

                if Mouse.colliderect(PagarEmprestimo1) and jogador.Emprestimos[1][2] != "" and not jogador.Emprestimos[1][3]:
                    if jogador.Dinheiro >= int(jogador.Emprestimos[1][2]):
                        if int(jogador.Emprestimos[1][2]) >= int(jogador.Emprestimos[1][0]):
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[1][0])
                            jogador.Emprestimos[1][2] = ""
                            jogador.Emprestimos[1][0] = ""
                            
                        else:
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[1][2])
                            jogador.Emprestimos[1][0] = str(int(jogador.Emprestimos[1][0]) - int(jogador.Emprestimos[1][2]))
                            jogador.Emprestimos[1][2] = ""
                            
                
                if Mouse.colliderect(PagarEmprestimo2) and jogador.Emprestimos[2][2] != "" and not jogador.Emprestimos[2][3]:
                    if jogador.Dinheiro >= int(jogador.Emprestimos[2][2]):
                        if int(jogador.Emprestimos[2][2]) >= int(jogador.Emprestimos[2][0]):
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[2][0])
                            jogador.Emprestimos[2][2] = ""
                            jogador.Emprestimos[2][0] = ""
                            
                        else:
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[2][2])
                            jogador.Emprestimos[2][0] = str(int(jogador.Emprestimos[2][0]) - int(jogador.Emprestimos[2][2]))
                            jogador.Emprestimos[2][2] = ""
                
                if Mouse.colliderect(PagarEmprestimo3) and jogador.Emprestimos[3][2] != "" and not jogador.Emprestimos[3][3]:
                    if jogador.Dinheiro >= int(jogador.Emprestimos[3][2]):
                        if int(jogador.Emprestimos[3][2]) >= int(jogador.Emprestimos[3][0]):
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[3][0])
                            jogador.Emprestimos[3][2] = ""
                            jogador.Emprestimos[3][0] = ""
                            
                        else:
                            jogador.Dinheiro = jogador.Dinheiro - int(jogador.Emprestimos[3][2])
                            jogador.Emprestimos[3][0] = str(int(jogador.Emprestimos[3][0]) - int(jogador.Emprestimos[3][2]))
                            jogador.Emprestimos[3][2] = ""

                if Mouse.colliderect(PedirEmprestimo) and jogador.Emprestimos[0][0] != "" and int(jogador.Emprestimos[0][0]) <= 5000 and not jogador.Emprestimos[0][1]:
                    for i in range(3):
                        if jogador.Emprestimos[i + 1][0] == "":
                            jogador.Emprestimos[i + 1][0] = jogador.Emprestimos[0][0]
                            jogador.Emprestimos[i + 1][1] = str(round(jogador.Score / 67))
                            jogador.Dinheiro = jogador.Dinheiro + int(jogador.Emprestimos[0][0])
                            jogador.Emprestimos[0][0] = ""
                            break
                    
        
            elif Tela_Despesas:

                if Mouse.colliderect(Botao_X):
                    Tela_Despesas = False
                    Tela_Inicial = True
                    
                if Mouse.colliderect(Botao_Pagar):
                    jogador.PagarDespesas()
                if Mouse.colliderect(jogador.despesas[0][3]):
                    jogador.despesas[0][2] = not jogador.despesas[0][2]
                if Mouse.colliderect(jogador.despesas[1][3]):
                    jogador.despesas[1][2] = not jogador.despesas[1][2]
                if Mouse.colliderect(jogador.despesas[2][3]):
                    jogador.despesas[2][2] = not jogador.despesas[2][2]
                if Mouse.colliderect(jogador.despesas[3][3]):
                    jogador.despesas[3][2] = not jogador.despesas[3][2]
                if Mouse.colliderect(jogador.despesas[4][3]):
                    jogador.despesas[4][2] = not jogador.despesas[4][2]
                if Mouse.colliderect(jogador.despesas[5][3]):
                    jogador.despesas[5][2] = not jogador.despesas[5][2]
                if Mouse.colliderect(jogador.despesas[6][3]):
                    jogador.despesas[6][2] = not jogador.despesas[6][2]
                if Mouse.colliderect(jogador.despesas[7][3]):
                    jogador.despesas[7][2] = not jogador.despesas[7][2]
                if Mouse.colliderect(jogador.despesas[8][3]):
                    jogador.despesas[8][2] = not jogador.despesas[8][2]
                    
                    if jogador.despesas[8][2]:
                        jogador.despesas[0][2] = True
                        jogador.despesas[1][2] = True
                        jogador.despesas[2][2] = True
                        jogador.despesas[3][2] = True
                        jogador.despesas[4][2] = True
                        jogador.despesas[5][2] = True
                        jogador.despesas[6][2] = True
                        jogador.despesas[7][2] = True 
                    else:
                        jogador.despesas[0][2] = False
                        jogador.despesas[1][2] = False
                        jogador.despesas[2][2] = False
                        jogador.despesas[3][2] = False
                        jogador.despesas[4][2] = False
                        jogador.despesas[5][2] = False
                        jogador.despesas[6][2] = False
                        jogador.despesas[7][2] = False 

            elif Tela_Noticias:

                if Mouse.colliderect(Botao_X):
                    Tela_Noticias = False
                    Tela_Inicial = True

    Mouse_X,Mouse_Y = pygame.mouse.get_pos()

    Mouse = pygame.Rect(Mouse_X - 5, Mouse_Y - 5, 10, 10)

    display.fill((255,255,255))

    pygame.draw.rect(display, VERDE_ESCURO, SideBar)
    pygame.draw.rect(display, BRANCO, Botao_Investimentos)
    pygame.draw.rect(display, BRANCO, Botao_Bens)
    pygame.draw.rect(display, BRANCO, Botao_Emprestimos)
    pygame.draw.rect(display, BRANCO, Botao_Despesas)
    pygame.draw.rect(display, BRANCO, Botao_Noticias)
    pygame.draw.rect(display, VERMELHO, Botao_Dinheiro)
    pygame.draw.rect(display, VERDE_ESCURO, Botao_FimRodada)

    display.blit(Chaves, (35,25))
    
    display.blit(AdventureCapitalist, (230,120))
    display.blit(TioPatinhas, (480,60))
    display.blit(SeuSirigueijo, (730,120))

    pygame.draw.ellipse(display, VERDE, (250, 160, 585, 292))
    
    display.blit(Burns, (310,375))
    pygame.draw.circle(display, AZUL, (700,435), 60)
    display.blit(monopoly, (640,375))
    

    display.blit(fonte.render("Investimentos", True, PRETO), (25, 165))
    display.blit(fonte.render("Bens", True, PRETO), (55, 245))
    display.blit(fonte.render("Emprestimos", True, PRETO), (28, 325))
    display.blit(fonte.render("Despesas", True, PRETO), (40, 405))
    display.blit(fonte.render("Noticias", True, PRETO), (45, 485))
    display.blit(fonte.render("Finalizar Rodada", True, BRANCO), (815, 35))
    display.blit(fonte.render("R$ " + str(jogador.Dinheiro), True, BRANCO), (200, 35))

    display.blit(fonteGrande.render("Rodada " + str(jogador.Rodada), True, PRETO), (470, 5))

    if Tela_Investimentos:

        pygame.draw.rect(display, AZUL_CLARO, PopUp)
        display.blit(fonte.render("X", True, PRETO), (910, 30))
        display.blit(fonteGrande.render("Investimentos", True, PRETO), (430, 30))
        display.blit(fonteGrande.render("____________", True, PRETO), (420, 35))
        display.blit(fonte.render("Bem-Vindo a corretora GL, aqui você poderá investir seu dinheiro em três", True, PRETO), (250, 105))
        display.blit(fonte.render("opções de investimentos.", True, PRETO), (430, 130))
        pygame.draw.rect(display, VERMELHO, Botao_Dinheiro)
        display.blit(fonte.render("R$ " + str(jogador.Dinheiro), True, BRANCO), (200, 35))

        pygame.draw.rect(display, BRANCO, pygame.Rect(205, 185, 140, 215))
        pygame.draw.rect(display, PRETO, pygame.Rect(205, 185, 140, 215), 1)
        if jogador.Investimentos[0][1]:
            pygame.draw.rect(display, VERMELHO, Text_Box_TesouroDireto)
        else:
            pygame.draw.rect(display, CINZA, Text_Box_TesouroDireto)
        pygame.draw.rect(display, PRETO, pygame.Rect(215, 420, 120, 30), 1)
        display.blit(fonte.render("TESOURO", True, PRETO), (235, 210))
        display.blit(fonte.render("DIRETO", True, PRETO), (245, 240))
        display.blit(fontePequena.render("Probabilidade: 90%", True, PRETO), (220, 310))
        display.blit(fontePequena.render("Retorno: 10%", True, PRETO), (220, 330))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[0][0], True, PRETO), (220, 425))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[0][2], True, PRETO), (220, 375))
        
        pygame.draw.rect(display, BRANCO, pygame.Rect(375, 185, 140, 215))
        pygame.draw.rect(display, PRETO, pygame.Rect(375, 185, 140, 215), 1)
        if jogador.Investimentos[1][1]:
            pygame.draw.rect(display, VERMELHO, Text_Box_Acoes)
        else:
            pygame.draw.rect(display, CINZA, Text_Box_Acoes)
        pygame.draw.rect(display, PRETO, pygame.Rect(385, 420, 120, 30), 1)
        display.blit(fonte.render("AÇÕES", True, PRETO), (415, 210))
        display.blit(fontePequena.render("Probabilidade: 70%", True, PRETO), (395, 310))
        display.blit(fontePequena.render("Retorno: 30%", True, PRETO), (395, 330))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[1][0], True, PRETO), (395, 425))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[1][2], True, PRETO), (395, 375))

        pygame.draw.rect(display, BRANCO, pygame.Rect(545, 185, 140, 215))
        pygame.draw.rect(display, PRETO, pygame.Rect(545, 185, 140, 215), 1)
        if jogador.Investimentos[2][1]:
            pygame.draw.rect(display, VERMELHO, Text_Box_CriptoMoedas)
        else:
            pygame.draw.rect(display, CINZA, Text_Box_CriptoMoedas)
        pygame.draw.rect(display, PRETO, pygame.Rect(555, 420, 120, 30), 1)
        display.blit(fonte.render("CRIPTO", True, PRETO), (585, 210))
        display.blit(fonte.render("MOEDAS", True, PRETO), (580, 240))
        display.blit(fontePequena.render("Probabilidade: 50%", True, PRETO), (565, 310))
        display.blit(fontePequena.render("Retorno: 50%", True, PRETO), (565, 330))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[2][0], True, PRETO), (565, 425))
        display.blit(fontePequena.render("R$ " + jogador.Investimentos[2][2], True, PRETO), (565, 375))

        pygame.draw.rect(display, BRANCO, pygame.Rect(715, 185, 140, 215))
        pygame.draw.rect(display, PRETO, pygame.Rect(715, 185, 140, 215), 1)
        display.blit(fonte.render("LONGO", True, PRETO), (755, 210))
        display.blit(fonte.render("PRAZO", True, PRETO), (755, 240))

        pygame.draw.rect(display, AZUL, Botao_Investir)
        display.blit(fonte.render("Investir", True, BRANCO), (795, 485))
        
        
    if Tela_Bens:

        pygame.draw.rect(display, VERDE_CLARO, PopUp)
        display.blit(fonte.render("X", True, PRETO), (910, 30))
        display.blit(fonteGrande.render("Bens", True, PRETO), (520, 30))
        display.blit(fonteGrande.render("_____", True, PRETO), (510, 35))
        display.blit(fonte.render("Aqui você poderá comprar bens que oferecem vantagens.", True, PRETO), (340, 90))
        pygame.draw.circle(display, VERDE, (900,520), 10)
        pygame.draw.rect(display, VERMELHO, Botao_Dinheiro)
        display.blit(fonte.render("R$ " + str(jogador.Dinheiro), True, BRANCO), (200, 35))

        if TrocaPaginas:
            inicio = 4
            fim = 7
        else:
            inicio = 0
            fim = 4

        count = 0

        for i in range(inicio, fim):
            
            pygame.draw.rect(display, CINZA, pygame.Rect(200, 150 + (count * 90), 700, 70)) if jogador.Bens[i][1] else pygame.draw.rect(display, BRANCO, pygame.Rect(200, 150 + (count * 90), 700, 70))
            display.blit(fonte.render(jogador.Bens[i][0], True, PRETO), (260, 155 + (count * 90)))
            display.blit(fonte.render(jogador.Bens[i][2], True, PRETO), (210, 195 + (count * 90)))
            display.blit(fonte.render("Preço: " + jogador.Bens[i][3], True, PRETO), (800, 155 + (count * 90)))
            pygame.draw.circle(display, AZUL, (230, 175 + (count * 90)), 20)

            if not jogador.Bens[i][1]:
                pygame.draw.rect(display, AZUL, pygame.Rect(800, 185 + (count * 90), 90, 30))
                display.blit(fonte.render("Comprar", True, BRANCO), (812, 190 + (count * 90)))
            
            count+= 1 

    if Tela_Emprestimos:

        pygame.draw.rect(display, VERDE_2, PopUp)
        display.blit(fonte.render("X", True, PRETO), (910, 30))
        display.blit(fonteGrande.render("Empréstimos", True, PRETO), (420, 30))
        display.blit(fonteGrande.render("____________", True, PRETO), (410, 35))
        display.blit(fonte.render("Aqui você poderá pegar emprestimos no Banco da Nação, mas lembre-se", True, PRETO), (260, 90))
        display.blit(fonte.render("de verificar a taxa de juros do emprestimo.", True, PRETO), (370, 120))
        pygame.draw.rect(display, BRANCO, pygame.Rect(200, 170, 700, 230))
        display.blit(fonte.render("Banco da Nação", True, PRETO), (480, 170))
        display.blit(fontePequena.render("Bem-vindo, aqui você pode pedir emprestimos financeiros de até R$ 5000,00. No entanto, a cada rodada em que", True, PRETO), (230, 200))
        display.blit(fontePequena.render("o emprestimo não for pago, o emprestado irá aumentar com base na taxa de juros.", True, PRETO), (290, 220))
        display.blit(fonte.render("Pedir empréstimo", True, PRETO), (230, 270))
        display.blit(fonte.render("Taxa de Juros", True, PRETO), (400, 270))
        display.blit(fonte.render("Dívidas", True, PRETO), (600, 270))
        display.blit(fonte.render("Score", True, PRETO), (200, 415))
        pygame.draw.rect(display, BRANCO, pygame.Rect(790, 420, 120, 30))
        display.blit(fonte.render(str(jogador.Score) + " pontos", True, VERDE), (805, 425))
        pygame.draw.rect(display, VERMELHO, Botao_Dinheiro)
        display.blit(fonte.render("R$ " + str(jogador.Dinheiro), True, BRANCO), (200, 35))
        pygame.draw.rect(display, CINZA, pygame.Rect(405, 305, 130, 20))
        pygame.draw.rect(display, PRETO, pygame.Rect(405, 305 , 130, 20) , 1)
        display.blit(fontePequena.render(str(round(jogador.Score / 67)) + "% a cada rodada", True, PRETO), (410, 305))
          
        display.blit(fontePequena.render("O score é um sistema de pontuação utilizado pelo banco para determinar se você pode pegar empréstimos ou não", True, PRETO), (210, 455))
        display.blit(fontePequena.render("e qual a taxa de juros será estabelecida. A pontuação varia de acordo com o pagamento das despesas fixas,", True, PRETO), (210, 475))
        display.blit(fontePequena.render("pedidos de empréstimo e pagamento dos empréstimos. Obs: Quanto maior sua pontuação mais fácil para o banco aceitar seu pedido.", True, PRETO), (210, 495))

        if jogador.Emprestimos[0][1]:
            pygame.draw.rect(display, VERMELHO, Text_Box_PedirEmprestimo)
        else:
            pygame.draw.rect(display, CINZA, Text_Box_PedirEmprestimo)

        pygame.draw.rect(display, PRETO, pygame.Rect(235, 305, 120, 30), 1)
        display.blit(fontePequena.render("R$ " + jogador.Emprestimos[0][0], True, PRETO), (240, 310))
        pygame.draw.rect(display, AZUL, PedirEmprestimo)
        display.blit(fonte.render("Confirmar", True, BRANCO), (255, 350))

        if jogador.Emprestimos[1][0] != "":
            pygame.draw.rect(display, CINZA, pygame.Rect(585, 300, 100, 20))
            pygame.draw.rect(display, PRETO, pygame.Rect(585, 300 , 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[1][0] + " | " + jogador.Emprestimos[1][1] + "%", True, PRETO), (590, 300))
            
            pygame.draw.rect(display, VERMELHO, Text_Box_PagarEmprestimo1) if jogador.Emprestimos[1][3] else pygame.draw.rect(display, CINZA, Text_Box_PagarEmprestimo1)
            pygame.draw.rect(display, PRETO, pygame.Rect(700, 300, 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[1][2], True, PRETO), (705, 300))
            pygame.draw.rect(display, AZUL, PagarEmprestimo1)
            display.blit(fonte.render("Pagar", True, BRANCO), (820, 296))
            
        if jogador.Emprestimos[2][0] != "":
            pygame.draw.rect(display, CINZA, pygame.Rect(585, 335, 100, 20))
            pygame.draw.rect(display, PRETO, pygame.Rect(585, 335 , 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[2][0] + " | " + jogador.Emprestimos[2][1] + "%", True, PRETO), (590, 335))
            
            pygame.draw.rect(display, VERMELHO, Text_Box_PagarEmprestimo2) if jogador.Emprestimos[2][3] else pygame.draw.rect(display, CINZA, Text_Box_PagarEmprestimo2)
            pygame.draw.rect(display, PRETO, pygame.Rect(700, 335, 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[2][2], True, PRETO), (705, 335))
            pygame.draw.rect(display, AZUL, PagarEmprestimo2)
            display.blit(fonte.render("Pagar", True, BRANCO), (820, 331))
            
        if jogador.Emprestimos[3][0] != "":
            pygame.draw.rect(display, CINZA, pygame.Rect(585, 370, 100, 20))
            pygame.draw.rect(display, PRETO, pygame.Rect(585, 370 , 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[3][0] + " | " + jogador.Emprestimos[3][1] + "%", True, PRETO), (590, 370))
            
            pygame.draw.rect(display, VERMELHO, Text_Box_PagarEmprestimo3) if jogador.Emprestimos[3][3] else pygame.draw.rect(display, CINZA, Text_Box_PagarEmprestimo3)
            pygame.draw.rect(display, PRETO, pygame.Rect(700, 370, 100, 20) , 1)
            display.blit(fontePequena.render("R$ " + jogador.Emprestimos[3][2], True, PRETO), (705, 370))
            pygame.draw.rect(display, AZUL, PagarEmprestimo3)
            display.blit(fonte.render("Pagar", True, BRANCO), (820, 366))
       
        
    if Tela_Despesas:

        pygame.draw.rect(display, LARANJA, PopUp)
        display.blit(fonte.render("X", True, PRETO), (910, 30))
        display.blit(fonteGrande.render("Despesas Fixas", True, PRETO), (420, 30))
        display.blit(fonteGrande.render("______________", True, PRETO), (410, 35))
        display.blit(fonte.render("Aqui está suas despesas da rodada, o pagamento da conta é opcional, no entanto,", True, PRETO), (250, 105))
        display.blit(fonte.render("contas não pagas iram ser aplicadas juros por rodada de 10%.", True, PRETO), (330, 130))
        pygame.draw.rect(display, VERMELHO, Botao_Dinheiro)
        display.blit(fonte.render("R$ " + str(jogador.Dinheiro), True, BRANCO), (200, 35))
        
        display.blit(fonte.render(jogador.despesas[0][0] + "...............................................................................................", True, PRETO), (300, 200))
        display.blit(fonte.render("R$" + jogador.despesas[0][1], True, PRETO), (805, 205))
        pygame.draw.circle(display, BRANCO, (280,212), 12)
        pygame.draw.circle(display, VERDE, (280,212), 10) if jogador.despesas[0][2] else pygame.draw.circle(display, VERMELHO, (280,212), 10)
        
        display.blit(fonte.render(jogador.despesas[1][0] + "............................................................................................", True, PRETO), (300, 230))
        display.blit(fonte.render("R$" + jogador.despesas[1][1], True, PRETO), (805, 235))
        pygame.draw.circle(display, BRANCO, (280,242), 12)
        pygame.draw.circle(display, VERDE, (280,242), 10) if jogador.despesas[1][2] else pygame.draw.circle(display, VERMELHO, (280,242), 10)
        
        display.blit(fonte.render(jogador.despesas[2][0] + "..........................................................", True, PRETO), (300, 260))
        display.blit(fonte.render("R$" + jogador.despesas[2][1], True, PRETO), (805, 265))
        pygame.draw.circle(display, BRANCO, (280,272), 12)
        pygame.draw.circle(display, VERDE, (280,272), 10) if jogador.despesas[2][2] else pygame.draw.circle(display, VERMELHO, (280,272), 10)
        
        display.blit(fonte.render(jogador.despesas[3][0] + "........................................................................................", True, PRETO), (300, 290))
        display.blit(fonte.render("R$" + jogador.despesas[3][1], True, PRETO), (805, 295))
        pygame.draw.circle(display, BRANCO, (280,302), 12)
        pygame.draw.circle(display, VERDE, (280,302), 10) if jogador.despesas[3][2] else pygame.draw.circle(display, VERMELHO, (280,302), 10)
        
        display.blit(fonte.render(jogador.despesas[4][0] + "........................................................................................", True, PRETO), (300, 320))
        display.blit(fonte.render("R$" + jogador.despesas[4][1], True, PRETO), (805, 325))
        pygame.draw.circle(display, BRANCO, (280,332), 12)
        pygame.draw.circle(display, VERDE, (280,332), 10) if jogador.despesas[4][2] else pygame.draw.circle(display, VERMELHO, (280,332), 10)

        display.blit(fonte.render(jogador.despesas[5][0] + "....................................................................................", True, PRETO), (300, 350))
        display.blit(fonte.render("R$" + jogador.despesas[5][1], True, PRETO), (805, 355))
        pygame.draw.circle(display, BRANCO, (280,362), 12)
        pygame.draw.circle(display, VERDE, (280,362), 10) if jogador.despesas[5][2] else pygame.draw.circle(display, VERMELHO, (280,362), 10)
        
        display.blit(fonte.render(jogador.despesas[6][0] + "............................................................................", True, PRETO), (300, 380))
        display.blit(fonte.render("R$" + jogador.despesas[6][1], True, PRETO), (805, 385))
        pygame.draw.circle(display, BRANCO, (280,392), 12)
        pygame.draw.circle(display, VERDE, (280,392), 10) if jogador.despesas[6][2] else pygame.draw.circle(display, VERMELHO, (280,392), 10)
        
        display.blit(fonte.render(jogador.despesas[7][0] + ".........................................................................................", True, PRETO), (300, 410))
        display.blit(fonte.render("R$" + jogador.despesas[7][1], True, PRETO), (805, 415))
        pygame.draw.circle(display, BRANCO, (280,422), 12)
        pygame.draw.circle(display, VERDE, (280,422), 10) if jogador.despesas[7][2] else pygame.draw.circle(display, VERMELHO, (280,422), 10)
        
        display.blit(fonte.render(jogador.despesas[8][0] + "............................................................................................", True, PRETO), (300, 440))
        display.blit(fonte.render("R$" + jogador.despesas[8][1], True, PRETO), (805, 445))
        pygame.draw.circle(display, BRANCO, (280,452), 12)
        pygame.draw.circle(display, VERDE, (280,452), 10) if jogador.despesas[8][2] else pygame.draw.circle(display, VERMELHO, (280,452), 10)

        display.blit(fonte.render("--------------------------", True, PRETO), (760, 425))

        pygame.draw.rect(display, AZUL, Botao_Pagar)
        
        display.blit(fonte.render("Pagar", True, BRANCO), (532, 483))

    if Tela_Noticias:

        pygame.draw.rect(display, BRANCO, PopUp)
        display.blit(fonte.render("X", True, PRETO), (910, 30))
        display.blit(fonteGrande.render("Notícias", True, PRETO), (500, 5))
        display.blit(fonteGrande.render("________", True, PRETO), (480, 7))
        display.blit(fonte.render("Leia o jornal e veja o que está acontecendo no mundo.", True, PRETO), (350, 55))
        
        display.blit(Jornal, (370, 80))
        display.blit(NotStonks, (573, 180))

        display.blit(fonte.render("JORNAL GLOBE", True, PRETO), (480, 95))
        display.blit(fonte.render("__________________________________", True, PRETO), (400, 100))
        display.blit(fonte.render("Investidor Arriscado: Perda Total", True, PRETO), (430, 130))
        display.blit(fontePequena.render("João Silva, apostando todas as", True, PRETO), (385, 180))
        display.blit(fontePequena.render("suas economias em criptomoedas,", True, PRETO), (380, 200))
        display.blit(fontePequena.render("viu sua renda evaporar devido", True, PRETO), (388, 220))
        display.blit(fontePequena.render("a uma queda drástica no mercado,", True, PRETO), (381, 240))
        display.blit(fontePequena.render("levando João à beira da falência.", True, PRETO), (385, 260))
        display.blit(fontePequena.render("Adam Smith aconselha:", True, PRETO), (480, 290))
        display.blit(fontePequena.render("diversifique seus investimentos para mitigar riscos.", True, PRETO), (415,310))
        display.blit(TioPatinhas, (400,370))
        display.blit(fonte.render("Tio Patinhas está devendo", True, PRETO), (525, 370))
        display.blit(fontePequena.render("Cuidado para essa divida", True, PRETO), (540, 400))
        display.blit(fontePequena.render("não virar uma bola de neve", True, PRETO), (540, 420))
        display.blit(fontePequena.render("Não se deve brincar com juros!", True, PRETO), (530, 450))
   
    fps.tick(60)

    pygame.display.flip()

