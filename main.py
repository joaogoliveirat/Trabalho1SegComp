from vigenere import cifrar_vigenere, decifrar_vigenere
from ataque import descobrir_senha

print("Deseja cifrar(1), decifrar(2) ou atacar(3)?")

numero = int(input())

if numero == 1:
    print("Qual a mensagem desejada?")
    mensagem = input()
    print("Qual a senha desejada?")
    senha = input()
    criptograma = cifrar_vigenere(mensagem, senha)
    print(criptograma)
if numero == 2:
    print("Qual o Criptograma desejado?")
    criptograma = input()
    print("Qual a senha desejada?")
    senha = input()
    mensagem = decifrar_vigenere(criptograma,senha)
    print(mensagem)
if numero == 3:
    print("Qual o idioma da mensagem?(1- portugues/2- ingles)")
    linguanum = int(input())
    if linguanum == 1:
        lingua = "portugues"
    elif linguanum == 2:
        lingua = 'ingles'
    else:
        print('idioma invalido, sera automatizado para ingles')
        lingua = 'ingles'
    print("Qual o criptograma?")
    criptograma = input()
    tentativa = descobrir_senha(criptograma, lingua)

