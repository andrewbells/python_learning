def breakNum(num):
    a = num % 10
    b = num % 100 // 10
    c = (num // 100) % 10
    d = num // 1000
    #print ("a ", a, "b ", b, "c ", c, "d ", d)
    summ = a + b + c + d
    print (a, '\t', b,'\n', c, '\t', d,'\n')
    print (summ)
