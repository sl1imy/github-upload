import random
import itertools

numbersAvailable = ["1","2","3","4","5","6","7","8","9"]

def printAscii():
  print("   +--------------+")
  print("  /|             /|")
  print(" / |            / |")
  print("*--+-----------*  |")
  print("|  |           |  |")
  print("|  |           |  |")
  print("|  |           |  |")
  print("|  +-----------+--+")
  print("| /            | /")
  print("|/             |/")
  print("*--------------*")
  

def checkMoves(box,target):
    valid = False
    for i in range(len(box)+1):
        for j in itertools.combinations(box,i):
            if sum(j) == target:
                valid = True
    return valid

def diceRoll(box):
    if 7 in box or 8 in box or 9 in box:
        first = random.randint(1,6)
        second = random.randint(1,6)
    else:
        print("Do you want to roll 1 dice or 2? (1/2): ")
        dice = int(input())
        if dice == 2:
          first = random.randint(1,6)
          second = random.randint(1,6)
        else:
          first = random.randint(1,6)
          second = 0
    return [first,second]



def getInput(number, target, box, nums):
  while True:
    print("")
    print(f"Enter Number {number}: ")
    num = input()
    if num not in numbersAvailable:
      print("Please enter a number from 1-9")
      continue
    else:
      num = int(num)
      valid = True
      if num not in box or num > target or sum(nums) + num > target or num in nums:
        print("Number not available")
        valid = False
      return [int(num),valid]


def turn (player):
  box = [1,2,3,4,5,6,7,8,9]
  possibleToPlay = True
  while possibleToPlay == True:
    print()
    dice = diceRoll(box)
    die1 = dice[0]
    die2 = dice[1]
    if die1 > 0:
      print(f"First dice: {die1}")
    if die2 > 0:
      print(f"Second dice: {die2}")
    target = dice[0] + dice[1]
    if checkMoves(box,target) == False:
      possibleToPlay = False
      while True:
        again = input("You lose! Would you like to play again? (y/n): ")
        if again == "y":
          turn("lewis")
        elif again == "n":
          exit()
        else:
          print("Please enter either 'y' or 'n'")
          continue
    print(f"Numbers left {box}")
    nums = []
    number = 1
    while sum(nums) < target:
      print(f"Numbers left {box}")
      num = getInput(number,target,box,nums)
      if num[1] == True:
        box.remove(num[0])
        number = number + 1
        nums.append(num[0])


def begin():
  name = input("What is your name? ")
  print(f"Welcome {name} to shut the box!")
  print("")
  printAscii()
  print("")
  turn(name)

begin()









import random
import itertools

numbersAvailable = ["1","2","3","4","5","6","7","8","9"]

def printAscii():
  print("   +--------------+")
  print("  /|             /|")
  print(" / |            / |")
  print("*--+-----------*  |")
  print("|  |           |  |")
  print("|  |           |  |")
  print("|  |           |  |")
  print("|  +-----------+--+")
  print("| /            | /")
  print("|/             |/")
  print("*--------------*")
  

def checkMoves(box,target):
    valid = False
    for i in range(len(box)+1):
        for j in itertools.combinations(box,i):
            if sum(j) == target:
                valid = True
    return valid

def diceRoll(box):
    if 7 in box or 8 in box or 9 in box:
        first = random.randint(1,6)
        second = random.randint(1,6)
    else:
        print("Do you want to roll 1 dice or 2? (1/2): ")
        dice = int(input())
        if dice == 2:
          first = random.randint(1,6)
          second = random.randint(1,6)
        else:
          first = random.randint(1,6)
          second = 0
    return [first,second]



def getInput(number, target, box, nums):
  while True:
    print("")
    print(f"Enter Number {number}: ")
    num = input()
    if num not in numbersAvailable:
      print("Please enter a number from 1-9")
      continue
    else:
      num = int(num)
      valid = True
      if num not in box or num > target or sum(nums) + num > target or num in nums:
        print("Number not available")
        valid = False
      return [int(num),valid]


def turn (player):
  box = [1,2,3,4,5,6,7,8,9]
  possibleToPlay = True
  while possibleToPlay == True:
    print()
    dice = diceRoll(box)
    die1 = dice[0]
    die2 = dice[1]
    if die1 > 0:
      print(f"First dice: {die1}")
    if die2 > 0:
      print(f"Second dice: {die2}")
    target = dice[0] + dice[1]
    if checkMoves(box,target) == False:
      possibleToPlay = False
      while True:
        again = input("You lose! Would you like to play again? (y/n): ")
        if again == "y":
          turn("lewis")
        elif again == "n":
          exit()
        else:
          print("Please enter either 'y' or 'n'")
          continue
    print(f"Numbers left {box}")
    nums = []
    number = 1
    while sum(nums) < target:
      print(f"Numbers left {box}")
      num = getInput(number,target,box,nums)
      if num[1] == True:
        box.remove(num[0])
        number = number + 1
        nums.append(num[0])


def begin():
  name = input("What is your name? ")
  print(f"Welcome {name} to shut the box!")
  print("")
  printAscii()
  print("")
  turn(name)

begin()
