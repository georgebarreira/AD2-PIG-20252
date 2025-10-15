from usuario import Usuario
from voos import Voos
from login import Login

def cadastroUsuario():
    
    nome=input("Digite seu nome: ")
    cpf=input("Digite seu CPF (somente números): ")
    data = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    email=input("Digite seu email: ")
    import uuid
    uuid_vlr = uuid.uuid4()
    user=Usuario()
    linhaUsuario= [uuid_vlr, nome, cpf, data, email, "offline"]
    user.cadastraUsuario(linhaUsuario)
    return user

def main():
    VERMELHO = '\033[1;31m'
    AZUL = '\033[1;34m'
    VERDE = '\033[0;32m'
    AMARELO = '\033[1;33m'
    RESET = '\033[0m'
    dados = []
    with open("voos.txt", "r",encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 7:
                dados.append(parts)
    file.close()
    voos=Voos()
    for linha in dados:
        voos.adicionaLinhaVoos(linha)
    
    dados=[]

    with open("assentos.txt", "r",encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                dados.append(parts)
    file.close()
    
    for linha in dados:
        voos.adicionaAssento(linha)

    user=[]

    
    usuario=Usuario()
    usuario.loadUsers() 
    
      
    logado=False
    while True:
        if logado==False:
            Bemvindo = "Rio AirWays - Sistema de Reserva de Viagens"
            print("\n"+Bemvindo+"\n")
           
            print("Menu Principal:\n")
            print("1 - Cadastrar Usuário")
            print("2 - Fazer Login")
            print("3 - Sair")
            print("Escolha uma opção:" ,end=" ")
            choice = input()
            try:
                if choice == "1":
                    usuario.cadastraUsuario()
                elif choice == "2":
                    print("Digite seu CPF (somente números):", end=" ")
                    cpf = input()
                    print("Digite seu email:", end=" ")
                    email = input()
                    login = Login(cpf, email)
                    user=login.login()
                    if len(user)!=0:
                        logado=True
                elif choice == "3":

                    print(f"\n{AMARELO}Saindo...{RESET}\n")
                    break
                else:
                    raise ValueError(f"{VERMELHO}\nOpção inválida. Tente novamente.{RESET}")
            except ValueError:
                print(f"{VERMELHO}\nOpção inválida. Tente novamente.{RESET}\n")
                continue
                    
        elif logado==True:
            
            
            
            print("\nBem-vindo(a),", user[0][1],"\n")
            
            logado=voos.emReserva(user[0])

            # itens a corrigir:

            # adicionar aos whiles erros validando entradas - corrigido
            # corrigir listar todas reservas - corrigido
            # adicionar salvar arquivos ao sofrerem modificações - pendente
            # fazer logout não funciona - Corrigido

            #Requisitos faltantes:
            
            # 1- O passageiro não pode reservar mais de um assento por voo - Corrigido
            # 2- Um assento na saída de emergência não pode ser reservado por um 
            # passageiro menor de 18 anos;
            # 3- Todas as ações realizadas por um usuário no sistema devem ser 
            # registradas em um log;
            # 4- Deve existir controle de concorrência para evitar conflitos em 
            # operações quando múltiplos usuários concorrem pelo mesmo recurso. 
            # Por exemplo, dois usuários podem tentar reservar o mesmo assento ao 
            # mesmo tempo.
            # 5- Múltiplos passageiros podem acessar e utilizar o sistema 
            # simultaneamente.

            # tenho que rever como vai funcionar pois o Usuario.loadUsers()
            # users deveria ser feito apenas dentro da classe para evitar 
            # #consumo excessivo de tudo
    return None
main()

