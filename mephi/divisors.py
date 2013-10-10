from prettytable import PrettyTable

def main():
    num_1 = int(input('add first number: '))
    num_2 = int(input('add last number: '))
    find_divisors(num_1, num_2)
    max_num_least(num_1, num_2)
    

def find_divisors(a, b):
    t = PrettyTable(["Number", "Divisors", "no Divisors"])
    t.padding_width = 1
    divisors_dict = {}
    num_divisors_dict = {}
    for x in range(a, b + 1):
        num_divisors = 0
        divisors_list = []
        t.add_row([x, '-', '-'])
        #print('number %d' %x)
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                num_divisors += 1
                divisors_list.append(y)
                divisors_dict[x] = divisors_list
                #print('has divisor %d' % y)
            
            else:
                divisors_dict[x] = divisors_list

        #start printing values in the table:
        if 1 <= (len(divisors_list)) <= 4:
            t.add_row([ '', divisors_list, ''])
        elif (len(divisors_list)) == 0:
            t.add_row([ '', '...', ''])
        else:
            #the case for lists longer than 4
            while len(divisors_list) > 5:
                t.add_row([ '', divisors_list[:4], ''])
                divisors_list = divisors_list[4:]
            #print the rest of the the list
            t.add_row([ '', divisors_list[:4], ''])


        if num_divisors == 0:
            t.add_row([ '-', '-', '...'])
        else:
            t.add_row([ '-', '-', num_divisors])
        '''in order to output num_divisors == 0 in the table comment out upper if else block and remove hash tag
        from the line below'''
        #t.add_row([ '-', '-', num_divisors])
        
        t.add_row(['------','-----------------','------'])

        num_divisors_dict[x] = num_divisors
        #print('number %d has %d divisors' % (x, num_divisors))
        
            
    #print(divisors_dict, 'Number of divisors', num_divisors_dict)
    print (t)
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
    #p = PrettyTable(["Number", "Divisors", "no Divisors"])
    #p.padding_width = 1
    for x in range(a, b + 1):
        output = []
        num_divisors = 0
        output.append(x)
        values.append(x)
        #p.add_row([x, '-', '-'])
        for y in range(2, x + 1):
            if x % y == 0 and x != y:
                num_divisors += 1
                #p.add_row([ '', y, ''])    
        #p.add_row([ '-', '-', num_divisors])
        #p.add_row(['------','------','------'])


        if num_divisors >= 1:
            num_div.append(num_divisors)
        '''if num_divisors == 0 is considered an option for the output of max_val,
        then comment out two upper lines and remove hash tag from the line below'''
        #num_div.append(num_divisors)


        output.append(num_divisors)
        master.append(output)
    #print (p)
    #print (master)
    #print (values)
    #print (num_div)
    '''
    note that i skipped zeros in num_divisors since we dont take values without divisors into account.
    if zeros should be included, then check upper comment.
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
