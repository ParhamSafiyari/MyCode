card_number = input("Please enter the card number: ")

if not card_number.isdigit():
    print("Invalid input! Only digits are allowed.")
else:
    total = 0
    reversed_digits = card_number[::-1]

    for i in range(len(reversed_digits)):
        digit = int(reversed_digits[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    if total % 10 == 0:
        first_two = int(card_number[:2])
        first_one = int(card_number[0])
        length = len(card_number)

        if length == 15 and (first_two == 34 or first_two == 37):
            print("AMEX")
        elif length == 16 and 51 <= first_two <= 55:
            print("MASTERCARD")
        elif (length == 13 or length == 16) and first_one == 4:
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
