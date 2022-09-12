import random
from abcGame import abcGame
from Hangman import hangman
from BattleShip import battleship
#from TicTacToe import tictactoe

#all list types
positiveWords = ['good', 'great', 'awsome', 'wonderful', 'ok', 'okay', 'alright', 'fine', 'well']
returnMoodWords = ['and you', 'how about you', 'doing well?', 'you?']
negativeWords = ['horribly', 'horrible', 'bad', 'awful', 'rough','not very good', 'not good', 'not doing well', 'not feeling', 'not great', 'not really great', 'not ok', 'not okay', 'not alright', 'not fine']
agreeWords = ['yes', 'yeah', 'sure', 'yep', 'you bet', 'absolutely']
stopWords = ['no', 'done', 'stop', 'fine']

  
def hasWord(string, wordlist):
  for i in range(len(wordlist)):
    if string.lower().__contains__(wordlist[i].lower()):
      return True;
  return False;


#code starts here
reply = input('Hi, how are you?\n')

if hasWord(reply,positiveWords) and not(hasWord(reply,negativeWords)):
  if hasWord(reply,returnMoodWords):
    print("that's great, i'm doing fine, thanks for asking!")
  else:
    print ("that's great!")
elif hasWord(reply,negativeWords):
  print('aw that\'s a shame :(\nI have an idea!\n\nhow about an inspirational quote to lift your spirits? :)')
  reply = 'sure'
  while hasWord(reply,agreeWords):
    #https://www.shopify.com/blog/motivational-quotes
    listOfQuotes = ['"Success is not final; failure is not fatal: It is the courage to continue that counts." — Winston S. Churchill', '"It is better to fail in originality than to succeed in imitation." — Herman Melville', '"The road to success and the road to failure are almost exactly the same." — Colin R. Davis', '“Success usually comes to those who are too busy looking for it.” — Henry David Thoreau', '“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” —Dale Carnegie', '"Nothing in the world can take the place of Persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan \'Press On\' has solved and always will solve the problems of the human race." —Calvin Coolidge', '“There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind.” —Mister Rogers', '“Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.” —John Wooden', '“I never dreamed about success. I worked for it.” —Estée Lauder', '“Success is getting what you want, happiness is wanting what you get.” ―W. P. Kinsella']
    quoteToGive = random.choice(listOfQuotes)
    print(quoteToGive)
    reply = input('\ndid that help you feel better?\n')
    if reply.lower().__contains__('no') or hasWord(reply, negativeWords):
      reply = input('aw, would you like another one?\n')
      if hasWord(reply, agreeWords):
        print()
      elif hasWord(reply,negativeWords) or reply.lower().__contains__('no'):
        print('welp, I hope you feel better.\n')
        break
      else:
        print('...')
        input()
        reply = 'sure'
    elif not hasWord(reply, agreeWords):
      print('...')
      input()
      reply = 'sure'
    else:
      print('that\'s great!\n')
      break
else:
  print(f'umm. I dont know what you mean by "{reply}" but how about something else? oh I know!')

print("how about a game!\n")
reply = ''
games = ['battleship', 'hangman', 'abcgame']
counter = 0
again = ''
while (not hasWord(reply, games)) or reply.lower().__contains__('no'):
  if again == '':
    reply = input("would you like to play 'battleship', 'hangman', or the 'abcgame'?\n")
  else:
    reply = again
  if reply.lower().__contains__('battleship'):
    again = ''
    print()
    battleship()
    counter = 0
    print('that was fun!')
    reply = input('would you like to play again?\n')
    if hasWord(reply, agreeWords):
      again = 'battleship'
  elif reply.lower().__contains__('hangman'):
    again = ''
    print()
    hangman()
    counter = 0
    print('that was fun!')
    reply = input('would you like to play again?\n')
    if hasWord(reply, agreeWords):
      again = 'hangman'
  # elif reply.lower().__contains__('tic'): #we don't talk about this...
  #   again = ''
  #   print()
  #   tictactoe()
  #   counter = 0
  #   print('that was fun!')
  #   reply = input('would you like to play again?\n')
  #   if hasWord(reply, agreeWords):
  #     again = 'tic'
  elif reply.lower().__contains__('abc'):
    again = ''
    print()
    abcGame()
    counter = 0
    print('that was fun!')
    reply = input('would you like to play again?\n')
    if hasWord(reply, agreeWords):
      again = 'abc'
  elif hasWord(reply, stopWords):
    print('okay, that\'s understandable.\n\nhave a nice day!')
    break
  else:
    print()
    if counter == 0:
      print('?\nlet me ask again\n')
    elif counter == 1:
      print('...')
      input()
      print('are you ok?')
      input()
      print('okay let me ask again\n')
    elif counter == 2:
      print('alright I\'m starting to get frustrated, so let me ask you one more time\n')
    elif counter == 3:
      print('I\'m done. I\'ve got better things to do and better people to talk to.\n\nGOODBYE')
      break
    counter += 1