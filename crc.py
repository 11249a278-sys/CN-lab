def xor(a, b):
    result = ""

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    return result


def mod2div(dividend, divisor):

    pick = len(divisor)
    temp = dividend[:pick]

    while pick < len(dividend):

        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[pick]
        else:
            temp = xor('0' * pick, temp) + dividend[pick]

        pick += 1

    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * pick, temp)

    return temp


data = input("Enter Data Bits: ")
key = input("Enter Generator Polynomial: ")

appended_data = data + '0' * (len(key) - 1)

remainder = mod2div(appended_data, key)

codeword = data + remainder

print("CRC Remainder:", remainder)
print("Transmitted Codeword:", codeword)

received = input("Enter Received Codeword: ")

check = mod2div(received, key)

if int(check) == 0:
    print("No Error Detected")
else:
    print("Error Detected")