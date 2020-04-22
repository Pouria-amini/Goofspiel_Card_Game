"""
        [===============================================================================================]
        [                                                                                               ]
        [                         Assignment NO: 3                                                      ]
        [                         Question NO: 4                                                        ]
        [                         Part: C                                                               ]
        [                         Author: Mahdi Amini                                                   ]                                                             ]
        [                         P.Con: Creating The Game of Pure Strategy card game                   ]
        [                         Date Started: 2020-03-25                                              ]
        [                         Date Finished: 2020-03-28                                             ]
        [                         ICS3UI-02 for Ms. Harris                                              ]
        [                                                                                               ]
        [-----------------------------------------------------------------------------------------------]
        [                                 Program Description                                           ]
        [                                                                                               ]
        [  Goofspiel is played using cards from a standard deck of cards, and is typically a two-player ]
        [ game, although more players are possible. Each suit is ranked A (low), 2, ..., 10, J, Q, K    ]
        [ (high).                                                                                       ]
        [                                                                                               ]
        [  1-One suit is singled out as the "prizes"; each of the remaining suits becomes a hand for one]
        [ player, with one suit discarded if there are only two players. The prizes are shuffled and one]
        [ card turned up.                                                                               ]
        [                                                                                               ]
        [  2-Play proceeds in a series of rounds. The players make "closed bids" for the top (face up)  ]
        [ prize by selecting a card from their hand (keeping their choice secret from their opponent).  ]
        [ Once these cards are selected, they are simultaneously revealed, and the player making the    ]
        [ highest bid takes the competition card. Rules for ties in the bidding vary,possibilities      ]
        [ including the competition card being discarded, or its value split between the tied players   ]
        [ (possibly resulting in fractional scores). Some play that the current prize may "roll over" to]
        [ the next round, so that two or more cards are competed for at once with a single bid card.    ]
        [                                                                                               ]
        [  3-The cards used for bidding are discarded,and play continues with a new upturned prize card.]
        [                                                                                               ]
        [  4-After 13 rounds, there are no remaining cards and the game ends. Typically, players earn   ]
        [ points equal to sum of the ranks of cards won (i.e. ace is worth one point, 2 is two points,  ]
        [ etc., jack 11, queen 12, and king 13 points). Players may agree upon other scoring schemes.   ]
        [                                                                                               ]
        [-----------------------------------------------------------------------------------------------]
        [                                           Sources                                             ]
        [                                                                                               ]
        [    1-"Goofspiel - Wikipedia."                                                                 ]
        [         https://en.wikipedia.org/wiki/Goofspiel.                                              ]
        [         Accessed 25 Mar. 2020.                                                                ]
        [         < The program description is borrowed from this source >                              ]
        [    2-"Card Game using pygame module - Code Review Stack Exchange." 9 Apr. 2019,               ]
        [         https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module   ]
        [         Accessed 28 Mar. 2020.                                                                ]
        [         < the idea of how to make a card game and some codes are borrowed from this website > ]
        [    3- "File:Playing card heart 2.svg - Wikimedia Commons." 25 Mar. 2007,                      ]
        [         https://commons.wikimedia.org/wiki/File:Playing_card_heart_2.svg.                     ]
        [         Accessed 30 Mar. 2020.                                                                ]
        [         < The picture of cards are borrowed from this website                                 ]
        [         *This file is licensed under the Creative Commons Attribution-Share Alike 3.0         ]
        [         Unported license.*                                                                    ]
        [         *** the other cards have the same source and license***
        [                                                                                               ]
        [===============================================================================================]
"""
import pygame
from random import shuffle
from itertools import product
from enum import Enum
from os import path

###------------------------------------------[CLASSES PART]----------------------------------------------------------###

# The classes numbers, suits, Card, and Player are borrowed and changed from the following website( also mentioned in the sources):
# "Card Game using pygame module - Code Review Stack Exchange." 9 Apr. 2019,
# https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module
# creating ranks and suits of the card game:
current_dir = path.dirname(__file__)
image_dir = path.join(current_dir, 'MahdiA3Q4C-img')

class numbers(Enum):
    ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING = range(1, 14)

class club(Enum):
    club = 1

class spade(Enum):
    spade = 2

class heart(Enum):
    heart = 3

class diamond(Enum):
    diamond = 4

