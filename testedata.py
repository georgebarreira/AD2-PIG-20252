

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
print("Entre com data de nascimento no formato DD/MM/AAAA: ", end="")
data_nascimento = input()






maiorIdade(data_nascimento)
