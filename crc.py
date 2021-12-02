import random

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        # XOR is 0 for equal elements and 1 for distinct
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def divide(divident, divisor):
    l = len(divisor)
    temp = divident[:l] # current part to divide
    while l < len(divident):
        if temp[0] == '1':
            # Apply XOR and add next bit
            temp = xor(temp, divisor) + divident[l]
            # Apply XOR with all zeros and add next bit
        else:
            temp = xor('0' * l, temp) + divident[l]
        l += 1
    # Final division
    if temp[0] == '1':
        remainder = xor(divisor, temp)
    else:
        remainder = xor('0' * l, temp)
    return remainder


print("--------CRC Simulation--------\n")
# Example
# inputData = '100100'
# G = '1101'

inputData = input("Enter data to send: ")
G = input("Enter G (must start with 1): ")

sendData = inputData + '0' * (len(G) - 1)

R = divide(sendData, G)
sendData = inputData + R

print("Sending data: {}".format(sendData))
receivedData = sendData

ans = input("Interfere data? (y/n): ")
while ans != 'y' and ans != 'n':
    print("Invalid option")
    ans = input("Interfere data? (y/n): ")

if ans == 'y':
    # Modify data
    arr = list(receivedData)
    pos = random.randrange(len(arr))
    arr[pos] = '1' if arr[pos] == '0' else '0'
    receivedData = ''.join(arr)

print("Received data: {}".format(receivedData))
# Divide by G. If remainder is 0 the data is valid, otherwise is invalid
remainder = divide(receivedData, G)
if remainder == '0' * len(remainder):
    print("Data is valid")
else:
    print("Data is invalid")