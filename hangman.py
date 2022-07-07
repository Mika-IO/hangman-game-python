from art import corpo
from random import randint
from words import words
import os


"""
    TODO:
        add sqlite suport to storage scores information
        refactory variables name to english
        put all words logic inside words.py
        get words list from json files
"""


def clean_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


def sortear_palavra_e_categoria(words):
    categoria = list(words.keys())[randint(0, len(list(words.keys())) - 1)]
    palavra = words[categoria][randint(0, len(words[categoria]) - 1)]
    return categoria, palavra


def run():
    start_message = """
    ###########################################################
    ############### HANGMAN GAME | JOGO DA FORCA ##############
    ###########################################################
    """

    try:
        file_score = open("score.txt", "r")
        file_defeats = open("defeat.txt", "r")
    except:
        file_score = open("score.txt", "w")
        file_score.write("0")
        file_score = open("score.txt", "r")
        file_defeats = open("defeat.txt", "w")
        file_defeats.write("0")
        file_defeats = open("defeat.txt", "r")

    score = int(file_score.read())
    defeats = int(file_defeats.read())

    continuar = True
    while continuar:
        # SORTEAR PALAVRA
        categoria_e_palavra = sortear_palavra_e_categoria(words)
        categoria = categoria_e_palavra[0]
        palavra = categoria_e_palavra[1]

        # CRIA UMA LISTA DO TAMANHO DA PAVRA COM '_' A PREENCHENDO
        letras_acertadas = ["_" for i in range(len(palavra))]

        # INCIALIZA VARIAVEIS NECESSARIAS
        acertou, enforcou = False, False
        erros = 0
        jogadas = 0

        while not acertou and not enforcou:
            clean_screen()

            print(start_message)

            print(
                f""" 
            VITÓRIA:     {score}
            DERROTAS:    {defeats}

            CATEGORIA: {categoria}
                """
            )

            print(corpo[erros])
            print(letras_acertadas)

            chute = input("Chute uma letra: ")

            # VERIFICA SE O CHUTE ESTÁ CORRETO E SUBSTITUE A LETRA NA LISTA DE LETRAS ACERTADAS
            if chute.upper() in palavra.upper():
                posicao = 0
                for letra in palavra:
                    if chute.upper() == letra.upper():
                        letras_acertadas[posicao] = letra
                    posicao += 1

            # INCREMENTA ERROS SE O CHUTE FOI ERRADO
            else:
                erros += 1

            # QND O JOGADOR ERRAR 7 VEZES ELE ENhangman
            if erros == 6:

                print(
                    """

            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||         ENFORCOU!!!        ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                
                """
                )

                print(corpo[6])
                print("CONTINUE A NADAR! CONTINUE A NADAR!")

                defeats += 1
                file_defeats = open("defeats.txt", "w")
                file_defeats.write(str(defeats))

                continuar = (
                    True if (input("Quer continuar? ")[0].upper() == "S") else False
                )
                break

            # QND O JOGADOR ACERTAR PARA O LOOP E IMPRIME UMA MSG
            if list(palavra) == letras_acertadas:
                clean_screen()
                print(start_message)
                print(corpo[erros])
                print(letras_acertadas)
                print(
                    f"""
    . _______ .  #####################################
    ._==_==_=_.  #####################################
    .-\\:/-.
    | (|:.|) |     PARABÉNS ACERTOU!!! você ganhou!!!     
    '-|:.|-'         A PALAVRA É {palavra.upper()}
    \\:: //    
    '::.::'    #####################################
        ) (      #####################################
    _.' '._
    '-------'

                    """
                )

                # INCREMENTA O SCORE E ADICIONA NO file
                score += 1
                file_score = open("score.txt", "w")
                file_score.write(str(score))

                continuar = (
                    True if (input("Quer continuar? ")[0].upper() == "S") else False
                )
                break
            jogadas += 1

    file_score.close()
    file_defeats.close()
