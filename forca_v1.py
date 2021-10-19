# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
from random import randint
from time import sleep

# Board (tabuleiro)
titulo = '\n\n\n>>>>>>>>>> Hangman <<<<<<<<<<'
board = ['''
    +---+
    |   |
    |
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |   |
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |  /
    |
=========''', '''
    +---+
    |   |
    |   O
    |  /|\\
    |  / \\
    |
=========''', '''
    +---+
    |   |
    |   X
    |  /|\\
    |  / \\
    |
=========''']


# Classe
class Hangman:

	num_error = int() #número de erros
	num_correct = int() #número de acertos
	list_correct = list()
	list_wrong = list()

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.num_error = 0
		self.num_correct = 0
		self.list_correct = []
		self.list_wrong = []

	# Método para verificar se o jogo terminou
	def hangman_over(self):
		#print(f'num error: {self.num_error}')
		#print(f'num correct: {self.num_correct}')
		#print(f'tamanho word: {len(set(self.word))}')
		if self.num_error > 6 or self.num_correct == len(set(self.word)): #len set remove letras duplicadas da palavra
			return True
		else:
			return False

	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		#print('\n' * 50)
		print(titulo)
		print(board[self.num_error], end='\t')
		#print('_ ' * len(self.word))
		self.hide_word()
	#print(f'word: {self.word}')
	#print(f'len word: {len(self.word)}')

	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			print('Acertou!!!')
			self.num_correct += 1
			self.list_correct.append(letter)
		#print(f'lista correta: {self.list_correct}')
		else:
			print('Errou!!!')
			self.num_error += 1
			self.list_wrong.append(letter)
		print(f'Letras erradas: {self.list_wrong}') #sempre imprime a lista de erros


	# Método para não mostrar a letra no board
	def hide_word(self):
		for letter in self.word:
			if letter in self.list_correct:
				print(letter, end=' ')
			else:
				print('_', end=' ')

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if self.num_error == 7:
			print(titulo)
			print(board[self.num_error])
			return False
		else:
			return True


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open("palavras.txt", "rt") as f:
		bank = f.readlines()
		#print(bank)
	#print(bank[randint(0,len(bank)-1)].strip())
	return bank[randint(0,len(bank)-1)].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():

		# Verifica o status do jogo
		game.print_game_status()

		letter = input('\nDigite a letra: ')
		if letter not in game.list_wrong and letter not in game.list_correct:
			game.guess(letter)
		else:
			print('Erro!!! Letra já digitada.')

		sleep(1)

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print('\nParabéns! Você venceu!!')
	else:
		print('\nGame over! Você perdeu.')
	print('A palavra era ' + game.word)
		
	print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

