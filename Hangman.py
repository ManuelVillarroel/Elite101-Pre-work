from EnglishWords import potentialWords
import random

def printoutList(list):
  #https://www.codingem.com/python-print-on-the-same-line/
  for x in list:
    print(x, end = ' ')
  print()

def printMan(numberMissed):
  if numberMissed == 7:
    print('     -----\n     |    |\n     O    |\n    / \\   |\n     |    |\n     |    |\n    / \\  ---')
  elif numberMissed == 6:
    print('     -----\n     |    |\n     O    |\n    / \\   |\n     |    |\n     |    |\n    /    ---')
  elif numberMissed == 5:
    print('     -----\n     |    |\n     O    |\n    / \\   |\n     |    |\n     |    |\n         ---')
  elif numberMissed == 4:
    print('     -----\n     |    |\n     O    |\n    / \\   |\n     |    |\n          |\n         ---')
  elif numberMissed == 3:
    print('     -----\n     |    |\n     O    |\n    / \\   |\n          |\n          |\n         ---')
  elif numberMissed == 2:
    print('     -----\n     |    |\n     O    |\n    /     |\n          |\n          |\n         ---')
  elif numberMissed == 1:
    print('     -----\n     |    |\n     O    |\n          |\n          |\n          |\n         ---')
  else:
    print('     -----\n     |    |\n          |\n          |\n          |\n          |\n         ---')
    
def printBoard(numbermissed, discoveries, guesses):
  printMan(numbermissed)
  print('\n\t', end = '')
  printoutList(discoveries)
  print('\tyou have guessed:')
  print('\t', end = '')
  printoutList(guesses)
  print()

def hangman():
  secretWord = random.choice(random.choice(potentialWords))
  discovered = []
  missed = 0
  guessedLetters = []
  correctlyGuessed = []
  for x in secretWord:
    discovered.append('_')

  reply = ''
  while discovered.count('_') > 0 and missed < 7:
    printBoard(missed,discovered,guessedLetters)
    reply = input('what letter are you guessing next?\n')
    if guessedLetters.count(reply[0].lower()) > 0 or correctlyGuessed.count(reply[0].lower()) > 0:
      while guessedLetters.count(reply[0]) > 0 or correctlyGuessed.count(reply[0].lower()) > 0:
        print(f'you\'ve already guessed {reply[0].upper()}!\n')
        reply = input('what letter are you guessing next?\n')
    if secretWord.lower().__contains__(reply[0].lower()):
      correctlyGuessed.append(reply[0].lower())
      for x in range(len(secretWord)):
        if secretWord[x].lower() == reply[0].lower():
          discovered[x] = reply[0].lower()
      if discovered.count(reply[0].lower()) > 1:
        print(f'there are {discovered.count(reply[0].lower())} {reply[0].upper()}\'s in my word!')
      else:
        print(f'there is a {reply[0].upper()} in my word!')
    else:
      print(f'\n there is no {reply[0].lower()} in my word :)')
      guessedLetters.append(reply[0].lower())
      missed += 1
    print()
  printBoard(missed,discovered,guessedLetters)
  if discovered.count('_') == 0:
    print(f'Great job! you found out that my word was {secretWord}!\n')
  else:
    print(f'aw that\'s a shame. My word was {secretWord}.\n')
  