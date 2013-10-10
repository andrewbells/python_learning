'''user inputs a positive int. program
calculates the sum of the following expression 1**n + 3**(n-1) + 5**(n-2) +
+ 7**(n-3) + ... + (2*n - 3)**2 + (2*n - 1)**1'''

def main():
    
    num = int(input('input a positive int: ' ))    
    values(num)
    
def values(n):
    '''
    j is number
    i is power
    beginning j = 1 j = 3, j = 5, j = 7 ... (2*n - 3), 2*n - 1
    i = n, i = n - 1, i = n - 2 ... i = 2, i = 1
    '''
    j = 1
    i = n
    result = 0
             
    while j <= (2*n-1) and j >= 1 and n >= 1:
        result += j**i
        j += 2
        i -= 1

    print(result)
    

if __name__ == '__main__':
    main()
