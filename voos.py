from assentos import Assento
import assentos
class Voos(Assento):
    def __init__(self, id=None, origem=None, destino=None, data=None, horai=None, horaf=None, valor=None):

        self.id = id
        self.origem = origem
        self.destino = destino
        self.data = data
        self.horai = horai
        self.horaf = horaf
        self.valor = valor
        self.assentos = []
        self.listaVoos = []
        
        
        return None
    def adicionaLinhaVoos(self, nova_linha):
        self.id = nova_linha[0]
        self.origem = nova_linha[1]
        self.destino = nova_linha[2]
        self.data = nova_linha[3]
        self.horai = nova_linha[4]
        self.horaf = nova_linha[5]
        self.valor = nova_linha[6]
        self.listaVoos.append(nova_linha)
        return None
    
    def adicionaAssento(self, nova_linha):
        assento = Assento(nova_linha[0], nova_linha[1], nova_linha[2], nova_linha[3], nova_linha[4], nova_linha[5])
        self.assentos.append(assento)
        return None
    
    def imprimirVoos(self):
        print("Lista de Voos Disponíveis:\n")
        for i in range(len(self.listaVoos)):
            print(f"ID: {self.listaVoos[i][0]}, Trajeto: {self.listaVoos[i][1]} x {self.listaVoos[i][2]}, Data: {self.listaVoos[i][3]}, Embarque: {self.listaVoos[i][4]}, Valor:R$ {self.listaVoos[i][6]},00")
        
        return None

    def salvarAssentos(self,idvoo):
        with open("assentos.txt", "w") as file:
            for assento in self.assentos:
                file.write(f"{assento.id},{assento.idvoo},{assento.estado},{assento.tipo},{assento.uuid}\n")
            file.close()
            return None
    
    def salvarVoos(voos):
        with open("voos.txt", "w") as file:
            for voo in voos:
                file.write(f"{voo.id},{voo.origem},{voo.destino},{voo.data},{voo.horai},{voo.horaf}\n")
            file.close()
        return None          
    
    def listarAssentos(self,idvoo,uuidUser):
        VERMELHO = '\033[1;31m'
        AZUL = '\033[1;34m'
        VERDE = '\033[0;32m'
        AMARELO = '\033[1;33m'
        RESET = '\033[0m'
        
        
        print("Assentos contendo: A e F possuem janela | B e E são entre assentos | C e D são no corredor")
        print("Classes: Premium iniciam com 1 | Econômica iniciam com 2 | Executiva iniciam com 3")
        print("Valores: Premium R$ 500,00 | Econômica R$ 300,00 | Executiva R$ 400,00\n")
        
        print(VERMELHO+"Ocupado"+RESET+" "+VERDE+"Disponível"+RESET+" "+AZUL+"Sua Reserva"+RESET+" "+AMARELO+"Restrito - Assentos restritos 18+ anos"+RESET+"\n")
        print("Lista de assentos para o voo", idvoo,"\n")
        for i in self.assentos:
            if i.idvoo == idvoo:
                if i.estado=="reservado" and i.uuid != uuidUser:
                    print(VERMELHO+i.id+RESET,end=" ")
                elif i.estado=="disponivel" and i.restricao=="nao":
                    print(VERDE+i.id+RESET,end=" ")
                elif i.estado=="reservado" and i.uuid == uuidUser:
                    print(AZUL+i.id+RESET,end=" ")
                elif i.restricao=="sim" and i.estado=="disponivel":
                    print(AMARELO+i.id+RESET,end=" ")
                
        print("\n")
        
        return None
    def reservaAssento(self, idvoo, idAssento, uuid):
       for i in self.assentos:
            try:
                if i.idvoo == idvoo and i.id == idAssento and i.estado == "disponivel":
                    if i.estado != "disponivel":
                        raise ValueError("\nAssento não está disponível.\n")
            except ValueError as e:
                print(e)
                return False
            if i.idvoo == idvoo and i.id == idAssento:
                if i.estado == "disponivel":
                    i.estado = "reservado"
                    i.uuid = uuid
                    
                    print("Assento reservado com sucesso!")
                    return True
                
    def verificaReserva(self, idvoo, uuid):
        AZUL = '\033[1;34m'
        RESET = '\033[0m'
        aux=[]
        for i in self.assentos:
            if i.idvoo == idvoo and i.uuid == uuid:
                
                if i.estado == "reservado":
                    aux.append(i.id)
        if len(aux) >0:
            print(f"Seus assentos reservados para o {idvoo} são: ", end="")
            for i in range(len(aux)):
                
                print(AZUL+aux[i]+RESET,end=" ")   
        else:
            print(f"Não há assento(s) reservado(s) para o {idvoo}.")
        print("\n")
               
        return
    def cancelarReserva(self, idvoo, idAssento, uuid):
        for i in self.assentos:
            if i.idvoo == idvoo and i.id == idAssento and i.uuid == uuid and i.estado == "reservado":
                try:
                    if i.estado != "reservado":
                        raise ValueError("\nAssento não está reservado.\n")
                except ValueError as e:
                    print("Erro ao verificar estado do assento:", e)
                    return False
                if i.estado == "reservado":
                    i.estado = "disponivel"
                    i.uuid = ""
                    print("\nReserva cancelada com sucesso!\n")
        return True

    def modificarReserva(self,userUuid):
        print("Favor digitar o ID do assento que deseja modificar:")
        idAssento = input()
        print("Favor digitar o ID do novo assento:")
        novoIdAssento = input()
        try:
            if not any(a.id == novoIdAssento and a.estado == "disponivel" for a in self.assentos):
                raise ValueError("\nNovo assento não está disponível.\n")
        except ValueError as e:
            print(e)
            return False
        for i in self.assentos:
            if i.id == idAssento and i.estado == "reservado" and i.uuid == userUuid and any(a.id == novoIdAssento and a.estado == "disponivel" for a in self.assentos):
                i.estado = "disponivel"
                i.uuid = ""
        for j in self.assentos:
            if j.id == novoIdAssento and j.estado == "disponivel":
                j.estado = "reservado"
                j.uuid = userUuid
                print("\nReserva modificada com sucesso!\n")
                return True
        print("Assento não encontrado ou não está reservado.")
        return False
    def verificaTodasReservas(self,uuidUser):
        AZUL = '\033[1;34m'
        VERMELHO = '\033[1;31m'
        RESET = '\033[0m'
        aux=[]
        
        try:
            for i in self.assentos:
                if i.uuid == uuidUser:
                    aux.append([i.idvoo,i.id])
            if len(aux) >0:
                print(f"\nSeus assentos reservados são:\n")
                for i in range(len(aux)):
                    
                    print(aux[i][0]+" - "+AZUL+aux[i][1]+RESET)   
            
        finally:
            if len(aux) == 0:
                print(f"\n{VERMELHO}Não há assento(s) reservado(s).{RESET}")
        print("\n")
        return None
    def verificaIDVoo(self, idvoo):
        for i in self.listaVoos:
            if i[0] == idvoo:
                return True
        return False
    
    def maiorIdade(data_nascimento):
        from datetime import datetime
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        dataAgora = datetime.today().date()
        print("data agora ", dataAgora)
        print("data agora ", dataAgora.strftime("%d/%m/%Y"))
        print("data nascimento ", data_nascimento.strftime("%d/%m/%Y"))
        idade = dataAgora.year - data_nascimento.year - ((dataAgora.month, dataAgora.day) < (data_nascimento.month, data_nascimento.day))
        print("Idade: ", idade)


        idade = dataAgora.year - data_nascimento.year - ((dataAgora.month, dataAgora.day) < (data_nascimento.month, data_nascimento.day))
        if idade >= 18:
            return True
        else:
            return False

    def emReserva(self, uuidUser):
        VERMELHO = '\033[1;31m'
        AMARELO = '\033[1;33m'
        RESET = '\033[0m'
        while True:
            print("Menu de Reservas:\n")
            print("1 - Reservar Assentos")
            print("2 - Cancelar Reserva")
            print("3 - Alterar Reserva")
            print("4 - Listar Suas Reservas")
            print("5 - Fazer Logout")
            choice = input("\nEscolha uma opção: ")
            try:
                if choice == "1" or choice == "3" or choice == "2":
                    print("Lista de Voos Disponíveis:\n")
                    self.imprimirVoos()
                    idvoo=input("Digite o ID do voo: \n")
                    vooValido=self.verificaIDVoo(idvoo)
                    if vooValido == False:

                        while vooValido == False:
                            print(f"\n{VERMELHO}ID do voo não encontrado. Tente novamente.{RESET}\n")
                            self.imprimirVoos()
                            idvoo=input("Digite o ID do voo: \n")
                            vooValido=self.verificaIDVoo(idvoo)
                    else:       
                        self.listarAssentos(idvoo, uuidUser)
                        
                        if choice == "1":
                            idAssento=input("Digite o ID do assento: ")
                            self.reservaAssento(idvoo, idAssento, uuidUser)
                            self.verificaReserva(idvoo, uuidUser)
                        elif choice == "2":
                            idAssento=input("Digite o ID do assento: ")
                            self.cancelarReserva(idvoo, idAssento, uuidUser)

                        elif choice == "3":
                            self.modificarReserva(uuidUser)
                            self.verificaReserva(idvoo, uuidUser)

                elif choice == "4":
                    #não está funcionando
                    self.verificaTodasReservas(uuidUser)
                elif choice == "5": 
                    user=[]
                    login=[]
                    logado=False
                    print(f"\n{AMARELO}Fazendo logout...{RESET}")
                    #não está funcionando o logout
                    break
                else:
                    raise ValueError(f"{VERMELHO}\nOpção inválida. Tente novamente.{RESET}")
            except ValueError:
                print(f"{VERMELHO}\nOpção inválida. Tente novamente.{RESET}\n")
                continue
            
                    
        return False