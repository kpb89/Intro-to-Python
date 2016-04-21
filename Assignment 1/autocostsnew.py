def getAmount(expense):
    return float(input("Enter the amount you pay for " + expense + " in the form xx.yy"))

def getTimes():
    return float(input("Now please enter the number of times per year this cost is incurred."))

def main():
    expenses = ['rent','cable','electric','parking', 'credit card', 'food', 'gas']
    annualCosts = 0
    for exp in expenses:
        annualCosts += getAmount(exp) *getTimes()

    print("Your total monthly cost is $",format(annualCosts / 12,",.2f"),sep = " ")
    print("Your total annual cost is $",format(annualCosts,",.2f"),sep = " ")

main()

    

