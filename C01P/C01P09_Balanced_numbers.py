def is_number_balanced(number):
    if len(str(number))==1:
        return True

    number = [int(x) for x in str(number)]
    first_half = number[:len(number)//2]
    second_half = number[len(number)//2:]
    
    if len(first_half)!=len(second_half):
        second_half = second_half[1:]

    return True if sum(first_half)==sum(second_half) else False


print(is_number_balanced(9) is True)
print(is_number_balanced(4518) is True)
print(is_number_balanced(28471) is False)
print(is_number_balanced(1238033) is True)