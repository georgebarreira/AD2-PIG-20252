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
    return "arquivoSaida.txt"

def leiaNomeArquivo():
    NomeArquivo = input("Digite o nome do arquivo: ")
    
    return NomeArquivo

def verificaArquivos(arquivoEntrada, arquivoSaida):
    teste = False
    bufferEntrada = []
    bufferSaida = []
    contadorEntrada = 0
    contadorSaida = 0
    

    # lê o arquivo de entrada e cria os arquivos temporários de entrada de acordo com o tamanho do buffer
    with open(arquivoEntrada, 'r', encoding='utf-8') as aEntrada: 
        for linha in aEntrada:
            bufferEntrada.append(linha.strip())
            if len(bufferEntrada) == 30:
                contadorEntrada += 1
                with open(f"Entrada{contadorEntrada}.temp", "a", encoding='utf-8') as tempEntrada:
                    for i in range(len(bufferEntrada)):
                        linha = bufferEntrada[i]
                        if i == len(bufferEntrada) - 1 and contadorEntrada == 1:
                            tempEntrada.write(linha)
                        else:
                            tempEntrada.write(linha + "\n")
                bufferEntrada = []
                tempEntrada.close()
            elif bufferEntrada != []:
                contadorEntrada += 1
                with open(f"Entrada{contadorEntrada}.temp", "a", encoding='utf-8') as tempEntrada:
                    for i in range(len(bufferEntrada)):
                        linha = bufferEntrada[i]
                        if i == len(bufferEntrada) - 1 and contadorEntrada == 1:
                            tempEntrada.write(linha)
                        else:
                            tempEntrada.write(linha + "\n")
                    bufferEntrada = []
                tempEntrada.close()
    aEntrada.close()

    # lê o arquivo de saída e cria os arquivos temporários de saída de acordo com o tamanho do buffer    
    with open(arquivoSaida, 'r', encoding='utf-8') as aSaida:
        for linha in aSaida:
            bufferSaida.append(linha.strip())
            if len(bufferSaida) == 30:
                contadorSaida += 1
                with open(f"Saida{contadorSaida}.temp", "a", encoding='utf-8') as tempSaida:
                    for i in range(len(bufferSaida)):
                        linha = bufferSaida[i]
                        if i == len(bufferSaida) - 1 and contadorSaida == 1:
                            tempSaida.write(linha)
                        else:
                            tempSaida.write(linha + "\n")
                bufferSaida = []
                tempSaida.close()
            elif bufferSaida != []:
                contadorSaida += 1
                with open(f"Saida{contadorSaida}.temp", "a", encoding='utf-8') as tempSaida:
                    for i in range(len(bufferSaida)):
                        linha = bufferSaida[i]
                        if i == len(bufferSaida) - 1 and contadorSaida == 1:
                            tempSaida.write(linha)
                        else:
                            tempSaida.write(linha + "\n")
                    bufferSaida = []
                tempSaida.close()
    aSaida.close()

    if contadorEntrada != contadorSaida:
        teste = False
        
        return teste
    elif contadorEntrada == contadorSaida:
        
        for i in range(contadorEntrada):
            with open(f"Entrada{i+1}.temp", "r", encoding='utf-8') as tempEntrada:
                bufferEntrada = tempEntrada.readlines()
                tempEntrada.close()
            with open(f"Saida{i+1}.temp", "r", encoding='utf-8') as tempSaida:
                bufferSaida = tempSaida.readlines()
                tempSaida.close()
            if len(bufferEntrada) != len(bufferSaida):
                teste =+ False
                return teste
            else:
                teste = True
                for i in range(len(bufferEntrada)):
                    if bufferEntrada[i] == bufferSaida[i]:
                        teste = True
                    else:
                        teste += False
                        

        # Remove os arquivos temporários de entrada e saída
        import os
        for i in range(contadorEntrada):
            os.remove(f"Entrada{i+1}.temp")
        for i in range(contadorSaida):
            os.remove(f"Saida{i+1}.temp")
        os.remove(arquivoSaida)
        
   
        aSaida.close()            
    aEntrada.close()
    
    #até aqui
    return teste




def main():
    arquivoEntrada = leiaNomeArquivo()
    arquivoSaida=manipulaArquivo(arquivoEntrada)

    if(verificaArquivos(arquivoEntrada, arquivoSaida)):
        print("Os arquivos são iguais.")
    else:
        print("Os arquivos são diferentes.")

main()            

    
    
            
    

