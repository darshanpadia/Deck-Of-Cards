from random import sample
class Card:
	def __init__(self,value,suit,worth):
		self.value = value
		self.suit = suit
		self.worth = worth
	def __repr__(self):
		return("{} of {}".format(self.value,self.suit))
class Deck:
	def __init__(self,i):
		self.cards = []
		for x in range(1,i+1):
			suit =["Hearts", "Diamonds", "Clubs","Spades"]
			value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
			for i in value:
				for j in suit:
					if i == 'A':
						wor = 11
					elif i in 'KQJ':
						wor = 10
					else:
						wor = int(i)
					card = Card(value = i, suit = j,worth= wor)
					self.cards.append(card)
		#print(self.cards)
	def __repr__(self):
		return "Deck of {} cards".format(len(self.cards))
	def count(self):
		return (len(self.cards))
	def _deal(self, num):
		count = self.count()  #### () imp*****
		actual = min([count,num])  ## imp
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		#cards = []
		#for i in range (actual):
		#	card = self.cards.pop()
		#	cards.append(card)
		return cards
		#hand = []                     ###  #######  ###
		#for i in range(0,num):        ###  WRONNGGG ###
		#	if len(self.cards) > 0:    ###  #######  ###
		#		card = self.cards.pop()
		#		hand.append(card)	
		#	else:
		#		raise ValueError("All cards have been dealt")
		#return(hand)	
		#print(len(self.cards))
		

	def shuffle(self,i):
		if len(self.cards) == 52*i:
			self.cards = sample(self.cards, len(self.cards)) 
	def deal_card(self):
		return self._deal(1)[0]    ### Deck() imp **************** ### self more imp note******* 
		                           ### can also access class methods using self as prefix ### mor imp*** 
	def deal_hand(self, num):
		return self._deal(num)
		

#s = Deck(4)
#s.shuffle(4)
#print(s.cards)
#print(s.cards[4].worth)
 #### s = s.shuffle() wrong###
#p2 = s._deal(3)
#print(p2)
#p1 = s._deal(3)
#print(p1)
#p3 = s._deal(3)
#print(p3)
#p4 = s._deal(3)
#print(p4)
#p5 = s._deal(3)
####print(Deck().deal_card())     *******######
#a = s._deal(4)
#print(a)
#p = s._deal(5)
#print(p)
#a = s.deal_hand(3)
#print(a)
#print(repr(s))
