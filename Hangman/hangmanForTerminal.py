import random
import os

game_Processing = True
point = 0
WHOLE_LIFE = 5
numberOfShow = 3
currentWord = ""
chosenWord = ""

SCORE = 0
WRONG_GUESS = set()
LIST_WORD = []
PASS_WORD = []
life = WHOLE_LIFE
# STRING START
def changeString1(word,index1):
    global currentWord
    words = len(word)* "_"
    for i,c in enumerate(currentWord) :
        if c == " ":
            words = ((words[:i] + word[i] + words[i+1:]))
    return ((words[:index1] + word[index1] + words[index1+1:]))

# STRING CHANGED WHEN PLAYER GUESS CORRECTLY
def changeString2(word, indexCorrect) :
    global chosenWord, currentWord
    if(len(indexCorrect) == 0):
        chosenWord = word
        return
    word = word[:indexCorrect[0]]+currentWord[indexCorrect[0]]+word[indexCorrect[0]+1:]
    indexCorrect.remove(indexCorrect[0])
    changeString2(word,indexCorrect)
        
def startGame():
    os.system('clear')
    global numberOfShow
    print("          H-A-N-G-M-A-N G-A-M-E")
    print("YOU HAVE 5 LIVES, MISS THEM ALL YOU'll DIE")
    print("             First Step !!\n(press E to choose Easy and H for Hard)")
    choice = raw_input("CHOOSE TYPE TO START : ")
    isChosen = False
    while(not isChosen) :
        if choice.lower() == "E".lower() :
            print("easy choice selected")
            file = open("animal.txt", "r")
            isChosen = True
            numberOfShow = 2
        elif choice.lower() == "H".lower() :
            print("hard choice selected")
            file = open("hardAnimal.txt", "r")
            isChosen = True
            numberOfShow = 1

        else :
            print("NO PATH YOU'VE CHOSEN")
            choice = raw_input("\nCHOOSING AGAIN : ")
        

    global LIST_WORD
    LIST_WORD = [e.strip("\n").lower() for e in file.readlines() if(e.strip("\n")!="")]

    # 
    print("-------------LET'S GET STARTED-------------")
    LoopGame()

def LoopGame():
    global LIST_WORD, life, numberOfShow, currentWord, chosenWord, SCORE, PASSWORD, WRONG_GUESS
    if(len(LIST_WORD)==0) :
        print("PASS TEST")
        return
    index = random.randint(0,len(LIST_WORD)-1)
    currentWord = LIST_WORD[index]
    chosenWord = changeString1(currentWord, random.randint(0,len(currentWord)-1))
    lengthOfWord = len(chosenWord)
    print("....Guess word....")
    print("WORD : {0}, hint : Animal , WRONG_GUESS : {1}".format(" ".join(chosenWord), WRONG_GUESS))
    guess = raw_input("GUESS : ")
    while(True) :
        if(len(guess) != 1):
            print("WRONG TYPE >> ASSIGN ONE CHARACTER")
            guess = raw_input("GUESS : ".format(life))
            if(len(guess)!=1): continue
        indexMatched = currentWord.find(guess)
        if( indexMatched != -1):
            indexCorrect = [i for i,c in enumerate(currentWord) if c==currentWord[indexMatched]]
            changeString2(chosenWord, indexCorrect)
            print("WORD : {0}, hint : Animal , WRONG_GUESS : {1}".format(" ".join(list(chosenWord)), WRONG_GUESS))
            if(chosenWord.find("_") == -1) :
                print("WORD DONE POINT PLUS 5")
                WRONG_GUESS = set()
                SCORE += 5
                LIST_WORD.remove(currentWord)
                PASS_WORD.append(currentWord)
                raw_input("-------enter to play next Word--------")
                os.system('clear')
                LoopGame()
                break
            guess = raw_input("RIGHT, GUESS : ")

        else:
            life -= 1
            if(life == 0):
                print("The word is ", currentWord)
                print("SAD YOU DIE")
                print("YOUR POINT IS {0}, {1} words : {2}".format(SCORE,len(PASS_WORD),PASS_WORD))
                break
            print("WRONG LOSE ONE LIFE , LIFE LEFT : {0}".format(life))
            WRONG_GUESS.add(guess)
            print("WORD : {0}, hint : Animal , WRONG_GUESS : {1}".format(" ".join(list(chosenWord)), WRONG_GUESS))
            guess = raw_input("Hang in there, GUESS AGAIN :")



startGame()
print("......END-GAME.......")

