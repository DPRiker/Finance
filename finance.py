
print("Enter amount of money in uah")
income = int(input('Income: '))

print("Enter amount of you want to save from this income in %")
savings = income * (float(input('Amount: '))/100)

#print("Now let's add planed big expenses for this month or tap next to continue calculations")
while str(input("Now let's add planed big expenses for this month or tap stop to continue calculations ")) != "stop":
    expenses = int(input('Expense: '))
    income -= expenses


money = income
mainPart = money * .55
tensPart = money * .1
forPresents = money * .05

print(f'For this month you have such amount of operation money - {money}')
print(f'For live and main expenses: {mainPart} uah')
print(f'For education and fun: {tensPart} uah')
print(f'For save and invest: {tensPart} uah')
print(f'For presents and philantropy: {forPresents} uah')
print(f'In this month you will save : {savings} uah or in a year it will be {savings * 12} uah')
