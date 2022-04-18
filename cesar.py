def crypt(plainStr, shiftInt):
    resultStr = ""
    for char in plainStr:
        if ord(char) + shiftInt > ord('z'):
            resultStr = resultStr + chr(ord(char) + shiftInt - 26)
        else:
            resultStr = resultStr + chr(ord(char) + shiftInt)
    print('crypt:' + resultStr)

def decrypt(cryptoStr, shiftInt):
    resultStr = ""
    for char in cryptoStr:
        if ord(char) - shiftInt < ord('a'):
            resultStr = resultStr + chr(ord(char) - shiftInt + 26)
        else:
            resultStr = resultStr + chr(ord(char) - shiftInt)
    print('decrypt:' + resultStr)


crypt("Zyeb myxdsxeob sv do pkenbk kxkvicob vo psmrsob nsczyxslvo sms ",10)
decrypt("Zyeb myxdsxeob sv do pkenbk kxkvicob vo psmrsob nsczyxslvo sms ",10)
