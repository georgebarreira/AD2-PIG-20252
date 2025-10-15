def manipulaArquivo(arquivoEntrada):
    with open(arquivoEntrada, 'r', encoding='utf-8') as arquivo:
        
        buffer=[]
        contador=0
        for linha in arquivo:
            buffer.append(linha.strip())
            if len(buffer)==10:
                contador+=1
                with open(f"{contador}temp.txt", "a", encoding='utf-8') as arquivoSaida:
                    buffer.reverse()  # Inverte a lista de linhas
                    for i in range(len(buffer)):
                        linha = buffer[i]
                        if i == len(buffer) - 1 and contador == 1:
                            arquivoSaida.write(linha) # Não adiciona nova linha na última linha do primeiro arquivo
                        else:
                            arquivoSaida.write(linha + "\n") # Adiciona nova linha nas demais linhas
                buffer=[]
                arquivoSaida.close()
        # Verifica se ainda há linhas no buffer após o loop
            elif buffer != []:
                contador+=1
                with open(f"{contador}temp.txt", "a", encoding='utf-8') as arquivoSaida:
                    buffer.reverse()  # Inverte a lista de linhas
                    for i in range(len(buffer)):
                            linha = buffer[i]
                            if i == len(buffer) - 1 and contador == 1:
                                arquivoSaida.write(linha)
                            else:
                                arquivoSaida.write(linha + "\n")
                    buffer=[]
                arquivoSaida.close()
    arquivo.close()
    aux=contador
    while contador > 0:
        with open("arquivoSaida.txt", "a", encoding='utf-8') as arquivoSaida:
            with open(f"{contador}temp.txt", "r", encoding='utf-8') as temp_file:
                for linha in temp_file:
                    arquivoSaida.write(linha)
                contador -= 1
            temp_file.close()
    arquivoSaida.close()
    import os # Remove os arquivos temporários
    for i in range(aux):
        os.remove(f"{i+1}temp.txt")
    return 

def leiaNomeArquivo():
    NomeArquivo = input("Digite o nome do arquivo: ")
    manipulaArquivo(NomeArquivo)
    return 

def main():
    leiaNomeArquivo()
main()            

    
    
            
    

