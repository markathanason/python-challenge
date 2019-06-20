import csv
budget_data_path = "Resources/budget_data.csv"

date = []
money = []

with open(budget_data_path, newline="", encoding="utf8") as budget_data:
	csvreader = csv.reader(budget_data, delimiter=",")
	next(csvreader)
	for row in csvreader:
		date.append(str(row[0]))
		money.append(int(row[1]))
#iterates through and adds the 2nd value to the previous
i = [money[i+1] - money[i] for i in range(len(money)-1)]

zipped = zip(date[1::], i[::])
zipped_list = list(zipped)

profit_sum = sum(money)
profit_average = sum(i) / len(i)

increase = max(i)
decrease = min(i)

for row in zipped_list:
	if row[1] == increase:
		month_inc = row[0]
	if row[1] == decrease:
		month_dec = row[0]

with open('Resources/output.txt', 'w') as text_file:
	print(f'Financial Analysis', file=text_file)
	print(f'-----------------------------------', file=text_file)
	print(f'Total Months: {len(date)}', file=text_file)
	print(f'Total: ${profit_sum}', file=text_file)
	print(f'Average Change: ${profit_average:.2f}', file=text_file)
	print(f'Greatest Increase in Profits: {month_inc} ({increase})', file=text_file)
	print(f'Greatest Decrease in Profits: {month_dec} ({decrease})', file=text_file)

print("Financial Analysis")
print("-----------------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${profit_sum}')
print(f'Average Change: ${profit_average:.2f}')
print(f'Greatest Increase in Profits: {month_inc} ({increase})')
print(f'Greatest Decrease in Profits: {month_dec} ({decrease})')