set = {1, 2, 4, 6, 8, 10}
for i in range(1, 11):
    if i not in set:
        print(i)

print("----------------")

prices = {"Pen": 10, "Book": 50, "Pencil": 5}

for item in prices:
    prices[item] = prices[item] * 1.10

print(prices)

print("----------------")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.copy()
result.update(set2)

print(result)

print("----------------")
