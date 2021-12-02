import random

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def divide(divident, divisor):
    l = len(divisor)
    temp = divident[:l]
    while l < len(divident):
        if temp[0] == '1':
            temp = xor(temp, divisor) + divident[l]
        else:
            temp = xor('0' * l, temp) + divident[l]
        l += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * l, temp)
    return temp


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
remainder = divide(receivedData, G)
if remainder == '0' * len(remainder):
    print("Data is valid")
else:
    print("Data is invalid")