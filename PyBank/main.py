import csv
import os

budget_data_path = "Resources/budget_data.csv"

date = []
profit_losses = []

with open(budget_data_path, newline="", encoding="utf8") as budget_data:
	csvreader = csv.reader(budget_data, delimiter=",")
	next(budget_data)
	for row in csvreader:

		date.append(str(row[0]))

		profit_losses.append(int(row[1]))
		#i is the variable for the list that steps through and subtracts the next value from the previous
		i = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]

profit_losses_sum = sum(profit_losses)
profit_losses_average = sum(i) / len(i)

print("Financial Analysis")
print("-----------------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${profit_losses_sum}')
print(f'Average Change: ${profit_losses_average:.2f}')
print(f'Greatest Increase in Profits: ${max(i)}')
print(f'Greatest Decrease in Profits: ${min(i)}')