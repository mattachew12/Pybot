#!/usr/bin/env python
import random
import time
import Dictionary
import string
import math
import sys
import os
from winsound import Beep


class WordChangingGame():
    def __init__(self):    
        self.Alphabet = string.ascii_lowercase
        self.WordList = Dictionary.dictionary()
        self.UsedList = []
        self.Cont = False
        self.LegalChange = False
        self.PlayerTurn = True
        self.GameOn = True
        self.giveUp = False
        print """
        Welcome to the Word Changing Game. In this game you type a word to start with,
        and then we take turns changing that word to another word with one change. It 
        can be a replacement, insertion, or deletion, but it can only be of one letter.
        Whoever cannot come up with another word loses. If you can't think on one, type
        "I give up" and we'll end. Let's begin!"""
        while self.GameOn:
            while self.PlayerTurn:
                self.NewWord = raw_input("Player: ").lower().strip()
                if self.NewWord == "i give up":
                    self.GameOn = False
                    self.giveUp = True
                    self.PlayerTurn = False
                    self.changeWord()
                    if self.PlayerTurn == False:
                        print "There was no other word you could have used. Good try!"
                    break
                if self.NewWord in self.WordList and self.NewWord not in self.UsedList:
                    if len(self.UsedList) == 0: # if this is the first word
                        self.UsedList.append(self.NewWord)
                        self.OldWord = self.NewWord
                        self.PlayerTurn = False 
                    else: # establishes a legal change, already established that word is known
                        for index in range(0, len(self.OldWord)+1):
                            for character in self.Alphabet:
                                self.TestWord = self.OldWord[:index] + character + self.OldWord[index + 1:] # replace
                                if self.TestWord == self.NewWord:                                
                                    self.LegalChange = True
                                    break
                                self.TestWord = self.OldWord[:index] + character + self.OldWord[index:] # insert
                                if self.TestWord == self.NewWord:                                
                                    self.LegalChange = True
                                    break
                            if not self.LegalChange: 
                                self.TestWord = self.OldWord[:index] + self.OldWord[index+1:] # delete
                                if self.TestWord == self.NewWord:
                                    self.LegalChange = True  
                            if self.LegalChange:
                                self.OldWord = self.NewWord
                                self.UsedList.append(self.NewWord)
                                self.LegalChange = False
                                self.PlayerTurn = False
                                break 
                    if self.PlayerTurn:
                        print "that was not a legal change. The word to change is %s" % self.OldWord
                elif self.NewWord in self.UsedList:
                        print "that word has already been used. The word to change is %s" % self.OldWord                       
                else:
                    print "that's not a recognized word. The word to change is %s" % self.OldWord
            while not self.PlayerTurn and not self.giveUp:
                self.changeWord()
                if not self.PlayerTurn: # computer can't find another word
                    print "Congratulations, you win!"
                    self.GameOn = False
                    break
    def checkWord(self):
        if self.NewWord in self.WordList and self.NewWord not in self.UsedList:
            if self.giveUp:
                print "Pybot: You could have used %s" % self.NewWord
                return True
            else:
                self.UsedList.append(self.NewWord)
                self.OldWord  = self.NewWord
                print "Pybot: " + self.NewWord 
                return True
        else:
            return False
    def changeWord(self): # changes if possible        
        for index in range(0, len(self.OldWord)+1):
            for character in self.Alphabet:
                self.NewWord = self.OldWord[:index] + character + self.OldWord[index + 1:] # replace
                if self.checkWord():                                
                    self.Cont = True
                    break
                self.NewWord = self.OldWord[:index] + character + self.OldWord[index:] # insert
                if self.checkWord():                
                    self.Cont = True
                    break
            if not self.Cont:
                self.NewWord = self.OldWord[:index] + self.OldWord[index+1:] # delete
                if self.checkWord():  
                    self.Cont = True
            if self.Cont:
                self.PlayerTurn = True
                self.Cont = False
                break

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print "Initalizing code..."
time.sleep(.3)
print "1%"
time.sleep(.5)
print "5%"
time.sleep(1)
print "10%"
time.sleep(1.3)
print "30%"
time.sleep(1.3)
print "50%"
time.sleep(1.3)
print "75%"
time.sleep(1.3)
print "100%"
time.sleep(0.4)
clearscreen()
print "Initalizing Complete. Pybot ready."
print ""
print '???: Hello! What is your name?'
UserName = raw_input("User:")
print '???: My name is Pybot. Have we met before? (y/n)'
UserInput = ""
while UserInput != "y" and UserInput != "n":
    UserInput = raw_input("%s:" % UserName)
    UserInput = UserInput.strip()
