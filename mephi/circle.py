'''This program defines whether a point [x, y] is within a chosen area - inside a circle [r],
but outside encircled triangle ABD as well as rectangle [a, a][a, -a][0, -a][0, a]'''
within_circle = False
within_rectangle = True
outside_triangle1 = False
outside_triangle2 = False
r = 500
a = r / 2
pos = [0, 0]
A = [-r, 0]
B = [0, r]
C = [0, 0]
D = [0, -r]
#x = 0
#y = 0


def main():
    global r, pos, within_circle, within_rectangle, outside_triangle1, outside_triangle2
    pos[0] = float(input('input x: '))
    pos[1] = float(input('input y: '))
    #pos[0] = x
    #pos[1] = y
    circleR(r)
    square()
    checkTriangle1()
    checkTriangle2()

    if within_circle == True and (within_rectangle == False or outside_triangle1 == True or outside_triangle2 == True):
        print ('point is within the chosen area')
    else:
        print ('point is outside the area')
    
def circleR(rad):
    global within_circle
    areaC = pow(pos[0], 2) + pow(pos[1], 2)
    if areaC < pow(rad, 2):
        within_circle = True
    else:
        within_circle = False
        
    return within_circle

def square():
    global r, a, within_rectangle 
    if pos[0] > a or pos[1] > a and pos[0] > 0 or pos[1] < -a and pos[0] > 0:
        within_rectangle = False
    else:
        within_rectangle = True
    return within_rectangle

def triangleArea(point1, point2, point3):
    
    #point1 = [x1, y1]
    #point2 = [x2, y2]
    #point3 = [x3, y3]
    '''Triangle area is calculated with help of vector method by matrix.'''
    areaTriangle = ((point1[0]-point3[0])*(point2[1]-point3[1])-(point2[0]-point3[0])*(point1[1]-point3[1])) / 2
    return areaTriangle

def checkTriangle1():
    global r, outside_triangle1, A, B, C, D
    areaABPos = triangleArea(A, pos, B)
    areaACPos = triangleArea(A, pos, C)
    areaBCPos = triangleArea(B, pos, C)
    areaABC = triangleArea(A, B, C)
    if abs(areaABC) != abs(areaABPos) + abs(areaACPos) + abs(areaBCPos) and pos[0] <= 0 and pos[1] >= 0:
        outside_triangle1 = True
    else:
        outside_triangle1 = False
    return outside_triangle1

def checkTriangle2():
    global r, outside_triangle2, A, B, C, D
    areaADPos = triangleArea(A, pos, D)
    areaACPos = triangleArea(A, pos, C)
    areaDCPos = triangleArea(D, pos, C)
    areaADC = triangleArea(A, D, C)
    if abs(areaADC) != abs(areaADPos) + abs(areaACPos) + abs(areaDCPos) and pos[0] <= 0 and pos[1] <= 0:
        outside_triangle2 = True
    else:
        outside_triangle2 = False
    return outside_triangle2

    

if __name__ == '__main__':
    main()

# test
'''dont forget to change main() to main(x, y) and add default values of x = 0, y = 0 to the top'''
    #for x in range(-7, 1):
#	for y in range(7):
#		print ('%d;' %x, '%d' %y)
#		main(x, y)
