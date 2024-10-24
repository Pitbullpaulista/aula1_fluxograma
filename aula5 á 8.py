# variáveis
#comentários
#tipos primitivos
#sinais comparativos
#sinais aritméticos
#i/o

#indentação é sobre encapsular corretamente so blocos de códigos
# A organização do codigo
#if 10 > 2:
#    pass    
#print('olá mundo')    

#if X:
#    var  =  10
#    print('olá')

#concatenação
#juntar dados

#%

#nome = 'carlos'

#print('ola %s'%(nome))

#f'

#nome = 'josé'
#print(f'olá {nome}{2}')


# .format
#print('olá{}'. format(nome))

#,

#nome = julia
#print('ola', nome)

#+ muito antigo não é mais eficiente

#nome = 'pedro'
#Print('olá' + '' + nome)



#formas de pular linha

# print('ola \n Mundo')

# print('''
# ola
# tudo bom 
# com 
# vc?
# ''')

#refaturação:

# bug - impede de funcionar como o planejado

#erro - impede o codigo de funcionar

# m1 = input(':')
# m2 = input(':')

# soma = n1 + n2
# print(soma)

#-----------------------------------------------

#-----------------------------------------------


#aula 7

#

#lista = [1,2,3,4,5,6,]

# n1 = lista[0]
# n2 = lista[1]

# lista[0] = 25
# lista[1] = 12

# lista.append(10)
# lista.append('teste')

# del lista[3] #remove por dentro
# lista.remove(5) #remove por fora
# lista.pop() #remove o ultimo
# lista += (10,3020,50,6,'teste', n2) #adiciona vario intens a lista
# lista.extend(1,2,3,6,6,) #adiciona item a lista, mas não adiciona texto. somente sumeros ou bool

# soma = n1 + n2
# print(lista)

# lista.clean() #limpa a lista
# print(lista)

# nova_lista = lista.copy()
# print(nova_lista)

# lista.insert(0,100)
# print(lista)

# lista2 = list(renge(1,151))
# print(lista2)

# numero = int(range(1,151))
# print(list.count(6))

# **inicio\ fim \ step by step \ (parametros)

# lista = list(range(2,11))
# print(lista)

#exercicio 7

#Exercício 1 Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

# lista = list(range(2,21,2))
# print(lista)

#Exercício 2: Escreva um programa que use a função range() para gerar os múltiplos de 5 em 5 até 50, em seguida, calcule e imprima a soma desses múltiplos.
# lis = list(range(0,55,5))
# soma_lista = sum(lis)
# print(soma_lista)

# #**Exercício 1:** Crie uma lista chamada pessoas que contenha os números inteiros de pessoa1 a pessoa5 e imprima-a na tela.

# pessoas_lista = ['pessoa1', 'pessoa2', 'pessoa3', 'pessoa4', 'pessoa5']
# print(pessoas_lista)

# #Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
# print(pessoas_lista[2])

# #Adicione o número 9 à lista numeros e imprima a lista atualizada.
# pessoas_lista.append(9)
# print(pessoas_lista)


# #Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.
# pessoas_lista.remove(pessoa5)
# print(pessoas_lista)

# #Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
# carros = ['uno', 'jeep', 'corsa']
# print(pessoas_lista + carros)

#-----------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------

# print('mercado')
# produtos = ['arriz', 'feijão', 'macarrão', 'molho']
# valores = [10.0, 15.00, 8.00, 3.50]
# carrinho = []
# meu_valores = []

# produto1 = int(input('''
# 1 - arroz
# 2 - feijão
# 3 - macarrão
# 4 - molho
# '''))

# produto2 = int(input('''
# 1 - arroz
# 2 - feijão
# 3 - macarrão
# 4 - molho
# '''))

# carrinho = [produtos[produto1], produto[produto2]]
# meu_valores = [valores[produto1],produto2]
# soma= sum(meu_valores)

# print(f'''
# ......................................
# CUPOM

# 1 - {produtos[produto1]} R${valores[produto1]:.2f}
# 2 - {produtos[produto2]} R${valores[produto2]:.2f}

# ........................................
# R$ {soma:.2f}

# ''')

#--------------------------------------------------------------------------
#----------------------------------------------------------------------------

#dicionario

#condicionais

#if : se        

# se condicao == true
#     faça isso

# numero = input(':')

# if 35 >= 45:   #if se
#     print('é maior')

# if 10 >= 20:
#     print('É MAIOR')
# elif 35 == 35:   #elif : se não ser
#     print('é igual')
# else:   #else se não
#     print('É menor')

# lista = [1,2,5,6,6,5]
# numero = int(input('>>'))

# if numero in lista:
#     print('Existe')
# else:
#     print('Não existe')

# import random

# import random

# numero_aleatorio = random.randint(1,10)
# chute = int(input('esclha um numero: '))

# if numero_aleatorio == chute:
#     print('show de bola, acertou em cheio')
#     print('é o numero', numero_aleatorio)
# else:
#     print('errou feio', numero_aleatorio)

#--------------------------------------------------------------
#--------------------------------------------------------------

#atividade 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.


digite = int(input('digite um numero'))
if digite > 0:
    print('positivo')
elif digite == 0:
    print('zero')
else:
    print('negativo')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.



# 3*

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

# 6*

# Verifique se um número é positivo e maior que 10

# 7*

# Verifique se um número é divisível por 3 ou 5.









