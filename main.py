
# TODO Add ace logic- if makes bust switch value to one
# TODO Add gambling
# TODO Implement ASCII art for cards
import random
import time
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
                time.sleep(.15)
                print("No more cards! Reshuffling!")
                time.sleep(.15)
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
    time.sleep(.15)
    print(f"Your cards are {', '.join(userOriginalCards)}")
    time.sleep(.15)
    return userOriginalCards


# deals user a single card
def hit():
    card = genCard()
    time.sleep(.15)
    print(f"Your card is {card}")
    time.sleep(.15)
    userCards.append(card)
    time.sleep(.15)
    print(f"Your current cards are: {', '.join(userCards)}")
    time.sleep(.15)
    return card

# checks player cards and determines win or loss
def checkWin():
    dealerTotal = dealerHand[0] + dealerHand[1]
    time.sleep(.15)
    print(f"Your cards were {', '.join(userCards)}")
    time.sleep(.15)
    print(f"Your total was {userTotal}")
    time.sleep(.15)
    print(f"Dealer's cards were {', '.join(dealerCards)}")
    time.sleep(.15)
    print(f"Dealer's total was {dealerTotal}")
    time.sleep(.15)
    if (dealerTotal <= 21) and (userTotal < dealerTotal):
        print("You Lost!")
        time.sleep(.15)
    elif (userTotal <= 21) and (userTotal > dealerTotal):
        print("You Win!")
        time.sleep(.15)
    elif (userTotal <= 21) == (dealerTotal <= 21):
        print("You Draw!")
        time.sleep(.15)
    elif (dealerTotal > 21) and (userTotal <= 21):
        print("You Win!")
        time.sleep(.15)


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
    time.sleep(.15)
    playAgain = input("Do you want to play Blackjack?(y/n)").lower()
    time.sleep(.15)
    if playAgain == 'y':
        while playAgain == 'y':
            userCards = dealCard()
            userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
            dealerHand, dealerCards = dealerPlay()
            time.sleep(.15)
            print(f"Dealer's visible card is {dealerCards[0]}")
            time.sleep(.15)
            # stand first turn
            hitOrStand = input("Do you want to hit or stand?(h/s)").lower()
            time.sleep(.15)
            if hitOrStand == 's':
                print("You stand!")
                time.sleep(.15)
            else:
                print("Invalid Input! You forfeit!")
                time.sleep(.15)
            while hitOrStand == 'h':
                newCard = hit()
                userTotal = cardValue(newCard) + userTotal
                if userTotal > 21:
                    print("You busted! Dealer Wins")
                    time.sleep(.15)
                    userBust = True
                    break
                hitOrStand = input("Do you want to hit or stand?(h/s)").lower()
                time.sleep(.15)
            # hit and subsequent stands loop
            if userBust is False:
                checkWin()
            playAgain = input("Play again?(y/n)").lower()
            time.sleep(.15)
            print("Thanks for playing!")
            time.sleep(.15)
    elif playAgain == 'n':
        print("Thanks for playing!")
        time.sleep(.15)
    else:
        print("Invalid input!")
        time.sleep(.15)

