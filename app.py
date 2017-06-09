# -*- coding: UTF-8 -*-

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'

	for nome in nomes:
		print nome

def menu():
	nomes = []
	escolha = ''

	while(escolha != '0'):
		print 'Digite 1 para cadastrar, 2 para listar ou 0 para terminar'
		escolha = raw_input()

		if (escolha == '1'):
			cadastrar(nomes)
		elif (escolha == '2'):
			listar(nomes)
		else:
			print('Escolha não suportada, digite denovo...')
menu()