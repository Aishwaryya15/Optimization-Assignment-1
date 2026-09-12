import numpy as np

# Transportation cost table
cost = np.array([
    [10, 2, 20, 11],
    [12, 7,  9, 20],
    [ 4,14, 16, 18]
], dtype=float)

# Final allocation obtained after MODI improvement
allocation = np.array([
    [0,  5,  0, 10],
    [0, 10, 15,  0],
    [5,  0,  0,  5]
], dtype=float)

rows = 3
cols = 4

# Calculate initial transportation cost
total_cost = 0

for i in range(rows):
    for j in range(cols):
        total_cost += allocation[i][j] * cost[i][j]

print("Initial VAM Cost = 475")
print("Starting MODI Method...")
print()

# Find occupied cells
occupied = []

for i in range(rows):
    for j in range(cols):
        if allocation[i][j] > 0:
            occupied.append((i, j))

# Calculate u and v values
u = [None] * rows
v = [None] * cols

u[0] = 0

changed = True

while changed:
    changed = False

    for i, j in occupied:

        if u[i] is not None and v[j] is None:
            v[j] = cost[i][j] - u[i]
            changed = True

        elif u[i] is None and v[j] is not None:
            u[i] = cost[i][j] - v[j]
            changed = True


print("u values =", u)
print("v values =", v)

# Calculate opportunity costs
print("\nOpportunity Costs:")

optimal = True

for i in range(rows):
    for j in range(cols):

        if allocation[i][j] == 0:

            opportunity_cost = cost[i][j] - u[i] - v[j]

            print(
                "Cell (", i + 1, ",", j + 1,
                ") =", opportunity_cost
            )

            if opportunity_cost < 0:
                optimal = False


print("\nFinal Allocation:")
print(allocation)

print("\nFinal Transportation Cost =", total_cost)

if optimal:
    print("Solution is optimal.")
else:
    print("Solution can be improved.")