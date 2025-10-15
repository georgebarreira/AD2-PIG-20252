import tkinter as tk
from usuario import Usuario
from voos import Voos

app = tk.Tk()
app.title("Rio AirWays - Sistema de Reserva de Viagens")
app.geometry("800x600")

def show_cadastro():
    cadastro_window = tk.Toplevel(app)
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("500x500")
    tk.Label(cadastro_window, text="Tela de Cadastro").pack(pady=10)

    tk.Label(cadastro_window, text="Nome:").pack(anchor="w", padx=20)
    entry_nome = tk.Entry(cadastro_window)
    entry_nome.pack(fill="x", padx=20)

    tk.Label(cadastro_window, text="CPF:").pack(anchor="w", padx=20)
    entry_cpf = tk.Entry(cadastro_window)
    entry_cpf.pack(fill="x", padx=20)

    tk.Label(cadastro_window, text="Data de Nascimento:").pack(anchor="w", padx=20)
    entry_data_nasc = tk.Entry(cadastro_window)
    entry_data_nasc.pack(fill="x", padx=20)

    tk.Label(cadastro_window, text="Email:").pack(anchor="w", padx=20)
    entry_email = tk.Entry(cadastro_window)
    entry_email.pack(fill="x", padx=20)

    tk.Label(cadastro_window, text="Senha:").pack(anchor="w", padx=20)
    entry_senha = tk.Entry(cadastro_window, show="*")
    entry_senha.pack(fill="x", padx=20)

    def salvar_cadastro():
        import uuid
        usuario=[]
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        data_nasc = entry_data_nasc.get()
        email = entry_email.get()
        senha = entry_senha.get()
        sucesso, usuario = Usuario().cadastraUsuario(nome,cpf,data_nasc,email,senha)

        if sucesso and len(usuario) > 0:
            cadastro_window.destroy()  # Fecha a janela de cadastro e retorna à tela inicial
        else:
            cadastro_window.destroy()
            show_cadastro()  # Reabre a janela de cadastro em caso de falha

        
        
        
        
    btn_salvar = tk.Button(cadastro_window, text="Salvar", command=salvar_cadastro)
    btn_salvar.pack(pady=20)

def show_login():
    login_window = tk.Toplevel(app)
    login_window.title("Login")
    login_window.geometry("700x500")
    tk.Label(login_window, text="Tela de Login").pack(pady=20)
    tk.Label(login_window, text="Email:").pack(anchor="w", padx=20)
    entry_email = tk.Entry(login_window)
    entry_email.pack(fill="x", padx=20)

    tk.Label(login_window, text="Senha:").pack(anchor="w", padx=20)
    entry_senha = tk.Entry(login_window, show="*")
    entry_senha.pack(fill="x", padx=20)

    def confirmar_login():
        email = entry_email.get()
        senha = entry_senha.get()
        # Aqui você pode adicionar a lógica de autenticação
        user=Usuario().validaLogin(email, senha)
        if user!=None:
            show_Reserva(user)  # Abre a janela de reserva se o login for bem-sucedido
            login_window.destroy()  # Fecha a janela de login
        else:
            login_window.destroy()
            show_login()  # Reabre a janela de login em caso de falha

    def cancelar_login():
        login_window.destroy()

    btn_frame = tk.Frame(login_window)
    btn_frame.pack(pady=20)

    btn_confirmar = tk.Button(btn_frame, text="Confirmar", command=confirmar_login)
    btn_confirmar.pack(side="left", padx=10)

    btn_cancelar = tk.Button(btn_frame, text="Cancelar", command=cancelar_login)
    btn_cancelar.pack(side="left", padx=10)
    # Adicione campos de login aqui
def show_SelecaoAssentos(assentos, user, idvoo):
    selecao_window = tk.Toplevel(app)
    selecao_window.title(f"Seleção de Assento Voo {idvoo}")
    selecao_window.geometry("800x600")
    tk.Label(selecao_window, text=f"Selecione um assento para o {idvoo}").pack(pady=20)
    
    row_frame = None  # Inicializa fora do loop
    for i, assento in enumerate(assentos):
        # Tenta extrair informações do assento, seja objeto ou tupla/lista
        if hasattr(assento, 'id'):
            assento_id = assento.id
            estado = getattr(assento, 'estado', 'disponivel')
            restricao = getattr(assento, 'restricao', False)
            uuid_assento = getattr(assento, 'uuid', None)
        else:
            assento_id = assento[0]
            estado = assento[1] if len(assento) > 1 else 'disponivel'
            restricao = assento[2] if len(assento) > 2 else False
            uuid_assento = assento[3] if len(assento) > 3 else None

        
        

        
        if estado == "reservado" and user.uuid == uuid_assento:
            bgcolor = 'blue'
        elif estado in ("ocupado", "reservado", "bloqueado"):
            bgcolor = 'red'
        elif estado == "disponivel" and restricao:
            bgcolor = 'yellow'
        elif estado == "disponivel" and not restricao:
            bgcolor = 'green'
        else:
            bgcolor = 'gray'

        # Cria uma nova linha (frame) a cada 6 assentos
        if i % 6 == 0:
            row_frame = tk.Frame(selecao_window)
            row_frame.pack(fill="x", padx=1, pady=1)
        frame_assento = tk.Frame(row_frame)
        frame_assento.pack(side="left", padx=1, pady=1)

        def confirmar_assento(idx=i):
            if hasattr(assentos[idx], 'id'):
                assento_id = assentos[idx].id
            else:
                assento_id = assentos[idx][0]
            selecao_window.destroy()
            # Aqui você pode adicionar lógica para reservar o assento

        # Botão habilitado apenas se disponível
        btn_confirmar = tk.Button(
            frame_assento,
            bg=bgcolor,
            text=f"{assento_id}",
            command=confirmar_assento,
            state="normal" if estado == "disponivel" else "disabled"
        )
        btn_confirmar.pack(side="left", padx=5)
    return
    

def show_Reserva(user):
    
    reserva_window = tk.Toplevel(app)
    reserva_window.title("Reserva de Viagem")
    reserva_window.geometry("800x600")
    tk.Label(reserva_window, text=f"Bem-vindo {user.nome}!").pack(pady=20)
    voos=Voos()
    
    for i in range(len(voos.listaVoos)):
        voo_info = f"{voos.listaVoos[i][0]}, {voos.listaVoos[i][1]} X {voos.listaVoos[i][2]}, Data: {voos.listaVoos[i][3]}, Hora: {voos.listaVoos[i][4]}"
        frame_voo = tk.Frame(reserva_window)
        frame_voo.pack(fill="x", padx=20, pady=5)
        tk.Label(frame_voo, text=voo_info).pack(side="left")

        def confirmar_voo(idx=i):
            
            assentos=voos.retornaAssentos(voos.listaVoos[idx][0])
            show_SelecaoAssentos(assentos, user, voos.listaVoos[idx][0])
            
            

        btn_confirmar = tk.Button(frame_voo, text="Confirmar", command=confirmar_voo)
        btn_confirmar.pack(side="right")

def sair():
    app.destroy()

# Frame centralizado
frame = tk.Frame(app)
frame.place(relx=0.5, rely=0.5, anchor="center")

btn_cadastro = tk.Button(frame, text="Cadastro", width=20, command=show_cadastro)
btn_cadastro.pack(pady=10)

btn_login = tk.Button(frame, text="Login", width=20, command=show_login)
btn_login.pack(pady=10)

btn_sair = tk.Button(frame, text="Sair", width=20, command=sair)
btn_sair.pack(pady=10)

app.mainloop()