def menu_principal():
    print("-------------------------------")
    print("-----      Bem Vindo      -----")
    print("----- Sistema Parquimetro -----")
    print("          Dia e hora:          ")
    print("")
    print("1. Administrador")
    print("2. Cliente")
    print("3. Opções")
    print("0. Sair")
    print("")
    print("-------------------------------")
    print("")
    opcaoMP=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMP==1):
        menu_administrador()
        
    elif(opcaoMP==2):
        menu_cliente()
        
    elif(opcaoMP==3):
        menu_opcoes()
        
    elif(opcaoMP==0):
        exit
        




def menu_administrador():
    print("-----------------------------------")
    print("-----      Administrador      -----")
    print("")
    print("1. Ver Zonas")
    print("2. Ver Maquinas")
    print("3. Ver Historico")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------------")
    print("")
    opcaoMA=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMA==1):
        menu_zonas()#Ficheiro
        
    elif(opcaoMA==2):
        menu_maquinas()#Possivelmente melhor em ficheiro
        
    elif(opcaoMA==3):
        #EXTRA
        menu_historicoADMIN()#Ficheiro e é extra para fazer
        
    elif(opcaoMA==4):
        menu_principal()
            
    elif(opcaoMA==0):
        exit

def menu_zonas():
    print("---------------------------")
    print("-----      Zonas      -----")
    print("")
    print()#Ficheiro(Total de Vagas em cada zona)
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("----------------------------")
    print("")
    opcaoMZ=int(input("Escolha a opção pretendida -> "))
        
    if(opcaoMZ==4):
        menu_administrador()
            
    elif(opcaoMZ==0):
        exit

def menu_maquinas():
    print("------------------------------")
    print("-----      Maquinas      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("------------------------------")
    print("")
    opcaoMM=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMM==4):
        menu_administrador()
            
    elif(opcaoMM==0):
        exit
    
def menu_historicoADMIN():
    print("-------------------------------")
    print("-----      Historico      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoMHA=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMHA==4):
        menu_administrador()
            
    elif(opcaoMHA==0):
        exit



def menu_cliente():
    print("-----------------------------")
    print("-----      Cliente      -----")
    print("")
    print("1. Estacionar")
    print("2. Ver Zonas")
    print("3. Ver Historico")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("------------------------------")
    print("")
    opcaoMC=int(input("Escolha a opção pretendida -> "))
    if(opcaoMC==1):
        menu_estacionar()
        
    elif(opcaoMC==2):
        menu_zonas()#Ficheiro
        
    elif(opcaoMC==3):
        menu_historicoCLIENTE()#Ficheiro e é extra para fazer
        
    elif(opcaoMC==4):
        menu_principal()
        
    elif(opcaoMC==0):
        exit

def menu_estacionar():
    print("--------------------------------")
    print("-----      Estacionar      -----")
    print("")
    print("1. Zona 1")
    print("2. Zona 2")
    print("3. Zona 3")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoME=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoME==1):
        print("")
        #ficheiro zona 1
        
    elif(opcaoME==2):
        print("")
        #ficheiro zona 2
        
    elif(opcaoME==3):
        print("")
        #ficheiro zona 3
        
    elif(opcaoME==4):
        menu_cliente()
        
    elif(opcaoME==0):
        exit

def menu_historicoCLIENTE():
    print("-------------------------------")
    print("-----      Historico      -----")
    print("")
    print()#NOME DO FICHEIRO
    print("")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("--------------------------------")
    print("")
    opcaoMHC=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMHC==4):
        menu_administrador()
            
    elif(opcaoMHC==0):
        exit
    
    
        
def menu_opcoes():
    print("----------------------------")
    print("-----      Opções      -----")
    print("")
    print("1. ")
    print("2. ")
    print("3. ")
    print("4. Voltar")
    print("0. Sair")
    print("")
    print("-----------------------------")
    print("")
    opcaoMO=int(input("Escolha a opção pretendida -> "))
    
    if(opcaoMO==1):
        print("")
        
    elif(opcaoMO==2):
        print("")
        
    elif(opcaoMO==3):
        print("")
        
    elif(opcaoMO==4):
        menu_principal()
        
    elif(opcaoMO==0):
        exit

   
menu_principal()