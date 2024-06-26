
# TODO Add ace logic- if makes bust switch value to one
# TODO Add gambling
# TODO Implement ASCII art for cards
import random

pickedCards = []


# generates a random card and stores it as variable 'card'
def genCard():
    cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    while True:
        card = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
        if card not in pickedCards:
            pickedCards.append(card)
            return card
        elif card in pickedCards:
            if len(pickedCards) == 52:
                pickedCards.clear()
                print("No more cards! Reshuffling!")
                break
            continue


# separate function to generate cards for dealer
def genCardDealer():
    cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    while True:
        card = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
        if card not in pickedCards:
            pickedCards.append(card)
            return card
        elif card in pickedCards:
            if len(pickedCards) == 52:
                pickedCards.clear()
                break
            continue


def cardValue(card):
    number = card.split(' ')[0]
    if number == 'ACE':
        return 11
    elif number == 'JACK' or number == 'QUEEN' or number == 'KING':
        return 10
    else:
        return int(number)


# deal a card the user can see one and can't see the other. ask user if they want to hit or stand
def dealCard():
    visibleCard = genCard()
    hiddenCard = genCard()
    userOriginalCards = [visibleCard, hiddenCard]
    print(f"Your cards are {', '.join(userOriginalCards)}")
    return userOriginalCards


# deals user a single card
def hit():
    card = genCard()
    print(f"Your card is {card}")
    userCards.append(card)
    print(f"Your current cards are: {', '.join(userCards)}")
    return card

# checks player cards and determines win or loss
def checkWin():
    dealerTotal = dealerHand[0] + dealerHand[1]
    print(f"Your cards were {userCards}")
    print(f"Your total was {userTotal}")
    print(f"Dealer's cards were {dealerCards}")
    print(f"Dealer's total was {dealerTotal}")
    if (dealerTotal <= 21) and (userTotal < dealerTotal):
        print("You Lost!")
    elif (userTotal <= 21) and (userTotal > dealerTotal):
        print("You Win!")
    elif (userTotal <= 21) == (dealerTotal <= 21):
        print("You Draw!")
    elif (dealerTotal > 21) and (userTotal <= 21):
        print("You Win!")


# define dealer score
def dealerPlay():
    dealerCards = [genCardDealer(), genCardDealer()]
    dealerHand = [cardValue(dealerCards[0]), cardValue((dealerCards[1]))]
    while (dealerHand[0] + dealerHand[1]) < random.randint(16, 18):
        dealerNewCard = genCardDealer()
        dealerCards.append(dealerNewCard)
        dealerHit = cardValue(dealerNewCard)
        dealerHand[0] += dealerHit
    return dealerHand, dealerCards


userBust = False
playAgain = True
while playAgain != 'y' and playAgain != 'n':
    playAgain = input("Do you want to play Blackjack?(y/n)")
    if playAgain == 'y':
        while playAgain == 'y':
            print(pickedCards)
            userCards = dealCard()
            userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
            dealerHand, dealerCards = dealerPlay()
            print(f"Dealer's visible card is {dealerCards[0]}")
            # stand first turn
            hitOrStand = input("Do you want to hit or stand?(h/s)")
            if hitOrStand == 's':
                print("You stand!")
            # hit and subsequent stands loop
            while hitOrStand == 'h':
                newCard = hit()
                userTotal = cardValue(newCard) + userTotal
                if userTotal > 21:
                    print("You busted! Dealer Wins")
                    userBust = True
                    break
                hitOrStand = input("Do you want to hit or stand?(h/s)")
            else:
                print("Invalid Input! You forefit!")
            if userBust is False:
                checkWin()
            playAgain = input("Play again?(y/n)")
            print("Thanks for playing!")
    elif playAgain == 'n':
        print("Thanks for playing!")
    else:
        print("Invalid input!")
