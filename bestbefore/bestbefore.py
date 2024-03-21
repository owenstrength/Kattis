# NOT DONE
og = input()
a,b,c = og.split('/')

year = ""
month = ""
day = ""

possible_year = []
possible_month = []
possible_days = []

if len(a) == 4:
    year = a
elif len(b) == 4:
    year = b
elif len(c) == 4:
    year = c

if len(a) == 1:
    a = "0" + a
if len(b) == 1:
    b = "0" + b
if len(c) == 1:
    c = "0" + c

possible_year = [a,b,c]
temp = []
for i in possible_year:
    if int(i) > 31:
        temp.append(i)

if len(temp) == 1:
    possible_year = [temp[0]]


if int(a) <= 12:
    possible_month.append(a)
if int(b) <= 12:
    possible_month.append(b)
if int(c) <= 12:
    possible_month.append(c)

if int(a) <= 31:
    possible_days.append(a)
if int(b) <= 31:
    possible_days.append(b)
if int(c) <= 31:
    possible_days.append(c)

if len(possible_month) == 1 and len(possible_year) == 1:
    if int(possible_month[0]) == 2:
        for i in possible_days:
            if int(i) > 28 and int(possible_year[0]) % 4 != 0:
                possible_days.remove(i)
            elif int(i) > 29 and int(possible_year[0]) % 4 == 0:
                possible_days.remove(i)
    elif int(possible_month[0]) in [4,6,9,11]:
        for i in possible_days:
            if int(i) > 30:
                possible_days.remove(i)


def check_valid():
    if len(possible_year) == 0 or len(possible_month) == 0 or len(possible_days) == 0:
        print(og + " is illegal")
        exit()

check_valid()

print(possible_year)
year = min(possible_year)
if str(year) in possible_month:
    possible_month.remove(str(year))
if len(str(year)) == 1:
    year = "200" + str(year)
elif len(str(year)) == 2:
    year = "20" + str(year)    
check_valid()
month = min(possible_month)

if str(month) in possible_days:
    possible_days.remove(str(month))
check_valid()
day = min(possible_days)

print(possible_year)

print(str(year) + "-" + str(month) + "-" + str(day))