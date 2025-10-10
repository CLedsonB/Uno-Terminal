import os
import copy
import time as t
import random as rd
from random import randrange as rand
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

configPadrao = {
'N* de Jogadores' : 3,
'N* de cartas' : 15,
'Ver Cartas' : 's',
'Tempo para exibir cartas' : 5,
'Metodo de organizacao de cartas' : 1,
'Icone Carregamento' : '@',
'Ciclos Carregamento' : 2
}

config = copy.deepcopy(configPadrao)

listConfig = []
for key in config.keys():
	listConfig.append(key)

nomeJogador = []
for i in range(config[listConfig[0]]):
	nomeJogador.append(f'Player{i+1}')


cores = ['A','B','C','D']
numeros = [num for num in range(10)]
poderes = ['+2','+4','><','@','COR']
cartas = []
cartasJogador = []


def carregamento():
	global config, listConfig

	caractere = config[listConfig[5]]
	limite = 15
	volta = config[listConfig[6]]
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
			config, nomeJogador = menuConfiguracao()
		elif opc == 3:
			creditos()
		elif opc == 4:
			exit()
		else:
			print('\n Numero invalido')
	#	except:
			print('\n Caractere invalido2')

def menuConfiguracao():
	global config, configPadrao, nomeJogador, listConfig

	while True:
		clear()

		print('\tConfiguracoes\n')
		i = 0
		for key in listConfig:
			print(f'\t[{i+1}]. ',key)
			i += 1
		print(f'\t[{i+1}].  Redefinir configuracoes')
		print(f'\t[{i+2}].  Sair e Salvar')
#		try:
		opc = int(input(' ~> '))

		if opc == 1:
			print('\n Digite o numero de jogadores\n')
			print(f' Valor atual : {config[listConfig[opc-1]]} -->> {nomeJogador}\n')
			config[listConfig[opc-1]] = int(input(' ~> '))
			nomeJogador = []
			for i in range(config[listConfig[opc-1]]):
				nome = input(f'\n Insira o nome do jogador {i+1}\n ~> ')
				nomeJogador.append(nome)
		elif opc == 2:
			print('\n Digite o numero de cartas para cada jogador')
			print(f' Valor atual : {config[listConfig[opc-1]]}\n')
			config[listConfig[opc-1]] = int(input(' ~> '))
		elif opc == 3:
			print('\n Exibir cartas no inicio da partida? (s / n)')
			print(f' Valor atual : {config[listConfig[opc-1]]}\n')
			config[listConfig[opc-1]] = input(' ~> ')
		elif opc == 4:
			print('\n Tempo em segundo para exibir as cartas')
			print(f' Valor atual : {config[listConfig[opc-1]]} segs\n')
			config[listConfig[opc-1]] = int(input(' ~> '))
		elif opc == 5:
			print('\n Escolha um metodo para organizacao das cartas')
			print(f' Valor atual : Metodo {config[listConfig[opc-1]]}\n')
			config[listConfig[opc-1]] = int(input(' ~> '))
		elif opc == 6:
			print('\n Escolha um caractere para a tela de carregamento')
			print(f' Valor atual : {config[listConfig[opc-1]]}\n')
			config[listConfig[opc-1]] = input(' ~> ')
		elif opc == 7:
			print('\n Quantidade de ciclos de carregamento')
			print(f' Valor atual : {config[listConfig[opc-1]]} ciclos\n')
			config[listConfig[opc-1]] = int(input(' ~> '))
		elif opc == 8:
			i = 0
			for k in range(len(configPadrao)):
				print(f' {listConfig[k]} : {config[listConfig[k]]} -->> {configPadrao[listConfig[k]]}')
				i += 1
			aux = input('\n Deseja redefinir todas as configuracoes? ( s / n )\n ~> ')
			if aux == 's':
				nomeJogador = []
				for i in range(len(configPadrao)):
					config[listConfig[i]] = configPadrao[listConfig[i]]
				for i in range(config[listConfig[0]]):
					nomeJogador.append(f'Player{i+1}')
			elif aux == 'n':
				print('\n Operacao cancelada')

			else:
				print('\n Comando invalido')
		elif opc == 9:
			print('\n Configuracoes atualizadas !!!')
			t.sleep(1)
			return config, nomeJogador
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
				cartas = cartas + [poderes[i] + cores[j]] * 3	 # +4A / ><
			if i == 3:
				cartas = cartas + [poderes[i] + ' ' + cores[j]] 	 # @
			if i == 4 and j == 0:
				cartas.append(poderes[i])			 # COR
	rd.shuffle(cartas)
	return cartas

def distribuirBaralho():
	global cartas, config, listConfig, cartasJogador

	for i in range(config[listConfig[0]]):
		aux = []
		for j in range(config[listConfig[1]]):
			aux.append(cartas.pop())
		cartasJogador.append(aux)

	return (cartas, cartasJogador)

def telaJogo():
	global cartas, cartasJogador, nomeJogador, config, listConfig
	vez = 0
	bloq = False
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

		if config[listConfig[2]] == 's':
			print(config[listConfig[0]],' - ',vez+1,' = ', (config[listConfig[0]])-vez-1)
			print(exbJogo)
			print(aux)
		else:
			i = config[listConfig[3]]
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

		if jogada > len(cartasJogador[vez]) and jogada < -1:
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
		else:
			# acao padrao das cartas
			cartas.insert(0,cartaInicial)
			cartaInicial = cartasJogador[vez].pop(jogada-1)

			if carta.count('>') == 1:	# acao da carta inverter sentido
				print(' ',nomeJogador[vez],' inverteu o sentido do jogo !!!')

				playerVez = nomeJogador[vez]
				nomeJogador.reverse()
				cartasJogador.reverse()
				vez = nomeJogador.index(playerVez)

			elif carta.count('+') == 1:	# acao das cartas de soma
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
				bloq = True
				numJ = config[listConfig[0]]
				if numJ - vez-1 == 0: # 3 - 2+1 == 0 ultimo
					print(f' {nomeJogador[0]} foi bloqueado !!!')
					vez = 1
				elif numJ - vez-1 == 1: # 3 - 1+1 == 1 anteultimo
					print(f' {nomeJogador[-1]} foi bloqueado !!!')
					vez = 0
				elif numJ - vez-1 > 1: # 3 - 0+1 == 2 normal
					print(f' {nomeJogador[vez+1]} foi bloqueado !!!')
					vez += 2

		if nCartas == 0:	#testar condicao de vitoria
			print(f'\n {nomeJogador[vez]} venceu o jogo !!!')
			nomeJogador.pop(vez)
			cartasJogador.pop(vez)
			if len(nomeJogador) == 0:
				break

		if bloq == False:
			vez += 1
		else:
			bloq = False

		t.sleep(1.5)

def creditos():
	mov = ['/','-','\\','|']

	for i in range(5):
		for j in range(len(mov)):
			clear()
			print('\n\n\t',mov[j])
			t.sleep(0.05)

	clear()
	print(f'\n\n\t2025 @ - CLedsonB')
	input()
