mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100
totalCost = mealCost + tip + tax
print("The total meal cost is " + str(round(totalCost)) + " dollars.")