class Card(object):
    """this class creates card object"""

    def __init__(self, suit, number, image = None):
        if number in numbers and (suit in diamond or suit in heart or suit in spade or suit in club):
            self.number = number
            self.suit = suit
        else:
            self.number = None
            self.suit = None
        self.image = image
        self.p_x, self.p_y = 0, 0
        self.x_dimension = None
        self.y_dimension = None

    def __str__(self):
        """this shows the name of the card"""
        return str(self.suit.name) + str(self.number.name)


class CLUB(object):
    """this class creates the club object for referring to the prize deck or player deck """

    def __init__(self):
        self.cards = [Card(club1, number) for number, club1 in product(numbers, club)]

    def __str__(self):
        """this shows the name of the cards in club suit"""
        return str([str(card) for card in self.cards])

    def cards_draw(self):
        """this returns the cards in the suit"""
        draw_cards = self.cards
        return draw_cards

    def deck_shuffle(self):
        """Shuffles the deck if it is chosen for the prize deck"""
        shuffle(self.cards)

class HEART(object):
    """this class creates the heart object for referring to the prize deck or player deck """

    def __init__(self):
        self.cards = [Card(heart1, number) for number, heart1 in product(numbers, heart)]

    def __str__(self):
        """this shows the name of the cards in heart suit"""
        return str([str(card) for card in self.cards])

    def cards_draw(self):
        """this returns the cards in the suit"""
        draw_cards = self.cards
        return draw_cards

    def deck_shuffle(self):
        """Shuffles the deck if it is chosen for the prize deck"""
        shuffle(self.cards)

class SPADE(object):
    """this class creates the spade object for referring to the prize deck or player deck """

    def __init__(self):
        self.cards = [Card(spade1, number) for number, spade1 in product(numbers, spade)]

    def __str__(self):
        """this shows the name of the cards in spade suit"""
        return str([str(card) for card in self.cards])

    def cards_draw(self):
        """this returns the cards in the suit"""
        draw_cards = self.cards
        return draw_cards

    def deck_shuffle(self):
        """Shuffles the deck if it is chosen for the prize deck"""
        shuffle(self.cards)

class DIAMOND(object):
    """this class creates the diamond object for referring to the prize deck or player deck """

    def __init__(self):
        self.cards = [Card(diamond1, number) for number, diamond1 in product(numbers, diamond)]

    def __str__(self):
        """this shows the name of the cards in diamond suit"""
        return str([str(card) for card in self.cards])

    def cards_draw(self):
        """this returns the cards in the suit"""
        draw_cards = self.cards
        return draw_cards

    def deck_shuffle(self):
        """Shuffles the deck if it is chosen for the prize deck"""
        shuffle(self.cards)

class Player(object):
    """class for creating player object"""

    def __init__(self, name, hand = None, score = 0, player_turn=False):
        self.name = name
        self.hand = hand
        self.score = score
        self.turn = player_turn
        self.selected_card = None

    def __str__(self):
        """shows the name of the player"""
        return str(self.name)

    def delete_card_from_hand(self, card):
        """Removes a card object from the players hand"""
        if card and card in self.hand:
            position = self.hand.index(card)
            del self.hand[position]
            return card
        return None

###------------------------------------------[FUNCTIONS PART]-----------------------------------------------------------###
# The functions load_card_image, show_winner, show_player_score, select_card (partly), switch_turn, winner goes first
# and turn are borrowed and changed from the following website( also mentioned in the sources):
#  "Card Game using pygame module - Code Review Stack Exchange." 9 Apr. 2019,
# https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module

def Deck_Chosen(deck):
    """this gets the prize deck and shuffle it"""

    if deck == 'diamond':  # checks if the diamond is the prize deck to shuffle
        T = DIAMOND()
        T.deck_shuffle()
        return T.cards_draw()
    if deck == 'heart':  # checks if the heart is the prize deck to shuffle
        T = HEART()
        T.deck_shuffle()
        return T.cards_draw()
    if deck == 'spade':  # checks if the spade is the prize deck to shuffle
        T = SPADE()
        T.deck_shuffle()
        return T.cards_draw()
    if deck == 'club':  # checks if the club is the prize deck to shuffle
        T = CLUB()
        T.deck_shuffle()
        return T.cards_draw()
    # returns an error if the prize deck is not club, diamond, spade or heart
    raise TypeError('wrong input for the prize deck***please restart the game and give the right input***')

