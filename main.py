import helpers


def toDecimal(number, base):
    partialSum = [helpers.letterToNum(number[0])]
    for i in range(len(number) - 1):
        partialSum.append(
            base * int(partialSum[i]) + helpers.letterToNum(number[i+1]))
    print("Horner:", end='\t')
    for i in range(len(number)):
        print(number[i], end="\t")
    print(f"\n{base}", end='\t')
    for i in range(len(partialSum)):
        print(partialSum[i], end='\t')
    print(f'\n {number} = {partialSum[-1]}')
    return partialSum[-1]


def toBase(number, base):
    if number == 0:
        print("0 = 0")
        return '0'
    result = []
    startNum = number
    while number != 0:
        print(f"{number}\t|{number%base}")
        result.append(helpers.numToStr(number % base))
        number = number // base
    result.reverse()
    inBase = ''.join(result)
    print(f"{startNum} = {inBase}")
    return inBase


def binaryFractions(float):
    integer = int(float)
    float -= integer
    afterComma = []
    precision = 0
    print("Fraction part:")
    while float > 0 and precision < 20:
        float *= 2
        print(f'{float}\t|*2')
        afterComma.append(str(int(float)))
        if float >= 1.0:
            float -= 1.0
        precision += 1
    print("Integer part:")
    binaryInteger = toBase(integer, 2)
    print(str(binaryInteger) + ',' + ''.join(afterComma))


def toSignMagnitude(number):
    if number >= 0:
        bin = toBase(number, 2)
        print(f'{number} = {helpers.byteSizedBin(bin)} (SM)')
    else:
        bin = toBase(number * (-1), 2)
        positiveSign = '1' + (helpers.findPossibleBitNumber(bin)-len(bin) - 1) * '0' + bin
        print(f'1. to SM: {positiveSign}')
        print(f'2. set SignBit: {number} = {positiveSign} (SM)')


def signMagnitudeToDec(sm):
    dec = toDecimal(sm[1:], 2)
    print(f'{sm} = { (-1 if sm[0] == "1" else 1) * dec}')


def twosComplement(number):
    if number >= 0:
        bin = toBase(number, 2)
        print(f'{number} = {helpers.byteSizedBin(bin)} (U2)')
    else:
        bin = toBase(-number, 2)
        bin = helpers.byteSizedBin(bin)
        print(f'1. Positive SM: {bin}')
        bin = helpers.magicInvertBits(bin)
        print(f'2. Invert bits: {bin}')
        bin = helpers.plusOne(bin)
        print(f'3. Plus 1: {bin}')
        print(f'{number} = {bin} (U2)')


def onesComplement(number):
    if number >= 0:
        bin = toBase(number, 2)
        print(f'{number} = {helpers.byteSizedBin(bin)} (U2)')
    else:
        bin = toBase(-number, 2)
        bin = helpers.byteSizedBin(bin)
        print(f'1. Positive SM: {bin}')
        bin = helpers.magicInvertBits(bin)
        print(f'2. Invert bits: {bin}')
        print(f'{number} = {bin} (U1)')


def program():
    helpers.clearScreen()
    print("Select Conversion")
    print("\t1. Decimal to [base]")
    print("\t2. [Base] to decimal")
    print("\t3. Float to binary")
    print("\t4. Decimal to sign magnitude")
    print("\t5. Sign Magnitude to decimal")
    print("\t6. Decimal to ones complement")
    print("\t7. Decimal to twos complement")
    print("\t8. Exit")

    option = input()

    if option == "1":
        helpers.clearScreen()
        number = int(input("Decimal number: "))
        base = int(input("Base: "))
        toBase(number, base)

    if option == "2":
        helpers.clearScreen()
        number = input("Number in base: ")
        base = int(input("Base: "))
        toDecimal(number, base)

    if option == "3":
        helpers.clearScreen()
        number = float(input("Decimal float: "))
        binaryFractions(number)

    if option == "4":
        helpers.clearScreen()
        number = int(input("Decimal integer: "))
        toSignMagnitude(number)

    if option == "5":
        helpers.clearScreen()
        number = input("Sign magnitude binary number: ")
        signMagnitudeToDec(number)

    if option == "6":
        helpers.clearScreen()
        number = int(input("Sign magnitude binary number: "))
        onesComplement(number)

    if option == "7":
        helpers.clearScreen()
        number = int(input("Sign magnitude binary number: "))
        twosComplement(number)

    if option == "8":
        return False

    input("Press a key to continue")

    return True


while program():
    pass
