import os
import time as t
import random as rd
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

Nconfig = {
'N* de Jogadores' : 3,
'N* de cartas' : 5,
'Ver Cartas' : 's',
'Tempo para exibir cartas' : 5,
'Metodo de organizacao de cartas' : 1,
'Icone Carregamento' : '@',
'Ciclos Carregamento' : 3
}

opcConfig = [
'N* de Jogadores',
'N* de cartas',
'Ver cartas',
'Tempo para exibicao de cartas',
'Metodo de organizacao de cartas',]

configPadrao = [3,5,'n',5,1]
config = configPadrao

cores = ['A','B','C','D']
numeros = [num for num in range(10)]
poderes = ['+2','+4','><','@','COR']
cartas = []
cartasJogador = []
nomeJogador = ['Player1','Player2','Player3']

def carregamento():
	caractere = '@'
	limite = 15
	volta = 3
	linha = []


	for i in range(volta):
		for j in range(limite):
			clear()
			linha.append(caractere)
			print('\n\n\t',*linha)
		for j in range(limite):
			clear()
			linha.pop()
			print('\n\n\t',*linha)


def menuInicial():
	while True:
		clear()
		print('''
		Jogue UNO!!!

	[1]. Novo Jogo
	[2]. Configuracoes
	[3]. Creditos
	[4]. Sair
''')
	#	try:
		opc = int(input(' ~> '))

		if opc == 1:
			cartas = resetarBaralho()
			cartas, cartasJogador = distribuirBaralho()
			carregamento()
			telaJogo()
		elif opc == 2:
			config = menuConfiguracao()
		elif opc == 3:
			creditos()
		elif opc == 4:
			exit()
		else:
			print('\n Numero invalido')
	#	except:
			print('\n Caractere invalido2')

def menuConfiguracao():
	global config, configPadrao, opcConfig, nomeJogador

	while True:
		clear()
		print('''
		Configuracoes

	[1]. N* de Jogadores
	[2]. N* de cartas inicial
	[3]. Mostrar cartas
	[4]. Tempo para exibir cartas
	[5]. Organizar cartas por :
	[6]. Redefinir configuracoes
	[7]. Sair e salvar
''')
#		try:
		opc = int(input(' ~> '))

		if opc == 1:
			print('\n Digite o numero de jogadores\n')
			print(f' Valor atual : {config[0]} -->> {nomeJogador}\n')
			config[0] = int(input(' ~> '))
			nomeJogador = []
			for i in range(config[0]):
				nome = input(f'\n Insira o nome do jogador {i+1}\n ~> ')
				nomeJogador.append(nome)
		elif opc == 2:
			print('\n Digite o numero de cartas para cada jogador')
			print(f' Valor atual : {config[1]}\n')
			config[1] = int(input(' ~> '))
		elif opc == 3:
			print('\n Exibir cartas no inicio da partida? (s / n)')
			print(f' Valor atual : {config[2]}\n')
			config[2] = int(input(' ~> '))
		elif opc == 4:
			print('\n Tempo em segundo para exibir as cartas')
			print(f' Valor atual : {config[3]} segs\n')
			config[3] = int(input(' ~> '))
		elif opc == 5:
			print('\n Escolha um metodo para organizacao das cartas')
			print(f' Valor atual : Metodo {config[4]}\n')
			config[4] = int(input(' ~> '))
		elif opc == 6:
			for i in range(len(configPadrao)):
				print(f' {opcConfig[i]} : {config[i]} -->> {configPadrao[i]}')
			aux = input('\n Deseja redefinir todas as configuracoes? ( s / n )\n ~> ')
			if aux == 's':
				nomeJogador = []
				for i in range(len(configPadrao)):
					config[i] = configPadrao[i]
				for i in range(config[0]):
					nomeJogador.append(f'Player{i+1}')
			elif aux == 'n':
				print('\n Operacao cancelada')

			else:
				print('\n Comando invalido')
		elif opc == 7:
			print('\n Configuracoes atualizadas !!!')
			t.sleep(1)
			return config
		else:
			print('\n Numero invalido')
#		except:
			print('\n Caractere invalido')
		t.sleep(1)

