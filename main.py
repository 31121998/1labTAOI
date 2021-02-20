from apyori import apriori
import csv

def keyFunc(item):
    return item[1]

filename = "baskets.csv"
transactions = []
with open(filename, 'r', newline='') as file:
    read = csv.reader(file)
    for lines in read:
        transactions.append(lines)

results = list(apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 4, min_length = 2))

results.sort(key=keyFunc)
for line in results:
    print(line)



