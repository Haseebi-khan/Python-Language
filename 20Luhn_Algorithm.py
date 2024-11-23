# The Luhn Algorithm is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, and more. It helps verify the validity of a number against simple errors like mistyped digits.

# Steps of the Luhn Algorithm:
# Reverse the Number: Reverse the digits of the number you're validating (this is done for processing convenience).

# Double Every Second Digit: Starting from the rightmost digit (now the leftmost after reversing), double every second digit.

# Subtract 9 if Greater than 9: If doubling a digit results in a number greater than 9, subtract 9 from it (or equivalently, sum the two digits of the result).

# Sum All Digits: Add all the digits together, including both the modified and unmodified ones.
# /////////////////////////////////////////////////////
# Check Divisibility by 10: If the total sum is divisible by 10, the number is valid; otherwise, it is invalid.
# You have accessed elements (characters) of a string before, using the index operator []. You can also use the index operator to access a range of characters in a string with
# string[start:stop:step]

# Account number      7   9  9  2  7  3  9   8  7  1  x
# Double every other  7  18  9  4  7  6  9  16  7  2  x
# Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()