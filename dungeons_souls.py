class SerHumano:
    def __init__(self):
        self.visual = 0 
        self.vida = 0 
    
    def setVida(self, vida):
        self.vida = vida

    def setVisual(self, visual):
        self.visual = visual

    def getVida(self):
        return self.vida
    
    def getVisual(self):
        return self.visual
    
    def atacar(self):
        return 'O player esta atacando'
    
    def andar(self):
        return 'O player esta andando'     

class Xp:
    def __init__(self):
        self.experiencia = 0
        self.visual = None 

    def setExperiencia(self, experiencia):
        self.experiencia = experiencia

    def setVisual(self, visual):
        self.visual = visual

    def getExperiencia(self):
        return self.experiencia
    
    def getVisual(self):
        return self.visual
        

class Bonfire:
    def __init__(self):
        self.visual = None 

    def setVisual(self, visual):
        self.visual = visual

    def getVisual(self):
        return self.visual
    
    def ressurgir(self):
        return 'O player foi ressucitado'
    
    def curarPlayer(self):
        return 'O player foi curado'

class Player(SerHumano, Bonfire, Xp):
    def __init__(self):
        SerHumano.__init__(self)
        Bonfire.__init__(self)
        Xp.__init__(self)  
        self.dano = 0
        self.nome = None
       
    def setDano(self, dano):
        self.dano = dano

    def setNome(self, nome):
        self.nome = nome

    def getDano(self):
        return self.dano
    
    def getNome(self):
        return self.nome
    


class Inimigo(SerHumano):
    def __init__(self):
        super().__init__()
        self.dano = 0 

    def setDano(self, dano):
        self.dano = dano

    def getDano(self):
        return self.dano

class Boss(Inimigo):
    def __init__(self):
        super().__init__()
        self.danoBoss = 0 if self.dano is None else self.dano * 2
        self.vidaBoss = 0 if self.vida is None else self.vida * 3

    def setDanoBoss(self, danoBoss):
        self.danoBoss = danoBoss 

    def setVidaBoss(self, vidaBoss):
        self.vidaBoss = vidaBoss

    def getDanoBoss(self):
        return self.danoBoss
    
    def getVidaBoss(self):
        return self.vidaBoss

class ArvoreHabilidade(Player):
    def __init__(self):
        super().__init__()  





   
def objHabilidade():
    habilidades = ArvoreHabilidade()

    return habilidades

def objBoss():
    boss = Boss()

    return boss  

def objXp():
    xp = Xp()

    return xp

def objPlayer():
    jogador = Player()
    
    print("----------------------------------------------")
    print("Criando o Player")
    print("----------------------------------------------")
    print(" ")
    dano = float(input("Digite o dano do jogador: "))
    nome = str(input("Digite o nome do jogador: "))
    vida = int(input("Digite a vida do jogador: "))
    visual = str(input("Digite o visual do jogador: "))
    
    jogador.setDano(dano)
    jogador.setNome(nome)
    jogador.setVida(vida)
    jogador.setVisual(visual)
    
    return jogador

def objInimigo():
    inimigo = Inimigo()

    print("----------------------------------------------")
    print("Criando Inimigo")
    print("----------------------------------------------")   
    print(" ") 
    dano = float(input("Digite o dano do Inimigo: "))
    vida = int(input("Digite a vida do Inimigo: "))
    visual = str(input("Digite o visual do Inimigo: "))

    inimigo.setDano(dano)
    inimigo.setVida(vida)
    inimigo.setVisual(visual)

    return inimigo 

    

def exibindoDadosObjInimigo(inimigo):
    print("Vida: {}".format(inimigo.getVida()))
    print("Dano: {}".format(inimigo.getDano()))
    print("Visual: {}".format(inimigo.getVisual()))

def exibindoDadosObjPlayer(jogador):
    print("Nome: {}".format(jogador.getNome()))
    print("Dano: {}".format(jogador.getDano()))
    print("Vida: {}".format(jogador.getVida()))
    print("Visual: {}".format(jogador.getVisual()))

def funcPlayer():
    print("[1] - Andar")
    print("[2] - Atacar")

contadorPlayer = 0

def catarXp():
    print("Deseja catar o XP? S/N")

while True:

    xpPlayer = objXp()
    boss = objBoss()
    
    if (contadorPlayer == 0):
        jogador = objPlayer()
        inimigo = objInimigo()

        contadorPlayer += 1
    else:
        if jogador != None:
            if inimigo != None:

                funcPlayer()

        funcaoPlayer = int(input("Qual opção deseja: "))

        if funcaoPlayer == 1:
            print(jogador.andar())
        elif funcaoPlayer == 2:
            print(jogador.atacar())

            if jogador.getVida() >= inimigo.getVida() and jogador.getDano() > inimigo.getDano():
                print("Inimigo derrotado")
                print(" ")

                catarXp()
                exp = str(input())

                if (exp == 'S'):
                    expAtual = jogador.getExperiencia()

                    newExp = expAtual + 1000
                    jogador.setExperiencia(newExp)

                    print("Deseja upar o dano? S/N ")
                    danoAument = str(input())

                    if (danoAument == 'S'):
                        print("Você tem {} XP".format(jogador.getExperiencia()))
                        print(" ")
                        print("Cada nivel custa 500Xp quantos niveis deseja upar: ")
                        nvlUp = int(input())

                        if (nvlUp == 0):
                            break

                        elif (500 * nvlUp == jogador.getExperiencia()):
                            jogador.setExperiencia(0)
                            dano_atual = jogador.getDano()
                            new_dmg = jogador.getDano() + (dano_atual * 0.43) 
                            jogador.setDano(newExp)

                            print("Dano antigo {}".format(dano_atual))
                            print("New dmg {}".format(new_dmg))
                    else:
                        print("Você nao tem xp suficiente")

                else:
                    pass
                enfrentarBoss = str(input("Deseja enfrentar o boss: S/N "))

                if (enfrentarBoss == 'S'):
                    if (jogador.getVida() >= boss.getVida() and jogador.getDano() > boss.getDano()):
                        xpBoss = 1200
                        newXpBoss = (xpBoss + jogador.getExperiencia())
                        
                        print("O boss dropou uma chave deseja pega-la? ")

                        opcaoChave = str(input())

                        if (opcaoChave == "S"):
                            print("Você zerou o jogo parabens")
                            break
                        else:
                            break
                    else:
                        print(jogador.ressurgir())
                        break    
                else:
                    break
                break
            else:
                print(jogador.ressurgir())
                break
        else:
            print("Erro")
            break
    # exibindoDadosObjPlayer(jogador)
    # exibindoDadosObjInimigo(inimigo)

        

  

    

