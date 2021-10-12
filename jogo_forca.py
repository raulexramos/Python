import random

print('='*20)
print('JOGO DA FORCA v1.0')
print('='*20)
print('Bem vindo ao Jogo da Forca! Vamos começar!')

nome = input("Digite o seu nome: ")
palavra = ('tyson', 'livia', 'rhuan', 'anelize')
palavra_forca = random.choice(palavra)

digitadas = []
acertos = []
erros = 0


while True:
    senha = ""
    for letra in palavra_forca:
        senha += letra if letra in acertos else "_ "
    print(senha)
    if senha == palavra_forca:
        print(f"{nome} acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra_forca:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
            print()
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print(f"{nome} Você foi enforcado!")
        break
