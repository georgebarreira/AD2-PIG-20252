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

    user.adicionaUsuario( uuid_vlr, nome, cpf, data, email, status="offline")
    return user

def main():
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
            if len(parts) == 5:
                dados.append(parts)
    file.close()
    for linha in dados:
        voos.adicionaAssento(linha)
    user=[]
    with open("usuarios.txt", "r",encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                user.append(parts)
    file.close()
    usuario=Usuario()
    for linha in user:
        usuario.adicionaUsuario(linha)
      
    logado=0
    while True:
        if logado==0:
            Bemvindo = "Rio AirWays - Sistema de Reserva de Viagens"
            print("\n"+Bemvindo+"\n")
           
            print("Menu Principal:\n")
            print("1 - Cadastrar Usuário")
            print("2 - Fazer Login")
            print("3 - Sair")
            print("Escolha uma opção:")
            choice = input()

            if choice == "1":
                cadastroUsuario()
            elif choice == "2":
                print("Digite seu CPF (somente números): ")
                cpf = input()
                print("Digite seu email: ")
                email = input()
                login = Login(cpf, email)
                user=login.login()
                if len(user)!=0:
                    logado=1
                
                
                

            elif choice == "3":

                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        elif logado==1:
            print("\nBem-vindo(a),", user[1],"\n")
            while logado==1:
                
                print("Menu Usuário:")
                
                print("1 - Reservar/alterar assentos")
                print("2 - Fazer Logout")
                choice = input("Escolha uma opção:")
                if choice == "1":
                    print("Lista de Voos Disponíveis:\n")
                    voos.imprimirVoos()
                    
                    emReserva=True
                    while emReserva:
                        idvoo=input("\nDigite o ID do voo que deseja reservar/alterar ou 2 para voltar: \n")
                        if idvoo == "2":
                            emReserva=False
                            idvoo=""
                        else:
                            voos.listarAssentos(idvoo)
                            voos.verificaReserva(idvoo, user[0])
                            assentoEmReserva=True
                            
                            while assentoEmReserva:
                                
                                    idAssento=input("Digite o ID do assento: ")
                                    print("1 - Reservar Assentos")
                                    print("2 - Cancelar Reserva")
                                    print("3 - Voltar")
                                    opção = input("Escolha uma opção:")
                                    
                                    if opção == "1":
                                        if voos.reservaAssento(idvoo, idAssento, user[0]):
                                            voos.reservaAssento(idvoo, idAssento, user[0])
                                            voos.listarAssentos(idvoo)
                                            voos.verificaReserva(idvoo, user[0])
                                            voos.imprimirVoos()
                                            assentoEmReserva=False
                                    elif opção == "2":
                                        if voos.cancelarReserva(idvoo, idAssento, user[0]):
                                            voos.cancelarReserva(idvoo, idAssento, user[0])
                                            voos.listarAssentos(idvoo)
                                            voos.verificaReserva(idvoo, user[0])
                                            voos.imprimirVoos()
                                            assentoEmReserva=False
                                    elif opção == "3":
                                        voos.imprimirVoos()
                                        print("\n")
                                        assentoEmReserva=False
                                

                        

                elif choice == "2":
                    logado=0
                    user=[]
                    login=[]
                    print("Fazendo logout...")
                    break
                      
                
                    
            

    return None
main()

