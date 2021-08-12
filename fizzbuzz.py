for x in range(1, 90):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizz buzz")
        continue
    elif x % 3 == 0:
        print("Fizz")
        continue
    elif x % 5 == 0:
        print("Buzz")
    else:print(x)
