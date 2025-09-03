

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

    def adicionaUsuario(self, nova_linha):
        usuario = Usuario(nova_linha[0], nova_linha[1], nova_linha[2], nova_linha[3], nova_linha[4], nova_linha[5])
        self.listaUsuarios.append(usuario)
        return None
    def cadastraUsuario(self, uuid_vlr, nome, cpf, data, email,status):
        try:
            teste= self.usuarioExiste(cpf , email)
            teste2 = self.validaDados(nome, cpf, data, email)
            print("resultado teste: ",teste)
            print("resultado teste2: ",teste2)
            if self.validaDados(nome, cpf, data, email) and self.usuarioExiste(cpf, email):
                
                
                self.novoUsuario(uuid_vlr, nome, cpf, data, email,status) 
            else:
                print()
                raise ValueError("Dados inválidos ou usuário já cadastrado.")
                
        except Exception as e:
            print()
            print(f"Erro ao cadastrar usuário: {e}")
        
        return
    
    
    
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
    
    def novoUsuario(self,uuid, nome, cpf, data, email,status): #talvez não precise
        usuario = Usuario(uuid, uuid, cpf, data, email, status)
        self.listaUsuarios.append(usuario)
        try:
            with open('usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"{uuid},{nome},{cpf},{data},{email},{status}\n")
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


            return True
        except Exception as e:
            print()
            print(f"Erro ao salvar usuário no arquivo: {e}")
            print()
        return False
   
            
        
        
    
                    
