def iban_formatter(iban):
    """" Taking into account that IBAN length is 22 symbols"""
    leveled_out_input = ''.join(iban.split(' '))

    if len(leveled_out_input) != 22:
        raise Exception('IBAN length is 22 symbols, please check your input !')

    substring = ''
    formatted_iban = ''
    counter = 0

    for symbol in leveled_out_input:
        substring += symbol
        counter += 1

        if len(substring) == 4:
            substring += ' '
            formatted_iban += substring
            substring = ''

        if counter == len(leveled_out_input):
            formatted_iban += substring

    return formatted_iban


print(iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78")

print(iban_formatter("BG80 BNBG 9661 1020 3456 78") == "BG80 BNBG 9661 1020 3456 78")

print(iban_formatter("BG14TTBB94005362446381") == "BG14 TTBB 9400 5362 4463 81")

print(iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54")
