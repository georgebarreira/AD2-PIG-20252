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

    with open("usuarios.txt", "r",encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                user.append(parts)
    file.close()
    usuario=Usuario()
    for linha in user:
        usuario.adicionaUsuario(linha)
      
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
                    cadastroUsuario()
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
            print("\nBem-vindo(a),", user[1],"\n")
            
            logado=voos.emReserva(user[0])
               # itens a corrigir:
               # adicionar aos whiles erros validando entradas
               # adicionar salvar arquivos ao sair e ao adicionar usuários
               # fazer logout não funciona - Corrigido
               
    return None
main()

