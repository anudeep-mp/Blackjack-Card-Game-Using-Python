import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,'Ace':11}

#**********************************************

#Card class which is used for creating the deck of cards
class Card:

	def __init__(self,suit,rank):
		self.suit=suit
		self.rank=rank
		self.value=values[rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"

#Deck Class which is used for creating cards with the help of Card Class
#Deck class is used for shuffling the cards and splitting between the two players
class Deck:

	def __init__(self):
		self.deck_of_cards=[]

		for suit in suits:
			for rank in ranks:
				self.deck_of_cards.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck_of_cards)

	def pick_one(self):
		return self.deck_of_cards.pop()

	def __len__(self):
		return len(self.deck_of_cards)

#Chips class which deals with betting chips
class Chips:

	def __init__(self,plname):
		self.chip_balance=100
		self.plname=plname
		self.amount=0

	def place_bet(self,amount):
		self.amount=amount
		if self.chip_balance>=self.amount:
			print(f"\n{self.plname}, You placed a bet of {self.amount} chips")
			return True
		else:
			print(f"\n{self.plname}, You dont have enough Chips to place this bet. Your Chip Balance is {self.chip_balance}")
			print(f"\nPlease try a lesser amount\n")
			return False

	def bet_lost(self):
		self.chip_balance-=self.amount
		print(f"\n{self.plname}, you lost the bet of {self.amount} chips")
		print(f"\nYour Chip Balance : {self.chip_balance}")

	def bet_win(self):
		self.chip_balance+=self.amount
		print(f"\n{self.plname}, you won the bet of {self.amount} chips")
		print(f"\nYour Chip Balance : {self.chip_balance}")

#Player Class which is used for adding cards to players hand and find the total value of cards
class Player:

	def __init__(self,name="Dealer"):
		self.hand=[]
		self.name=name
		self.player_total=0

	def find_total(self):
		total=0
		z=0
		
		for i in self.hand:
			total+=i.value
			if i.value == 11:
				z+=1

		for i in range(0,z):
			if total>21:
				total-=10

		return total

	def add_card(self,card):
		self.hand.append(card)
		print(f"\nAdded 1 card to {self.name}'s hand")

	def send_hand(self):
		return self.hand

	def clear_hand(self):
		self.hand.clear()

	def __str__(self):
		z=0
		total=0
		
		for i in self.hand:
			total+=i.value
			if i.value == 11:
				z+=1

		for i in range(0,z):
			if total>21:
				total-=10

		return f"{self.name}'s Hand = {total}"


#********************************************************

#function used to print the top bar which contains the players names
def printtopbar():
	print("\n"*3)
	print((f"{dealer.name}'s Hand".ljust(29) +"||"+ f"{player.name}'s Hand".rjust(29)).center(100))
	print(("_"*35+"||"+"_"*35).center(100))