def load_card_images(player):
    """this Loads image, and dimensions to card objects"""

    for card in player.hand:  # this take out each card in the player hand
        card.image = pygame.image.load(path.join(image_dir,'Playing_card_'+str(card)+'.svg.png'))  # this loads the card image
        width, height = card.image.get_size()  # this gets the size of the image and put it into the card object
        card.x_dimension = width
        card.y_dimension = height

def show_player_hand(sc, player):
    """Displays all cards in hand of player on pygame display object"""

    if player == player_1:  # if it's player one turn, show the cards in his/her hand
        x, y, space_between_cards = 5, 5, 30

        for card in player.hand:
            card.p_x, card.p_y = x, y
            sc.blit(card.image, (x, y))
            y += space_between_cards  # this shows the hand card in a column

    else:  # if it's player two turn, show the cards in his/her hand
        x, y, space_between_cards = 1158, 5, 30

        for card in player.hand:
            card.p_x, card.p_y = x, y
            sc.blit(card.image, (x, y))
            y += space_between_cards  # this shows the hand card in a column

def show_prize_deck(sc, prize_deck, x):
    """shows the prize card in the middle of the screen and increases its size"""

    x[0].image = pygame.image.load(path.join(image_dir,'Playing_card_' + str(x[0]) + '.svg.png'))
    changed_image = pygame.transform.scale(x[0].image,(153, 180))
    sc.blit(changed_image, (460, 400))

def select_card(sc, player, mouse_x, mouse_y):
    """Player selects a card to play"""

    for card in player.hand:  # this goes through all the player hand
        lower_x, upper_x = (card.p_x, card.p_x + card.x_dimension)  # this gets the left-up and right-up position of the card
        lower_y, upper_y = (card.p_y, card.p_y + 30)  # this gets the 30 pixels below the top of the card
        # if the mouse position is between the card x position
        if lower_x < mouse_x < upper_x:
            # and if the mouse is between the top 30 pixels of the card
            if lower_y < mouse_y < upper_y:
                if player == player_1:
                    sc.blit(card.image, (lower_x+50, lower_y))  # shows the whole card chosed for the player
                else:
                    sc.blit(card.image, (lower_x - 50, lower_y))  # shows the whole card chosed for the player
                # if the mouse is clicked
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    # chose the card for player
                    player.selected_card = card


def show_back_card(sc,player):
    """Display the back of the card played"""

    if player == player_1:
        # if the player one chosed his card, place the back of the card in the middle of the screen
        sc.blit(pygame.image.load(path.join(image_dir,'Card_back.png')), (400, 200))
    if player == player_2:
        # if the player two chosed his card, place the back of the card in the middle of the screen
        sc.blit(pygame.image.load(path.join(image_dir,'Card_back.png')), (800, 200))


def show_winner(sc, player1, player2, my_font):
    """Display text stating game winner at end of game"""

    # fil the screen with green when the game ends
    sc.fill(GREEN)
    # determine the winner and show it in the screen
    if player1.score > player2.score:
        winner = str(player1)
    elif player1.score > player2.score:
        winner = str(player2)
    else:
        winner = '!BOTH PLAYERS! << The scores are EQUAL >>'
    textsurface = my_font.render("The winner is: " + winner, False, (0, 0, 0))
    sc.blit(textsurface, (300, 270))


def find_winner(sc, player1, player2, check):
    """determines who won round and updates their score"""

    round_winner = None

    if player_1.selected_card and player_2.selected_card:
        pygame.time.delay(1000)

        # determines who chosed more valuable card
        if player_1.selected_card.number.value > player_2.selected_card.number.value:
            round_winner = player_1
            # adds the value of the prize card to the score of the player
            round_winner.score += Prize_Deck[0].number.value
            check = True  # this changes the prize card

        elif player_1.selected_card.number.value < player_2.selected_card.number.value:
            round_winner = player_2
            # adds the value of the prize card to the score of the player
            round_winner.score += Prize_Deck[0].number.value
            check = True  # this changes the prize card

        elif player_1.selected_card.number.value == player_2.selected_card.number.value:
            check = True
        Prize_Deck.pop(0)  # this remove the prize card which just played
        player1.selected_card, player2.selected_card = None, None  # restarts the card selected by players

    return round_winner, check  # returns the player who just won the round


