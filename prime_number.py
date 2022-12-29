# input from the user
# check the prime number

number = int(input('Input the number to check primenumber: '))
flag = False
for i in range(2, number):
    if (number % i) == 0:
        flag = True
        break
    
if flag:
    print(f'{number} is not a prime number')
else:
    print(f'{number} is a prime number')

print(type(flag))