#function used for printing both the dealer and player cards when both the dealer and player have same number of cards in their hands
def printcard(d,p):
	if d!=' ':
		a=d.suit
		b=d.value
		c=d.rank
		x=p.suit
		y=p.value
		z=p.rank
	else:
		a=' '
		b="Card Down"
		c=' '
		x=p.suit
		y=p.value
		z=p.rank

	print("||".center(100))
	print(((" "+"_"*10+" ").ljust(29) +"||"+ (" "+"_"*10+" ").rjust(29)).center(100))
	print((("|          |").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
	print((("|"+f"{a}".center(10)+"|").ljust(29) +"||"+ ("|"+f"{x}".center(10)+"|").rjust(29)).center(100))
	print((("|          |").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
	print((("|"+f"{b}".center(10)+"|").ljust(29) +"||"+ ("|"+f"{y}".center(10)+"|").rjust(29)).center(100))
	print((("|          |").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
	print((("|"+f"{c}".center(10)+"|").ljust(29) +"||"+ ("|"+f"{z}".center(10)+"|").rjust(29)).center(100))
	print((("|"+"_"*10+"|").ljust(29) +"||"+ ("|"+"_"*10+"|").rjust(29)).center(100))

#function used to print dealer card alone when an extra card is there in dealer's hand when compared with player's hand
def dealer_printcard(d):
    print("||".center(100))
    print(((" "+"_"*10+" ").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|          |").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|"+f"{d.suit}".center(10)+"|").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|          |").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|"+f"{d.value}".center(10)+"|").ljust(29) +"||"+("            ").rjust(29)).center(100))
    print((("|          |").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|"+f"{d.rank}".center(10)+"|").ljust(29) +"||"+ ("            ").rjust(29)).center(100))
    print((("|"+"_"*10+"|").ljust(29) +"||"+ ("            ").rjust(29)).center(100))

#function used to print player card alone when an extra card is there in player's hand when compared with dealer's hand
def player_printcard(p):
    print("||".center(100))
    print((("            ").ljust(29) +"||"+ (" "+"_"*10+" ").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|"+f"{p.suit}".center(10)+"|").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|"+f"{p.value}".center(10)+"|").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|          |").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|"+f"{p.rank}".center(10)+"|").rjust(29)).center(100))
    print((("            ").ljust(29) +"||"+ ("|"+"_"*10+"|").rjust(29)).center(100))

#function which takes cares of printing cards based on the number of cards with each player
def display(z=0):

    d_hand=dealer.send_hand()
    p_hand=player.send_hand()

    def displayloop(l,z):
        for i in range(1,l):
                if z==0:
                    printcard(' ',p_hand[i])
                else:
                    printcard(d_hand[i],p_hand[i])
    printtopbar()
    printcard(d_hand[0],p_hand[0])

    d_l=len(d_hand)
    p_l=len(p_hand)

    if d_l==p_l:
        displayloop(p_l,z)

    elif  p_l > d_l:
        displayloop(d_l,z)
        for i in range(d_l,p_l):
            player_printcard(p_hand[i])

    elif  d_l > p_l:
        displayloop(p_l,z)
        for i in range(p_l,d_l):
            dealer_printcard(d_hand[i])

    print()

#function which prints the sum to all values of both players
def disp_values():
	print(dealer)
	print(player)

#main logic of the game which controls every part of game
def game_on():
	player.add_card(new_deck.pick_one())
	dealer.add_card(new_deck.pick_one())
	player.add_card(new_deck.pick_one())
	dealer.add_card(new_deck.pick_one())
	
	display()
	print(player)

	dl_play=True 
	still=True

	while True:

		while True:
			hs_inp=input("\nWould like to Hit or Stand? Enter H or S?: ").lower()
	        
			if hs_inp == 'h':
				hs_inp=True
			elif hs_inp == 's':
			    hs_inp= False
			else:
			    print("Sorry, please try again.")
			    continue
			break
			
		if hs_inp:
			player.add_card(new_deck.pick_one())
			total=player.find_total()

			if total>21:
				display(1)
				print()
				print(player)
				print(("BUST").center(100))
				print()
				print((f"{player.name} LOST").center(100))
				print()
				print((f"{dealer.name} WON").center(100))
				pl_chip.bet_lost()
				dl_play=False
				still=False
				break

			display()
			print()
			print(player)
		else:
			print()
			print((f"{player.name} Stands. Dealer starts playing...").center(100))
			display(1)
			disp_values()
			break

	while dl_play and dealer.find_total() < 17:
		s=input("\nDealer Hits")
		if s:
			pass
		else:
			dealer.add_card(new_deck.pick_one())
			total=dealer.find_total()
			display(1)
			print()
			disp_values()

			if total>21:
				print(("BUST").center(100))
				print()
				print((f"{dealer.name} LOST").center(100))
				print()
				print((f"{player.name} WON").center(100))
				pl_chip.bet_win()
				still=False
				break

	if still:
		d_total=dealer.find_total()
		p_total=player.find_total()
		
		if d_total>p_total:
			display(1)
			disp_values()
			print(("DEALER WINS").center(100))
			pl_chip.bet_lost()

		elif p_total>d_total:
			display(1)
			disp_values()
			print((f"{player.name} WINS").center(100))
			pl_chip.bet_win()

		else:
			display(1)
			disp_values()
			print((f'PUSH').center(100))

#base function from where game starts
def main_base_call():
	while True:
		print()
		bet=int(input("How many chips you would like to bet: "))
		accept=pl_chip.place_bet(bet)
		if accept == True:
			break

	global new_deck
	new_deck=Deck()
	new_deck.shuffle()
	dealer.clear_hand()
	player.clear_hand()
	print()
	print(("---Lets start the Black Jack game---").center(100))
	print(("\nShuffling Cards..."))
	game_on()

#main function which takes players names and create objects for few classes
if __name__=="__main__":
	print()
	plname=input("Your name : ").capitalize()
	player=Player(plname)
	dealer=Player()
	pl_chip=Chips(plname)
	global final_player_total
	
	main_base_call()
	while pl_chip.chip_balance>0:
		print()
		
		while True:
			choice = input("Do you want to play again; Y or N: ").lower()

			if choice=='y' or choice=='yes':
				choice=True
			elif choice=='n' or choice=='no':
			    choice= False
			else:
			    print("Sorry, please try again.")
			    continue
			break

		if choice:
			main_base_call()
		else:
			print(("THANK YOU").center(100))
			break
	else:
		print("\nYour Chip Balance is nill. You cannot play the game anymore\n")
		print(("THANK YOU").center(100))