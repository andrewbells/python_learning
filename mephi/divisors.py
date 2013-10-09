
divisors_dict = {}
num_divisors_dict = {}
def main():
    
    find_divisors(int(input('add first number: ')), int(input('add last number: ')))
    

def find_divisors(a, b):
    #global divisors_dict
    #global num_divisors_dict
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

          
  
    
        


if __name__ == '__main__':
    main()
