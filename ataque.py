from vigenere import limpar_texto, decifrar_vigenere
from freq import frequencias_portugues, frequencias_ingles

def indice_coincidencia(texto): #calcula o ic de um texto. o IC ajuda a ver se o texto parece ter sido escrito em linguagem natural
    n = len(texto) #tamanho do texto
    freq = [texto.count(chr(i + ord('A'))) for i in range(26)] #conta a freq de cada letra
    ic = sum(f * (f - 1) for f in freq) / (n * (n - 1)) if n > 1 else 0 #calcula a probabilidade de 2 letras aleatoriamente escolhidas no texto serem iguais
    return ic

def estimar_tamanho_chave(criptograma, max_chave=20):#tenta adivinhar o tamanho da chave usada na cifra. testa tamanhos e ve qual deixa os blocos de texto com um ic natural.
    criptograma = limpar_texto(criptograma)
    medias = [] #guardar a media dos ics p cada tamanho testado
    for tamanho in range(1, max_chave + 1): #testa tamanhos de 1 ate max chave(no caso 20)
        ics = []# guarda os ics de cada bloco pro tamanho testado atual
        for i in range(tamanho):#divide o criptograma em x blocos, sendo x = tamanho
            bloco = criptograma[i::tamanho]#pega um bloco de tamanho em tamanho letras. se tamanho = 3, pega a letra 1,4,7.10..
            ics.append(indice_coincidencia(bloco))#guarda o ic de cada bloco
        medias.append((tamanho, sum(ics) / len(ics)))#calcula e guarda a media junto c os tamanhos
    medias.sort(key=lambda x: -x[1])#organiza as medias d maior pra menor

    print("Tamanhos de chaves e possibilidades: ", medias)
    
    return medias[0][0]#retorna o tamanho de chave com a maior media

def frequencia_relativa(texto):#frequência relativa (em porcentagem) de cada letra no texto
    total = len(texto)#total de letras no texto
    return [texto.count(chr(i + ord('A'))) / total for i in range(26)]#frequencia de cada letra dividido pelo total

def chi_quadrado(obs, exp):
    return sum((o - e)**2 / e for o, e in zip(obs, exp))#comparar duas distribuições de frequência (uma observada e uma esperada)

def descobrir_senha(criptograma, lingua):
    criptograma = limpar_texto(criptograma)
    freq_ref = frequencias_portugues if lingua == 'portugues' else frequencias_ingles #define qual tabela de ref usar
    freq_ref = [freq_ref[chr(i + ord('A'))]/100 for i in range(26)] #converte de porcentagem pra proporcao

    tamanho = estimar_tamanho_chave(criptograma)
    print("Tamanho estimado da chave de maior possibilidade: ", tamanho)
    print("Gostaria de continuar com esse tamanho? S/N")
    simounao = input()
    if simounao.upper() == "S":
        tamanho = tamanho
    else:
        print("Qual o tamanho de chave que você gostaria?")
        tamanho = int(input())
    senha = ''

    for i in range(tamanho):
        bloco = criptograma[i::tamanho]
        melhor_chave = 0
        menor_chi = float('inf')

        for k in range(26):#tenta todas as letras do alfabeto
            decifrado = ''.join(chr((ord(c) - ord('A') - k) % 26 + ord('A')) for c in bloco)#decifra o bloco atual com cada letra
            freq = frequencia_relativa(decifrado)#calcula a freq relativa do bloco
            chi = chi_quadrado(freq, freq_ref)#compara essa freq com a freq da lingua de referencia
            if chi < menor_chi:
                menor_chi = chi #atualiza o menor chi quadrado
                melhor_chave = k#guarda a letra da chave que gerou esse chi
        
        senha += chr(melhor_chave + ord('A'))#adiciona a letra da chave encontrada à senha estimada
    print("Senha estimada:" + senha)
    mensagem_estimada = decifrar_vigenere(criptograma, senha)
    print("Mensagem estimada:" + mensagem_estimada)

    return senha



