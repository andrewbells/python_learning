

def main():
    num_1 = int(input('add first number: '))
    num_2 = int(input('add last number: '))
    #find_divisors(num_1, num_2)
    max_num_least(num_1, num_2)
    

def find_divisors(a, b):
    #global divisors_dict
    #global num_divisors_dict
    divisors_dict = {}
    num_divisors_dict = {}
    for x in range(a, b + 1):
        num_divisors = 0
        divisors_list = []
        print('number %d' %x)
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                num_divisors += 1
                divisors_list.append(y)
                divisors_dict[x] = divisors_list
                
                print('has divisor %d' % y)
            
            else:
                divisors_dict[x] = divisors_list
        
        num_divisors_dict[x] = num_divisors
        print('number %d has %d divisors' % (x, num_divisors))
        
            
    print(divisors_dict, 'Number of divisors', num_divisors_dict)
    return divisors_dict, num_divisors_dict

    '''lets find the max value from the interval, which has least
    
    amount of divisors''' 
    '''
    Euclid algorithm
    def gdc(a, b):
        while a != 0:
            a, b = b % a, a
            return b
    '''
def max_num_least(a, b):
    '''
    here i decided to count all the values and number of divisors once more and
    put them into a new separate LISTS, not dictionaries, since probably i lack skill of working with dict.
    Otherwise this could be the only function of the program -- the above one returns nicer looking data
    representation in dicts. Besides i dont define values of divisors in this function.
    '''
    master = []
    num_div = []
    values = []
    for x in range(a, b + 1):
        output = []
        num_divisors = 0
        output.append(x)
        values.append(x)
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                num_divisors += 1
                    

        if num_divisors >= 1:
            num_div.append(num_divisors)
        output.append(num_divisors)
        master.append(output)
    print (master)
    #print (values)
    #print (num_div)
    '''
    note that i skipped zeros in num_divisors since we dont take values without divisors into account
    as soon as i get all three lists filled we can start analyzing:
    '''
  
    val_min_div = []    
    for i in range(len(master)):
        if master[i][1] == min(num_div):
            val_min_div.append(master[i][0])
    max_val = max(val_min_div)
    print ('The max value from the interval, which has least amount of divisors is %d' % max_val)
    return max_val
            
        


if __name__ == '__main__':
    main()
