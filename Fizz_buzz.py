# set starting value
i = 1

#start while loop
while i <= 100:
    print(i)
    i = i + 1

#add if divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
#add if divisible by 3
    elif i % 3 == 0:
        print("Fizz")
#add if divisble by 5
    elif i % 5 == 0:
        print("Buzz")