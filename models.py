# -*- coding: UTF-8 -*-

class Perfil(object):
	
	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		# deixa o atribulo "privado" -> p pytho gera um nome aleatório para o atributo em todos os
		# lugares aonde ele é usado para o desenvolvedor não conseguir acessar o atributo
		self.__curtidas = 0
	
	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas

class Perfil_Vip(Perfil):
	
	def __init__(self, nome, telefone, empresa, apelido):
		# consigo acessar o construtor da classe pai e passar os atributos que são dele
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		# acessa o self da classe pai com o super, e tem que passar a classe filha
		return super(Perfil_Vip, self).obter_curtidas() * 10.0