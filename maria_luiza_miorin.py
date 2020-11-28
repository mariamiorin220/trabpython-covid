# -*- coding: utf-8 -*-
"""Maria-Luiza-Miorin

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Fy0ml0ir6UOfFRhquJzWyPO8YS3F6_I

Questão 2:
Opção 2)
 Sua tarefa é construir uma função Python chamada caixaPlus que recebe
como parâmetros de entrada: (i) um valor numérico inteiro, correspondente ao valor do saque do
cliente; e (ii) uma lista cujos elementos são “duplas” (listas com dois elementos), que informam o valor
e a quantidade de cada tipo de nota disponível, e retorna, como parâmetro de saída, uma lista com
formada por duplas contendo, cada uma delas, o valor e a quantidade de cada nota entregue para
atender à solicitação de saque com a menor quantidade de notas possível. Caso não seja possível
atender, sua função deve retornar uma lista vazia.
"""

def caixaPlus(saque,estoque):
  resposta=[]
  lista=[estoque[x][0]*estoque[x][1] for x in range(0,len(estoque))]
  if sum(lista)<saque:
    a1=False
  else:
    a1=True
  for x in range(0,len(estoque)):
    nota=estoque[x]
    disp=nota[1]
    valor=nota[0]
    lista=[disp*valor]
    troco=saque%valor
    a2=int((saque-troco)/valor)
    if a2<=disp and troco!=1 and troco!=3:
        resposta.append([valor,a2])
        saque=troco
    if a2>disp:
        a2=int(a2-disp)
        troco=troco+(a2*valor)
        saque=troco
        resposta.append([valor,disp])
  if a1==True:
    sacado=[]
    for x in range(0,len(resposta)):
      if resposta[x][1]!=0:
        sacado.append(resposta[x])
    return sacado
  elif a1==False:
    return []

disponivel=[[200,4],[100,5],[50,8],[20,2],[10,0],[5,1],[2,20]]

caixaPlus(10000,disponivel)

caixaPlus(555,disponivel)

caixaPlus(6,disponivel)

"""Questão 3:
Sua tarefa é construir uma função Python chamada cabo que recebe como parâmetro de entrada uma
string longa com os nomes COMPLETOS dos alunos de uma turma e retorna como parâmetros de saída:
(i) a lista ordenada dos primeiros nomes dos alunos da turma; (ii) o nome do aluno que, se sorteado pelo
professor, acarretará em um empate no Cabo de Guerra Informático descrito acima; e (iii) a posição
deste aluno na lista. Caso não seja possível haver empate, sua função deverá retornar, além da lista de
nomes, os valores False e “Sem empate”.

"""

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

nomes1='''Ana
Bruna
Cro
Digory
Emerson
Fiaror
Geomar
Iago
Zacarias'''

#import random as rd
def lista_primeiros_nomes(nomes):
  nome=nomes.split('\n')
  primeiros_nomes=[]
  #lista primeiros nomes
  for x in range(0,len(nome)):
    nome_aluno=nome[x].split(' ')
    primeiros_nomes.append(nome_aluno[0])
  return primeiros_nomes

def pontuação_equipes(pessoa_sorteada,nomes):
  primeiros_nomes=nomes
  posicao_ps=primeiros_nomes.index(pessoa_sorteada)
  #equipe1
  pontuação1=0
  for x in range(0,posicao_ps):
    frça_aluno=0
    for y in range(0,len(primeiros_nomes[x])):
      frça_aluno=frça_aluno+ord(primeiros_nomes[x][y])
    pontos_aluno=(posicao_ps-x)*frça_aluno
    pontuação1=pontuação1+pontos_aluno
  #equipe2
  pontuação2=0
  for x in range(posicao_ps+1,len(primeiros_nomes)):
    frça_aluno=0
    for y in range(0,len(primeiros_nomes[x])):
      frça_aluno=ord(primeiros_nomes[x][y])
    pontos_aluno=(x-posicao_ps)*frça_aluno
    pontuação2=pontuação2+pontos_aluno
  return pontuação1,pontuação2,posicao_ps

def cabo(stringcomnomes):
  listanomes=lista_primeiros_nomes(stringcomnomes)
  aux=False
  for x in range(0,len(listanomes)):
    a=pontuação_equipes(listanomes[x],listanomes)
    if a[0]==a[1]:
      aux=True
      return listanomes,listanomes[x],a[2]
  if aux==False:
      return(listanomes,aux,'sem Empate')

cabo(nomes2)

def pontuação_equipes(pessoa_sorteada,nomes):
  primeiros_nomes=nomes
  posicao_ps=primeiros_nomes.index(pessoa_sorteada)
  #equipe1
  pontuação1=0
  for x in range(0,posicao_ps):
    frça_aluno=0
    for y in range(0,len(primeiros_nomes[x])):
      frça_aluno=frça_aluno+ord(primeiros_nomes[x][y])
    pontos_aluno=(posicao_ps-x)*frça_aluno
    print(l[x],frça_aluno,(posicao_ps-x),pontos_aluno,)
    pontuação1=pontuação1+pontos_aluno
    print(pontuação1)
  #equipe2
  pontuação2=0
  for x in range(posicao_ps+1,len(primeiros_nomes)):
    frça_aluno=0
    for y in range(0,len(primeiros_nomes[x])):
      frça_aluno=frça_aluno+ord(primeiros_nomes[x][y])
    pontos_aluno=(x-posicao_ps)*frça_aluno
    print(l[x],frça_aluno,(x-posicao_ps),pontos_aluno,)
    pontuação2=pontuação2+pontos_aluno
    print(pontuação2)
  return pontuação1,pontuação2,posicao_ps

l=lista_primeiros_nomes(nomes1)
ps=rd.choice(l)
pontuação_equipes('Emerson',l)

nomes1=nomes1.replace('Ana','Walter')
l=lista_primeiros_nomes(nomes1)
ps=rd.choice(l)
pontuação_equipes('Emerson',l)

"""Apesar de conseguir encontrar as forças, multiplica-las pelo seu fator de maneira correta, encontrar a pontuação que cada aluno adiciona para a equipe e adicionar a pontuação total da equipe, não consegui encontrar um empate para Emerson. Realizei minha prova pelo Google Collab e não pelo Spyder."""