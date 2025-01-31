# Anthony Silva
# 1/30/2025
# CIT 95



try:
    # gathers the input for three integers
    one = int(input('Give me your first Integer: '))
    two = int(input('Give me your second Integer: '))
    three = int(input('Give me your third Integer: '))

# Nested conditionals that check whether the input if input is greater than the other
# and then prints the greater integers result.
    if one > two and one > three:
        print('the greatest number is: ', one)
    else:
        if two > one and two > three:
            print('the greatest number is: ', two)
        else:
            if three > one and three > two:
                print('the greatest number is: ', three)
            else:
                print('no greater number')
except ValueError:
    print('please enter a proper integer and try again:')
    quit()