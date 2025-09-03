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
        assento = Assento(nova_linha[0], nova_linha[1], nova_linha[2], nova_linha[3], nova_linha[4])
        self.assentos.append(assento)
        return None
    def imprimirVoos(self):
        for i in range(len(self.listaVoos)):
            print(f"ID: {self.listaVoos[i][0]}, Trajeto: {self.listaVoos[i][1]} x {self.listaVoos[i][2]}, Data: {self.listaVoos[i][3]}, Embarque: {self.listaVoos[i][4]}, Valor:R$ {self.listaVoos[i][6]},00")
        
        return None

    def salvarAssentos(idvoo):
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
    
    def listarAssentos(self,idvoo):
        VERMELHO = '\033[1;31m'
        AZUL = '\033[1;34m'
        VERDE = '\033[0;32m'
        AMARELO = '\033[1;33m'
        RESET = '\033[0m'
        
        print("\nLegenda:")
        print("Assentos com as letras A e F são na janela")
        print("Assentos com as letras B e E são no meio")
        print("Assentos com as letras C e D são no corredor")
        print(VERMELHO+"Ocupado"+RESET+" "+VERDE+"Disponível"+RESET+" "+AZUL+"Reservado"+RESET+" "+AMARELO+"Bloqueado"+RESET+"\n")
        print("Lista de assentos para o voo", idvoo,"\n")
        for i in self.assentos:
            if i.idvoo == idvoo:
                if i.estado=="ocupado":
                    print(VERMELHO+i.id+RESET,end=" ")
                elif i.estado=="disponivel":
                    print(VERDE+i.id+RESET,end=" ")
                elif i.estado=="reservado":
                    print(AZUL+i.id+RESET,end=" ")
                elif i.estado=="bloqueado":
                    print(AMARELO+i.id+RESET,end=" ")
        print("\n")
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
            for i in range(len(aux)):
                print(f"Seus assentos reservados para o voo {idvoo} são: ", end="")
                print(AZUL+aux[i]+RESET,end=" ")   
        else:
            print(f"Não há assento(s) reservado(s) para o voo {idvoo}.")
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
                    print("Reserva cancelada com sucesso!")
        return True
    
    

       
    
      