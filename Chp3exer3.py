# Anthony Silva
# CIT 95
# 1/24/2025


score = float(input('please enter your score between 1.0 or 0: '))

if score < 0 or score > 1.0:
    print("please enter in a proper score!")
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')

