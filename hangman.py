from tracemalloc import start
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


def sort_word(words):
    category = list(words.keys())[randint(0, len(list(words.keys())) - 1)]
    word = words[category][randint(0, len(words[category]) - 1)]
    return category, word


def defeat_message():
    message = """
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||         ENFORCOU :<<       ||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    """
    print(message)


def start_message():
    message = """
    ###########################################################
    ############### HANGMAN GAME | JOGO DA FORCA ##############
    ###########################################################
    """
    print(message)


def victory_message(word):
    message = f"""
    🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
    🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
    
    PARABÉNS ACERTOU!!! VOCÊ VENCEU!!!     
        A PALAVRA É {word.upper()}!!
        
    🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
    🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆🏆
    """
    print(message)


def get_files():
    try:
        score_file = open("score.txt", "r")
        defeats_files = open("defeat.txt", "r")
    except:
        score_file = open("score.txt", "w")
        score_file.write("0")
        score_file = open("score.txt", "r")
        defeats_files = open("defeat.txt", "w")
        defeats_files.write("0")
        defeats_files = open("defeat.txt", "r")

    return score_file, defeats_files


def run():
    score_file, defeats_files = get_files()

    score = int(score_file.read())
    defeats = int(defeats_files.read())

    continuar = True
    while continuar:
        # SORTEAR PALAVRA
        category_e_palavra = sort_word(words)
        category = category_e_palavra[0]
        palavra = category_e_palavra[1]

        # CRIA UMA LISTA DO TAMANHO DA PAVRA COM '_' A PREENCHENDO
        letras_acertadas = ["_" for i in range(len(palavra))]

        # INCIALIZA VARIAVEIS NECESSARIAS
        acertou, enforcou = False, False
        erros = 0
        jogadas = 0

        while not acertou and not enforcou:
            clean_screen()
            start_message()

            print("=========================")
            print(f"VITÓRIA:     {score}")
            print(f"DERROTAS:    {defeats}")
            print(f"CATEGORY:    {category}")
            print("=========================")

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
                defeat_message()

                print(corpo[6])
                print("CONTINUE A NADAR! CONTINUE A NADAR!")

                defeats += 1
                defeats_files = open("defeats.txt", "w")
                defeats_files.write(str(defeats))

                continuar = (
                    True if (input("Quer continuar? ")[0].upper() == "S") else False
                )
                break

            # QND O JOGADOR ACERTAR PARA O LOOP E IMPRIME UMA MSG
            if list(palavra) == letras_acertadas:
                clean_screen()
                start_message()

                print(corpo[erros])
                print(letras_acertadas)

                victory_message(palavra)

                # INCREMENTA O SCORE E ADICIONA NO file
                score += 1
                score_file = open("score.txt", "w")
                score_file.write(str(score))

                continuar = (
                    True if (input("Quer continuar? ")[0].upper() == "S") else False
                )
                break
            jogadas += 1

    score_file.close()
    defeats_files.close()
