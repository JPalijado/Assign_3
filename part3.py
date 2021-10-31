import math
def getMoney():
    money = float(input("Enter the amount of money you have: P"))
    return money

def inputPrice():
    applePrice = float(input("What is the price of an apple? P"))
    return applePrice

def computeAppleNumber(money, applePrice):
    numApple = (money) // (applePrice)
    wNumApple = math.trunc(numApple)
    return wNumApple

def computeChange(money, applePrice):
    change = (money) % (applePrice)
    return change

def displayOutput(wNumApple, change):
    print(f"You can buy {wNumApple} apples and your change is {change:.2f} pesos.")

money = getMoney()
applePrice = inputPrice()

wNumApple = computeAppleNumber(money, applePrice)
change = computeChange(money, applePrice)

displayOutput(wNumApple,change)

