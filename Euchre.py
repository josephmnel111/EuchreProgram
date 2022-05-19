from random import randrange
import random

class PlayerOne:
    Name = "Player"
    Cards = ["None", "None", "None", "None", "None"]
    Team = "Team1"

class PlayerTwo:
    Name = "Player"
    Cards = ["None", "None", "None", "None", "None"]
    Team = "Team2"

class PlayerThree:
    Name = "Player"
    Cards = ["None", "None", "None", "None", "None"]
    Team = "Team1"

class PlayerFour:
    Name = "Player"
    Cards = ["None", "None", "None", "None", "None"]
    Team = "Team2"




cards = [
        "9 Spades", 
         "10 Spades", 
         "Jack Spades", 
         "Queen Spades", 
         "King Spades", 
         "Ace Spades", 
         "9 Clubs", 
         "10 Clubs", 
         "Jack Clubs", 
         "Queen Clubs", 
         "King Clubs", 
         "Ace Clubs", 
         "9 Hearts", 
         "10 Hearts", 
         "Jack Hearts", 
         "Queen Hearts", 
         "King Hearts", 
         "Ace Hearts", 
         "9 Diamonds", 
         "10 Diamonds", 
         "Jack Diamonds", 
         "Queen Diamonds", 
         "King Diamonds", 
         "Ace Diamonds"
         ]
playerOne = PlayerOne()
playerTwo = PlayerTwo()
playerThree = PlayerThree()
playerFour = PlayerFour()


def pickCard(cards, randNum): #Picks a random card given a random number
    return cards[randNum]

def nextPlayer(playerNumber): #Makes it the next player's turn
    if (playerNumber < 4):
        playerNumber = playerNumber + 1
    else:
        playerNumber = 1
    return playerNumber


def checkWinner(points): #Finds the player with the highest card points and returns that player
    winner = 1
    winnerPoints = points[0]
    for a in range(4):
        if (points[a] > winnerPoints):
            winner = a + 1
            winnerPoints = points[a]
    return winner

def assignPoints(playerCards, trump): #Assigns points to the card values
    points = [-1, -1, -1, -1]
    for a in range(4):
        if (playerCards[a] == "9 Spades") :
            points[a] = 9
        elif (playerCards[a] == "10 Spades") :
            points[a] = 10
        elif (playerCards[a] == "Jack Spades") :
            points[a] = 11
        elif (playerCards[a] == "Queen Spades") :
            points[a] = 12
        elif (playerCards[a] == "King Spades") :
            points[a] = 13
        elif (playerCards[a] == "Ace Spades") :
            points[a] = 14
        elif (playerCards[a] == "9 Clubs") :
            points[a] = 9
        elif (playerCards[a] == "10 Clubs") :
            points[a] = 10
        elif (playerCards[a] == "Jack Clubs") :
            points[a] = 11
        elif (playerCards[a] == "Queen Clubs") :
            points[a] = 12
        elif (playerCards[a] == "King Clubs") :
            points[a] = 13
        elif (playerCards[a] == "Ace Clubs") :
            points[a] = 14
        elif (playerCards[a] == "9 Hearts") :
            points[a] = 9
        elif (playerCards[a] == "10 Hearts") :
            points[a] = 10
        elif (playerCards[a] == "Jack Hearts") :
            points[a] = 11
        elif (playerCards[a] == "Queen Hearts") :
            points[a] = 12
        elif (playerCards[a] == "King Hearts") :
            points[a] = 13
        elif (playerCards[a] == "Ace Hearts") :
            points[a] = 14
        elif (playerCards[a] == "9 Diamonds") :
            points[a] = 9
        elif (playerCards[a] == "10 Diamonds") :
            points[a] = 10
        elif (playerCards[a] == "Jack Diamonds") :
            points[a] = 11
        elif (playerCards[a] == "Queen Diamonds") :
            points[a] = 12
        elif (playerCards[a] == "King Diamonds") :
            points[a] = 13
        elif (playerCards[a] == "Ace Diamonds") :
            points[a] = 14

        if trump in playerCards[a]: #If the card is trump, add 50 to the value
            points[a] = points[a] + 50

    return points


