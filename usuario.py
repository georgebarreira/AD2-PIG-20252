import tkinter as tk
from tkinter import messagebox

class Usuario(object):
    def __init__(self,uuid_vlr=None, nome=None, cpf=None, data=None, email=None,status=None,senha = None):
        self.uuid_vlr = uuid_vlr
        self.nome = nome
        self.cpf = cpf
        self.data = data
        self.email = email
        self.status = status
        self.senha = senha
        self.listaUsuarios=[]
        return None

    
    
    def buscaUsuario(self, uuid):
        aux=[]
        for i in self.listaUsuarios:
            if i.uuid_vlr == uuid:
                aux.append(i)
        return aux

    
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
    
    
    def cadastraUsuario(self, nome, cpf, data, email, senha, cadastro_callback=None):
        import uuid
        user = []
        uuid_vlr = uuid.uuid4()
        linhaUsuario = [uuid_vlr, nome, cpf, data, email, "offline", senha]
        try:
            if self.validaDados(linhaUsuario[1], linhaUsuario[2], linhaUsuario[3], linhaUsuario[4]) and self.usuarioExiste(linhaUsuario[2], linhaUsuario[4]):
                self.novoUsuario(linhaUsuario[0], linhaUsuario[1], linhaUsuario[2], linhaUsuario[3], linhaUsuario[4], linhaUsuario[5], linhaUsuario[6])
            else:
                tk.messagebox.showerror("Erro", "Dados inválidos ou usuário já cadastrado.")
                return False, user
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")
            
            return False , user

        user = self.login(linhaUsuario[2], linhaUsuario[4])
        return True ,user
    def validaLogin(self,cpf,senha):
        user_obj = None
        try:
            with open('usuarios.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    usuario = line.strip().split(',')
                    if cpf == usuario[2] and senha == usuario[6]:
                    # Cria e retorna o objeto Usuario ao invés do array
                        user_obj = Usuario(
                            uuid_vlr=usuario[0],
                            nome=usuario[1],
                            cpf=usuario[2],
                            data=usuario[3],
                            email=usuario[4],
                            status=usuario[5],
                            senha=usuario[6]
                        )
                        user_obj.status = "online"
                
            f.close()
            return user_obj
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao validar login: {e}")
            return user_obj
        
                    
            
    def login(self,cpf,senha):
        user_obj = None
        aux=[]
        try:
            aux=self.validaLogin(cpf,senha)
            if len(aux) > 0:
                
                        return aux
            else: 
                tk.messagebox.showerror("Erro", "CPF ou senha inválidos.")
                return aux
        finally:   
            return aux
    
    def novoUsuario(self,uuid, nome, cpf, data, email,status,senha): 
        usuario = Usuario(uuid, uuid, cpf, data, email, status)
        self.listaUsuarios.append(usuario)
        try:
            with open('usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"\n{uuid},{nome},{cpf},{data},{email},{status},{senha}")
                f.close()
            tk.messagebox.showinfo("Cadastro",f"Usuário cadastrado!\nNome: {nome}\nCPF: {cpf}\nData: {data}\nEmail: {email}\n")
                                  

           
            self.loadUsers()


            return True
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Erro ao salvar usuário no arquivo: {e}")
        return False
    
    def loadUsers(self):
        with open ('usuarios.txt', 'r',encoding='utf-8') as file:
            for linha in file:
                aux=linha.strip().split(',')
                self.listaUsuarios.append(aux)
                Usuario(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6])
            
            file.close()
        return None
    def saveUsers(self):
        with open('usuarios.txt', 'w', encoding='utf-8') as file:
            for i in range(len(self.listaUsuarios)):
                file.write(f'{self.listaUsuarios[i][0]},{self.listaUsuarios[i][1]},{self.listaUsuarios[i][2]},{self.listaUsuarios[i][3]},{self.listaUsuarios[i][4]},{self.listaUsuarios[i][5]}\n')
            file.close()
        return None
    
        
    
                    
