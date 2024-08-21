numbers = {1,2,3,4,5,6,7,8,9,10,35,43,23,22,68,90}
even = []
odd = []

def output(numbers):
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            if num % 2 != 0:
                odd.append(num)

output(numbers)


    

