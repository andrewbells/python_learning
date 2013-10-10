'''here i copied algorythm used in C.
Finding the maximul number, having least amount of divisors from array'''

def main():
    num_1 = int(input('add first number: '))
    num_2 = int(input('add last number: '))
    max_num_least(num_1, num_2)
    


def max_num_least(a, b):
    l, r = 0, 0
    
    #x is value iterable
    #y is divisor
    #l,r are divisors iterator
    for x in range(a, b + 1):
        num_divisors = 0
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                num_divisors += 1
        
        if l >= num_divisors:
            l = num_divisors
            v = x
        if r <= num_divisors:
            r = num_divisors
            e = x

    print('%d is the maximum number having the least - %d divisors' % (v, l))
    print('%d is the maximum number having the most - %d divisors' % (e, r))            
        


if __name__ == '__main__':
    main()
