from desenhos_fofin import corpo
from random import randint
from palavras import palavras

def run():
    print("""
    ###########################################################
    #################### JOGO DA FORCA #########################
    ###########################################################
    """)

    try:
        # ABRE OS ARQUIVOS DE SCORE E DERROTA EM MODO LEITURA
        arquivo_score = open('score_forca.txt','r')
        arquivo_derrotas = open('derrotas_forca.txt','r')
    except:
        # CRIA O ARQUIVO PRA PONTUAÇÃO CASO ELE N EXISTA
        arquivo_score = open('score_forca.txt','w')
        arquivo_score.write('0')
        arquivo_score = open('score_forca.txt','r')
        # CRIA O ARQUIVO PRA DERROTAS CASO ELE N EXISTA
        arquivo_derrotas = open('derrotas_forca.txt','w')
        arquivo_derrotas.write('0')
        arquivo_derrotas = open('derrotas_forca.txt','r')

    score = int(arquivo_score.read())
    derrotas = int(arquivo_derrotas.read())

    def sortear_palavra_e_categoria(palavras):
        categoria = list(palavras.keys())[randint(0,len(list(palavras.keys()))-1)]
        palavra = palavras[categoria][randint(0,len(palavras[categoria])-1)]
        return categoria,palavra
        
    continuar = True
    while continuar:
        # SORTEAR PALAVRA
        categoria_e_palavra = sortear_palavra_e_categoria(palavras)
        categoria = categoria_e_palavra[0]
        palavra = categoria_e_palavra[1]

        # CRIA UMA LISTA DO TAMANHO DA PAVRA COM '_' A PREENCHENDO
        letras_acertadas = ['_' for i in range(len(palavra))]

        # INCIALIZA VARIAVEIS NECESSARIAS
        acertou, enforcou = False, False
        erros = 0
        jogadas = 0

        print(f""" 
    VITÓRIA:     {score}
    DERROTAS:    {derrotas}

    CATEGORIA: {categoria}
        """)

        while(not acertou and not enforcou):

            print(corpo[erros])
            print(letras_acertadas)

            chute = input('Chute uma letra: ')
            
            # VERIFICA SE O CHUTE ESTÁ CORRETO E SUBSTITUE A LETRA NA LISTA DE LETRAS ACERTADAS
            if (chute.upper() in palavra.upper()):
                posicao = 0
                for letra in palavra:
                    if chute.upper() == letra.upper():
                        letras_acertadas[posicao] = letra
                    posicao += 1
            
            # INCREMENTA ERROS SE O CHUTE FOI ERRADO
            else:
                erros += 1

            # QND O JOGADOR ERRAR 7 VEZES ELE ENFORCA  
            if erros == 6:
                
                print("""

            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||         ENFORCOU!!!        ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||                            ||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                
                """)

                print(corpo[6])
                print('CONTINUE A NADAR! CONTINUE A NADAR!')
                
                # INCREMENTA O DERROTAS E ADICIONA NO ARQUIVO
                derrotas += 1
                arquivo_derrotas = open('derrotas_forca.txt','w')
                arquivo_derrotas.write(str(derrotas))
                
                continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
                break

            # QND O JOGADOR ACERTAR PARA O LOOP E IMPRIME UMA MSG
            if list(palavra) == letras_acertadas:

                print(f"""
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

                    """)
                
                # INCREMENTA O SCORE E ADICIONA NO ARQUIVO
                score += 1
                arquivo_score = open('score_forca.txt','w')
                arquivo_score.write(str(score))
                
                continuar = True if (input('Quer continuar? ')[0].upper() == 'S') else False
                break
            jogadas += 1

    arquivo_score.close()
    arquivo_derrotas.close()
