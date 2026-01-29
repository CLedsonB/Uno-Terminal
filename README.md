# Jogo de Cartas UNO

## Descrição
Este é um jogo de cartas UNO desenvolvido em Python, onde os jogadores podem competir uns contra os outros.

## Configuração
O jogo possui diversas configuraçõe, entre elas estão: 

* Número de jogadores : pode ser configurado para 2 ou mais jogadores.
* Número de cartas: pode ser configurado para qualquer número inteiro positivo.
* Exibição de cartas: as cartas podem ser exibidas após um tempo em segundos determinado pelo usuário
* Ícone de carregamento: é possível escolher qualquer caractere para ser exibido durante o carregamento do jogo
* ciclos de carregamento: é possível escolher o tempo em ciclos que o carregamento vai durar.

-------- Trecho abaixo em produção ------------

* Método de organização das cartas : Penso em organizar de 5 formas diferentes 
1. Cor crescente : organizando as cartas de A até D, números de 0 até 9, poderes seriam as últimas cartas em cada cor, carta Coringa no final
2. Número crescente : organizando as cartas de 0 até 9, cores de A até D, poderes seriam as últimas cartas de cada número, carta Coringa no final
3. Cor decrescente : organizando as cartas de D até A, números de 9 até 0, poderes seriam as primeiras cartas em cada cor, carta Coringa no final
4. Número decrescente : organizando as cartas de 9 até 0, cores de D até A, poderes seriam as primeiras cartas de cada cor, carta Coringa no final
5. Força Total: Carta Coringa é a primeira, demais poderes em seguida e cartas de número e letra no final

Deve haver uma letra para cada tipo de organização que pode ser acionada durante a partida sem pular a vez do jogador
----------------------------------

## Como jogar
1. Execute o arquivo `jogo.py` em um terminal.
2. Configure o número de jogadores e o número de cartas.
3. Clique em "Iniciar Jogo" para começar.
4. Cada jogador receberá um conjunto de cartas.
5. O jogo prosseguirá de acordo com as regras definidas.

## Cartas do jogo

No jogo as cores das cartas são definitiva com base em letras, sendo elas -> [A,B,C,D].
Possui também dez números diferentes sendo eles ->  [0,1,2,3,4,5,6,7,8,9,0]

O jogo inclui as seguintes cartas:

**Carta de Número e Cor**: Permite ao jogador jogar uma carta com o mesmo número ou cor da carta anterior.
**Carta +2**: Obriga o próximo jogador a comprar 2 cartas e pular a sua vez.
**Carta +4**: Obriga o próximo jogador a comprar 4 cartas e pular a sua vez.
**Carta Inverter Sentido** (><): Inverte o sentido do jogo, de horário para anti-horário ou vice-versa
**Carta Bloqueio** (@): Bloqueia o próximo jogador.
**Carta Coringa** (COR): Pode ser jogada sobre qualquer carta do jogo e permite ao jogador escolher a cor que o próximo jogador deve jogar.

## Licença
* Este jogo é de código aberto e pode ser modificado e distribuído livremente.