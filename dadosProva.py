#####################
##### QUESTÃO 1 #####
#####################

def intro():
    # Esta função já está pronta
    print('Bem vindo ao Jogo da Memória')
    print('Você tem que encontrar pares de símbolos iguais')
    print('Informe a posição de cada peça que você quer "virar".')
    print('Se você acertar um par, as peças ficarão viradas,')
    print('mas se errar, você verá as peças viradas apenas por pouco tempo,')
    print('e elas voltarão a ficar ocultas logo depois. Então, preste atenção!')
    print('Para começar, diga seu nome: ')
    n=input()
    print('Com quantos pares de valores você quer jogar?')
    pares=int(input())
    return n,pares

def montaPares(p):
    # Esta função já está pronta

    # Retorna uma lista com p pares aleatórios de caracteres ASCII

    # começa criando uma string com caracteres ASCII dentro de uma faixa de valores (são os caracteres legais)
    # os caracteres de código entre 33 e 126 são caracteres os habituais de textos no nosso idioma
    s=''
    for i in range(33,127):       # a função chr(n) retorna o caracter ASCII correspondente ao inteiro n
        s=s+chr(i)*(chr(i)!='*')  # não queremos o caracter * pois ele já faz parte da máscara

    l=list(s)
    rd.shuffle(l)
    l=l[:p]
    l=l+l
    rd.shuffle(l)
    return l