def playCards(currentPlayer, trump): #Asks the player which card they want to play
    validInput = "false"
    while(validInput == "false"):
        if (currentPlayer == 1):
            print("Player 1's Cards:")
            for a in range(5):
                print(playerOne.Cards[a])
            card = input("Which card would player 1 like to play?")
            for a in range(5):
                if (card == playerOne.Cards[a]):
                    playerOne.Cards[a] = "None"
                    validInput = "true"
        if (currentPlayer == 2):
            print("Player 2's Cards:")
            for a in range(5):
                print(playerTwo.Cards[a])
            card = input("Which card would player 2 like to play?")
            for a in range(5):
                if (card == playerTwo.Cards[a]):
                    playerTwo.Cards[a] = "None"
                    validInput = "true"
        if (currentPlayer == 3):
            print("Player 3's Cards:")
            for a in range(5):
                print(playerThree.Cards[a])
            card = input("Which card would player 3 like to play?")
            for a in range(5):
                if (card == playerThree.Cards[a]):
                    playerThree.Cards[a] = "None"
                    validInput = "true"
        if (currentPlayer == 4):
            print("Player 4's cards: ")
            for a in range(5):
                print(playerFour.Cards[a])
            card = input("Which card would player 4 like to play?")
            for a in range(5):
                if (card == playerFour.Cards[a]):
                    playerFour.Cards[a] = "None"
                    validInput = "true"
    return card

def dealCards(newCards):
    trump = "None"
    random.shuffle(newCards)
    for a in range(5):
        b = ((a*4) + 0)
        c = ((a*4) + 1)
        d = ((a*4) + 2)
        e = ((a*4) + 3)
        playerOne.Cards[a] = newCards[b]
        playerTwo.Cards[a] = newCards[c]
        playerThree.Cards[a] = newCards[d]
        playerFour.Cards[a] = newCards[e]
    trump = newCards[21]
    print(trump)
    if (trump.find("Spades") != -1):
        trump = "Spades"
    if (trump.find("Hearts") != -1):
        trump = "Hearts"
    if (trump.find("Clubs") != -1):
        trump = "Clubs"
    if (trump.find("Diamonds") != -1):
        trump = "Diamonds"
    return trump

def startGame(): #Starts the game for the users
    teamOneTotal = 0
    teamTwoTotal = 0
    while ((teamOneTotal < 10) and (teamTwoTotal < 10)): #Loops until a team reaches 10 points
        teamOneRound = 0
        teamTwoRound = 0
        currentCards = ["None", "None", "None", "None"]
        trump = dealCards(cards)
        dealer = nextPlayer(1)
        currentPlayer = dealer
        makeTrump = "false"
        i = 0
        while ((makeTrump == "false") and (i != 4)): #Someone must declare trump
            stringCurrentPlayer = str(currentPlayer)
            inputVal = "Make Trump? (Yes or No) Player " + stringCurrentPlayer + ": "
            userTrump = input(inputVal)
            if ((userTrump == "no") or (userTrump == "No")):
                i = i + 1
            else: #Executes when individual declares trump
                makeTrump = "true"
                for a in range(5):
                    for a in range(4):
                        currentPlayer = nextPlayer(currentPlayer)
                        playedCard = playCards(currentPlayer, trump)
                        currentCards[a] = playedCard
                    points = assignPoints(currentCards, trump)
                    winner = checkWinner(points)
                    if ((winner == 1) or (winner == 3)):
                        teamOneRound = teamOneRound + 1
                    else:
                        teamTwoRound = teamTwoRound + 1
                if (teamOneRound > teamTwoRound):
                    teamOneTotal = teamOneTotal + 1
                    print("Players 1 and 3 won that round.")
                elif (teamTwoRound > teamOneRound):
                    teamTwoTotal = teamTwoTotal + 1
                    print("Players 2 and 4 won that round.")
                else:
                    print("That round was a tie.")

        print(playerOne.Cards[0], playerOne.Cards[1])
    if (teamOneTotal > teamTwoTotal):
        print("Team 1 is the winner!")
    else:
        print("Team 2 is the winner!")

def main(): #Assigns main values such as random cards and allows people to enter their names
    cardCount = 23
    array = ["None"] * cardCount
    for b in range(cardCount):
        array[b] = cards[b]

    playerOne.Name = input("Enter Player One Name: ")
    playerTwo.Name = input("Enter Player Two Name: ")
    playerThree.Name = input("Enter Player Three Name: ")
    playerFour.Name = input("Enter Player Four Name: ")
    startGame()

main()