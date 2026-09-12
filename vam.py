import numpy as np

# Transportation cost table
cost = np.array([
    [10, 2, 20, 11],
    [12, 7,  9, 20],
    [ 4,14, 16, 18]
], dtype=float)

supply = [15, 25, 10]
demand = [5, 15, 15, 15]

allocation = np.zeros((3, 4))

supply = supply.copy()
demand = demand.copy()

while sum(supply) > 0 and sum(demand) > 0:

    row_penalty = []

    for i in range(3):
        if supply[i] > 0:
            values = []

            for j in range(4):
                if demand[j] > 0:
                    values.append(cost[i][j])

            values.sort()

            if len(values) >= 2:
                penalty = values[1] - values[0]
            else:
                penalty = values[0]

            row_penalty.append(penalty)
        else:
            row_penalty.append(-1)

    col_penalty = []

    for j in range(4):
        if demand[j] > 0:
            values = []

            for i in range(3):
                if supply[i] > 0:
                    values.append(cost[i][j])

            values.sort()

            if len(values) >= 2:
                penalty = values[1] - values[0]
            else:
                penalty = values[0]

            col_penalty.append(penalty)
        else:
            col_penalty.append(-1)

    # Find largest penalty
    max_row = max(row_penalty)
    max_col = max(col_penalty)

    if max_row >= max_col:

        i = row_penalty.index(max_row)

        # Find cheapest cell in selected row
        cheapest = 999999
        j = -1

        for col in range(4):
            if demand[col] > 0 and cost[i][col] < cheapest:
                cheapest = cost[i][col]
                j = col

    else:

        j = col_penalty.index(max_col)

        # Find cheapest cell in selected column
        cheapest = 999999
        i = -1

        for row in range(3):
            if supply[row] > 0 and cost[row][j] < cheapest:
                cheapest = cost[row][j]
                i = row

    # Allocate as much as possible
    amount = min(supply[i], demand[j])

    allocation[i][j] = amount

    supply[i] -= amount
    demand[j] -= amount


# Calculate transportation cost
total_cost = 0

for i in range(3):
    for j in range(4):
        total_cost += allocation[i][j] * cost[i][j]


print("VAM Allocation:")
print(allocation)

print("\nInitial Transportation Cost =", total_cost)
