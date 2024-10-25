# for loop
#Fizzbizz = i %3
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        #fizz
    elif i % 3 == 0:
        print("Fizz")
        #bizz
    elif i % 5 == 0:
        print("Buzz")
        #remainder
    else:
        print(i)