def show_player_scores(screen, player1, player2):
    """Left corner is player 1 score, right corner is player 2 score"""

    font_size = 22
    my_font = pygame.font.SysFont('Times New Roman', font_size)
    textsurface1 = my_font.render("Player 1 score: " + str(player1.score), False, (0, 0, 0))  # player one score display
    textsurface2 = my_font.render("Player 2 score: " + str(player2.score), False, (0, 0, 0))  # player two score display
    screen.blit(textsurface1, (120, 0))
    screen.blit(textsurface2, (950, 0))


def switch_turns(player1, player2):
    """Changes the turn of player1 and player2"""

    player1.turn = not player1.turn
    player2.turn = not player2.turn


def turn(sc, player, mouse_x, mouse_y):
    """Player will select card using mouse_x, and mouse_y, card will be removed from hand """

    select_card(sc, player, mouse_x, mouse_y)
    player.delete_card_from_hand(player.selected_card)


def winner_goes_first(winner, loser):
    """Sets the winner to the starter of the next round"""

    winner.turn = True
    loser.turn = False

def show_turn(sc, player, font):
    """Shows which player should play"""

    if player == player_1:
        textsurface = my_font.render(str(player_1.name)+"'s Turn", False, (0, 0, 0))
        sc.blit(textsurface, (100, 100))

    else:
        textsurface = my_font.render(str(player_2.name)+"'s Turn", False, (0, 0, 0))
        sc.blit(textsurface, (900, 100))

# The output of this function are borrowed from the following website( also mentioned in the sources):
# "Goofspiel - Wikipedia."
#https://en.wikipedia.org/wiki/Goofspiel.
def SOS():
    print("\n 1-One suit is singled out as the \"prizes\"; each of the remaining suits becomes a hand for one player, \n"
          " with one suit discarded if there are only two players. The prizes are shuffled and one card turned up."
          "\n***"
          "\n2-Play proceeds in a series of rounds. The players make \"closed bids\" for the top (face up) prize by \n"
          " selecting a card from their hand "
          "(keeping their choice secret from their opponent). Once these cards\n are selected, "
          ",the player making the highest bid takes the competition card.\n Rules for ties in the bidding "
          "vary,possibilities including the competition card being discarded,\n or its value split between the tied "
          "players (possibly "
          "resulting in fractional scores).\n Some play that the current prize may \"roll over\" to the next round,\n "
          "so that two or more "
          "cards are competed for at once with a single bid card."
          "\n***"
          "\n3-The cards used for bidding are discarded, and play continues with a new upturned prize card."
          "\n***"
          "\n4-After 13 rounds, there are no remaining cards and the game ends. Typically, players earn points\n equal "
          "to sum of the "
          "ranks of cards won (i.e. ace is worth one point, 2 is two \n points, etc., jack 11, queen 12, and king 13 "
          "points).\n \n source:  \"Goofspiel - Wikipedia.\" "
          "https://en.wikipedia.org/wiki/Goofspiel. Accessed 25 Mar. 2020. \n")

###------------------------------------------[CODING PART]-----------------------------------------------------------###

screen_width, screen_height = 1266, 669
size_of_font = 30
check = True  # This checks whether it is time for the prize card to be shown or not

print("********************************************")
print("** Welcome to \"The Game of Pure Strategy\" **")
print("********************************************")

# Setting up the game and get the cards for each player
player_1_name = input("GO AHEAD and Type the NAME OF PLAYER << 1 >>: ")
player_2_name = input("NOW it's time for PLAYER << 2 >>, Type your name: ")
print()
check_if_the_player_knows_the_game = input("^ If you are not familiar with this game type << help >>, if you are, press Enter \n>> ")
if check_if_the_player_knows_the_game.lower() == 'help':
    SOS()
deck_chosed = input("Type the PRIZE DECK from the followings (only: diamond, spade, heart, club): \n>> ")
deck_chosed = deck_chosed.lower()
print("!! MAKE SURE THAT YOU DO NOT USE ONE DECK TWICE !!")
deck1 = input("Player << 1 >> Type your deck from the followings (only: diamond, spade, heart, club):\n>> ")
deck1 = deck1.lower()
deck2 = input("player << 2 >> Type your deck from the followings (only: diamond, spade, heart, club):\n>> ")
deck2 = deck2.lower()
if deck1 == deck2 or deck2 == deck_chosed or deck1 == deck_chosed:
    raise TypeError('two decks are the same ***restart the game and give correct the inputs***')

