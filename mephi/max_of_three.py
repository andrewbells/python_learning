def main():
    
    a = int(input('input a: '))
    b = int(input('input b: '))
    c = int(input('input c: '))
    compare(a, b, c)
    print ('\n\nand now an easy way:')
    easyway(a, b, c)

def compare(a, b, c):
     
    if a > b and a > c:
        print ('a = %a is the max' %a)
    elif b > a and b > c:
        print ('b = %a is the max' %b)
    elif c > a and c > b:
        print ('c = %a is the max' %c)
    elif a > b and c > b and a == c:
        print ('a = c = %a are the max' %a)
    elif b > a and c > a and b == c:
        print ('b = c = %a are the max' %b)
    elif a > c and b > c and a == b: 
        print ('a = b = %a are the max' %a)
    else:
        print ('all three values are equal')

def easyway(a, b, c):
    m = max(a, b, c)
    print (m, ' is the max')
    


if __name__ == "__main__":
    main()
