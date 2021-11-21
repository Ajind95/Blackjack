#---------------------------MILESTONE PROJECT 2 - BLACKJACK-------------------------------#
import random
import os
suits = ('Hearts','Diamonds','Club','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':0}

class Card():
    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def draw(self):

        return self.all_cards.pop(0)

class Player():
    def __init__(self,name,account):
        self.name = name
        self.account = account
        self.player_hand = []

    def bet(self,amount):
        if self.account >= amount:
            self.account -= amount
            return True
        else:
            print("Insufficient balance to place bet, please buy chips. Game Over!")
            return False

    def win(self,amount):
        self.account += round(amount)

    def hit(self,new_card):
        self.player_hand.append(new_card)

    def clean(self):
        self.player_hand.clear()

    def __str__(self):

        return f"{self.name} has {self.player_hand[0]} - {self.player_hand[1]}"

class Dealer():
    '''Describes Dealer'''
    def __init__(self):
        self.dealer_hand = []

    def hit(self,new_card):
        self.dealer_hand.append(new_card)

    def clean(self):
        self.dealer_hand.clear()

    def __str__(self):
        return f"Dealer has {self.dealer_hand[1]}"

def Player_initialize():
    name= input("Please Enter the name of Player: ")

    while True:

        Player_account = input("Please enter the buyin of the Player: $")

        if Player_account.isdigit():
            Player_account = int(Player_account)
            break

    return Player(name,Player_account) #player created

def place_bet(Player1):

    if Player1.account < 5:
        print("Insufficient balance to place bet, please buy chips. Game Over!")
        return 0,False

    while True:

            player_bet = input("Please place the bet: $")

            if player_bet.isdigit() and int(player_bet) != 0:
                player_bet = int(player_bet)
                game_on = Player1.bet(player_bet) #returns True or False. Game loop begins with Game_on as True
                break

    return player_bet, game_on

def deal(player1_bet,table):

    if player1_bet != 0:

        player1_score = 0
        player1_Ace = 0
        dealer_score = 0
        dealer_Ace = 0

        for i in range(2):
            Player1.clean()
            Automated_Dealer.clean()

        print(f"{Player1.name} account has {Player1.account}")
        print(f"{Player1.name} has placed a bet of {player1_bet}")
        table += player1_bet
        player1_bet = 0

        for i in range(2):
            card_created = New_Deck.draw()
            Automated_Dealer.hit(card_created)
            if card_created.rank != 'Ace':
                dealer_score += card_created.value
            else:
                dealer_Ace += 1

        for i in range(2):
            card_created = New_Deck.draw()
            Player1.hit(card_created)
            if card_created.rank != 'Ace':
                player1_score += card_created.value
            else:
                player1_Ace += 1

        return player1_score, player1_Ace, dealer_score, dealer_Ace,player1_bet,table

def if_Ace(name,no_of_Ace,score,pscore):

    for aces in range(no_of_Ace):

        if name == "Dealer":

            if 21 - score == 1:
                score += 1
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
            elif 21 - score == 11:
                score += 11
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
            elif (pscore - score <= 11) and (21 - score >11):
                score += 11
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
            elif 16-score>=11:
                score += 11
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
            else:
                score += 1
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'


        elif name != 'Dealer':

            acceptable_choices = ['1','11']
            choice = 'wrong'

            if 21 - score == 1:
                score += 1
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
                break
            if 21 - score == 11:
                score += 11
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
                break

            while choice not in acceptable_choices:

                choice = input(f'{name} You have 1 Aces, please choose the value (1 or 11): ')

            if choice == '1':
                score += 1
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'
            else:
                score += 11
                print(f"\n{name} Score is ** {score} **")
                choice = 'wrong'

    return score,0

def player_choice(game_on,bet):

    if game_on and bet == 0:

        acceptable_choices = ['h','H','s','S']
        choice = 'Wrong'

        while choice not in acceptable_choices:

            choice = input("Would you like to Hit? (h/H) \nOr \nWould you like to stand? (s/S): \n")

        return choice

def play_again():
    acceptable = ['y','Y','n','N']
    play = "wrong"

    while play not in acceptable:

        play = input("Do you want to play again? (Y/N): ")

        if play == 'n' or play == 'N':
            os.system("cls")
            return 0, False,0,0,False

        elif play == 'y' or play == 'Y':
            os.system("cls")
            print(f"you have {Player1.account} in your account")
            bet,game_on = place_bet(Player1)
            return bet,game_on,0,0,True

