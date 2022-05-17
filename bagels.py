import random
numOfDigits = 3
def main():
    maxGuesses = 10
    
    print('''i am thinking of a {} digit number with a no repeated digit 
    try to guess what it is.Here are some clues
    when i say :  that means
    pico           one digit is correct but in the wrong position
    fermi          one digit is correst and in the correct position
    bagles          no digit is correct
    for example, if the secret number was 248 and your guess was 843,the 
    clue would be fermi pico'''.format(numOfDigits))
    while True:
        secretKey = getSecretKey()
        guesses = 1
        guess = ""
        while guesses <= maxGuesses:
            guess = input("guess#{}>".format(guesses))
            while not isValidGuess(guess):
                guess = input("guess#{}>".format(guesses))
                getClue(guess,secretKey)
            
            if guess == secretKey:    
                print("you won")
                break
            guesses+=1
        answer = input("do you want to play again(yes or no)")
        if answer != "yes":
            break

    
def getSecretKey():
    numbers = list("0123456789")
    random.shuffle(numbers)
    number = ""
    for i in range(numOfDigits):
        number+=numbers[i]
    return number
def isValidGuess(guess):
    if len(guess) == numOfDigits and guess.isdecimal():
        return True
    return False
def getClue(guess,key):
    for i in range(numOfDigits):
        if key[i] == guess[i]:
            print('fermi')
        elif key[i] in guess:
            print('pico')
        else :
            print('begle')
   
if __name__ == "__main__":
   main()