# Define as sequências ANSI para as cores e estilos desejados
class Assento(object):
    
    def __init__(self, id, idvoo, estado, tipo, uuid):
        self.id = id
        self.idvoo = idvoo
        self.estado = estado
        self.tipo = tipo
        self.uuid = uuid
    def getCor(self,identificador):
        VERMELHO = '\033[1;31m'
        AZUL = '\033[1;34m'
        VERDE = '\033[0;32m'
        AMARELO = '\033[1;33m'
        RESET = '\033[0m'
        if self.estado == "ocupado":
            self.cor = VERMELHO+identificador+RESET
        elif self.estado == "disponivel":
            self.cor = VERDE+identificador+RESET
        elif self.estado == "reservado":
            self.cor = AZUL+identificador+RESET
        elif self.estado == "bloqueado":
            self.cor = AMARELO+identificador+RESET
        return self.cor
     

        # Exemplo de uso
        #print(f"{VERMELHO}Este texto aparece em vermelho.{RESET}")
        #print(f"{AZUL}Este texto aparece em azul.{RESET}")
        #print(f"{VERDE}Este texto aparece em verde.{RESET}")
        #print(f"Este texto volta ao normal.")