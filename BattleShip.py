import random

def hasWord(string, wordlist):
  for i in range(len(wordlist)):
    if string.lower().__contains__(wordlist[i].lower()):
      return True;
  return False;

def printoutListList(listlist):
  for i in listlist:
    for x in i:
      print(x, end = ' ')
    print()
  print()

def listlistCount(listlist, subject):
  total = 0
  for x in listlist:
    total += x.count(subject)
  return total

def printboard(board):
  quickalphabet = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
  for x in quickalphabet:
    print(x, end = ' ')
  print()
  for x in range(len(board)):
    print(x + 1, end = ' ')
    for i in board[x]:
      print(i, end = ' ')
    print()

def inputShipCoords(prompt):
  reply = ''
  acceptedletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  acceptednumbers = ['1', '2', '3', '4', '5', '6', '7']
  while True:
    reply = input(prompt)
    if len(reply) == 0:
      print('that\'s not a ship placement\n')
      reply = ''
    elif len(reply) != 2:
      print('that\'s not a ship placement\n')
      reply = ''
    elif not hasWord(reply[0].upper(), acceptedletters):
      print('that\'s not a ship placement\n')
      reply = ''
    elif not hasWord(reply[1], acceptednumbers):
      print('that\'s not a ship placement\n')
      reply = ''
    else:
      break
  print()
  return reply

def battleship():
  playerboard = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],]
  computerboard = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],]
  computerboardvisual = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],]
  #upping this number increases how many ships each side has
  totalshipcount = 3
  playerships = 0
  computerships = totalshipcount
  while listlistCount(computerboard, 'O') < totalshipcount:
    computerboard[random.randint(0,6)][random.randint(0,6)] = 'O'
  letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
  numbers = ['1', '2', '3', '4', '5', '6', '7']
  while playerships < totalshipcount:
    reply = ''
    print('your board:\n')
    printboard(playerboard)
    print()
    reply = inputShipCoords('where would you like a ship to go?\n')
    if not playerboard[numbers.index(reply[1])][letters.index(reply[0].upper())] == 'O':
      playerboard[numbers.index(reply[1])][letters.index(reply[0].upper())] = 'O'
      playerships += 1
    else:
      print('there\'s already a ship there')
  printboard(playerboard)
  print('\nready?')
  input()
  reply = ''
  while playerships > 0 and computerships > 0:
    loop = True
    while loop and computerships != 0 and playerships != 0:
      print('your board:')
      printboard(playerboard)
      print('\n---------------\n')
      print('my board:')
      printboard(computerboardvisual)
      print ('your turn!')
      reply = inputShipCoords('where do you want to aim?\n')
      if computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] == '_' or computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] == 'X':
        while computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] == '_' or computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] == 'X':
          print('you\'ve already shot there!')
          reply = inputShipCoords('where do you want to aim?\n')
      if computerboard[numbers.index(reply[1])][letters.index(reply[0].upper())] == 'O':
        computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] = 'X'
        computerships -= 1
      else:
        computerboardvisual[numbers.index(reply[1])][letters.index(reply[0].upper())] = '_'
        loop = False

    loop = True
    while loop and computerships != 0 and playerships != 0:
      print('your board:')
      printboard(playerboard)
      print('\n---------------\n')
      print('my board:')
      printboard(computerboardvisual)
      print ('my turn!')
      input('\n')
      compRow = random.randint(0,6)
      compCol = random.randint(0,6)
      if playerboard[compRow][compCol] == '_' or playerboard[compRow][compCol] == 'X':
        while playerboard[compRow][compCol] == '_' or playerboard[compRow][compCol] == 'X':
          compRow = random.randint(0,6)
          compCol = random.randint(0,6)
      if playerboard[compRow][compCol] == 'O':
        playerboard[compRow][compCol] = 'X'
        playerships -= 1
      else:
        playerboard[compRow][compCol] = '_'
        loop = False

  if playerships == 0:
    for x in range(7):
      for y in range(7):
        if computerboard[x][y] == 'O' and computerboardvisual[x][y] != 'X':
          computerboardvisual[x][y] = 'O'
  print('your board:')
  printboard(playerboard)
  print('\n---------------\n')
  print('my board:')
  printboard(computerboardvisual)
  if playerships == 0:
    print('\nI win!', end = ' ')
  elif computerships == 0:
    print('\ncongrats you win!', end = ' ')
  input()
    