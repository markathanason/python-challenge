import csv

election_data_path = "Resources/election_data.csv"

manifest = []
individual = []
vote_count = []
vote_percent =[]
count = 0

with open(election_data_path, newline="", encoding="utf8") as election_data:
	csvreader = csv.reader(election_data, delimiter=",")
	next(csvreader)
	for row in csvreader:
		count = count+1
		manifest.append(row[2])
	for i in list(sorted(set(manifest), key=manifest.index)):
		individual.append(i)
		j = manifest.count(i)
		vote_count.append(j)
		k = (j/count)*100
		vote_percent.append(k)

	winner_count = max(vote_count)
	w = individual[vote_count.index(winner_count)]

with open('Resources/output.txt', 'w') as output:
	print("-----------------------", file=output)
	print("Election Results", file=output)   
	print("-----------------------", file=output)
	print(f'Total Votes : {str(count)}', file=output)  
	print("-----------------------", file=output)
	for i in range(len(individual)):
		print(f'{individual[i]} : %{vote_percent[i]:.3f} {vote_count[i]}', file=output)
	print("-----------------------", file=output)
	print(f'The winner is: {w}', file=output)
	print("-----------------------", file=output)


print("-----------------------")
print("Election Results")   
print("-----------------------")
print(f'Total Votes : {str(count)}')    
print("-----------------------")
for i in range(len(individual)):
	print(f'{individual[i]} : %{vote_percent[i]:.3f} {vote_count[i]}')
print("-----------------------")
print(f'The winner is: {w}')
print("-----------------------")