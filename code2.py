def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

numbers = [5, 7, 10, 3, 8]

results = []

for num in numbers:
    fact = factorial(num)
    results.append(str(fact))

print(", ".join(results))
