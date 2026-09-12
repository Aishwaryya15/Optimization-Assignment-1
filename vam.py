# Vogel's Approximation Method

cost = [
    [2, 3, 1],
    [5, 4, 8],
    [5, 6, 8]
]

supply = [180, 150, 100]
demand = [100, 120, 210]

rows = len(supply)
cols = len(demand)

allocation = [[0 for j in range(cols)] for i in range(rows)]

while True:

    # Check if all supply and demand are completed
    if sum(supply) == 0 and sum(demand) == 0:
        break

    row_penalty = [-1] * rows
    col_penalty = [-1] * cols

    # Row penalties
    for i in range(rows):
        if supply[i] > 0:
            values = []

            for j in range(cols):
                if demand[j] > 0:
                    values.append(cost[i][j])

            if len(values) >= 2:
                values.sort()
                row_penalty[i] = values[1] - values[0]
            elif len(values) == 1:
                row_penalty[i] = values[0]

    # Column penalties
    for j in range(cols):
        if demand[j] > 0:
            values = []

            for i in range(rows):
                if supply[i] > 0:
                    values.append(cost[i][j])

            if len(values) >= 2:
                values.sort()
                col_penalty[j] = values[1] - values[0]
            elif len(values) == 1:
                col_penalty[j] = values[0]

    # Find largest penalty
    max_row = max(row_penalty)
    max_col = max(col_penalty)

    if max_row >= max_col:

        i = row_penalty.index(max_row)

        j = -1
        minimum = float("inf")

        for k in range(cols):
            if demand[k] > 0 and cost[i][k] < minimum:
                minimum = cost[i][k]
                j = k

    else:

        j = col_penalty.index(max_col)

        i = -1
        minimum = float("inf")

        for k in range(rows):
            if supply[k] > 0 and cost[k][j] < minimum:
                minimum = cost[k][j]
                i = k

    # Allocate as much as possible
    amount = min(supply[i], demand[j])

    allocation[i][j] += amount

    supply[i] -= amount
    demand[j] -= amount

# Calculate total cost
total_cost = 0

for i in range(rows):
    for j in range(cols):
        total_cost += allocation[i][j] * cost[i][j]

print("\nVogel's Approximation Method")
print("-----------------------------")

print("\nAllocation Table:")

for i in range(rows):
    print(allocation[i])

print("\nTotal Transportation Cost =", total_cost)