def bust_player(score,Player1,table):

    if score > 21:

        print(f"{Player1.name} Busted!")
        print(f"{Player1.name} your new account is {Player1.account}")
        return play_again()

    elif score == 21 and len(Player1.player_hand) == 2:

        print(f"{Player1.name} win BlackJack!")
        print(f"{Player1.name} your previous account was {Player1.account}")
        Player1.win(table*2.5)
        print(f"{Player1.name} your new account is {Player1.account}")
        return play_again()

    else:
        return 0,True,score,table,False

def bust_dealer(dealer_score,player_score,Player1,table):

    if dealer_score > 21:

        print(f"{Player1.name} win!")
        print(f"{Player1.name} your previous account was {Player1.account}")
        Player1.win(table*2)
        print(f"{Player1.name} your new account is {Player1.account}")
        return play_again()

    else:
        return 0,True,player_score,table,False

def winner(dealer_score,player_score,table):
    
    if dealer_score < player_score:
        print(f"{Player1.name} win!")
        print(f"{Player1.name} your previous account was {Player1.account}")
        Player1.win(table*2)
        print(f"{Player1.name} your new account is {Player1.account}")
        return play_again()
        
    elif dealer_score > player_score:
        print(f"{Player1.name} lost!")
        print(f"{Player1.name} your new account is {Player1.account}")
        return play_again()

    elif dealer_score == player_score:
        print("It is a tie")
        Player1.win(table)
        print(f"{Player1.name} your account is {Player1.account}")
        return play_again()

def print_game(choice):

    if choice =='s' or choice == "S":
        os.system("cls")
        print("\n\n")
        print(Automated_Dealer,"-",Automated_Dealer.dealer_hand[0],"-",end=" ")
        for i in range(len(dealer_new_card)):
            print(dealer_new_card[i], "-", end =" ")
        print("\n\n")
        print(Player1, "-", end =" ")
        for i in range(len(player_new_cards)):
            print(player_new_cards[i], "-", end=" ")
        print("\n")
        print(f"\n{Player1.name} Score is ** {player_score} **")
        print(f"Dealer score is ** {dealer_score} **")

    else:
        os.system("cls")
        print("\n\n")
        print(Automated_Dealer,"\n\n")
        print(Player1, "-", end =" ")
        for i in range(len(player_new_cards)):
            print(player_new_cards[i], "-", end=" ")
        print("\n")
        print(f"\n{Player1.name} Score is ** {player_score} **")

Player1 = Player_initialize()
(bet,game_on) = place_bet(Player1)
first = True

while game_on:

    if first:
        os.system("cls")
        table = 0
        choice = 'wrong'
        player_new_cards = []
        dealer_new_card = []
        New_Deck = Deck()
        New_Deck.shuffle() # shuffled deck prepared
        Automated_Dealer = Dealer() # Dealer created
        (player_score, player_Ace, dealer_score, dealer_Ace,bet,table) = deal(bet,table) #cards dealt and displayed
        print("\n\n")
        print(Automated_Dealer,"\n\n")
        print(Player1)
        print(f"\n{Player1.name} Score is ** {player_score} **")
        (player_score,player_Ace) = if_Ace(Player1.name,player_Ace,player_score,player_score)
        first = False

    (bet,game_on,player_score,table,first) = bust_player(player_score, Player1,table)
    choice = player_choice(game_on,bet)

    while choice == 'h' or choice == 'H':
        card_created = New_Deck.draw()
        Player1.hit(card_created)
        player_new_cards.append(card_created)
        if card_created.rank != 'Ace':
            player_score += card_created.value
        else:
            player_Ace += 1
        print_game(choice)
        (player_score,player_Ace) = if_Ace(Player1.name,player_Ace,player_score,player_score)
        (bet,game_on,player_score,table,first) = bust_player(player_score, Player1,table)
        choice = player_choice(game_on,bet)

    if game_on and not(first):
        print_game(choice)
        (dealer_score,dealer_Ace) = if_Ace("Dealer",dealer_Ace,dealer_score,player_score)
        if dealer_score <= 16:
            while dealer_score <= 16:
                card_created = New_Deck.draw()
                Automated_Dealer.hit(card_created)
                dealer_new_card.append(card_created)
                if card_created.rank != 'Ace':
                    dealer_score += card_created.value
                else:
                    dealer_Ace += 1
                print_game(choice)
                (dealer_score,dealer_Ace) = if_Ace("Dealer",dealer_Ace,dealer_score,player_score)
                (bet,game_on,player_score,table,first) = bust_dealer(dealer_score, player_score,Player1,table)

    if game_on and not(first):
        print_game(choice)
        (dealer_score,dealer_Ace) = if_Ace("Dealer",dealer_Ace,dealer_score,player_score)
        (bet,game_on,player_score,table,first) = winner(dealer_score,player_score,table)        