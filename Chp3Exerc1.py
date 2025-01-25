# Anthony Silva
# Cit 95
# 1/23/2025

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = int(input('Enter your hours: '))
rate = float(input('Enter your rate: '))

if hours > 40:
    regularPay = 40 * rate
    overTimePay = (hours - 40) * (rate * 1.5)
    totalPay = regularPay * overTimePay
else:
    totalPay = hours * rate
print('your pay: ', totalPay)


