
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
    print(f"Your cards are {', '.join(userOriginalCards)}")
    time.sleep(.15)
    return userOriginalCards


# deals user a single card
def hit():
    card = genCard()
    print(f"Your card is {card}")
    time.sleep(.15)
    userCards.append(card)
    print(f"Your current cards are: {', '.join(userCards)}")
    time.sleep(.15)
    return card

# checks player cards and determines win or loss
def checkWin(userMoney):
    dealerTotal = dealerHand[0] + dealerHand[1]
    print(f"Your cards were {', '.join(userCards)}")
    time.sleep(.15)
    print(f"Your total was {userTotal}")
    time.sleep(.15)
    print(f"Dealer's cards were {', '.join(dealerCards)}")
    time.sleep(.15)
    print(f"Dealer's total was {dealerTotal}")
    time.sleep(.15)
    if (dealerTotal <= 21) and (userTotal < dealerTotal):
        userMoney = userMoney
        print("You Lost!")
        print(f"You lost {userBet} dollars!")
        time.sleep(.15)
    elif (userTotal <= 21) and (userTotal > dealerTotal):
        print("You Win!")
        userMoney = userBet*2 + userMoney
        print(f"You won {userBet*2} dollars!")
        time.sleep(.15)
        return userMoney
    elif (userTotal <= 21) == (dealerTotal <= 21):
        print("You Draw, no one lost anything!")
        userMoney = userBet + userMoney
        time.sleep(.15)
    elif (dealerTotal > 21) and (userTotal <= 21):
        userMoney = userBet*2 + userMoney
        print("Dealer busted!")
        time.sleep(.15)
        print("You Win!")
        print(f"You won {userBet*2} dollars!")
        time.sleep(.15)
    return userMoney

def delayPrint(text):
    print(text)
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

def generateUserMoney():
    money = random.randint(1,1000)
    time.sleep(.15)
    print(f"You have {money} dollars")
    time.sleep(.15)
    return money

def bet(userMoney):
    time.sleep(.15)
    while True:
        userBet = int(input("How much money would you like to bet? "))
        if userBet > userMoney:
            print(f"You don't have enough money! You can bet upto {userMoney} dollars")
            time.sleep(.15)
        else:
            userMoney = userMoney - userBet
            print(f"You bet {userBet} dollars")
            time.sleep(.15)
            print(f"You have {userMoney} dollars left!")
            time.sleep(.15)
            break
    return userMoney, userBet


userMoney = generateUserMoney()
playAgain = True
while playAgain != 'y' and playAgain != 'n':
    playAgain = input("Do you want to play Blackjack?(y/n)").lower()
    if playAgain == 'y':
        while playAgain == 'y' and userMoney != 0:
            userBust = False
            userMoney, userBet = bet(userMoney)
            userCards = dealCard()
            userTotal = cardValue(userCards[0]) + cardValue(userCards[1])
            dealerHand, dealerCards = dealerPlay()
            print(f"Dealer's visible card is {dealerCards[0]}")
            while True:
                hitOrStand = input("Do you want to hit, stand or double down?(h/s/dd)").lower()
                if hitOrStand == 's':
                    print("You stand!")
                    time.sleep(.15)
                    break
                elif hitOrStand == 'dd':
                    if userMoney < userBet:
                        print("You don't have enough money!")
                        time.sleep(.15)
                        continue
                    else:
                        userMoney = userMoney - userBet
                        userBet = userBet * 2
                        print(f"Your new bet is {userBet} dollars")
                        time.sleep(.15)
                        print(f"You have {userMoney} dollars left!")
                        time.sleep(.15)
                        newCard = hit()
                        userTotal = cardValue(newCard) + userTotal
                        if userTotal > 21:
                            print("You busted! Dealer Wins")
                            time.sleep(.15)
                            userBust = True
                            print(f"You lost {userBet} dollars!")
                            break
                        else:
                            break
                # hit and subsequent stands loop
                elif hitOrStand == 'h':
                    newCard = hit()
                    userTotal = cardValue(newCard) + userTotal
                    if userTotal > 21:
                        print("You busted! Dealer Wins")
                        print(f"You lost {userBet} dollars!")
                        time.sleep(.15)
                        userBust = True
                        print("Thanks for playing!")
                        break

            if not userBust:
                dealerTotal = sum(dealerHand)
                userMoney = checkWin(userMoney)
            playAgain = input("Play again?(y/n)").lower()
            print(f"You have {userMoney} dollars left!")
            time.sleep(.15)
    elif playAgain == 'n':
        time.sleep(.15)
        print("Thanks for playing!")
    else:
        print("Invalid input!")
        time.sleep(.15)

