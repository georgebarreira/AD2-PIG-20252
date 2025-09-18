

class Usuario(object):
    def __init__(self,uuid_vlr=None, nome=None, cpf=None, data=None, email=None,status=None):
        self.uuid_vlr = uuid_vlr
        self.nome = nome
        self.cpf = cpf
        self.data = data
        self.email = email
        self.status = status
        self.listaUsuarios=[]
        return None

    
    
    
    
    def validaDados(self, nome, cpf, data, email):
            if not nome or not cpf or not data or not email:
                return False
            if len(cpf) != 11 or not cpf.isdigit():
                return False
            if not self.validaData(data):
                return False
            if not self.validaEmail(email):
                return False
            return True   
    def validaData(self, data):
        dia, mes, ano = data.split('/')
        if len(dia) != 2 or len(mes) != 2 or len(ano) != 4:
            return False
        if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
            return False
        return True 

    def validaEmail(self, email):
        for char in email:
            if char == '@':
                return True
        return False
    def usuarioExiste(self, cpf, email): #rever essa função
            lista_usuarios = []
            with open('usuarios.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    usuario = line.strip().split(',')
                    lista_usuarios.append(usuario)
                    
            
                for user in lista_usuarios:
                    
                    
                    cpf_user = user[2]
                    email_user = user[4]
                    if cpf == cpf_user:
                        return False
                    elif email == email_user:
                        return False
                f.close()
                return True
    
    
    def cadastraUsuario(self):
        nome=input("Digite seu nome: ")
        cpf=input("Digite seu CPF (somente números): ")
        data = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        email=input("Digite seu email: ")
        import uuid
        uuid_vlr = uuid.uuid4()
        
        linhaUsuario= [uuid_vlr, nome, cpf, data, email, "offline"]
        try:
            teste= self.usuarioExiste(linhaUsuario[2] , linhaUsuario[4])
            teste2 = self.validaDados(linhaUsuario[1], linhaUsuario[2], linhaUsuario[3], linhaUsuario[4])
            print("resultado teste: ",teste)
            print("resultado teste2: ",teste2)
            if self.validaDados(linhaUsuario[1], linhaUsuario[2], linhaUsuario[3], linhaUsuario[4]) and self.usuarioExiste(linhaUsuario[2], linhaUsuario[4]):
                self.novoUsuario(linhaUsuario[0], linhaUsuario[1], linhaUsuario[2], linhaUsuario[3], linhaUsuario[4], linhaUsuario[5])
            else:
                print()
                raise ValueError("Dados inválidos ou usuário já cadastrado.")
                
        except Exception as e:
            print()
            print(f"Erro ao cadastrar usuário: {e}")
        user=self.login(linhaUsuario[2],linhaUsuario[4])
        
        return user
    
    def login(self,cpf,email):
        for user in self.listaUsuarios:
            if cpf == self.listaUsuarios[user][2] and email == self.listaUsuarios[user][4]:
                return self.listaUsuarios[user]
        return None
    
    def novoUsuario(self,uuid, nome, cpf, data, email,status): 
        usuario = Usuario(uuid, uuid, cpf, data, email, status)
        self.listaUsuarios.append(usuario)
        try:
            with open('usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{uuid},{nome},{cpf},{data},{email},{status}")
                f.close()
            print("\n")
            print("Usuário cadastrado com sucesso!")
            print(f"Nome cadastrado: {nome}")
            print(f"CPF cadastrado: {cpf}")
            print(f"Data de nascimento: {data}")
            print(f"Email cadastrado: {email}")
            print(f"Status: {status}")
            print("\n")
            input("Pressione enter para retornar ao menu")
            print("\n")
            self.loadUsers()


            return True
        except Exception as e:
            print()
            print(f"Erro ao salvar usuário no arquivo: {e}")
            print()
        return False
    
    def loadUsers(self):
        with open ('usuarios.txt', 'r',encoding='utf-8') as file:
            for linha in file:
                aux=linha.strip().split(',')
                self.listaUsuarios.append(aux)
            print(self.listaUsuarios)
            file.close()
        return None
    def saveUsers(self):
        with open('usuarios.txt', 'w', encoding='utf-8') as file:
            for i in range(len(self.listaUsuarios)):
                file.write(f'{self.listaUsuarios[i][0]},{self.listaUsuarios[i][1]},{self.listaUsuarios[i][2]},{self.listaUsuarios[i][3]},{self.listaUsuarios[i][4]},{self.listaUsuarios[i][5]}\n')
            file.close()
        return None
    
        
    
                    
