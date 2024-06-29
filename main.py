import random
import time
pickedCards = []

# generates a random card
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

# determines value of a card
def cardValue(card):
    number = card.split(' ')[0]
    if number == 'ACE':
        return 11
    elif number == 'JACK' or number == 'QUEEN' or number == 'KING':
        return 10
    else:
        return int(number)

# deals user cards
def dealCard():
    visibleCard = genCard()
    hiddenCard = genCard()
    userOriginalCards = [visibleCard, hiddenCard]
    delayPrint("Your cards are:")
    showHand(userOriginalCards)
    return userOriginalCards

# deals user a single card called a hit
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

# checks player cards against dealer cards to determine a win or loss
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

# delays printing of text by .15 seconds to make reading easier
def delayPrint(text):
    time.sleep(.15)
    print(text)
    time.sleep(.15)

# delays printing of text by .1 seconds to make reading easier used mostly in printing cards
def smallDelayPrint(text):
    time.sleep(.1)
    print(text)
    time.sleep(.1)

# plays the whole game for the dealer and determines score
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

# generates a random amount of money between 1-1000 for the user to start betting with
def generateUserMoney():
    money = random.randint(1,1000)
    delayPrint(f"You have {money} dollars")
    return money

# allows the user to bet money at specific times
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

# if the user or dealer total is over 21, and they have an ace in their hand, 10 is subtracted from the total score.
# This effectively makes the ace worth 1
def aceCheck(userCards, userTotal):
    checkSet = ['ACE of DIAMONDS', 'ACE of HEARTS', 'ACE of SPADES', 'ACE of CLUBS']
    for element in checkSet:
        if element in userCards and userTotal > 21 and element not in aceStorage:
            aceStorage.append(element)
            userTotal = userTotal - 10
            break
    return userTotal

# parses card to find suit and rank to be used in card printing
def cardParse(card):
    number = card.split(' ')[0]
    suit = card.split(' ')[2]
    parsedCard = [number, suit]
    return parsedCard

# changes royalty and aces to letters for card printing. Creates the part of the card that change in the card printing
# process. If statement accounts for 10 being double digits
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

# assembles card parts from card print into something cohesive
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

# the code that puts the above 3 functions together
def showHand(userHand):
    brokenCards = []
    for n in range(len(userHand)):
        parsedCard = cardParse(userHand[n])
        cardPrint(parsedCard, brokenCards)
    cardPaste(brokenCards)

# main game logic
aceStorage = []
userMoney = generateUserMoney()
playAgain = True
while playAgain != 'y' and playAgain != 'n':
    time.sleep(.15)
    playAgain = input("Do you want to play Blackjack?(y/n)").lower()
    time.sleep(.15)
    if playAgain == 'y':
        time.sleep(.15)
        rules = input("Do you know the rules of Blackjack?(y/n)").lower()
        time.sleep(.15)
        if rules == 'n':
            delayPrint("The rules of Blackjack are as follows:")
            delayPrint(
                "Your main goal is to have the cards in your hand be higher than the cards in the dealer's hand "
                "without going over 21!")
            delayPrint(
                "You will initially be dealt two cards. After this, you will have the option to hit, stand, "
                "or double down.")
            delayPrint("You can initially see only one of the dealer's cards.")
            delayPrint("If you decide to hit, you will be dealt another card.")
            delayPrint("If you decide to stand, you effectively end your turn and go into the scoring process.")
            delayPrint(
                "If you decide to double down, you double your original bet, get dealt another card, and then stand.")
            delayPrint("The scoring process determines the winner based on the values of the hands.")
            delayPrint("Card values are as follows:")
            delayPrint("  - Number cards (2-10) are worth their face value.")
            delayPrint("  - Face cards (Jack, Queen, King) are worth 10.")
            delayPrint("  - Aces can be worth 1 or 11, depending on which value is more favorable for your hand.")
            delayPrint("If your hand exceeds 21, you bust and automatically lose.")
            delayPrint("If the dealer busts, you win (provided you haven't already busted).")
            delayPrint("If neither you nor the dealer busts, the higher hand wins.")
            delayPrint("In case of a tie, it's a push and your bet is returned.\n")
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
                        break
                    else:
                        delayPrint("You have already hit! You can't double down!")
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
