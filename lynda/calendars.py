#===============================================================================
# y = 198 + 167
# print (y)
#===============================================================================
import calendar

#===============================================================================
c = calendar.TextCalendar(calendar.MONDAY)
# str = c.formatmonth(2013, 1, 0, 0)
# print (str)
# 
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# str = hc.formatmonth(2013, 1)
# print (str)
#===============
# for i in c.itermonthdays(2013, 8):
#     print (i)

#===============================================================================
# for name in calendar.month_name:
#     print (name)
#     
# for day in calendar.day_name:
#     print (day)
#===============================================================================
for m in range(1, 13):
    cal = calendar.monthcalendar(2013, m)
    weekone = cal[0]
    weektwo = cal[1]
    
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
    print ('%10s %2d' % (calendar.month_name[m], meetday))