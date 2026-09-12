# MODI Method

cost = [
    [2, 3, 1],
    [5, 4, 8],
    [5, 6, 8]
]

allocation = [
    [0, 0, 180],
    [30, 120, 0],
    [70, 0, 30]
]

rows = 3
cols = 3

# Find initial total cost
total_cost = 0

for i in range(rows):
    for j in range(cols):
        total_cost += allocation[i][j] * cost[i][j]

print("Initial Transportation Cost =", total_cost)

# Find u and v values
u = [None] * rows
v = [None] * cols

u[0] = 0

changed = True

while changed:
    changed = False

    for i in range(rows):
        for j in range(cols):

            if allocation[i][j] > 0:

                if u[i] is not None and v[j] is None:
                    v[j] = cost[i][j] - u[i]
                    changed = True

                elif v[j] is not None and u[i] is None:
                    u[i] = cost[i][j] - v[j]
                    changed = True

print("\nu values =", u)
print("v values =", v)

# Calculate opportunity costs
print("\nOpportunity Costs:")

optimal = True

for i in range(rows):
    for j in range(cols):

        if allocation[i][j] == 0:

            opportunity = cost[i][j] - (u[i] + v[j])

            print("Cell", i + 1, j + 1, "=", opportunity)

            if opportunity < 0:
                optimal = False

# Check optimality
if optimal:
    print("\nThe solution is optimal.")
    print("Minimum Transportation Cost =", total_cost)
else:
    print("\nThe solution is not optimal.")