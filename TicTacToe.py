import random
from BattleShip import printoutListList

def attemptPlayerMove(move):
  verticalList = ['top', 'middle', 'bottom']
  horizontalList = ['right', 'middle', 'left']
  if not move.__contains__('-'):
    return False
  splitword = move.split('-')
  if len(splitword) != 2:
    return False
  elif not verticalList.__contains__(splitword[0].lower()):
    return False
  elif not horizontalList.__contains__(splitword[1].lower()):
    return False
  else:
    return True

#main code that fails this program (remove tictactoe)
def getplace(board, symbol):
  opponentsymbol = ''
  if symbol == 'O':
    opponentsymbol = 'X'
  else:
    opponentsymbol = 'O'
  freespace = []
  opponentspace = []
  myspace = []
  for y in range(3):
    for x in range(3):
      if board[y][x] == symbol:
        myspace.append([y, x])
      elif board[y][x] == opponentsymbol:
        opponentspace.append([y, x])
      elif board[y][x] == '.':
        freespace.append([y, x])

  bestspace = opponentspace[0]
  skip = 0
  #i[0] = y, i[1] = x
  while opponentspace.__contains__(bestspace) or myspace.__contains__(bestspace):
    #rule 1, if you can win, win
    for i in myspace:
      if myspace.__contains__([i[0] - 1, i[1]]) and skip <= 0:
        if i[0] == 1:
          bestspace = [i[0] + 1, i[1]]
        else:
          bestspace = [i[0] - 2, i[1]]
        if opponentspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
          skip = 1;
      elif myspace.__contains__([i[0], i[1] + 1]) and skip <= 1:
        if i[1] == 1:
          bestspace = [i[0], i[1] - 1]
        else:
          bestspace = [i[0], i[1] + 2]
        if opponentspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
          skip = 2;
      elif myspace.__contains__([i[0] + 1, i[1]]) and skip <= 2:
        if i[0] == 1:
          return [i[0] - 1, i[1]]
        else:
          return [i[0] + 2, i[1]]
        if opponentspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
          skip = 3;
      elif myspace.__contains__([i[0], i[1] + 1]) and skip <= 3:
        if i[1] == 1:
          bestspace = [i[0], i[1] - 1]
        else:
          bestspace = [i[0], i[1] + 2]
        if opponentspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
          skip = 4;
      elif myspace.__contains__([i[0] - 1, i[1] - 1]) and skip <= 4:
        if i[1] == 2:
          skip = 5
        else:
          if i[0] == 1:
            bestspace = [i[0] + 1,i[1] + 1]
          else:
            bestspace = [i[0] - 2,i[1] - 2]
          if opponentspace.__contains__(bestspace):
            skip = 5
      elif myspace.__contains__([i[0] - 1, i[1] + 1]) and skip <= 5:
        if i[1] == 0:
          skip = 6
        else:
          if i[0] == 1:
            bestspace = [i[0] + 1, i[1] - 1]
          else:
            bestspace = [i[0] - 2,i[1] + 2]
          if opponentspace.__contains__(bestspace):
            skip = 6
      elif myspace.__contains__([i[0] + 1, i[1] - 1]) and skip <= 6:
        if i[1] == 2:
          skip = 7
        else:
          if i[0] == 1:
            bestspace = [i[0] - 1,i[1] + 1]
          else:
            bestspace = [i[0] + 2,i[1] - 2]
          if opponentspace.__contains__(bestspace):
            skip = 7
      elif myspace.__contains__([i[0] + 1, i[1] + 1]) and skip <= 7:
        if i[1] == 0:
          skip = 8
        else:
          if i[0] == 1:
            bestspace = [i[0] - 1,i[1] - 1]
          else:
            bestspace = [i[0] + 2,i[1] + 2]
          if opponentspace.__contains__(bestspace):
            skip = 8
    #rule 2, if the opponent can win, stop them
    if skip > 7:
      for i in opponentspace:
        if opponentspace.__contains__([i[0] - 1, i[1]]) and skip <= 8:
          if i[0] == 1:
            bestspace = [i[0] + 1, i[1]]
          else:
            bestspace = [i[0] - 2, i[1]]
          if myspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
            skip = 9;
        elif opponentspace.__contains__([i[0], i[1] + 1]) and skip <= 9:
          if i[1] == 1:
            bestspace = [i[0], i[1] - 1]
          else:
            bestspace = [i[0], i[1] + 2]
          if myspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
            skip = 10;
        elif opponentspace.__contains__([i[0] + 1, i[1]]) and skip <= 10:
          if i[0] == 1:
            return [i[0] - 1, i[1]]
          else:
            return [i[0] + 2, i[1]]
          if myspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
            skip = 11;
        elif opponentspace.__contains__([i[0], i[1] + 1]) and skip <= 11:
          if i[1] == 1:
            bestspace = [i[0], i[1] - 1]
          else:
            bestspace = [i[0], i[1] + 2]
          if myspace.__contains__(bestspace) or bestspace[0] < 0 or bestspace[1] < 0 or bestspace[0] > 2 or bestspace[1] > 2:
            skip = 12;
        elif opponentspace.__contains__([i[0] - 1, i[1] - 1]) and skip <= 12:
          if i[1] == 2:
            skip = 13
          else:
            if i[0] == 1:
              bestspace = [i[0] + 1,i[1] + 1]
            else:
              bestspace = [i[0] - 2,i[1] - 2]
            if myspace.__contains__(bestspace):
              skip = 13
        elif opponentspace.__contains__([i[0] - 1, i[1] + 1]) and skip <= 13:
          if i[1] == 0:
            skip = 14
          else:
            if i[0] == 1:
              bestspace = [i[0] + 1, i[1] - 1]
            else:
              bestspace = [i[0] - 2,i[1] + 2]
            if myspace.__contains__(bestspace):
              skip = 14
        elif opponentspace.__contains__([i[0] + 1, i[1] - 1]) and skip <= 14:
          if i[1] == 2:
            skip = 15
          else:
            if i[0] == 1:
              bestspace = [i[0] - 1,i[1] + 1]
            else:
              bestspace = [i[0] + 2,i[1] - 2]
            if myspace.__contains__(bestspace):
              skip = 15
        elif opponentspace.__contains__([i[0] + 1, i[1] + 1]) and skip <= 15:
          if i[1] == 0:
            skip = 16
          else:
            if i[0] == 1:
              bestspace = [i[0] - 1,i[1] - 1]
            else:
              bestspace = [i[0] + 2,i[1] + 2]
            if myspace.__contains__(bestspace):
              skip = 16
    # #rule 3, if theres a space available next my own, take it
    if skip > 15:
      for i in myspace:
        if freespace.__contains__(i[0] - 1 , i[1]):
          bestspace = [i[0] - 1, i[1]]
        elif freespace.__contains__(i[0], i[1] + 1):
          bestspace = [i[0], i[1] + 1]
        elif freespace.__contains__(i[0], i[1] - 1):
          bestspace = [i[0], i[1] - 1]
        elif freespace.__contains__(i[0] + 1, i[1]):
          bestspace = [i[0] + 1, i[1]]
        elif freespace.__contains__(i[0] - 1, i[1] - 1):
          bestspace = [i[0] - 1, i[1] - 1]
        elif freespace.__contains__(i[0] - 1, i[1] + 1):
          bestspace = [i[0] - 1, i[1] + 1]
        elif freespace.__contains__(i[0] + 1, i[1] - 1):
          bestspace = [i[0] + 1, i[1] - 1]
        elif freespace.__contains__(i[0] + 1, i[1] + 1):
          bestspace = [i[0] + 1, i[1] + 1]
    #rule 4, if none of the other 3 work, pick a random spot
    if len(myspace) == 0:
      bestspace = random.choice(freespace)
  return bestspace
