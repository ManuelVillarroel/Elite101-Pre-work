import random
from EnglishWords import potentialWords
#https://replit.com/talk/ask/How-to-check-if-a-word-is-an-English-word-with-Python/31374
from spellchecker import SpellChecker
dictionary = SpellChecker()

def isEnglishWord(word):
  return word.lower() == dictionary.correction(word).lower()

def abcGame():
  reply = ''
  counter = 0
  skipAll = False
  while True:
    reply = input('do you want to hear the rules on how to play the abcGame? (yes/no)\n')
    if reply.lower().__contains__('yes') or reply.lower().__contains__('no'):
      break
    elif counter < 2:
      counter += 1
      print("that's not a 'yes' or 'no'.")
      input()
    else:
      print('...')
      input()
      skipAll = True
      break
  if skipAll:
    return
  if reply.lower().__contains__('yes'):
    print("\nOkay!\n\nThe rules are simple!\n* starting from the letter A, a player has to say a word on their turn that starts with their letter\n* the next player has to say a word that starts with the next letter\nlooping on the alphabet, this continues until a player:\n*\tsays a non-english word\n*\tdoen't say a word that starts with the next letter\n*\tor repeats a word that's already been said\n")
  else:
    print()

  print('ready?')
  input()
  firstTurn = random.randint(1,2)
  computerList = []
  wordsSaidList = []
  theAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  currentLetter = 0
  if firstTurn == 1:
    print('my turn first!\n')
  else:
    print('you\'re first!\n')
  #adjust her range for higher difficulty!
  for i in range(100):
    selection = random.choice(random.choice(potentialWords))
    computerList.append(selection)
  while len(computerList) > 0:
    if firstTurn == 1:
      for x in computerList:
        if x.lower()[0] == theAlphabet[currentLetter]:
          print(x)
          computerList.remove(x)
          wordsSaidList.append(x)
          break
      else:
        print(f'ugh, I can\'t think of a word that starts with "{theAlphabet[currentLetter].upper()}"\nyou win!\n')
        break
      currentLetter += 1;
      if currentLetter == len(theAlphabet):
        currentLetter = 0
    else:
      firstTurn = 1
      
    playerResponse = input()
    if playerResponse.rstrip().__contains__(' '):
      print('\nhey that\'s cheating!\nyou can\'t say more than one word!\ndisqualified!\n\nI win!\n')
      break
    if isEnglishWord(playerResponse) and playerResponse.lower()[0] == theAlphabet[currentLetter] and not wordsSaidList.__contains__(playerResponse.lower()):
      if computerList.__contains__(playerResponse.lower()):
        computerList.remove(playerResponse.lower())
      wordsSaidList.append(playerResponse.lower())
    else:
      if not isEnglishWord(playerResponse):
        print(f'{playerResponse.lower()} is not an english word!')
      elif playerResponse.lower()[0] != theAlphabet[currentLetter]:
        print(f'{playerResponse.lower()} does not start with the letter {theAlphabet[currentLetter].upper()}!')
      elif wordsSaidList.__contains__(playerResponse.lower()):
        print(f'{playerResponse.lower()} has already been said!')
      print('I win!\n')
      break
    currentLetter += 1;
    if currentLetter == len(theAlphabet):
      currentLetter = 0