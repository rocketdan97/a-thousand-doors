# count_divisors() is taken from 
# https://stackoverflow.com/questions/9076336/how-do-you-implement-the-divisor-function-in-code

door_dict = {0:'closed', 1: 'open'}

def count_divisors(n):
    count = 0
    for i in range(1,int((n/2) + 1)):
        if (n % i == 0):
            count = count + 1
    return count + 1    # +1 to account for number itself as a divisor

f = open('divisors.txt','w')

for i in range(1000):
    f.write('door ' + str(i) + ' is ' + door_dict[count_divisors(i)%2] +\
    ' after ' + str(count_divisors(i)) + ' door flips\n') 