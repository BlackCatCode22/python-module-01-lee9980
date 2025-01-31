# Anthony Silva
# Cit 95
# 1/30/2025

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate) :
    print("in computepay", hours, rate)
    if hours > 40:
        regularPay = 40 * rate
        overTimePay = (hours - 40) * (rate * 1.5)
        totalPay = regularPay * overTimePay
    else:
        totalPay = hours * rate
    print("returning", totalPay)
    return totalPay


hr = int(input('Enter your hours: '))
rt = float(input('Enter your rate: '))

pay = computepay(hr,rt)

print('your pay: ', pay)
