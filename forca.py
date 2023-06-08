import random

def jogar():

    abertura() #imprime mensagem na função de abertura
    
    palavra_secreta = carrega_plavara_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)


    enforcou = False
    acertou = False
    erros = 0



    #enquanto true
    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
          marca_chute(chute,letras_acertadas, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros) #mostra erros cometidos

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vitoria()
        
    else:
        imprime_mensagem_derrota(palavra_secreta)#para chamar na função da derrota

    print('Fim de jogo')

def carrega_plavara_secreta():
    arquivo = open('palavras.txt', 'r') #readline
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()


    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def abertura():
    print("------------------*-----------------")
    print('Bem vindo ao Jogo da Forca')
    print('------------------*-----------------')


def inicializa_letras_acertadas(palavra):
    lista =['_' for letra in palavra]
    return lista


def pede_chute():
    chute = input('Qual letra?: ').lower()
    chute = chute.strip().upper()
    return chute


def marca_chute(chute,letras_acertadas, palavra_secreta):
    index = 0  # posição
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()