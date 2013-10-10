from prettytable import PrettyTable

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
    t = PrettyTable(["num", "result"])
    t.padding_width = 1
    j = 1
    i = n
    result = 0
    counter = 0         
    while j <= (2*n-1) and j >= 1 and n >= 1:
        result += j**i
        j += 2
        i -= 1
        counter += 1
        t.add_row([counter, result])
    print(t)
    print('Result of the expression is %d' %result)
    

if __name__ == '__main__':
    main()
