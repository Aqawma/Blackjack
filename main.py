
import random

pickedCards = []
#generates a random card and stores it as variable 'card'
def genCard():
    cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    while True:
      card = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
      if card not in pickedCards:
        pickedCards.append(card)
        return card
        break
      elif card in pickedCards:
        if len(pickedCards) == 52:
            pickCards.clear()
            print("No more cards! Reshuffling!")
            break
        continue
#seperate function to generate cards for dealer
def genCardDealer():
    cardNumber = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    cardSuit = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
    while True:
      card = random.choice(cardNumber) + ' of ' + random.choice(cardSuit)
      if card not in pickedCards:
        pickedCards.append(card)
        return card
        break
      elif card in pickedCards:
        if len(pickedCards) == 52:
            pickCards.clear()
            break
        continue
        return dcard

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
    dealerCards = [genCardDealer(), genCardDealer()]
    dealerHand = [cardValue(dealerCards[0]), cardValue((dealerCards[1]))]
    dealerTotal = dealerHand[0]
    while dealerTotal < random.randint(16,18):
        dealerHit = cardValue(genCardDealer())
        dealerHand[0] += dealerHit
        dealerTotal = dealerHand[0]
    return dealerHand
    print(dealerCards)
    print(dealerHand)
a = dealerPlay()
print(a)
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
