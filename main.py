
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
                aceStorage.clear()
                delayPrint("No more cards! Reshuffling!")
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
    delayPrint("Your cards are:")
    showHand(userOriginalCards)
    return userOriginalCards

# deals user a single card
def hit():
    card = genCard()
    hitCard = [card]
    delayPrint("Hit!")
    delayPrint("Your new card is:")
    showHand(hitCard)
    userCards.append(card)
    delayPrint("Your current hand is:")
    showHand(userCards)
    return card

# checks player cards and determines win or loss
def checkWin(userMoney):
    delayPrint("Your cards were:")
    showHand(userCards)
    delayPrint(f"Your total was {userTotal}")
    delayPrint(f"Dealer's cards were:")
    showHand(dealerCards)
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
    elif (userTotal > 21) and (dealerTotal <= 21):
        delayPrint("You busted!")
        delayPrint("You Lost!")
        delayPrint(f"You lost {userBet} dollars!")
    elif (dealerTotal > 21) and (userTotal > 21):
        delayPrint("You both lost!")
        delayPrint("No one lost any money!")
        userMoney = userBet + userMoney
    return userMoney

def delayPrint(text):
    time.sleep(.15)
    print(text)
    time.sleep(.15)

def smallDelayPrint(text):
    time.sleep(.1)
    print(text)
    time.sleep(.1)
# define dealer score
def dealerPlay():
    dealerCards = [genCard(), genCard()]
    dealerTotal = cardValue(dealerCards[0]) + cardValue(dealerCards[1])
    if dealerTotal > 21:
        dealerTotal = aceCheck(dealerCards, dealerTotal)
    while dealerTotal < random.randint(16, 18):
        dealerNewCard = genCard()
        dealerCards.append(dealerNewCard)
        dealerHit = cardValue(dealerNewCard)
        dealerTotal = dealerHit + dealerTotal
        dealerTotal = aceCheck(dealerCards, dealerTotal)
    if dealerTotal > 21:
        dealerTotal = aceCheck(dealerCards, dealerTotal)
    return dealerTotal, dealerCards

def generateUserMoney():
    money = random.randint(1,1000)
    delayPrint(f"You have {money} dollars")
    return money

def bet(userMoney):
    while True:
        time.sleep(.15)
        while True:
            userBet = input("How much money would you like to bet? ")
            try:
                userBet = int(userBet)
                break
            except ValueError:
                delayPrint("Please enter a number!")
        if userBet > userMoney:
            delayPrint(f"You don't have enough money! You can bet upto {userMoney} dollars")
        else:
            userMoney = userMoney - userBet
            delayPrint(f"You bet {userBet} dollars")
            delayPrint(f"You have {userMoney} dollars left!")
            break
    return userMoney, userBet

def aceCheck(userCards, userTotal):
    checkSet = ['ACE of DIAMONDS', 'ACE of HEARTS', 'ACE of SPADES', 'ACE of CLUBS']
    for element in checkSet:
        if element in userCards and userTotal > 21 and element not in aceStorage:
            aceStorage.append(element)
            userTotal = userTotal - 10
            break
    return userTotal

def cardParse(card):
    number = card.split(' ')[0]
    suit = card.split(' ')[2]
    parsedCard = [number, suit]
    return parsedCard

def cardPrint(parsedCard, brokenCards):
    global number, suit
    blankCard = False
    if parsedCard[0] == 'ACE':
        number = 'A'
    elif parsedCard[0] == 'JACK':
        number = 'J'
    elif parsedCard[0] == 'QUEEN':
        number = 'Q'
    elif parsedCard[0] == 'KING':
        number = 'K'
    elif parsedCard[0] == 'BLANK':
        blankCard = True
    else:
        number = parsedCard[0]
    if parsedCard[1] == 'SPADES':
        suit = '♠'
    elif parsedCard[1] == 'CLUBS':
        suit = '♣'
    elif parsedCard[1] == 'DIAMONDS':
        suit = '♦'
    elif parsedCard[1] == 'HEARTS':
        suit = '♥'
    elif parsedCard[1] == 'BLANK':
        blankCard = True
    if number == '10':
        tenCheck = True
    else:
        tenCheck = False
    if blankCard:
        cardLineTwo = "│░░░░│"
        cardLineThree = "│░░░░│"
        cardParts = [cardLineTwo, cardLineThree]
        brokenCards.append(cardParts)
    else:
        if tenCheck:
            cardLineTwo = f"│{number} {suit}│"
            cardLineThree = f"│{suit} {number}│"
        else:
            cardLineTwo = f"│{number}  {suit}│"
            cardLineThree = f"│{suit}  {number}│"
        cardParts = [cardLineTwo, cardLineThree]
        brokenCards.append(cardParts)

def cardPaste(brokenCards):
    topList = []
    topMidList = []
    bottomMidList = []
    bottomList = []
    for n in range(len(brokenCards)):
        topList.append("┌────┐")
    smallDelayPrint(f"{' '.join(topList)}")
    for n in range(len(brokenCards)):
        topMidList.append(brokenCards[n][0])
    smallDelayPrint(f"{' '.join(topMidList)}")
    for n in range(len(brokenCards)):
        bottomMidList.append(brokenCards[n][1])
    smallDelayPrint(f"{' '.join(bottomMidList)}")
    for n in range(len(brokenCards)):
        bottomList.append("└────┘")
    smallDelayPrint(f"{' '.join(bottomList)}")

def showHand(userHand):
    brokenCards = []
    for n in range(len(userHand)):
        parsedCard = cardParse(userHand[n])
        cardPrint(parsedCard, brokenCards)
    cardPaste(brokenCards)

aceStorage = []
userMoney = generateUserMoney()
playAgain = True
while playAgain != 'y' and playAgain != 'n':
    time.sleep(.15)
    playAgain = input("Do you want to play Blackjack?(y/n)").lower()
    time.sleep(.15)
    if playAgain == 'y':
        while playAgain == 'y' and userMoney != 0:
            userBust = False
            userMoney, userBet = bet(userMoney)
            userCards = dealCard()
            userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
            userTotal = aceCheck(userCards, userTotal)
            dealerTotal, dealerCards = dealerPlay()
            doubleDownProtection = []
            singleDealerCard = [dealerCards[0], 'BLANK of BLANK']
            delayPrint("Dealer's cards are:")
            showHand(singleDealerCard)
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
                    elif not doubleDownProtection:
                        userMoney = userMoney - userBet
                        userBet = userBet * 2
                        delayPrint(f"Your new bet is {userBet} dollars")
                        delayPrint(f"You have {userMoney} dollars left!")
                        newCard = hit()
                        userTotal = cardValue(newCard) + userTotal
                        userTotal = aceCheck(userCards, userTotal)
                        doubleDownProtection.append(hitOrStand)
                        if userTotal > 21:
                            break
                    else:
                        delayPrint("You have already hit! You can't double down!")
                # hit and subsequent stands loop
                elif hitOrStand == 'h':
                    newCard = hit()
                    userTotal = cardValue(newCard) + userTotal
                    userTotal = aceCheck(userCards, userTotal)
                    doubleDownProtection.append(hitOrStand)
                    if userTotal > 21:
                        break
                else:
                    delayPrint("Invalid input!")
            userMoney = checkWin(userMoney)
            playAgain = input("Play again?(y/n)").lower()
            delayPrint(f"You have {userMoney} dollars left!")
    elif playAgain == 'n':
        delayPrint("Thanks for playing!")
    else:
        delayPrint("Invalid input!")
