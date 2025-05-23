criptograma = ""
def limpar_texto(texto): #remove acentos, espaços, pontuação e transforma tudo em letra maiuscula p simplificar
    return ''.join(c.upper() for c in texto if c.isalpha())

def repetir_senha(senha, tamanho): #repete a senha até ela ter o mesmo tamanho da mensagem(combinar os tamanhos)
    senha = limpar_texto(senha)
    return (senha * (tamanho // len(senha) + 1))[:tamanho]

def cifrar_vigenere(mensagem, senha):#responsavel pela cifra
    mensagem = limpar_texto(mensagem)
    senha_repetida = repetir_senha(senha, len(mensagem))
    criptograma = []#guarda as letras cifradas

    for m, s in zip(mensagem, senha_repetida):#p cada letra da mensagem e da senha
        cifra = (ord(m) - ord('A') + ord(s) - ord('A')) % 26 #pega a posição da letra da mensagem e soma c a da senha(%26 pra manter o resultado no alfabeto)
        #a subtração do ord('A') eh pra transformar num numero basico(ord('A') = 65), (ord('B') = 66) e assim vai
        criptograma.append(chr(cifra + ord('A')))#converte o numero p letra e guarda
    
    return ''.join(criptograma)

def decifrar_vigenere(criptograma, senha):#responsavel por decifrar
    criptograma = limpar_texto(criptograma)
    senha_repetida = repetir_senha(senha, len(criptograma))
    mensagem = []

    for c, s in zip(criptograma, senha_repetida):
        letra = (ord(c) - ord('A') - (ord(s) - ord('A'))) % 26#caminho inverso da cifra
        mensagem.append(chr(letra + ord('A')))
    
    return ''.join(mensagem)