if UserInput=="n":
    print 'Pybot: Hello ' + UserName +'. I am PyBot. I am here to entertain you when you get bored. Say "list" for a list of words I understand.'
elif UserInput=="y":
    print 'Pybot: Welcome back!'
else:
    print 'Pybot: I did not understand your response. Please type "y" or "n".'
commands = ["list","morse code", "annoyance mode","hangman","number guess", "quit", "word game"]
fun = ["annoyance mode","number guess","hangman", "word game"]
game = ""
print 'Pybot: What do you want to do?'
while True:
    UserInput = raw_input("%s:" % UserName)
    while UserInput not in commands:
        print 'Pybot: What was that? For a list of words I understand, type "list".'
        UserInput = raw_input("%s:" % UserName)
        UserInput = UserInput.strip()
    game = UserInput
    if UserInput == "list":
        print commands
    elif UserInput == "annoyance mode":
        print 'Annoyance mode loaded. Say "end" to return.'
        print "type a string, any string."
        while UserInput != "end":
            UserInput = raw_input("%s:" % UserName)
            UserInput = UserInput.strip()
            if UserInput!= "end":
                print "Pybot: " + UserInput                
                
    elif UserInput == "hangman":
        end = 0
        while end == 0:
            def allinstances(string, letter):
                listindex = []
                i = string.find(letter,1) # 1 is because there is a space added before word. don't know what that does
                while i >= 0:
                    listindex.append(i)
                    i = string.find(letter, i + 1)
                return listindex
            
            def printhang():
                if badguess == 0:
                    print """
               ______
               |    |
                    |
                    |
                    |
                  __|__"""
                if badguess == 1:
                    print """
               ______
               |    |
               o    |
                    |
                    |
                  __|__"""   
                if badguess == 2:
                    print """
               ______
               |    |
               o    |
               |    |
                    |
                  __|__"""
                if badguess == 3:
                    print """
               ______
               |    |
               o    |
               |    |
                \   |
                  __|__"""
                if badguess == 4:
                    print """
               ______
               |    |
               o    |
               |    |
              / \   |
                  __|__"""
                if badguess == 5:
                    print """
               ______
               |    |
               o_   |
               |    |
              / \   |
                  __|__"""
                if badguess == 6:
                    print """
               ______
               |    |
              _o_   |
               |    |
              / \   |
                  __|__"""  
                    print "You hung him! The word was '%s' \n Why don't you try this one?" % (word)
                    
            words = Dictionary.dictionary()
            print "Pybot: Welcome to Hangman!"
            win = input("How many words would you like to play to win:")
            while win < 0 or win > 57949:
                win = input("I'm sorry, please type in an integer less than or equal to 57949 and more than 0:")
            if win == 0:
                break
            print "Ok, Here's the first one for you!"
            q = 1
            wincompare = 0
            while q == 1:
                word = random.choice(words)
                badguess = 0
                usedlistwrong = ""
                UnusedLetters = string.lowercase # this from string import
                looping = len(word)
                underscores = "_ " * looping
                print """
The word is %d letters long, and you can make 6 incorrect guesses. 
If you want to guess on the word, just type it in all lowercase! 
Now go ahead and guess a letter! To exit, type end, to skip to 
another word, type skip""" % (len(word))
                printhang()
                dontend = 1
                while dontend == 1:
                    letterguess = raw_input("%s:" % UserName).lower()
                    if letterguess == "":
                        print "Oh come on! Enter is not a letter!"
                        continue
                    if letterguess == "skip":
                        break
                    if letterguess =="end":
                        end = 1
                        q = 0 
                        break
                    if len(letterguess) > 1 and letterguess != word:
                        print "I'm sorry, that's not the word."
                        continue # this loops back to the start.
                    if letterguess == word:
                        wincompare+=1
                        if wincompare == win:
                            print "You win!"
                            end = 1
                            q = 0
                            break
                        else:
                            print """That's right! the word is %s! Good job.
I've got plenty more though! Here's another for you!""" % (word)      
                        words.remove(word)  
                        break
                    if letterguess not in UnusedLetters:
                        print "You can't use %s" % letterguess
                        continue
                    clearscreen()
                    placement = allinstances(" " + word, letterguess)
                    if letterguess in word:
                        green = 0
                        x = 0
                        while x < len(placement):
                            underscores = underscores[:placement[green] * 2 - 2] + letterguess + " " + underscores[placement[green] * 2:]
                            green+=1
                            x+=1
                        printhang()
                        print usedlistwrong
                        print underscores
                        if "_" not in underscores:
                            print "Congratulations, you got it! The word was %s" % (word)
                            wincompare+=1
                            if wincompare == win:
                                print "You win!"
                                end = 1
                                q = 0
                                break
                            print """You got it! The word was %s! I've got plenty more though! 
Here's another for you!""" % (word)
                            break
                        if "_" in underscores:
                            print "guess again!"
                        del placement[:]
                        UnusedLetters = UnusedLetters[:UnusedLetters.index(letterguess)] + UnusedLetters[UnusedLetters.index(letterguess) + 1:]
                    if letterguess not in word:
                        usedlistwrong = usedlistwrong + letterguess +" "
                        badguess +=1
                        printhang()
                        if badguess == 6:
                            break
                        print usedlistwrong
                        print underscores
                        print "there is no %s. Guess again!" % (letterguess)
                        UnusedLetters = UnusedLetters[:UnusedLetters.index(letterguess)] + UnusedLetters[UnusedLetters.index(letterguess) + 1:]
                        # this removes a incorrect letter from the unused letters.
    elif UserInput == "number guess":
        def findguesses(amount):
            NeededGuesses = math.trunc(math.log(amount,2)) + 1
            return NeededGuesses
        while True:
            choice = raw_input("""
Pybot:Would you like to guess a number or choose one for me? (guess/choose) To go back to another game you can type 'end'.
User: """)
            if choice == "guess":
                print """Pybot:Please type the starting and ending numbers of the game. 
for example, for a game guessing between 1 and 20, first type 1, hit enter, and then 20.
to stop a round, type end"""
                first = input("Starting number:")
                second = input("Ending number:")
                endr = 0
                while endr == 0:  
                    GuessesNeeded = findguesses(second-first)
                    number = random.randint(first,second)
                    GuessesTaken = 0
                    print 'Pybot: I am thinking of a number between %d and %d.' % (first,second)
                    while GuessesTaken < GuessesNeeded ** 2:
                        print 'Pybot: Take a guess.'
                        UserInput = raw_input("%s:" % UserName)
                        if UserInput == "end":
                            break
                        UserInput = int(UserInput)
                        GuessesTaken += 1
                        if UserInput < number:
                            if UserInput < first:
                                print "Pybot:Please enter an integer number between %d and %d." % (first,second)
                            else:
                                print 'Pybot: Your guess is too low.'
                        if UserInput > number:
                            if UserInput > second:
                                print "Please enter an integer number between %d and %d." % (first,second)
                            else:
                                print 'Pybot: Your guess is too high.'
                        if UserInput == number:
                            print 'Pybot: Good job, you guessed my number in %d guesses!' % (GuessesTaken)
                            if GuessesTaken >= GuessesNeeded + 1:
                                print "I could have done it in %d guesses!" % (GuessesNeeded)
                            break
                               
                    if UserInput != number and UserInput != "end":
                        print 'Pybot: Nope. The number I was thinking of was %d' % (number)
                    else:
                        while UserInput!="y" and UserInput!= "n":
                            print 'Pybot: Want to play again? (y/n) \n'
                            UserInput = raw_input("%s:" % UserName).strip().lower()[0]
                            if UserInput == "y":
                                print "Pybot: Ok, let's play again!"
                            elif UserInput == "n":
                                endr = 1
                            else:
                                print 'Pybot:What? Please answer with "y" or "n".'
                continue # stops it from saying what was that
            if choice == "choose":
                print """Pybot: Ok, you won't defeat me! What is the number between?
To stop a round, type 'end'"""
                first = input("lowest number:")
                second = input("highest number:")
                loop = findguesses(second-first)
                cheatfind = 0
                print "Pybot:I'll do it in %d guesses or less!" % (loop)
                continuing = 1
                while continuing == 1:
                    cheatfind += 1
                    if cheatfind > loop:
                        print "Pybot:Cheater! I'm not playing with you anymore."
                        time.sleep(3)
                        sys.exit(1)
                    guess = (second-first)/2 + first
                    print "Pybot:Is it %d? (If so, please tell me yes! If not, type 'higher' or 'lower'" % guess
                    UserInput = raw_input("%s:" % UserName)
                    if UserInput == "higher":
                        first = guess
                    elif UserInput == "lower":
                        second = guess
                    elif UserInput == "yes" or UserInput == "Yes!" or UserInput == "Yes" or UserInput == "yes!":
                        print "Yay! I got it!"
                        break
                    elif UserInput == "end":
                        break
                    else:
                        print "Pybot:I'm sorry, I didn't understand that."
                        cheatfind -= 1
                continue
            if choice == "end":
                break
            else: 
                choice = raw_input("Pybot: I'm sorry, what did you say? Please type either guess or choose:")    
    elif UserInput == "word game":
        WordChangingGame()
    elif UserInput == "morse code":
        EngtoM = { # dictionary containing the morse code equivalents of the alphabet
            "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
            "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
            "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
            "Y": "-.-- ", "Z": "--.. ", " ": "  ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "...._", 
            "5": "....- ", "6": "-...- ", "7": "--..- ", "8": "---.- ", "9": "----- ", "0": "----- ", " ": "  ",
            ".": ".-.-.- ", ",": "--..-- ", "?": "..--.. ", "'": ".----. ", "!": "-.-.-- ", "/": "-..-. ", 
            "(": "-.--. ", ")": "-.--.- ", "&": ".-... ", ":": "---... ", ";": "-.-.-. ", "=": "-...- ", "+": ".-.-. ", 
            "- ": "-....- ", "_": "..--.- ", '"': ".-..-. ", "$": "...-..- ", "@": ".--.-. "}
        MtoEng = { # dictionary containing the morse code equivalents of the alphabet
                ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
                "-.--": "y", "--..": "z", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
                "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0", "": " ", ".-.-.-": ".",
                "--..--": ",", "..--..": "?", ".----.": "'", "-.-.--": "!", "-..-.": "/", "-.--.": "(", "-.--.-": ")",
                ".-...": "&", "---...":":", "-.-.-.": ";", "-...-": "=", ".-.-.": "+", "-....-": "-", "..--.-": "_",
                ".-..-.": '"', "...-..-": "$", ".--.-.": "@"}
        choice = raw_input("Pybot: Would you like me to translate from English-Morse, Morse-English, or English-Morse-Beep (em, me, emb):")
        print "Pybot: if you want to leave, type 'end'"
        if choice == "em":            
            while True:
                message = raw_input("What would you like me to translate?").upper()
                code = ""
                if message == "END":
                    print "Pybot: What would you like to do next?"
                    break
                for letter in message:
                    if letter in EngtoM:
                        code += EngtoM[letter]
                    else:
                        print "I didn't recognize %s. It will be skipped in the translation" % (letter)
                print "Pybot: " + code
        elif choice == "me":            
            while True:
                message = raw_input("What would you like me to translate?")
                if message == "end":
                    print "Pybot: What would you like to do next?"
                    break
                message = message.split("  ")
                uinput = []
                code = ""
                newcode = ""
                for each in message:
                    uinput += each.split(" ")
                for each in uinput:
                    if each not in MtoEng:
                        print "I'm sorry, I didn't recognize '%s', it will be skipped." % (each)
                        continue
                    each = MtoEng[each]
                    code += each
                code = code.capitalize().replace(" god ", " God ").replace(" jesus ", " Jesus ")
                code = code.replace(" holy spirit ", " Holy Spirit ").replace(" bible ", " Bible ").replace(" i ", " I ")
                code = code.replace(" i'", " I'").strip().split(". ") # the split capitalizes sentences.
                for each in code:
                    if each != code[len(code)-1]:
                        newcode += each.capitalize() + ". "
                    else:
                        newcode += each.capitalize()
                if newcode.endswith(".. "):
                    newcode = newcode[:len(newcode)-2] # 2 because there is a space after the period.
                print "Pybot: " + newcode
        if choice == "emb":
            print "I suggest taking off your headphones (but keep them plugged in), it will be better on your ears and it actually sounds better too."
            while True:
                message = raw_input("What would you like me to translate?").upper()
                code = ""
                if message == "END":
                    print "Pybot: What would you like to do next?"
                    break
                for letter in message:
                    if letter in EngtoM:
                        code += EngtoM[letter]
                    else:   
                        print "I didn't recognize %s. It will be skipped in the translation" % (letter)
                print code
                time.sleep(1.5)
                for char in code: # play morse code
                    if char is '.':
                        Beep(850, 200)
                    elif char is '-':
                        Beep(850, 600)
                    elif char is ' ':
                        time.sleep(.2)
                    time.sleep(.05)
        else:
            print "What would you like to do?"
    if game in fun:
        print 'Pybot: That was fun. What next?'
    if UserInput == "quit":
        print "Pybot: Bye!"
        time.sleep(1)
        break
