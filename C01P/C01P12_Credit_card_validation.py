def is_credit_card_valid(number):
    digit_list = list(reversed([int(x) for x in str(number)]))
    number_to_validate = []

    for n in range(len(digit_list)):
        num = digit_list[n]
        if n % 2 != 0:
            num = digit_list[n]
            num *= 2
            if num >= 10:
                num = int(str(num)[0]) + int(str(num)[1])
        number_to_validate.append(num)
    return True if sum(number_to_validate) % 10 == 0 else False


print(is_credit_card_valid(79927398713) is True)
print(is_credit_card_valid(79927398715) is False)
print(is_credit_card_valid(4417123456789113) is True)
