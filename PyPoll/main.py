import csv
import os

poll_data_path = "Resources/election_data.csv"

total_votes = []
khan_votes = []
correy_votes = []
li_votes = []
tooley_votes = []

with open(poll_data_path, newline="", encoding="utf8") as poll_data:
	csvreader = csv.reader(poll_data, delimiter=",")
	next(poll_data)
	for row in csvreader:

		total_votes.append(row[0])

print("Election Results")
print("-------------------------")
print(f'Total Votes: {len(total_votes)}')