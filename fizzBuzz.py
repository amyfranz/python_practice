def fizzbuzz(input):
    if not input % 3 and not input % 5:
        return "FizzBuzz"
    elif not input % 3:
        return "Fizz"
    elif not input % 5:
        return "Buzz"
    else:
        return input

print(fizzbuzz(3), fizzbuzz(15), fizzbuzz(5), fizzbuzz(7))