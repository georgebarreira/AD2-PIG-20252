
class Login(object):
    
    def __init__(self,cpf,email):
        self.cpf = cpf
        self.email = email
    def login(self):    
        aux=[]    
        lista_usuarios = []
        with open('usuarios.txt', 'r', encoding='utf-8') as f:
            for line in f:
                usuario = line.strip().split(',')
                lista_usuarios.append(usuario)
        f.close()
        for user in lista_usuarios:
            cpf_user = user[2]
            email_user = user[4]
            if cpf_user == self.cpf and email_user == self.email:
                
                aux.append([user[0],user[1],user[2],user[3],user[4],user[5]])
            print(aux)
        if aux:
            return aux
        raise ValueError("\nUsuário não encontrado. Verifique o CPF e o email.\n")
    
