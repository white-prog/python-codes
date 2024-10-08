def isValid(card_number):
    sum_of_products = []
    sum_of_non = []
    char_card_number = [i for i in str(card_number)]
    count = 1
    for i in char_card_number:
        if count % 2 != 0:
            sum_of_products.append(int(i)*2)
            count = count + 1
        else:
            sum_of_non.append(int(i))
            count = count + 1
    sum_filter = 0
    for i in sum_of_products:
        if len(str(i)) > 1:
            for j in str(i):
                sum_filter += int(j)
        else:
            sum_filter += i
    if (sum_filter + sum(sum_of_non)) % 10 == 0:
        return "Legit"
    return "Non Legit"


#program is not completed i will cover this code some time 
# CS50 2024 x problem set 2 credit => luhn's algorithm AMEX card and which type card identifying is not coded


print(isValid(4003600000000014))
print(isValid(4111111111111111))
print(isValid(5555555555554444))
print(isValid(378282246310005))