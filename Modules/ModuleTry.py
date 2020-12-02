import calendar
cal = calendar.month(2020, 12)
print(cal)
print(calendar.isleap(2020))

import user_made_module as umm

n = 105
print(umm.sum(n,5))
print(umm.isEven(n))
print(umm.isOdd(n))