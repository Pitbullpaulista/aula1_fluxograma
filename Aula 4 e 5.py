#aula 4 *******************************
#1  -  Criar 3 variáveis, notas, tipo float()***
#2 -   Mostre no console a média das 3 variáveis***
#3 - Passou de ano?  -  media >= 7

#nota1 = float(input('digite a nota 1 :'))
#nota2 = float(input('digite a nota 2 :'))
#nota3 = float(input('digite a nota 3 :'))
#media = (nota1 + nota2 + nota3)//3
#nome = input('digite seu nome: ')
#print('media: ', media)
#situacao = media >=7
#print('situação do aluno', nome, 'Aprovado ->', situacao)



#Modulo: traz o resto da conta de divisao

#%

#RESTO = 10%2 == 0
#RESTO = 11%2 == 1
#print(RESTO)

#logica
# >
#print(10>2)

#<
#print(10<2)

#>=
#print(10>=20)

#<=
#print(10<=2)

#!=
#Print(10!=2)


#-------------------------------------------------------------------------------------------------------------------------------------------------------
#atividade aula 4
### 1 - Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.

### 2 - Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.

### 3 - Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.

### 4 - Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.

### 5 - Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.


#minha verção
#n = int(input('>>'))
#q = n**2
#print(q)


#nome = input('Digie seu nome:')
#sobrenome = str(input('Digite seu Sobrenome'))
#print(nome, sobrenome)

#numero1 =  int(input('digite o numero'))
#numero2 =  int(input('digite o numero'))
#print(str(numero1, numero2))

#armazenar_a_palavra = ('Pyhon')
#quadrado = 60

#print (armazenar_a_palavra, n)
#print('meu nome é ', nome, sobrenome)
 


 #-------------------------------------------------------
#aula 5 função ******
#len so pode ussado com textos, não funciona em numero.

#palavra = 'olá como vai'
#comprimento = len(palavra)
#print(comprimento)

#lista, o correto é manter a lista ou so numero ou so texto.
#lista = [20,5,'a']
#lista2 = [20,3,6,65]
#lista3 = [a,b,c,d]

#tupla, constante não pode ser alterado
#tupla = (10,20,30,10)

#conjunto não repete o dado.
#conjuntos = {20,20,30,40}

#lista= list(range(1,11))
#tupla = tuple(range(1,11))
#conjunto = set(range(1,11))
#print(lista, tupla, conjunto)


#lista 
#imprimir numero especifico na lista pelo indice
#minha_lista = [10,20,30,40]
#     indice   [0  1  2  3]
#     indice  [-3 -2 -1 -0]
#print(minha_lista[2])
 
# sum soma a lista inteira
#soma = sum (minha_lista)
#print(soma)
#indice = minha_lista[-1]
#print(indice)

#menor numero da lista
#menor = min(minha_lista)
#print(menor)

#maior numero da lista
#maior = mas(minha_lista)
#print(maior)

#sort orgniza a minha lista
#minha_lista.sort()
#print(minha_lista)

#minha_lista.sort(re)


#notas = []

#n1, n2, n3 = float(input('>')), float(input('>')), float(input('>'))
#notas += (n1, n2,n3)
#media = sum(notas)/len(notas)
#print('notas - ',notas)
#print('notas - ',notas)

#------------------------------------------------------------------------------------------

#atividade 5

#Exercícios: 

#1 Imprima uma mensagem de boas-vindas na tela.
#print('Boas Vindas!')



#2 Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
variavel_bool = True
true(verdadeiro)


#3 Imprima o resultado da multiplicação de dois números decimais de sua escolha
#n1 = 10
#n2 = 20
#multiplicação = n1 * n2
#print(multiplicação)


#4 Imprima o resultado da divisão de dois números inteiros de sua escolha.

#n3 = 50
#n4 = 20
#divicao = n3 / n4
#print(divicao)


#5 Imprima o resultado da subtração de dois números inteiros de sua escolha

#n5 = 50
#n6 = 20
#subtracao = n3 - n4
#print(subtracao)

#6 Imprima o resultado da divisão inteira de dois números inteiros de sua escolha.

#n7 = 50
#n8 = 20
#divicao = n7 / n8
#print(int(divicao))

#7 Imprima o resultado da multiplicação de 4 números decimais de sua escolha

#n9 = 10
#n10 = 20
#n11 = 30
#n12 = 40
#multiplicação = n9 * n10 * n11 * n12
#print(multiplicação)

#8 Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número

#numero = 40
#d = numero*2
#print(d)


#9 Crie uma calculadora de soma com as ferramentas que vc já conhece(Use apenas input, print e variavel)
#n1, n2 = int(input('>')), int(input('>'))
#soma = n1 + n2
#2print(soma)

#10 Crie um sistema de cadastro com as estruturas que vc já conhece(Use apenas input, print e variavel)
#print('cadastro! digite as informações')

#nome = str(input('Digite seu nome!'))
#sobre_nome = str(input('digite seu sobrenome'))
#nome_completo = (nome + sobre_nome)
#print('seu nome é', nome_completo)

#endereço = str(input('Digite seu endereço!'))
#numero_casa = int(input('digite seu numero da casa'))
#endereço_completo = (endereço, numero_casa)
#print(endereço_completo)
