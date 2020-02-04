

import time

class Deck():

	def __init__(self):
		card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
		card_suits = ['♠', '♦', '♥', '♣']

		self.deck = [ (n, s) for n in card_numbers for s in card_suits ]

	def shuffle(self):
		import random
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()



class Hand():

	def __init__(self, computer_turn=False):
		self.cards = []
		self.value = 0
		self.aces = 0
		self.computer_turn = computer_turn
		self.computer_faceup_card = 0
		self.win = 0

	def add_card(self, card):
		self.cards.append(card)

		self.number = card[0]

		if len(self.cards) == 1:
			if self.computer_turn == False:
				if self.number == 'J' or self.number == 'Q' or self.number == 'K':
					self.computer_faceup_card = 10
				elif self.number == 'A':
					self.computer_faceup_card = 11
				else:
					self.computer_faceup_card = self.number

		if self.number == 'J' or self.number == 'Q' or self.number == 'K':
			self.value += 10

		elif self.number == 'A':
			self.aces +=1
			self.value += 11
		else:
			self.value += int(self.number)

		if self.value > 21 and self.aces > 0:
			self.aces -= 1
			self.value -= 10

	def show_hand_player(self):

		print("Player's Hand:")
		for card in self.cards:
			if card[0] == '10':
				print(f'  {card[0]} of {card[1]}')
			else:
				print(f'   {card[0]} of {card[1]}')



	def show_hand_computer(self):

		if self.computer_turn == True:
			print("Dealer's Hand:")
			for card in self.cards:
				if card[0] == '10':
					print(f'  {card[0]} of {card[1]}')
				else:
					print(f'   {card[0]} of {card[1]}')

		else:
			print("Dealer's Hand:")
			if self.cards[0][0] == '10':
				print(f'  {self.cards[0][0]} of {self.cards[0][1]}')
			else:
				print(f'   {self.cards[0][0]} of {self.cards[0][1]}')

			print('  Hidden Card')




def player_draws_card():
	player_hand.add_card(deck.deal())

def computer_draws_card():
	computer_hand.add_card(deck.deal())

def check_bust_player():
	if player_hand.value > 21:
		return True

	else:
		return False

def check_bust_computer():
	if computer_hand.value >21:
		return True
	else:
		return False

def ask_player_move():
	while True:
		move = input('\nHit or Stand? ')
		if move == 'Hit' or move == 'hit' or move == 'h' or move == 'H':
			player_draws_card()
			print('\n--------------------------\n')
			break
		elif move == 'Stand' or move == 'stand' or move == 's' or move == 'S':
			print('\n--------------------------\n')
			global player_turn
			player_turn = False
			break
		else:
			print('Please, make a legal move')

def check_blackjack():
	if player_hand.value == 21:
		global player_turn
		player_turn = False
		global blackjack
		blackjack = True
		print("It' a BlackJack!")

def ask_to_play_again():
	while True:
		answer = input('\n\nDo you want to play again (Y/N)? ')
		if answer == 'N' or answer == 'n':
			print_final_score()
			print('\nThank you for playing!')
			return False
		elif answer == 'Y' or answer == 'y':
			print('\n')
			return True
		else:
			print('Please, input a valid answer')

def print_score():
	print(f'Rounds: {rounds}\n\nPlayer score: {player_wins}\nDealer score: {dealer_wins}\n       Draws: {draws}\n')
def print_final_score():
	print(f'\n\nFINAL SCORE\n\nRounds: {rounds}\n\nPlayer score: {player_wins}\nDealer score: {dealer_wins}\n       Draws: {draws}\n')


# GAME INTRODUCTION
print('Welcome to the Black Jack Game!\n')
print()

play_again = True

# GAME STARTS
rounds = 0
player_wins = 0
dealer_wins = 0
draws = 0
while play_again:
	time.sleep(1)
	rounds += 1
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	computer_hand = Hand(computer_turn=False)

	player_draws_card()
	player_draws_card()
	computer_draws_card()
	computer_draws_card()

	player_hand.show_hand_player()
	print(f'Total: {player_hand.value}\n')
	computer_hand.show_hand_computer()
	print(f'Total: {computer_hand.computer_faceup_card}\n')

	player_turn = True
	blackjack = False

	check_blackjack()

	# PLAYER'S TURN START
	while player_turn:
		time.sleep(1)
		ask_player_move()

		player_hand.show_hand_player()
		print(f'Total: {player_hand.value}\n')
		computer_hand.show_hand_computer()
		print(f'Total: {computer_hand.computer_faceup_card}\n')
		time.sleep(1)
		if check_bust_player():
			break
		if check_blackjack():
			break
	time.sleep(2)

	if check_bust_player() == False:

		print("\nEND OF PLAYER'S TURN\n")
		print('xxxxxxxxxxxxxxxxxxxxxxxxxx\n')
		time.sleep(2)
		# COMPUTER'S TURN START
		computer_hand.computer_turn = True


		if 	computer_hand.value < 17:
			while computer_hand.value < 17:
				time.sleep(.5)
				player_hand.show_hand_player()
				print(f'Total: {player_hand.value}\n')
				computer_hand.show_hand_computer()
				print(f'Total: {computer_hand.value}\n')
				time.sleep(3)
				computer_draws_card()
				print('\n--------------------------\n')
				time.sleep(.5)

			player_hand.show_hand_player()
			print(f'Total: {player_hand.value}\n')
			computer_hand.show_hand_computer()
			print(f'Total: {computer_hand.value}\n')
			time.sleep(2)
			print("END OF DEALER'S TURN\n")
			time.sleep(2)

		else:
			player_hand.show_hand_player()
			print(f'Total: {player_hand.value}\n')
			computer_hand.show_hand_computer()
			print(f'Total: {computer_hand.value}\n')
			time.sleep(2)
			print("END OF DEALER'S TURN\n")
			time.sleep(2)


	# CHECK WHO WINS
	if check_bust_player():
		print('The Player busted!\nThe winner is the Dealer!')
		dealer_wins += 1
	elif check_bust_computer():
		print("The Dealer busted!\nThe winner is the Player!")
		player_wins += 1
	elif player_hand.value > computer_hand.value:
		print('PLAYER WINS')
		player_wins += 1
	elif player_hand.value < computer_hand.value:
		print('DEALER WINS')
		dealer_wins += 1
	else:
		print("IT'S A DRAW")
		draws += 1
	time.sleep(2)
	print("END OF ROUND\n\n--------------------------\n--------------------------\n")
	print_score()
	time.sleep(2)
	play_again = ask_to_play_again()
