import random


#generates a random card and stores it as variable 'card'
def genCard():
    cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    card = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
    return card

def genCardDealer():
  cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
  cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
  Dcard = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
  return Dcard

def cardValue(card):
    number = card.split(' ')[0]
    if number == 'ACE':
        return 11
    elif number == 'JACK' or number == 'QUEEN' or number == 'KING':
        return 10
    else:
        return int(number)


#deal a card the user can see one and can't see the other. ask user if they want to hit or stand
def dealCard():
    visibleCard = genCard()
    hiddenCard = genCard()
    userCards = [visibleCard, hiddenCard]
    print(f"Your visible card is {visibleCard}")
    print(f"Your hidden card is [hidden]")
    return userCards


#deals user a single card
def hit():
    card = genCard()
    print(f"Your card is {card}")
    userCards.append(card)
    print(userCards)
    return card


#checks player cards and determines win or loss
def checkWin():
    print(f"Your cards were {userCards}")
    print(f"Your total is {userTotal}")
    if userTotal > 21:
        print("You busted!")
    elif userTotal <= 21:
        print("You win!")


#define dealer score
def dealerPlay():
    dealerHand = [cardValue(genCardDealer()), cardValue(genCard())]
    eval(dealerHand)
    if dealerHand[0] < random.randint(16,18):
      dealerHand.append(cardValue(genCardDealer()))
        if de

    return dealerHand



print(dealerPlay())
#beginning of main code- sets up play again loop and introduces the game. Maybe add rules?
playAgain = 'y'
while playAgain == 'y':
    gameStart = input("Do you want to play Blackjack?(y/n)")
    if gameStart == 'y':
        userCards = dealCard()
        userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
        print(userTotal)
        #stand first turn
        hitOrStand = input("Do you want to hit or stand?(h/s)")
        if hitOrStand == 's':
            print("You stand!")
            checkWin()
        #hit and subsequent stands loop
        while hitOrStand == 'h':
            newCard = hit()
            userTotal = cardValue(newCard) + userTotal
            print(userTotal)
            if userTotal > 21:
                print("You busted!")
                break
            elif userTotal == 21:
                print("You win!")
                break
            hitOrStand = input("Do you want to hit or stand?(h/s)")
        checkWin()
        playAgain = input("Play again?(y/n)")
    else:
        print("Thanks for playing!")
        break