def resetarBaralho():
	global cartas
	cartas = []
	for i in range(len(numeros)):
		for j in range(len(cores)):
			cartas.append(str(numeros[i]) + ' ' + cores[j])		# 0 A
			if i == 0:
				cartas = cartas + [poderes[i] + cores[j]] * 2	 # +2A * 2
			if i == 1 or i == 2:
				cartas = cartas + [poderes[i] + cores[j]]	 # +4A / ><
			if i == 3:
				cartas = cartas + [poderes[i] + ' ' + cores[j]]	 # @
			if i == 4 and j == 0:
				cartas.append(poderes[i])			 # COR
	rd.shuffle(cartas)
	return cartas

def distribuirBaralho():
	global cartas, config, cartasJogador

	for i in range(config[0]):
		aux = []
		for j in range(config[1]):
			aux.append(cartas.pop())
		cartasJogador.append(aux)

	return (cartas, cartasJogador)

def telaJogo():
	global cartas, cartasJogador, nomeJogador, config
	bloq = False
	invt = False
	vez = 0
	cartaInicial = cartas.pop()

	while True:
		aux , auxatr = '',''
		exbJogo = f'''
 Voltar : [-1]
 Cavar  : [0]


  Montante : {len(cartas)}

	{cartaInicial}


  Vez do jogador : {nomeJogador[vez]}
'''
		for i in range(len(cartasJogador[vez])):
			if i % 5 == 0:
				aux += f'\n {i+1}.[ '+cartasJogador[vez][i]+' ] '
				auxatr += f'\n {i+1}.[ *** ] '
			else:
				aux += f' {i+1}.[ '+cartasJogador[vez][i]+' ]  '
				auxatr += f' {i+1}.[ *** ] '

		clear()

		if config[2] == 's':
			print(exbJogo)
			print(aux)
		else:
			i = config[3]
			while i >= 1:
				print(exbJogo)
				print(f'\n\t[ {i} ] Segundos para exibicao das cartas !!! ')
				print(auxatr)
				t.sleep(1)
				clear()
				i -= 1
			print(exbJogo)
			print(aux)

		jogada = int(input('\n\nEscolha uma de suas cartas\n ~> '))
		carta = cartasJogador[vez][jogada-1]
		nCartas = len(cartasJogador[vez])-1
		print('\n')

		if jogada > len(cartasJogador[vez]):
			print('\n Numero incorreto !!!')
			vez -= 1

		elif jogada == -1:
			carregamento()
			menuInicial()
		elif jogada == 0:	# acao de cavar cartas no monte
			if len(cartas) > 0:
				cava = cartas.pop()
				cartasJogador[vez].append(cava)
				vez -= 1
			else:
				print(' O montante esta vazio... passarei a sua vez de jogar')

		elif carta.count('>') == 1:	# acao da carta inverter sentido
			cartas.insert(0,cartaInicial)
			cartaInicial = cartasJogador[vez].pop(jogada-1)

			print(' ',nomeJogador[vez],' inverteu o sentido do jogo !!!')
			nomeJogador.reverse()
			cartasJogador.reverse()
			if invt == False:
				vez -= 1
			else:
				vez -= 2

		elif carta.count('+') == 1:	# acao das cartas de soma
			cartas.insert(0,cartaInicial)
			cartaInicial = cartasJogador[vez].pop(jogada-1)

			if carta.count('2') == 1:	# acao da carta +2
				quant = 2
			elif carta.count('4') == 1:	# acao da carta +4
				quant = 4
			for i in range(quant):
				aux = cartas.pop()
				try:
					cartasJogador[vez+1].append(aux)
				except:
					cartasJogador[0].append(aux)
			try:
				print(f' {nomeJogador[vez+1]} ganhou {quant} cartas !!!')
			except:
				print(f' {nomeJogador[0]} ganhou {quant} cartas !!!')

		elif carta.count('@') == 1:	# acao da carta bloqueio
			cartas.insert(0,cartaInicial)
			cartaInicial = cartasJogador[vez].pop(jogada-1)

			try:
				print(f' {nomeJogador[vez+1]} foi bloqueado !!!')
			except:
				print(f' {nomeJogador[0]} foi bloqueado !!!')
				bloq == True
			vez += 1
		else:	# acao das demais cartas
			cartas.insert(0,cartaInicial)
			cartaInicial = cartasJogador[vez].pop(jogada-1)


		if nCartas == 0:	#testar condicao de vitoria
			print(f'\n {nomeJogador[vez]} venceu o jogo !!!')
			nomeJogador.pop(vez)
			cartasJogador.pop(vez)
			if len(nomeJogador) == 0:
				break
		vez += 1

		if bloq == True:
			vez -= 1
		elif vez+1  > config[0]:
			vez = 0
		t.sleep(1.5)

