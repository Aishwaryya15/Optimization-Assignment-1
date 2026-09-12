import numpy as np

M = 1000

# Variables: x1, x2, s2, s3, A1, A2
A = np.array([
    [3, 1,  0, 0, 1, 0],
    [4, 3, -1, 0, 0, 1],
    [1, 2,  0, 1, 0, 0]
], dtype=float)

b = np.array([3, 6, 4], dtype=float)

# Original problem:
# Min Z = 4x1 + x2
#
# We convert it to:
# Max (-Z) = -4x1 - x2
#
# Artificial variables have penalty -M
c = np.array([-4, -1, 0, 0, -M, -M], dtype=float)

variables = ["x1", "x2", "s2", "s3", "A1", "A2"]

# Initial basic variables: A1, A2, s3
basis = [4, 5, 3]

for iteration in range(10):

    # Form basis matrix
    B = A[:, basis]
    B_inv = np.linalg.inv(B)

    # Current basic solution
    current_solution = B_inv @ b

    # Cost of basic variables
    cb = c[basis]

    # Calculate Zj
    zj = cb @ B_inv @ A

    # Calculate Cj - Zj
    cj_zj = c - zj

    print("\nIteration:", iteration)
    print("Basic variables:", [variables[i] for i in basis])
    print("Solution:", current_solution)
    print("Cj-Zj:", cj_zj)

    # Check optimality
    if np.max(cj_zj) <= 0:
        break

    # Choose entering variable
    entering = np.argmax(cj_zj)

    # Ratio test
    direction = B_inv @ A[:, entering]

    ratios = []

    for i in range(len(b)):
        if direction[i] > 0:
            ratios.append(current_solution[i] / direction[i])
        else:
            ratios.append(np.inf)

    # Choose leaving variable
    leaving_row = np.argmin(ratios)

    # Update basis
    basis[leaving_row] = entering


# Final calculation
B = A[:, basis]
B_inv = np.linalg.inv(B)

final_basic_solution = B_inv @ b

solution = np.zeros(len(variables))

for i in range(len(basis)):
    solution[basis[i]] = final_basic_solution[i]


print("\nFinal Solution")
print("----------------------")

for i in range(len(variables)):
    print(variables[i], "=", round(solution[i], 4))

# Since we maximized -Z, convert back to minimum Z
maximum_value = c @ solution
minimum_Z = -maximum_value

print("\nMinimum Z =", round(minimum_Z, 4))