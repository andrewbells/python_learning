#===============================================================================
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta

print (timedelta(days = 365, hours = 5, minutes = 1))

print ('today is ' + str(datetime.now()))

print ('one year from now will be ' + str(datetime.now() + timedelta(days = 365)))
print ('in 3 weeks and 2 days from now will be ' + str(datetime.now() + timedelta(weeks = 3, days = 2)))

t = datetime.now() - timedelta(weeks = 2)
s = t.strftime('%A, %d %B, %Y')
print ('two weeks ago was ' + s)

today = date.today()
afd = date(today.year, 4, 1)

if afd < today:
    print ('april fools day went by %d days ago' %((today - afd).days))
    afd = afd.replace(year = today.year + 1)
    
time_to_afd = abs(afd - today)
print (time_to_afd.days, 'days until april fools day!')
#def main():
    
    
    #===========================================================================
    # now = datetime.now()
    # print (now.strftime('%Y'))
    # print (now.strftime('%a, %d %B, %Y'))
    # 
    # print (now.strftime('%c'))
    # print (now.strftime('%x'))
    # print (now.strftime('%X'))
    # 
    # print (now.strftime('%I:%M:%S, %p'))
    # print (now.strftime('%H:%M'))
    #===========================================================================
    #===========================================================================
    # today = date.today()
    # 
    # print ('today is ', today)
    # print ("today's components: ", today.day, today.month, today.year)
    # print ("today's weekday # ", today.weekday())
    # 
    # today = datetime.now()
    # print ("the current date and time is: ", today)
    # 
    # t = datetime.time(datetime.now())
    # print ("current time is: ", t)
    #===========================================================================
    #===========================================================================
    # today = date.today()
    # wd = date.weekday(today)
    # days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    # print ("today's day number is %d" %wd)
    # print ("and this day is " + days[wd])
    #===========================================================================
#===============================================================================
# class myClass():
#     def method1(self):
#         print ('myClass method1')
#         
#     def method2(self, someString):
#         print ('myClass method2: ' + someString)
# 
# class anotherClass(myClass):
#     def method2(self):
#         print ('another class method2')
#         
#     def method1(self):
#         myClass.method1(self);
#         print ('anotherClass method1')
#         
# def main():
#     c = myClass()
#     
#     c.method1()
#     c.method2('This is the damn string')
#     c2 = anotherClass()
#     c2.method1()
#     c2.method2()
#===============================================================================
    #===========================================================================
    # days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    # 
    # for day in days:
    #     print (day)
    #===========================================================================
#     days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
#     
#     for i, d in enumerate(days):
#         print (i, d)
    #===========================================================================
    # x = 0
    # for x in range(5, 10):
    #     #if x == 7: break
    #     if x % 2 == 0: continue
    #     print (x)
    #===========================================================================
#     while x < 5:
#         print (x)
#         x += 1
        
#===============================================================================
# #        for x in range(5, 10):
# #         print (x)
#===============================================================================
   # x, y = 20, 23
    
    #===========================================================================
    # if (x < y):
    #     st = 'x is less than y'
    # elif (y < x):
    #     st = 'y is less than x'
    # else:
    #     st = 'x equals y'
    #===========================================================================
  #=============================================================================
  #   st = 'x is greater than y' if (x > y) else 'x is less or equal to y'
  #   
  #   print (st)
  # 
  #=============================================================================
 
 
# if __name__ == '__main__':
#      main()


#===============================================================================
# def addUp(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result
# 
# print (addUp(1,2,3,4, 100, 9))
#===============================================================================
