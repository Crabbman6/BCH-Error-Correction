
def mod11(x):
    return x % 11


def inverse(x):
    return pow(x, 0, 11)


def sqrt(x):
   
    x = mod11(x)

    for i in range(0, 11):
        if (i ** 2) % 11 == x:
            return i
    return None




def BCHGenerator(sixDigitInput):
    print("Encoder Input:", sixDigitInput)
   
    if sixDigitInput == "-":
        return "-"

    # making sure array is global so it can be used outside the function
    global digits

    # digits array 
    digits = []

    # add all characters that were inputted with the function call into the digits array, transfers from character into digits data type 
    for character in str(sixDigitInput):
        digits.append(int(character))

    # Calculating the parity numbers
    digit7 = mod11(
        (4 * digits[0]) + (10 * digits[1]) + (9 * digits[2]) + (2 * digits[3]) +
        digits[4] + (7 * digits[5]))
    digit8 = mod11(
        (7 * digits[0]) + (8 * digits[1]) + (7 * digits[2]) + digits[3] + (9 * digits[4]) + (6 * digits[5]))
    digit9 = mod11((9 * digits[0]) + digits[1] + (7 * digits[2]) + (8 * digits[3]) + (7 * digits[4]) + (7 * digits[5]))
    digit10 = mod11((digits[0]) + (2 * digits[1]) + (9 * digits[2]) + (10 * digits[3]) + (4 * digits[4]) + digits[5])

    # Checking if any digit is 10
    if digit7 == 10 or digit8 == 10 or digit9 == 10 or digit10 == 10:
        return None

    else:
        # parity digits are added to the digits array as they will be used to decode
        digits.append(digit7)
        digits.append(digit8)
        digits.append(digit9)
        digits.append(digit10)

        # result blank string for all array integers to go into
        result = ''
        for digit in digits: result += str(digit)
        return result


def BCHDecoder(tenDigitInput):

    print("Decoder Input:", tenDigitInput)
    global digits


    # Error correction if the encoding step is skipped
    try:
        # Calculates the sum of all the digits in the array; Used for syndrome1
        digitSum = 0
        for digit in digits: digitSum += digit


    except NameError:
        # print("NameError triggered...")
        # Creates an array for the new numbers to be put into
        digits = []
        # Adds each character into the array
        for character in tenDigitInput: digits.append(int(character))
        print("digits:", digits)
        # Sum of all the digits in the array
        digitSum = 0
        for digit in digits: digitSum += digit

    # syndrome calculation
    syndrome1 = mod11(digitSum)
    
    syndrome2 = mod11(digits[0] + 2 * digits[1] + 3 * digits[2] + 4 * digits[3] + 5 * digits[4] + 6 * digits[5] + 7 * digits[6] + 8 * digits[7] + 9 * digits[8] + 10 * digits[9])
    
    syndrome3 = mod11(digits[0] + 4 * digits[1] + 9 * digits[2] + 5 * digits[3] + 3 * digits[4] + 3 * digits[5] + 5 * digits[6] +9 * digits[7] + 4 * digits[8] + digits[9])
    
    syndrome4 = mod11(digits[0] + 8 * digits[1] + 5 * digits[2] + 9 * digits[3] + 4 * digits[4] + 7 * digits[5] + 2 * digits[6] +6 * digits[7] + 3 * digits[8] + 10 * digits[9])
    
    print("s1, s2, s3, s4:", "[" + str(syndrome1)+",", str(syndrome2)+",", str(syndrome3)+",", str(syndrome4)+"]")

   
   
    # 0 error check

    if syndrome1 + syndrome2 + syndrome3 + syndrome4 == 0:
        print("No errors")
        result = ''

        for digit in digits: result += str(digit)
        return result

    # if there is at least 1 error: 

    else:
        P = mod11(syndrome2 ** 2 - syndrome1 * syndrome3)
        Q = mod11(syndrome1 * syndrome4 - syndrome2 * syndrome3)
        R = mod11(syndrome3 ** 2 - syndrome2 * syndrome4)

        print("P, Q, R:", "[" + str(P) + ",", str(Q) + ",", str(R) + "]\n")

        # Determining whether it's a single error or double
        if P + Q + R == 0:
            errorMagnitude = syndrome1
            errorPosition = mod11(syndrome2 * inverse(syndrome1))

            if errorPosition == 0:
                return "Error Position value is equal to 0 - there are more than 2 errors"
            print("Single Error...")
            print("errorMagnitude (a):", errorMagnitude)
            print("errorPosition (i):", errorPosition)

            # Error correction
            result = ''
            digits[errorPosition - 1] = mod11(digits[errorPosition - 1] - errorMagnitude)
            for digit in digits: result += str(digit)
            return result

        # Else will run if double errors detected (i.e. p,q,r are not equal to 0.)
        else:
            if P == 0:
                return "More than 2 errors, as P value is equal to 0"
            try:
                errorPositioni = mod11((-Q + sqrt(Q ** 2 - 4 * P * R)) * inverse(2 * P))
                errorPositionj = mod11((-Q - sqrt(Q ** 2 - 4 * P * R)) * inverse(2 * P))
            # TypeError would trigger when the square root doesn't work, thus more than two errors.

            except TypeError:
                return "No square root, therefore more than two errors..."

            if errorPositionj == 0 or errorPositioni == 0:
                return "Error Position value is equal to 0, therefore there are more than 2 errors."
            errorMagnitudeb = mod11((errorPositioni * syndrome1 - syndrome2) * inverse(errorPositioni - errorPositionj))

            errorMagnitudea = mod11(syndrome1 - errorMagnitudeb)

            # The check below would sort out values similar to the one in the final test
            if errorMagnitudea > 9 or errorMagnitudeb > 9:
                return "One of the error magnitudes is greater than 9. There are more than two errors."

            print("Two Errors...")
            print("i,j:", "[" + str(errorPositioni) + ",", str(errorPositionj) + "]")
            print("a,b:", "[" + str(errorMagnitudea) + ",", str(errorMagnitudeb) + "]")



            # Correcting the error by editing the array with the new calculated value...
            result = ''
            digits[errorPositioni - 1] = mod11(digits[errorPositioni - 1] - errorMagnitudea)
            digits[errorPositionj - 1] = mod11(digits[errorPositionj - 1] - errorMagnitudeb)
            # and putting all into the string variable 'digit'.
            for digit in digits: result += str(digit)
            return result


# Enter 10 digit number into BCHDecoder

#print("Decoder Output is:", BCHDecoder('3745195876'))
#print(" Decoder Output is:", BCHDecoder('3945195876'))
#print(" Decoder Output is:", BCHDecoder('3745995876'))
#print("4. Decoder Output is:", BCHDecoder('3715195076'))
#print("5. Decoder Output is:", BCHDecoder('0743195876'))
#print("6. Decoder Output is:", BCHDecoder('3745195840'))
#print("7. Decoder Output is:", BCHDecoder('2745795878'))
#print("8. Decoder Output is:", BCHDecoder('8745105876'))

#Additional test for BCH (10,6)

print("Additonal test for BCH -----------------------------")

print("1. Decoder Output is:", BCHDecoder('3121195876'))
print("2. Decoder Output is:", BCHDecoder('1135694766'))
print("3. Decoder Output is:", BCHDecoder('0888888074'))
print("4. Decoder Output is:", BCHDecoder('5614216009'))
print("5. Decoder Output is:", BCHDecoder('9990909923'))
print("6. Decoder Output is:", BCHDecoder('1836703776'))
print("7. Decoder Output is:", BCHDecoder('9885980731'))






