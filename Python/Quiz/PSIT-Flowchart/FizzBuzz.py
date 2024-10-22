counter = 1
num = int(input())
while counter <= num:
    if not counter % 15:
        print("FizzBuzz")
    elif not counter % 5:
        print("Buzz")
    elif not counter % 3:
        print("Fizz")
    else:
        print(counter)
    counter = counter + 1