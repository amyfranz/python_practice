even_numbers = 0

for n in range(1, 11):
    if not n % 2:
        print(n)
        even_numbers += 1
print(f"There are {even_numbers} even numbers.")