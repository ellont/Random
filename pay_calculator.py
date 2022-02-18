# Hours worked less or equal to 40(hrs) are paid at normal rate
# Hours worked above 40(hrs) are paid at 1.5 times the normal rate

hour_threshold = 40
rate_multiplier = 1.5

def valid_Hour(h):
    while True:
        global str_hour
        try: 
            float(h)
        except:
            print('Not a numeric number, please re-enter')
            h = input('Hours worked:')
            str_hour = h
            continue
        if float(h) > 0:
            break
        else:
            print('Invalid number.')
            h = input('Hours worked:')
            str_hour = h
            continue

str_hour = input('Hours worked:')
valid_Hour(str_hour)
hour = float(str_hour)
print('You worked', hour, 'hr(s)') 

def valid_Rate(r):
    while True:
        global str_rate
        try: 
            float(r)
        except:
            print('Not a numeric number, please re-enter')
            r = input('Hourly rate:')
            str_rate = r
            continue
        if float(r) > 0:
            break
        else:
            print('Invalid number, please re-enter.')
            r = input('Hourly rate:')
            str_rate = r
            continue

str_rate = input('Hourly rate:')
valid_Rate(str_rate)
rate = float(str_rate)
print('Your hourly rate is', rate)


def compute_Pay(hour,rate):
    if hour <= hour_threshold:
        return hour * rate
    else:
        return hour_threshold * rate + (hour-hour_threshold) * rate * rate_multiplier

pay = compute_Pay(hour, rate)
print('Your pay is:', pay)