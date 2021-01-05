from datetime import date

print("Enter amount of money in uah")
while True:
    try:
        income = int(input('Income: '))
    except:
        print('value should be int')
        continue
    else: 
       break 

print("Enter amount of you want to save from this income in %")
savings = income * (float(input('Amount: '))/100)

plannedExpences = {}
#print("Now let's add planed big expenses for this month or tap next to continue calculations")
str(input("Now let's add planed big expenses for this month or tap stop to see the results"))
while True:
    expenseName = str(input('Name of the expense: '))
    if expenseName == "stop":
        break
    expenses = int(input('Expense: '))
    plannedExpences[expenseName] = expenses
    income -= expenses
    if income < 0:
        print('sorry to much expenses')
        break 


money = income
mainPart = "{:.2f}".format(money * .55)
tensPart = "{:.2f}".format(money * .1)
forPresents = "{:.2f}".format(money * .05)

txtFile= open(f"finance{date.today()}.txt","w+")

txtFile.write(f'For this month you have such amount of operation money : {money} \n') 
txtFile.write(f'For live and main expenses: {mainPart} uah \n')
txtFile.write(f'For education and fun: {tensPart} uah \n')
txtFile.write(f'For save and invest: {tensPart} uah \n')
txtFile.write(f'For presents and philantropy: {forPresents} uah \n')
txtFile.write(f'In this month you will save : {savings} uah or in a year it will be {savings * 12} uah \n')
for k in plannedExpences.keys():
    txtFile.write("{}:{}\n".format(k, plannedExpences[k]))
txtFile.close()