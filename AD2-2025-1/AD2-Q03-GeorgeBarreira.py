def lerArquivo(nome_arquivo):
    """Lê o conteúdo de um arquivo e retorna uma string com o texto."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return ""

def limparTexto(texto):
    """Remove pontuações e converte o texto para minúsculas."""
    texto_limpo = ''
    for caractere in texto:
        if caractere.isalnum() or caractere.isspace():
            texto_limpo += caractere.lower()
    return texto_limpo

def contarPalavras(texto):
    """Conta as ocorrências de cada palavra no texto e retorna um dicionário."""
    palavras = texto.split()
    contador = {}
    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1
    return contador

def frequencia(contador):
    """Ordena o dicionário de palavras por frequência decrescente."""
    return sorted(contador.items(), key=lambda item: item[1], reverse=True)

def imprimir(palavras_ordenadas):
    """Imprime as palavras e suas contagens."""
    for palavra, contagem in palavras_ordenadas:
        print(f"{palavra} {contagem}")

def main():
    nome_arquivo = input("Digite o nome do arquivo texto: ").strip()
    texto = lerArquivo(nome_arquivo)
    if texto:
        texto_limpo = limparTexto(texto)
        contador = contarPalavras(texto_limpo)
        palavras_ordenadas = frequencia(contador)
        imprimir(palavras_ordenadas)


main()
