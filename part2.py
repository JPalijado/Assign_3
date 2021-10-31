def inputNumApple():
    numApple = int(input("How many apples you want to buy? "))
    return numApple

def inputNumOrange():
    numOrange = int(input("How many orange you want to buy? "))
    return numOrange

def computePriceApple(numApple):
    priceApple = numApple * 20
    return priceApple

def computePriceOrange(numOrange):
    priceOrange = numOrange * 25
    return priceOrange

def computeTotalPrice(priceApple, priceOrange):
    total = priceApple + priceOrange
    return total

def displayOutput(total):
    print(f"The total amout is {total:.2f}.")

numApple = inputNumApple()
numOrange = inputNumOrange()

priceApple = computePriceApple(numApple)
priceOrange = computePriceOrange(numOrange)
total = computeTotalPrice(priceApple, priceOrange)

displayOutput(total)