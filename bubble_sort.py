'''bubble sort'''

def main():
    global swapped
    array = [5, 3, 4, 1, 2, 0, 10, 6, 3]
    print(array)
    one_pass(array)
    while swapped == True:
        one_pass(array)
    
    print('sorting is done')
    print(array)

    
def one_pass(a):
    global swapped
    swapped = False
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            a[i - 1], a[i] = a[i], a[i - 1]
            swapped = True
        print(i, swapped, a)
        
    
        


if __name__ == '__main__':
    main()