def tictactoe():
    gameboard = [
      ['.', '.', '.'],
      ['.', '.', '.'],
      ['.', '.', '.']
    ]
    reply = ''
    while reply.lower() != 'x' and reply.lower() != 'o':
        reply = input('okay, would you like \'X\'s or \'O\'s\n')
        if reply.lower() != 'x' and reply.lower() != 'o':
            print('that\'s not an X or O\n')
    playersymbol = reply.upper()
    compsymbol = ''
    if playersymbol == 'X':
        compsymbol = 'O'
    else:
        compsymbol = 'X'
    print('\ngame board:')
    printoutListList(gameboard)
    verticalList = ['top', 'middle', 'bottom']
    horizontalList = ['left', 'middle', 'right']
    compWin = False
    playerWin = False
    reply = ''
    skip = False
    while not (compWin) and not (playerWin):
      skip = False
      reply = input(
            f'tell me where you want to place your {playersymbol}, {random.choice(verticalList).capitalize()}-{random.choice(horizontalList)}, {random.choice(verticalList).capitalize()}-{random.choice(horizontalList)}, etc.\n')
      if not attemptPlayerMove(reply):
        print('no that\'s not right.\n')
        skip = True
      else:
        splitword = reply.split('-')
        gameboard[verticalList.index(splitword[0].lower())][horizontalList.index(splitword[1].lower())] = playersymbol
      if not skip:
        print()
        printoutListList(gameboard)
        print('my turn!')
        placement = getplace(gameboard,compsymbol)
        gameboard[placement[0]][placement[1]] = compsymbol
        printoutListList(gameboard)