def imprimeTela(mascara):
    # Você vai precisar completar o código dessa função
    
    # Imprime na tela o cabeçalho e a composição atual da máscara
    
    pares=int(len(mascara)/2)
    
    # Cabeçalho
    lin0='+'+'-+'*(2*pares)
    lin1='|'
    lin2='|'
    for i in range(1,pares*2+1):
        if i//10!=0:
            lin1=lin1+str(i//10)+'|'
        else:
            lin1=lin1+' |'
        lin2=lin2+str(i%10)+'|'

    print(lin0)
    print(lin1)
    print(lin2)
    print(lin0)

    # Máscara
    
    ### 1 #############################################################################
    ###################################################################################
    # Escreva aqui o código necessário para imprimir na tela os caracteres da máscara #
    # Observe no vídeo como essa máscara aparece na tela para fazer da mesma forma    #
    ###################################################################################
    ###################################################################################
    


def recebePalpite(mascara,n):
    # Você vai precisar completar o código dessa função
    
    # Recebe o palpite n, sendo n igual a 0 ou 1 (são dois palpites a cada rodada do jogo)

    if n==0:
        print('Primeiro palpite')
    else:
        print('Segundo palpite')
        

    while True:
    ### 2 #############################################################################
    ###################################################################################
    # Escreva aqui o código necessário para receber um palpite de uma posição válida  #
    # Observe no vídeo a mensagem que é apresentada na tela, e veja a descrição das   #
    # condições de validação do palpite, detalhadas na função principal               #
    # Retorne com o palpite (posição) válido                                          #
    ###################################################################################
    ###################################################################################

    
def memoria(nome, p):
    # Você vai precisar completar o código dessa função
    
    # Sorteia os p pares: misterio é uma lista com 2*p elementos, do elemento 0 ao elemento (2*p-1)
    misterio=montaPares(p)
    
    # Cria uma máscara de 2*p asteriscos, do elemento 0 ao elemento (2*p-1)
    mascara=list('*'*p*2)

    while '*' in mascara:
        # Manda imprimir a tela com a configuração atual da máscara
        imprimeTela(mascara)
        
        # Recebe os dois palpites (posições)
        #    Condições de validação de um palpite:
        #    - devem ser números dentro da quantidade de peças
        #    - não podem ser palpites de posições já "viradas" anteriormente
        #    - o jogador pode dar um ENTER vazio - isso vai fazer o jogo parar
        #    - a validação dos palpites é feita na função recebePalpite
        
        pos=[0,0]  # Posições dos palpites
        car=[0,0]  # Caracteres do mistério que estão nas posições dos palpites
        for i in range(2):    # Este loop controla o recebimento dos dois palpites
            ### 3 ###
            # Substitua o @@@@ abaixo com o código necessário para receber o palpite válido
            
            pos[i]=@@@@ # Chama a função que valida e retorna os palpites

            if pos[i]=='': # O jogador pode dar um ENTER vazio para parar o jogo
                return

            # Para um palpite válido:
            ### 4 ###
            # Substitua o @@@@ abaixo com o código necessário para guardar em 
            # car[i] o caracter correspondente à posição do palpite
            car[i]=@@@@

            ### 5 ###
            # Substitua o @@@@ abaixo com o código necessário para colocar o caracter
            # na posição correspondente na máscara, substituindo o asterisco 
            mascara@@@@
            
            # Manda imprimir a tela com a configuração atual da máscara
            imprimeTela(mascara)

        ### 6 ###
        # Substitua o @@@@ abaixo com o código necessário testar se os caracteres escolhidos são iguais 
        if @@@@ # Se os caracteres correspondentes às posições forem iguais, ACHOU!
            print('Bom palpite! Você encontrou um par')
            time.sleep(1)  # Esse comando dá um tempinho de pausa para o jogador ler a tela     

        else: # Se não forem, tem que virar as peças de novo (colocar * nas posições)
            print('Que pena, você não encontrou um par... Vamos continuar tentando!')
            
            ### 7 ###
            # Substitua o @@@@ abaixo com o código necessário para colocar de novo o asterisco
            # nas posições correspondentes na máscara

            mascara@@@@
            mascara@@@@
            
            time.sleep(3) # Esse comando dá um tempinho de pausa para o jogador ler a tela
    
    ### 8 ###
    # Substitua o @@@@ abaixo com o código necessário verificar se o jogo acabou
    if @@@@
        print()
        print('Muito bom, '+nome+', você encontrou todos os pares!')


#####################
##### QUESTÃO 1 #####
#####################
###########################################
###          ROTINA INICIAL              ###
### Chama o jogo e roda enquanto desejar ###
###          Já está pronta              ###
############################################

import random as rd
import time

nome,p=intro()
jogar='s'

while jogar.startswith('s'):
    # Chama a função principal que controla o jogo
    memoria(nome,p)
    print('\n'+'Quer jogar novamente? [S ou N]')
    jogar=input().lower()


####################
##### QUESTÃO 3 ####
####################
# Dados para teste #
#####################
#Para esses nomes, há empate no aluno Emerson
nomes1='''Ana
Bruna
Cro
Digory
Emerson
Fiaror
Geomar
Iago
Zacarias'''

#Para esses nomes, não testei...
nomes2='''Alan Borges do Couto;
Alan Sauberman Ribeiro;
Bernardo Millan Morgado;
Bernardo Torres da Silva Nascimento;
Breno Tiago Oliveira;
Bruna Valadares Vinhas Antunes;
Catarina Kreitlon Pereira;
Daniel Augusto Medeiros Veloso;
Eduardo Bithencourt Irie;
Emanuelle Peixoto Nunes;
Felipe Domingues Fernandes;
Felipe Luna Silveira Rodrigues;
Flávio Guimarães Bittencourt do Valle;
Gabriel Junqueira Cabral Braga;
Gabriel Thomas da Justa Lemos;
Guilherme Antônio Cota;
Guilherme Braga Moreira Gonçalves;
Guilherme Fernandes Viana de Andrade;
Gustavo Lopes Braga Dias;
Gustavo Schlemper;
Haislan Wellington Gouveia dos Santos;
Henrique Videira da Silva Diniz;
Isabelle Gagno de Miranda;
João Gabriel Antonini Soares da Silveira Lobo;
João Pedro Magalhães Lordelo de Souza;
João Pedro Nascimento Ramos;
João Pedro San Sebastian de Carvalho;
Juan de Araujo Nogueira;
Julia Haddad Motta;
Júlia Miranda Guimarães;
Kaio Torres Dias;
Laura Mondelli Leonardi;
Leonardo Lourenço Gomes;
Lorenzo de Souza Fernandes;
Louise Alves da Cruz;
Lucas Ferreira de Carvalho Marques;
Lucas Rafael de Andrade;
Lucas Teixeira Bonelli;
Luis Felipe Bithencourt Oranges;
Maria Catharina Kako Kamiguchi;
Maria Helena Santos Escaleira de Macedo;
Maria Luiza Miorin de Morais;
Nicholas Alves da Cunha Ribeiro;
Pedro Henrique Santos Soares de Oliveira;
Pedro Lages Gaya;
Renato Smith Lopes;
Victor de Lemos Souza Fernandes;
Victor Duval Senra;
Vinícius Hector Pires Ferreira'''







