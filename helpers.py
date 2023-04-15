import platform
import os

SYSTEM = platform.system()


def clearScreen():
    if SYSTEM in ["Linux", "Darwin"]:
        os.system("clear")
    else:
        os.system("cls")


def letterToNum(letter):
    if letter.isdigit():
        return int(letter)
    else:
        return ord(letter.lower()) - ord('a') + 10


def numToStr(num):
    if num < 10:
        return str(num)
    else:
        return chr(num + ord('a') - 10)


def findPossibleBitNumber(bin):
    bytes = 0
    while 2**bytes < len(bin) + 1:
        bytes += 1
    return 2**bytes


def magicInvertBits(bin):
    bin = bin.replace('0', '8')
    bin = bin.replace('1', '0')
    bin = bin.replace('8', '1')
    return bin


def byteSizedBin(bin):
    return (findPossibleBitNumber(bin)-len(bin))*"0" + bin


def plusOne(bin):
    result = ''
    added = False
    for x in reversed(bin):
        if added:
            result += x
        else:
            if x == "0":
                result += "1"
                added = True
            else:
                result += "0"
    return result[::-1]


