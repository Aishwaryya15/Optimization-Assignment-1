import numpy as np

M = 1000

# Variables: x1, x2, s1, s2, a1

c = np.array([3, 2, 0, 0, -M], dtype=float)

A = np.array([
    [1, 1, -1, 0, 1],
    [1, 2, 0, 1, 0]
], dtype=float)

b = np.array([4, 6], dtype=float)

# Artificial variable a1 and slack variable s2
basis = [4, 3]

names = ["x1", "x2", "s1", "s2", "a1"]

for iteration in range(10):

    B = A[:, basis]
    Binv = np.linalg.inv(B)

    table = Binv @ A
    rhs = Binv @ b

    cb = c[basis]
    zj = cb @ table
    cj_zj = c - zj

    print("\nIteration", iteration)
    print("Basic variables:",
          [names[i] for i in basis])

    print("Tableau:")
    print(table)

    print("RHS:", rhs)
    print("Cj-Zj:", cj_zj)

    # Check whether solution is optimal
    if max(cj_zj) <= 0:
        break

    # Entering variable
    entering = np.argmax(cj_zj)

    # Ratio test
    ratios = []

    for i in range(len(rhs)):
        if table[i][entering] > 0:
            ratios.append(rhs[i] / table[i][entering])
        else:
            ratios.append(float("inf"))

    leaving = np.argmin(ratios)

    print("Entering variable:", names[entering])
    print("Leaving variable:", names[basis[leaving]])

    basis[leaving] = entering


# Final answer

solution = np.zeros(len(c))

for i in range(len(basis)):
    solution[basis[i]] = rhs[i]

z = c @ solution

print("\nFinal Solution")
print("x1 =", solution[0])
print("x2 =", solution[1])
print("Maximum Z =", z)