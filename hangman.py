import random, time
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple', 'cantaloupe', 'grapefuit', 'jackfruit', 'papaya']
superHeroes = ['hawkeye', 'robin', 'galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']
#Variable to store game statistics
userGuessList = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

#The game info
name = input("Enter your name : ")
print("Hello", name.capitalize(), "let's start playing hangman!")
time.sleep(1)
print("The objective of the game is to guess the secret word that has been prepared")
time.sleep(1)
print("You can guess only one letter at a time. don't press 'enter key' after each guess!")
time.sleep(2)
print("Let the fun begin!")
time.sleep(1)

while True:
    #Choosing random word
    while True:
        if category.upper() == 'S':
            secretWord = random.choice(superHeroes)
            break
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        else :
            category = input("Please select a category: 'F' for fruits / 'S' for super heroes, 'X' to exit")

        if category.upper() == 'X':
            print("Bye, see you next time!")
            playGame = False
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 2)
        
        #Utility function to print user's guesses
        def printGuessedLetter():
            print("Your Secret Word is : " + ''.join(userGuessList))
        
        #Adding blank line to userGuessList to create the blank secret word
        for n in secretWordList:
            userGuessList.append('_')
        printGuessedLetter()
        
        print("The number of allowed guesses for this word is : ", attempts)
        
        #Starting the game
        while True:
            print("Guess a letter : ")
            letter = input()
            
            if letter in userGuesses:
                print("You already guess this letter, try something else")
            
            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, " guess left!")
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuessList[letterIndex] = letter.upper()
                    printGuessedLetter()
                            
                else:
                    print("Oops! try again")
                    if attempts > 0:
                        print("You have ", attempts, " guess left!")
                    printGuessedLetter()
                    
            #Win/loss condition for game
            joinedList = ''.join(userGuessList)
            if joinedList.upper() == secretWord.upper():
                print("Yay! you won!")
                break
            elif attempts == 0:
                print("Too many guess, try next time!")
                print("The secret word is : "+secretWord.upper())
                break
                    
        #Play again logic for the game
        continueGame = input("Do you want to play again? [Y] continue, press any other key to quit")
        if continueGame == 'y':
            category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
            userGuessList = []
            userGuesses = []
            playGame = True
        
        else:
            print("Thank you for playing with us")
            break
                    
    else:
        break