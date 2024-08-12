# set starting value
i = 1

#start while loop
while i in range(100):
    
#add if divisible by 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        i = i +1
        print("FizzBuzz")

#add if divisible by 3
    elif i % 3 == 0:
        i = i + 1
        print("Fizz")

#add if divisble by 5
    elif i % 5 == 0:
        print("Buzz")
        i = i + 1

    else:    
        print(i)
        i = i + 1