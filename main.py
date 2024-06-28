
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
                delayPrint("No more cards! Reshuffling!")
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
    delayPrint(f"Your cards are {', '.join(userOriginalCards)}")
    return userOriginalCards


# deals user a single card
def hit():
    card = genCard()
    delayPrint(f"Your card is {card}")
    userCards.append(card)
    delayPrint(f"Your current cards are: {', '.join(userCards)}")
    return card

# checks player cards and determines win or loss
def checkWin(userMoney):
    dealerTotal = dealerHand[0] + dealerHand[1]
    delayPrint(f"Your cards were {', '.join(userCards)}")
    delayPrint(f"Your total was {userTotal}")
    delayPrint(f"Dealer's cards were {', '.join(dealerCards)}")
    delayPrint(f"Dealer's total was {dealerTotal}")
    if (dealerTotal <= 21) and (userTotal < dealerTotal):
        userMoney = userMoney
        delayPrint("You Lost!")
        delayPrint(f"You lost {userBet} dollars!")
    elif (userTotal <= 21) and (userTotal > dealerTotal):
        delayPrint("You Win!")
        userMoney = userBet*2 + userMoney
        delayPrint(f"You won {userBet*2} dollars!")
        return userMoney
    elif (userTotal <= 21) == (dealerTotal <= 21):
        delayPrint("You Draw, no one lost anything!")
        userMoney = userBet + userMoney
    elif (dealerTotal > 21) and (userTotal <= 21):
        userMoney = userBet*2 + userMoney
        delayPrint("Dealer busted!")
        delayPrint("You Win!")
        delayPrint(f"You won {userBet*2} dollars!")
        
    return userMoney

def delayPrint(text):
    time.sleep(.15)
    print(text)

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

def generateUserMoney():
    money = random.randint(1,1000)
    delayPrint(f"You have {money} dollars")
    return money

def bet(userMoney):

    while True:
        time.sleep(.15)
        userBet = int(input("How much money would you like to bet? "))
        if userBet > userMoney:
            delayPrint(f"You don't have enough money! You can bet upto {userMoney} dollars")
        else:
            userMoney = userMoney - userBet
            delayPrint(f"You bet {userBet} dollars")
            delayPrint(f"You have {userMoney} dollars left!")
            break
    return userMoney, userBet


userMoney = generateUserMoney()
playAgain = True
while playAgain != 'y' and playAgain != 'n':
    time.sleep(.15)
    playAgain = input("Do you want to play Blackjack?(y/n)").lower()
    if playAgain == 'y':
        while playAgain == 'y' and userMoney != 0:
            userBust = False
            userMoney, userBet = bet(userMoney)
            userCards = dealCard()
            userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
            dealerHand, dealerCards = dealerPlay()
            delayPrint(f"Dealer's visible card is {dealerCards[0]}")
            while True:
                time.sleep(.15)
                hitOrStand = input("Do you want to hit, stand or double down?(h/s/dd)").lower()
                if hitOrStand == 's':
                    delayPrint("You stand!")
                    break
                elif hitOrStand == 'dd':
                    if userMoney < userBet:
                        delayPrint("You don't have enough money!")
                        continue
                    else:
                        userMoney = userMoney - userBet
                        userBet = userBet * 2
                        delayPrint(f"Your new bet is {userBet} dollars")
                        delayPrint(f"You have {userMoney} dollars left!")
                        newCard = hit()
                        userTotal = cardValue(newCard) + userTotal
                        if userTotal > 21:
                            delayPrint("You busted! Dealer Wins")
                            userBust = True
                            delayPrint(f"You lost {userBet} dollars!")
                            break
                        else:
                            break
                # hit and subsequent stands loop
                elif hitOrStand == 'h':
                    newCard = hit()
                    userTotal = cardValue(newCard) + userTotal
                    if userTotal > 21:
                        delayPrint("You busted! Dealer Wins")
                        delayPrint(f"You lost {userBet} dollars!")
                        userBust = True
                        delayPrint("Thanks for playing!")
                        break
            if not userBust:
                dealerTotal = sum(dealerHand)
                userMoney = checkWin(userMoney)
            time.sleep(.15)
            playAgain = input("Play again?(y/n)").lower()
            delayPrint(f"You have {userMoney} dollars left!")
    elif playAgain == 'n':
        delayPrint("Thanks for playing!")
    else:
        delayPrint("Invalid input!")
        

