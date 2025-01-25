# Anthony Silva
# 1/24/2025
# CIT 95

try:
    hours = int(input('Enter your hours: '))
    rate = float(input('Enter your rate: '))
except:
    print('please enter a numeric value: ')
    quit()

if hours > 40:
    regularPay = 40 * rate
    overTimePay = (hours - 40) * (rate * 1.5)
    totalPay = regularPay * overTimePay
else:
    totalPay = hours * rate
print('your pay: ', totalPay)