# Determines the suits for each player
if deck1 == 'diamond':
    ch1 = DIAMOND()
elif deck1 == 'spade':
    ch1 = SPADE()
elif deck1 == 'heart':
    ch1 = HEART()
elif deck1 == 'club':
    ch1 = CLUB()
else:  # If the player chosed none of the suits in the game, return and error
    raise TypeError("wrong input is given for the player one deck***please restart the game and give the right input***")

# Create a player object for player one and give him/her the hand chosed. player one starts the game first
player_1 = Player(player_1_name, hand=ch1.cards_draw(), player_turn=True)


if deck2 == 'diamond':
    ch2 = DIAMOND()
elif deck2 == 'spade':
    ch2 = SPADE()
elif deck2 == 'heart':
    ch2 = HEART()
elif deck2 == 'club':
    ch2 = CLUB()
else:  # If the player chosed none of the suits in the game, return and error
    raise TypeError("wrong input is given for the player two deck***please restart the game and give the right input***")

# Create a player object for player two and give him/her the hand chosed.
player_2 = Player(player_2_name, hand=ch2.cards_draw())

# Get the prize deck
Prize_Deck = Deck_Chosen(deck_chosed)

GREEN = (0, 255, 0)  # Color for background

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

load_card_images(player_1)  # Loading the cards chosed by player one
load_card_images(player_2)  # Loading the cards chosed by player two


pygame.display.set_caption("The Game of Pure Strategy")

# Set up the font
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', size_of_font)

done = False

clock = pygame.time.Clock()

# -------- Main Program Loop ----------- #
while not done:

    mouse_position_x, mouse_position_y = None, None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    mouse_position_x, mouse_position_y = pygame.mouse.get_pos()  # --- Getting the coordinate of the mouse for choosing card

    # --- Fill the screen with color green
    screen.fill(GREEN)

    if check:
        show_prize_deck(screen, deck_chosed, Prize_Deck)  # --- If it is the time for the prize card to be shown, show it

    # Some parts of the following part is borrowed from this source: (also mentioned in the sources)
    # "Card Game using pygame module - Code Review Stack Exchange." 9 Apr. 2019,
    # https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module
    #------------------------------------------------------------------------------------------------------------------#
    if player_1.turn:
        # --- If it is the player one's turn, show his/her hand and turn and select the card that player chosed
        # and switch turns
        show_player_hand(screen, player_1)
        turn(screen, player_1, mouse_position_x, mouse_position_y)
        show_turn(screen, player_2, my_font)
        if player_1.selected_card:
            switch_turns(player_1, player_2)

    if player_1.selected_card and player_2.selected_card is None:
        # --- If player one played, show the back of the card he/she played
        show_back_card(screen, player_1)

    if player_2.turn:
        # --- If it is the player one's turn, show his/her hand and turn and select the card that player chosed
        # and switch turns
        show_player_hand(screen, player_2)
        turn(screen, player_2, mouse_position_x, mouse_position_y)
        show_turn(screen, player_1, my_font)
        if player_2.selected_card:
            switch_turns(player_1, player_2)
    #------------------------------------------------------------------------------------------------------------------#
    if player_2.selected_card and player_1.selected_card is None:
        # --- If player one chosed a card, show the back of his card in the center
        show_back_card(screen, player_2)

    if player_1.selected_card and player_2.selected_card:
        # --- Change the prize card
        check = False

    # The following part is partly borrowed from this source: (also mentioned in the sources)
    # "Card Game using pygame module - Code Review Stack Exchange." 9 Apr. 2019,
    # https://codereview.stackexchange.com/questions/217109/card-game-using-pygame-module
    #------------------------------------------------------------------------------------------------------------------#
    # --- Evaluate the the winner
    winner, check = find_winner(screen, player_1, player_2, check)

    # --- Show the score of each player
    show_player_scores(screen, player_1, player_2)

    if winner:
        # --- Checks which player won the round, the winner plays the next round first
        if winner == player_1:
            winner_goes_first(player_1, player_2)
        else:
            winner_goes_first(player_2, player_1)

    if not player_1.hand and not player_2.hand:
        # --- If both players finish their cards in hand, show the winner and finish the game
        show_winner(screen, player_1, player_2, my_font)
        pygame.display.update()
        pygame.time.delay(5000)
        done = True
    # ------------------------------------------------------------------------------------------------------------------#
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
